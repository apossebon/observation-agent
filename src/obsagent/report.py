"""Report and dashboard data — assembled from validated JSON, no model."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from .cache import RunState, file_fingerprint


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def load_drafts(out: Path) -> list[dict]:
    drafts = []
    for p in sorted((out / "drafts").glob("*.md")) if (out / "drafts").exists() else []:
        text = p.read_text("utf-8")
        meta = {}
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1); meta[k.strip()] = v.strip().strip('"')
        drafts.append({"file": p.name, "title": meta.get("title", p.stem), "opportunity": meta.get("opportunity", ""),
                       "type": meta.get("type", ""), "size": len(text)})
    return drafts


def build_report(corpus: Path, out: Path):
    opp_path = out / "opportunities.json"
    if not opp_path.exists():
        raise SystemExit("[obsagent] report: out/opportunities.json missing — run economics first")
    inputs = [opp_path, out / "messages.json", out / "validation.json"] + sorted((out / "drafts").glob("*.md")) if (out / "drafts").exists() else [opp_path, out / "messages.json", out / "validation.json"]
    inputs = [p for p in inputs if p.exists()]
    fp = file_fingerprint(inputs)
    state = RunState(out)
    data = json.loads(opp_path.read_text("utf-8"))
    idx = json.loads((out / "messages.json").read_text("utf-8"))
    msgs = {m["id"]: m for m in idx["messages"]}
    obs_val = json.loads((out / "validation.json").read_text()) if (out / "validation.json").exists() else {}
    syn_val = json.loads((out / "validation_synthesis.json").read_text()) if (out / "validation_synthesis.json").exists() else {}
    drafts = load_drafts(out)
    drafts_by_opp = {}
    for d in drafts:
        drafts_by_opp.setdefault(_slug(d["opportunity"]), []).append(d)

    opps = data["opportunities"]
    for o in opps:
        o["slug"] = _slug(o["name"])
        o["drafts"] = drafts_by_opp.get(o["slug"], [])
        for c in o["evidence"]:
            m = msgs.get(c["msg"], {})
            c["date"] = (m.get("date") or "")[:10]
            c["sender"] = m.get("sender", "")
            c["subject"] = m.get("subject", "")
        o["participants"] = sorted({msgs[m]["sender"] for m in o["messages"] if m in msgs and msgs[m]["sender"]})[:12]

    dashboard = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "corpus": {"files": idx["files"], "unique": idx["unique"], "duplicates": idx["duplicates"],
                   "undated": idx["undated"], "batches": idx["batches"], "fingerprint": idx["corpus_fingerprint"]},
        "validation": {"observations": {k: obs_val.get(k) for k in ("checked", "valid", "rejected", "processes_dropped")},
                       "synthesis": {k: syn_val.get(k) for k in ("checked", "valid", "rejected", "processes_dropped")}},
        "threshold": data["threshold_dollars_per_month"],
        "total_dollars_saved_per_month": data["total_dollars_saved_per_month"],
        "total_hours_saved_per_month": data["total_hours_saved_per_month"],
        "opportunities": opps,
        "drafts": drafts,
    }
    (out / "dashboard.json").write_text(json.dumps(dashboard, indent=1), "utf-8")
    (out / "report.md").write_text(render_markdown(dashboard), "utf-8")
    state.mark("report", fp, opportunities=len(opps), drafts=len(drafts))
    print(f"[obsagent] report: {len(opps)} opportunities, {len(drafts)} drafts -> out/report.md, out/dashboard.json")


def render_markdown(d: dict) -> str:
    L = []
    L.append("# Observation report — where this company loses time\n")
    L.append(f"Generated {d['generated_at'][:19]}Z from {d['corpus']['files']} raw messages "
             f"({d['corpus']['unique']} unique after removing {d['corpus']['duplicates']} duplicates; "
             f"{d['corpus']['undated']} without a usable date).\n")
    L.append(f"**Total automation opportunity: ${d['total_dollars_saved_per_month']:,.0f} / month "
             f"({d['total_hours_saved_per_month']:,.1f} hours / month at a blended $85/hour).**\n")
    L.append("Every figure below is computed from validated citations: each quote was matched verbatim "
             "against the raw file, and any claim that failed was discarded before this report was written. "
             f"Observation stage: {d['validation']['observations']['valid']}/{d['validation']['observations']['checked']} citations held; "
             f"synthesis stage: {d['validation']['synthesis']['valid']}/{d['validation']['synthesis']['checked']}.\n")
    L.append("## Ranked opportunities\n")
    L.append("| # | Opportunity | Occurrences / month | Hours saved / month | $ / month | Messages | Draft |")
    L.append("|---|---|---:|---:|---:|---:|---|")
    for o in d["opportunities"]:
        e = o["economics"]
        draft = ", ".join(x["file"] for x in o["drafts"]) or ("—" if not o["draft_required"] else "(missing)")
        L.append(f"| {o['rank']} | {o['name']} | {e['occurrences_per_month']} | {e['hours_saved_per_month']} | "
                 f"{e['dollars_saved_per_month']:,.0f} | {e['messages_total']} | {draft} |")
    L.append("")
    for o in d["opportunities"]:
        e = o["economics"]
        L.append(f"## {o['rank']}. {o['name']}\n")
        L.append(o.get("description", "").strip() + "\n")
        L.append(f"- **Who touches it:** {', '.join(o.get('participants', [])) or 'n/a'}")
        L.append(f"- **How often:** {e['occurrences_per_month']} occurrences/month "
                 f"({e['messages_dated']} dated messages over {e['active_months']} active months, {e['first_date']} → {e['last_date']})")
        if o.get("stall_points"):
            L.append(f"- **Where it stalls:** {o['stall_points']}")
        if o.get("automation"):
            L.append(f"- **Automation:** {o['automation']}")
        L.append(f"- **Estimate:** {e['minutes_per_occurrence']:.0f} min/occurrence × {e['automatable_fraction']:.0%} automatable "
                 f"→ {e['hours_saved_per_month']} h/month → **${e['dollars_saved_per_month']:,.0f}/month**")
        if o.get("estimate_rationale"):
            L.append(f"- **Why that estimate:** {o['estimate_rationale']}")
        if o["drafts"]:
            L.append("- **Drafted artifacts:** " + ", ".join(f"`drafts/{x['file']}`" for x in o["drafts"]))
        L.append("\n**Evidence**\n")
        for c in o["evidence"]:
            L.append(f"- `{c['msg']}` (line {c['line']}, {c['date'] or 'undated'}, {c['sender']}): "
                     f"“{c['quote'].strip()}”")
        L.append("")
    L.append("## Method\n")
    L.append("1. Deterministic parse of every file; duplicates removed by normalised sender+subject+body; "
             "invalid or out-of-range dates set to null.\n"
             f"2. Messages grouped into subject threads and packed into {d['corpus']['batches']} batches, "
             "each read in full by one observer subagent that reported processes as JSON with verbatim quotes.\n"
             "3. Every quote checked against the raw file by code; failures logged in `validation.json`.\n"
             "4. A synthesizer merged per-batch processes into company-wide ones; its citations were checked again.\n"
             "5. Hours and dollars computed by code from dated message counts and two model-supplied estimates "
             "(minutes per occurrence, automatable fraction), both shown beside each result.\n"
             "6. Drafts produced only for opportunities above the threshold "
             f"(${d['threshold']:,.0f}/month).\n")
    return "\n".join(L)
