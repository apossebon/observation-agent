"""`python -m obsagent <command>` — the deterministic half of the pipeline.

Stages (in order):
  prepare     parse + dedupe the corpus, plan batches           -> out/messages.json, out/batches/
  validate    check every citation in the observer outputs      -> out/observations_valid.json, out/validation.json
  economics   validate the synthesis, compute hours/$ and rank  -> out/opportunities.json
  report      write report.md and the dashboard data            -> out/report.md, out/dashboard.json
  serve       serve the dashboard on localhost
  status      print which stages are complete for this corpus

Model-driven stages (observe, synthesize, draft) are run by Claude Code via
the /observe command; this CLI only consumes their JSON outputs.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .batch import plan_batches, write_batches, DEFAULT_BATCH_TOKENS
from .cache import RunState, STAGES, corpus_fingerprint, file_fingerprint
from .citations import CorpusIndex, ValidationReport, validate_citation, validate_processes
from .dedup import dedupe
from .economics import compute, rank
from .parse import parse_corpus

ROOT = Path(__file__).resolve().parents[2]


def log(msg: str):
    print(f"[obsagent] {msg}", file=sys.stderr, flush=True)


def load_messages(out: Path) -> dict:
    return json.loads((out / "messages.json").read_text("utf-8"))


def make_index(corpus: Path, out: Path) -> CorpusIndex:
    data = load_messages(out)
    return CorpusIndex(corpus, [m["id"] for m in data["messages"]], data["aliases"])


# ---------------------------------------------------------------- prepare
def cmd_prepare(a):
    corpus, out = Path(a.corpus), Path(a.out)
    msgs = parse_corpus(corpus, a.max_body_chars)
    fp = corpus_fingerprint([(m.path, m.sha1) for m in msgs])
    state = RunState(out)
    if state.is_done("prepare", fp) and not a.force:
        log(f"prepare: corpus unchanged ({fp[:12]}), {len(msgs)} files — skipping")
        return
    state.invalidate_from("prepare", STAGES)
    unique, aliases = dedupe(msgs)
    batches = plan_batches(unique, a.batch_tokens)
    (out / "batches").mkdir(parents=True, exist_ok=True)
    for old in (out / "batches").glob("batch_*.md"):
        old.unlink()
    write_batches(batches, out / "batches")
    index = {
        "corpus_fingerprint": fp,
        "files": len(msgs),
        "unique": len(unique),
        "duplicates": len(aliases),
        "undated": sum(1 for m in unique if not m.date),
        "truncated": sum(1 for m in unique if m.truncated),
        "batches": len(batches),
        "aliases": aliases,
        "messages": [
            {k: v for k, v in m.to_dict().items() if k not in ("body", "extra")} for m in unique
        ],
    }
    (out / "messages.json").write_text(json.dumps(index, indent=1), "utf-8")
    state.mark("prepare", fp, files=len(msgs), unique=len(unique), batches=len(batches))
    log(f"prepare: {len(msgs)} files, {len(unique)} unique ({len(aliases)} duplicates), "
        f"{index['undated']} undated, {index['truncated']} truncated, {len(batches)} batches of ≤{a.batch_tokens} tokens")


# --------------------------------------------------------------- validate
def cmd_validate(a):
    corpus, out = Path(a.corpus), Path(a.out)
    obs_dir = out / "observations"
    files = sorted(obs_dir.glob("batch_*.json"))
    if not files:
        log("validate: no observation files found"); sys.exit(2)
    fp = file_fingerprint(files)
    state = RunState(out)
    if state.is_done("validate", fp) and not a.force:
        log("validate: observations unchanged — skipping"); return
    state.invalidate_from("validate", STAGES)
    index = make_index(corpus, out)
    manifest = json.loads((out / "batches" / "manifest.json").read_text())
    expected = {b["index"] for b in manifest}
    report = ValidationReport()
    valid, covered, per_batch = [], set(), {}
    for f in files:
        try:
            data = json.loads(f.read_text("utf-8"))
        except json.JSONDecodeError as e:
            report.rejected.append({"source": f.name, "reason": f"invalid JSON: {e}"}); continue
        bidx = int(data.get("batch", f.stem.split("_")[-1]))
        expected.discard(bidx)
        procs = validate_processes(index, data.get("processes", []), report, source=f.name)
        for p in procs:
            p["batch"] = bidx
            covered.update(p["messages"])
        per_batch[bidx] = {"processes_in": len(data.get("processes", [])), "processes_out": len(procs)}
        valid.extend(procs)
    summary = report.summary() | {"batches_validated": len(per_batch), "batches_missing": sorted(expected),
                                  "processes_kept": len(valid), "messages_attributed": len(covered)}
    (out / "observations_valid.json").write_text(json.dumps({"summary": summary, "per_batch": per_batch, "processes": valid}, indent=1), "utf-8")
    # Compact view for the synthesizer: enough to merge by, small enough to fit one context.
    compact = [{
        "ref": f"{p['batch']}:{p['name']}",
        "name": p["name"],
        "description": (p.get("description") or "")[:200],
        "participants": [x.split("@")[0] for x in (p.get("participants") or [])[:4]],
        "messages": len(p["messages"]),
        "frequency_hint": p.get("frequency_hint", ""),
        "stall_points": (p.get("stall_points") or "")[:120],
        "automation": (p.get("automation") or "")[:120],
        "minutes_per_occurrence": p.get("minutes_per_occurrence"),
        "automatable_fraction": p.get("automatable_fraction"),
        "sample_quote": (p["evidence"][0]["quote"][:110] if p["evidence"] else ""),
    } for p in valid]
    (out / "observations_compact.json").write_text(json.dumps(compact, separators=(",", ":")), "utf-8")
    (out / "validation.json").write_text(json.dumps({"stage": "observe", **summary, "rejected": report.rejected}, indent=1), "utf-8")
    state.mark("validate", fp, **{k: v for k, v in summary.items() if not isinstance(v, list)})
    log(f"validate: {summary['valid']}/{summary['checked']} citations valid, {len(valid)} processes kept, "
        f"{len(report.processes_dropped)} dropped, missing batches: {summary['batches_missing']}")
    if expected and a.strict:
        sys.exit(3)


def expand_merged(processes: list[dict], out: Path) -> list[dict]:
    """Resolve `merged_from` refs ("<batch>:<name>") into the validated per-batch
    processes: union their message ids and citations deterministically, so the
    synthesizer never has to copy hundreds of ids or re-type quotes."""
    ov_path = out / "observations_valid.json"
    by_ref: dict[str, dict] = {}
    if ov_path.exists():
        for p in json.loads(ov_path.read_text("utf-8"))["processes"]:
            by_ref[f"{p['batch']}:{p['name']}"] = p
    result = []
    for p in processes:
        p = dict(p)
        msgs, evidence, seen_q, unresolved = list(p.get("messages", []) or []), list(p.get("evidence", []) or []), set(), []
        for ref in p.get("merged_from", []) or []:
            src = by_ref.get(str(ref))
            if not src:
                unresolved.append(ref); continue
            for m in src["messages"]:
                if m not in msgs:
                    msgs.append(m)
            for c in src["evidence"]:
                key = (c["msg"], c["quote"].strip())
                if key not in seen_q:
                    seen_q.add(key); evidence.append({"msg": c["msg"], "quote": c["quote"]})
        p["messages"], p["evidence"], p["merged_unresolved"] = msgs, evidence, unresolved
        result.append(p)
    return result


# -------------------------------------------------------------- economics
def cmd_economics(a):
    corpus, out = Path(a.corpus), Path(a.out)
    syn_path = out / "synthesis.json"
    if not syn_path.exists():
        log("economics: out/synthesis.json missing"); sys.exit(2)
    fp = file_fingerprint([syn_path]) + f":t={a.threshold}:m={a.min_months}"
    state = RunState(out)
    if state.is_done("economics", fp) and not a.force:
        log("economics: synthesis unchanged — skipping"); return
    state.invalidate_from("economics", STAGES)
    index = make_index(corpus, out)
    dates = {m["id"]: m["date"] for m in load_messages(out)["messages"]}
    data = json.loads(syn_path.read_text("utf-8"))
    procs = expand_merged(data.get("processes", []), out)
    # Coverage: every validated per-batch process must be merged or explicitly dropped.
    ov = out / "observations_valid.json"
    all_refs = {f"{p['batch']}:{p['name']}" for p in json.loads(ov.read_text("utf-8"))["processes"]} if ov.exists() else set()
    used = {r for p in data.get("processes", []) for r in (p.get("merged_from") or [])}
    dropped = set(data.get("dropped") or [])
    unreferenced = sorted(all_refs - used - dropped)
    if unreferenced:
        log(f"economics: WARNING {len(unreferenced)} observed processes neither merged nor dropped by the synthesizer: {unreferenced[:5]}{' ...' if len(unreferenced) > 5 else ''}")
    report = ValidationReport()
    procs = validate_processes(index, procs, report, source="synthesis.json")
    opps = []
    for p in procs:
        p["economics"] = compute(p, dates, int(a.min_months))
        opps.append(p)
    opps = rank(opps)
    recurring = [o for o in opps if o["economics"]["recurring"]]
    episodes = [o for o in opps if not o["economics"]["recurring"]]
    total = round(sum(o["economics"]["dollars_saved_per_month"] for o in recurring), 2)
    threshold = float(a.threshold)
    for o in opps:
        o["draft_required"] = o["economics"]["recurring"] and o["economics"]["dollars_saved_per_month"] >= threshold
    result = {
        "min_recurring_months": int(a.min_months),
        "recurring_count": len(recurring),
        "episode_count": len(episodes),
        "episodes_dollars_per_month": round(sum(o["economics"]["dollars_saved_per_month"] for o in episodes), 2),
        "validation": report.summary(),
        "synthesis_coverage": {"observed": len(all_refs), "merged": len(used & all_refs), "dropped": len(dropped & all_refs),
                               "unreferenced": unreferenced, "unknown_refs": sorted(used - all_refs)},
        "threshold_dollars_per_month": threshold,
        "total_dollars_saved_per_month": total,
        "total_hours_saved_per_month": round(sum(o["economics"]["hours_saved_per_month"] for o in recurring), 2),
        "opportunities": opps,
    }
    (out / "opportunities.json").write_text(json.dumps(result, indent=1), "utf-8")
    (out / "validation_synthesis.json").write_text(json.dumps({"stage": "synthesize", **report.summary(), "rejected": report.rejected}, indent=1), "utf-8")
    state.mark("economics", fp, opportunities=len(opps), total_dollars=total)
    log(f"economics: {len(opps)} opportunities ({len(recurring)} recurring, {len(episodes)} episodes), ${total:,.0f}/month recurring total, "
        f"{sum(o['draft_required'] for o in opps)} above ${threshold:,.0f} threshold; "
        f"{report.valid}/{report.checked} citations valid, dropped {len(report.processes_dropped)}")


# ------------------------------------------------------------------ check
REQUIRED_PROCESS_FIELDS = ("name", "description", "participants", "frequency_hint", "stall_points",
                           "automation", "minutes_per_occurrence", "automatable_fraction", "messages", "evidence")


def check_observation_file(path: Path, corpus: Path, out: Path) -> list[str]:
    """Problems with one observer/synthesizer JSON file. Empty list == acceptable."""
    problems: list[str] = []
    try:
        data = json.loads(path.read_text("utf-8"))
    except Exception as e:
        return [f"not valid JSON: {e}"]
    if not isinstance(data, dict) or not isinstance(data.get("processes"), list):
        return ['top level must be an object with a "processes" list']
    index = make_index(corpus, out)
    is_batch = path.name.startswith("batch_")
    allowed: set[str] | None = None
    if is_batch:
        manifest = json.loads((out / "batches" / "manifest.json").read_text())
        bidx = int(path.stem.split("_")[-1])
        if data.get("batch") != bidx:
            problems.append(f'"batch" must be {bidx}')
        allowed = set(next((b["message_ids"] for b in manifest if b["index"] == bidx), []))
    if not data["processes"]:
        problems.append("no processes reported — a batch of this size always contains some recurring work")
    names = set()
    for i, p in enumerate(data["processes"]):
        tag = f"processes[{i}] ({p.get('name', '?')})"
        missing = [f for f in REQUIRED_PROCESS_FIELDS if f not in p] if is_batch else [f for f in ("name", "description", "minutes_per_occurrence", "automatable_fraction") if f not in p]
        if missing:
            problems.append(f"{tag}: missing fields {missing}")
        if p.get("name") in names:
            problems.append(f"{tag}: duplicate process name")
        names.add(p.get("name"))
        try:
            mins = float(p.get("minutes_per_occurrence", 0)); frac = float(p.get("automatable_fraction", 0))
            if not (0 < mins <= 480): problems.append(f"{tag}: minutes_per_occurrence must be in (0, 480]")
            if not (0 <= frac <= 1): problems.append(f"{tag}: automatable_fraction must be in [0, 1]")
        except (TypeError, ValueError):
            problems.append(f"{tag}: minutes_per_occurrence / automatable_fraction must be numbers")
        ev = p.get("evidence") or []
        if is_batch and len(ev) < 2:
            problems.append(f"{tag}: give at least 2 evidence quotes")
        bad = 0
        for c in ev:
            r = validate_citation(index, c)
            if not r.ok:
                bad += 1
                problems.append(f"{tag}: evidence rejected ({r.reason}): msg={c.get('msg')!r} quote={str(c.get('quote'))[:80]!r}")
            elif allowed is not None and r.msg not in allowed and c.get("msg") not in index.aliases:
                problems.append(f"{tag}: evidence cites {r.msg}, which is not in this batch")
        if ev and bad == len(ev):
            problems.append(f"{tag}: no valid evidence at all — drop the process or fix the quotes")
        if is_batch:
            for m in p.get("messages") or []:
                r = index.resolve(str(m))
                if not r:
                    problems.append(f"{tag}: messages contains unknown id {m!r}")
                elif r not in allowed:
                    problems.append(f"{tag}: messages contains {r}, which is not in this batch")
        for ref in p.get("merged_from") or []:
            if not isinstance(ref, str) or ":" not in ref:
                problems.append(f"{tag}: merged_from entries must look like '<batch>:<process name>'")
    return problems


def cmd_check(a):
    """Used by the PostToolUse hook. Reads hook JSON from stdin when no path is given.
    Exit 2 with the problems on stderr => Claude Code feeds them back to the agent."""
    path = a.path
    if not path:
        try:
            payload = json.load(sys.stdin)
            path = payload.get("tool_input", {}).get("file_path") or payload.get("tool_input", {}).get("path")
        except Exception:
            path = None
    if not path:
        return
    p = Path(path)
    out = Path(a.out)
    watched = p.name.startswith("batch_") and p.suffix == ".json" and p.parent.name == "observations" or p.name == "synthesis.json"
    if not watched or not p.exists():
        return
    problems = check_observation_file(p, Path(a.corpus), out)
    log_path = out / "logs" / "hooks.log"; log_path.parent.mkdir(parents=True, exist_ok=True)
    from datetime import datetime, timezone
    with log_path.open("a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()} check {p.name}: {len(problems)} problems\n")
        for pr in problems: f.write("    " + pr + "\n")
    if problems:
        print(f"{p.name} has {len(problems)} problem(s) — fix the file and write it again:\n- " + "\n- ".join(problems[:25]), file=sys.stderr)
        sys.exit(2)
    print(f"{p.name}: OK")


# ----------------------------------------------------------- draft inputs
def cmd_draft_inputs(a):
    """Write one small JSON per opportunity above the threshold for the drafter subagents."""
    out = Path(a.out)
    data = json.loads((out / "opportunities.json").read_text("utf-8"))
    msgs = {m["id"]: m for m in load_messages(out)["messages"]}
    d = out / "draft_inputs"; d.mkdir(exist_ok=True)
    (out / "drafts").mkdir(exist_ok=True)
    from .report import _slug
    todo = []
    for o in data["opportunities"]:
        if not o["draft_required"]:
            continue
        slug = _slug(o["name"])
        existing = list((out / "drafts").glob(f"{slug}-*.md"))
        if existing and not a.force:
            continue
        ev = [{"msg": c["msg"], "line": c["line"], "quote": c["quote"], "date": (msgs.get(c["msg"], {}).get("date") or "")[:10],
               "sender": msgs.get(c["msg"], {}).get("sender", ""), "subject": msgs.get(c["msg"], {}).get("subject", "")} for c in o["evidence"][:12]]
        payload = {"slug": slug, "name": o["name"], "description": o.get("description"), "stall_points": o.get("stall_points"),
                   "automation": o.get("automation"), "participants": sorted({msgs[m]["sender"] for m in o["messages"] if m in msgs})[:10],
                   "economics": o["economics"], "evidence": ev, "output_prefix": f"out/drafts/{slug}-"}
        (d / f"{slug}.json").write_text(json.dumps(payload, indent=1), "utf-8")
        todo.append(slug)
    print(json.dumps(todo))


# ----------------------------------------------------------------- report
def cmd_report(a):
    from .report import build_report
    build_report(Path(a.corpus), Path(a.out))


def cmd_serve(a):
    from .server import serve
    serve(Path(a.corpus), Path(a.out), a.host, a.port)


def cmd_status(a):
    state = RunState(Path(a.out))
    for s in STAGES:
        info = state.data["stages"].get(s)
        print(f"{s:12s} {'done ' + info['at'] if info else 'pending'}")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="obsagent")
    ap.add_argument("--corpus", default=str(ROOT / "corpus"))
    ap.add_argument("--out", default=str(ROOT / "out"))
    ap.add_argument("--force", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare"); p.add_argument("--batch-tokens", type=int, default=DEFAULT_BATCH_TOKENS); p.add_argument("--max-body-chars", type=int, default=6000); p.set_defaults(fn=cmd_prepare)
    p = sub.add_parser("validate"); p.add_argument("--strict", action="store_true"); p.set_defaults(fn=cmd_validate)
    p = sub.add_parser("economics"); p.add_argument("--threshold", default=100); p.add_argument("--min-months", default=6); p.set_defaults(fn=cmd_economics)
    p = sub.add_parser("check"); p.add_argument("path", nargs="?"); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("draft-inputs"); p.set_defaults(fn=cmd_draft_inputs)
    p = sub.add_parser("report"); p.set_defaults(fn=cmd_report)
    p = sub.add_parser("serve"); p.add_argument("--host", default="127.0.0.1"); p.add_argument("--port", type=int, default=8765); p.set_defaults(fn=cmd_serve)
    p = sub.add_parser("status"); p.set_defaults(fn=cmd_status)
    a = ap.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
