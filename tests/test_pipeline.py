"""Tests for the deterministic pipeline. None of these touch a model."""
import json
from pathlib import Path

from obsagent.batch import group_threads, plan_batches, render_message, write_batches
from obsagent.cache import RunState, STAGES, corpus_fingerprint
from obsagent.citations import CorpusIndex, ValidationReport, find_quote, validate_citation, validate_processes
from obsagent.dedup import dedupe
from obsagent.economics import active_months, compute, rank, BLENDED_RATE
from obsagent.parse import parse_corpus, parse_date, normalize_subject, split_quoted, clean_for_model


# ------------------------------------------------------------------ parsing
def test_parse_reads_every_file(corpus):
    msgs = parse_corpus(corpus)
    assert len(msgs) == 5
    assert {m.id for m in msgs} == {"giron-d/sent/1", "farmer-d/logistics/2", "lokay-m/inbox/3", "lokay-m/inbox/4", "lokay-m/inbox/5"}
    m = next(m for m in msgs if m.id == "giron-d/sent/1")
    assert m.mailbox == "giron-d" and m.folder == "sent"
    assert m.sender == "a@enron.com" and m.recipients == ["b@enron.com"]
    assert m.date == "2001-10-30T02:59:07+00:00"


def test_invalid_and_out_of_range_dates_become_none(corpus):
    by_id = {m.id: m for m in parse_corpus(corpus)}
    assert by_id["lokay-m/inbox/4"].date is None          # "Tues, 32 Febuary 2001 25:61:00"
    assert by_id["lokay-m/inbox/4"].date_raw.startswith("Tues")
    assert by_id["lokay-m/inbox/5"].date is None          # year 2031
    assert parse_date(None) is None
    assert parse_date("Mon, 29 Oct 2001 18:59:07 -0800 (PST)") == "2001-10-30T02:59:07+00:00"


def test_subject_normalisation():
    assert normalize_subject("RE: Fw:  FWD: Calpine  Daily Gas Nomination ") == "calpine daily gas nomination"
    assert normalize_subject("") == ""


def test_split_quoted_and_capping():
    body = "Thanks.\n\n-----Original Message-----\nFrom: X\nSent: Y\n\n" + "quoted " * 1000
    head, tail = split_quoted(body)
    assert head == "Thanks."
    assert tail.startswith("-----Original Message-----")
    text, truncated = clean_for_model(body, 6000)
    assert truncated and "quoted tail truncated" in text and text.startswith("Thanks.")
    assert len(text) < 3000
    text2, trunc2 = clean_for_model("x" * 10_000, 6000)
    assert trunc2 and len(text2) < 6100


# -------------------------------------------------------------------- dedup
def test_dedupe_drops_same_content_with_different_message_id(corpus):
    unique, aliases = dedupe(parse_corpus(corpus))
    ids = {m.id for m in unique}
    assert "giron-d/sent/1" in ids and "lokay-m/inbox/3" not in ids
    assert aliases == {"lokay-m/inbox/3": "giron-d/sent/1"}
    assert len(unique) == 4


def test_dedupe_is_deterministic(corpus):
    msgs = parse_corpus(corpus)
    a, _ = dedupe(msgs)
    b, _ = dedupe(list(reversed(msgs)))
    assert [m.id for m in a] == [m.id for m in b]


# ------------------------------------------------------------------ batches
def test_threads_group_by_subject_and_batches_cover_everything(corpus, tmp_path):
    unique, _ = dedupe(parse_corpus(corpus))
    threads = group_threads(unique)
    calpine = next(t for t in threads if t[0].subject_norm == "calpine daily gas nomination")
    assert [m.id for m in calpine] == ["giron-d/sent/1", "farmer-d/logistics/2"]
    batches = plan_batches(unique, budget_tokens=50)   # tiny budget forces several batches
    covered = [i for b in batches for i in b.message_ids]
    assert sorted(covered) == sorted(m.id for m in unique)
    assert len(set(covered)) == len(covered)
    assert len(batches) > 1
    paths = write_batches(batches, tmp_path / "b")
    manifest = json.loads((tmp_path / "b" / "manifest.json").read_text())
    assert len(paths) == len(manifest) == len(batches)
    assert "### MSG giron-d/sent/1" in render_message(unique[0]) or any("### MSG" in p.read_text() for p in paths)


def test_batch_never_exceeds_budget_unless_single_message(corpus):
    unique, _ = dedupe(parse_corpus(corpus))
    for b in plan_batches(unique, budget_tokens=60):
        assert b.tokens <= 60 or len(b.message_ids) == 1


# ---------------------------------------------------------------- citations
def test_find_quote_is_whitespace_insensitive_but_case_sensitive():
    raw = "line one\nConfirmed on my end.  Same volumes\n   as yesterday.\n"
    assert find_quote(raw, "Confirmed on my end. Same volumes as yesterday.") == 2
    assert find_quote(raw, "confirmed on my end") is None
    assert find_quote(raw, "not in there at all") is None


def test_validate_citation_rules(corpus):
    unique, aliases = dedupe(parse_corpus(corpus))
    idx = CorpusIndex(corpus, [m.id for m in unique], aliases)
    ok = validate_citation(idx, {"msg": "giron-d/sent/1", "quote": "Same volumes as yesterday, no changes to the path."})
    assert ok.ok and ok.line == 11  # body starts on line 11 of the fixture
    # alias of a dropped duplicate is redirected to the kept copy
    via_alias = validate_citation(idx, {"msg": "lokay-m/inbox/3", "quote": "Same volumes as yesterday, no changes to the path."})
    assert via_alias.ok and via_alias.msg == "giron-d/sent/1"
    assert not validate_citation(idx, {"msg": "nope/1", "quote": "Same volumes as yesterday"}).ok
    assert validate_citation(idx, {"msg": "giron-d/sent/1", "quote": "Same"}).reason == "quote too short"
    assert validate_citation(idx, {"msg": "giron-d/sent/1", "quote": "Same volumes as tomorrow, honestly"}).reason == "quote not found verbatim"
    assert validate_citation(idx, {"msg": "giron-d/sent/1", "quote": "x" * 401}).reason == "quote too long"


def test_processes_without_valid_evidence_are_dropped(corpus):
    unique, aliases = dedupe(parse_corpus(corpus))
    idx = CorpusIndex(corpus, [m.id for m in unique], aliases)
    procs = [
        {"name": "good", "messages": ["farmer-d/logistics/2", "ghost/9"],
         "evidence": [{"msg": "giron-d/sent/1", "quote": "Confirmed on my end. Same volumes as yesterday"},
                      {"msg": "giron-d/sent/1", "quote": "this quote was hallucinated by a model"}]},
        {"name": "bad", "messages": ["giron-d/sent/1"], "evidence": [{"msg": "giron-d/sent/1", "quote": "invented claim about nominations"}]},
    ]
    rep = ValidationReport()
    kept = validate_processes(idx, procs, rep, source="t")
    assert [p["name"] for p in kept] == ["good"]
    assert kept[0]["messages"] == ["farmer-d/logistics/2", "giron-d/sent/1"]  # ghost removed, evidence msg added
    assert rep.checked == 3 and rep.valid == 1 and len(rep.rejected) == 2
    assert rep.processes_dropped == ["t:bad"]


# ---------------------------------------------------------------- economics
def test_active_months_and_arithmetic():
    assert active_months([]) == 1
    assert active_months(["2001-01-15T00:00:00+00:00", "2001-03-02T00:00:00+00:00"]) == 3
    dates = {"m1": "2001-01-15T00:00:00+00:00", "m2": "2001-02-01T00:00:00+00:00", "m3": None}
    e = compute({"messages": ["m1", "m2", "m3"], "minutes_per_occurrence": 30, "automatable_fraction": 0.5}, dates)
    assert e["messages_total"] == 3 and e["messages_dated"] == 2 and e["active_months"] == 2
    assert e["occurrences_per_month"] == 1.0
    assert e["gross_hours_per_month"] == 0.5
    assert e["hours_saved_per_month"] == 0.25
    assert e["dollars_saved_per_month"] == 0.25 * BLENDED_RATE == 21.25


def test_economics_clamps_model_inputs():
    e = compute({"messages": ["m"], "minutes_per_occurrence": 99999, "automatable_fraction": 7}, {"m": "2001-01-01T00:00:00+00:00"})
    assert e["minutes_per_occurrence"] == 480 and e["automatable_fraction"] == 1.0
    e = compute({"messages": [], "minutes_per_occurrence": "oops" if False else 10, "automatable_fraction": -1}, {})
    assert e["dollars_saved_per_month"] == 0.0


def test_rank_orders_by_dollars_then_name():
    opps = [{"name": "b", "economics": {"dollars_saved_per_month": 10}},
            {"name": "a", "economics": {"dollars_saved_per_month": 10}},
            {"name": "c", "economics": {"dollars_saved_per_month": 99}}]
    assert [o["name"] for o in rank(opps)] == ["c", "a", "b"]
    assert [o["rank"] for o in rank(opps)] == [1, 2, 3]


# -------------------------------------------------------------------- cache
def test_run_state_skips_unchanged_and_invalidates_downstream(tmp_path):
    fp = corpus_fingerprint([("a", "1"), ("b", "2")])
    assert fp == corpus_fingerprint([("b", "2"), ("a", "1")])
    st = RunState(tmp_path)
    assert not st.is_done("prepare", fp)
    st.mark("prepare", fp); st.mark("validate", "x"); st.mark("report", "y")
    assert RunState(tmp_path).is_done("prepare", fp)
    st.invalidate_from("validate", STAGES)
    st2 = RunState(tmp_path)
    assert st2.is_done("prepare", fp) and not st2.is_done("validate", "x") and not st2.is_done("report", "y")


# ---------------------------------------------------------------------- CLI
def test_cli_end_to_end_without_a_model(corpus, tmp_path):
    from obsagent.cli import main
    out = tmp_path / "out"
    main(["--corpus", str(corpus), "--out", str(out), "prepare"])
    idx = json.loads((out / "messages.json").read_text())
    assert idx["files"] == 5 and idx["unique"] == 4 and idx["duplicates"] == 1
    # simulate an observer output with one good and one fabricated citation
    (out / "observations").mkdir()
    (out / "observations" / "batch_000.json").write_text(json.dumps({"batch": 0, "processes": [
        {"name": "Daily nomination confirmation", "messages": ["giron-d/sent/1", "farmer-d/logistics/2"],
         "evidence": [{"msg": "giron-d/sent/1", "quote": "no changes to the path"},
                      {"msg": "farmer-d/logistics/2", "quote": "fabricated"}]}]}))
    main(["--corpus", str(corpus), "--out", str(out), "validate"])
    v = json.loads((out / "validation.json").read_text())
    assert v["checked"] == 2 and v["valid"] == 1 and v["rejected"][0]["reason"] in ("quote too short", "quote not found verbatim")
    (out / "synthesis.json").write_text(json.dumps({"processes": [
        {"name": "Daily nomination confirmation", "messages": ["giron-d/sent/1", "farmer-d/logistics/2"],
         "minutes_per_occurrence": 15, "automatable_fraction": 0.8,
         "evidence": [{"msg": "giron-d/sent/1", "quote": "Same volumes as yesterday"}]}]}))
    main(["--corpus", str(corpus), "--out", str(out), "economics", "--threshold", "1"])
    o = json.loads((out / "opportunities.json").read_text())
    e = o["opportunities"][0]["economics"]
    assert e["messages_dated"] == 2 and e["active_months"] == 1 and e["occurrences_per_month"] == 2.0
    assert e["dollars_saved_per_month"] == round(2 * 15 / 60 * 0.8 * 85, 2)
    assert o["opportunities"][0]["draft_required"] is True
    assert o["total_dollars_saved_per_month"] == e["dollars_saved_per_month"]


# ------------------------------------------------------- hook check + merge
def _prepared(corpus, tmp_path):
    from obsagent.cli import main
    out = tmp_path / "out"
    main(["--corpus", str(corpus), "--out", str(out), "prepare"])
    return out


def test_check_flags_schema_and_citation_problems(corpus, tmp_path):
    from obsagent.cli import check_observation_file
    out = _prepared(corpus, tmp_path)
    (out / "observations").mkdir()
    f = out / "observations" / "batch_000.json"
    good = {"name": "Nomination confirmation", "description": "d", "participants": ["a@enron.com"], "frequency_hint": "daily",
            "stall_points": "s", "automation": "a", "minutes_per_occurrence": 10, "automatable_fraction": 0.5,
            "messages": ["giron-d/sent/1"],
            "evidence": [{"msg": "giron-d/sent/1", "quote": "Confirmed on my end. Same volumes"},
                         {"msg": "giron-d/sent/1", "quote": "no changes to the path."}]}
    f.write_text(json.dumps({"batch": 0, "processes": [good]}))
    assert check_observation_file(f, corpus, out) == []
    bad = dict(good, minutes_per_occurrence=0, evidence=[{"msg": "giron-d/sent/1", "quote": "made up text here"}], messages=["zzz/1"])
    del bad["automation"]
    f.write_text(json.dumps({"batch": 7, "processes": [bad, good]}))
    probs = check_observation_file(f, corpus, out)
    joined = "\n".join(probs)
    assert '"batch" must be 0' in joined
    assert "missing fields ['automation']" in joined
    assert "minutes_per_occurrence must be in (0, 480]" in joined
    assert "at least 2 evidence" in joined
    assert "quote not found verbatim" in joined
    assert "unknown id 'zzz/1'" in joined
    f.write_text("{not json")
    assert check_observation_file(f, corpus, out)[0].startswith("not valid JSON")


def test_check_cli_exits_2_on_problems_and_logs(corpus, tmp_path, monkeypatch, capsys):
    import io
    from obsagent.cli import main
    out = _prepared(corpus, tmp_path)
    (out / "observations").mkdir()
    f = out / "observations" / "batch_000.json"
    f.write_text(json.dumps({"batch": 0, "processes": []}))
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps({"tool_input": {"file_path": str(f)}})))
    import pytest as _pt
    with _pt.raises(SystemExit) as e:
        main(["--corpus", str(corpus), "--out", str(out), "check"])
    assert e.value.code == 2
    assert "no processes reported" in capsys.readouterr().err
    assert "batch_000.json: 1 problems" in (out / "logs" / "hooks.log").read_text()
    # unrelated files are ignored
    other = tmp_path / "notes.md"; other.write_text("x")
    monkeypatch.setattr("sys.stdin", io.StringIO(json.dumps({"tool_input": {"file_path": str(other)}})))
    main(["--corpus", str(corpus), "--out", str(out), "check"])


def test_merged_from_expands_messages_and_evidence(corpus, tmp_path):
    from obsagent.cli import main
    out = _prepared(corpus, tmp_path)
    (out / "observations").mkdir()
    (out / "observations" / "batch_000.json").write_text(json.dumps({"batch": 0, "processes": [
        {"name": "Nomination confirmation", "messages": ["giron-d/sent/1"],
         "evidence": [{"msg": "giron-d/sent/1", "quote": "Confirmed on my end. Same volumes"}]},
        {"name": "Nomination follow-up", "messages": ["farmer-d/logistics/2"],
         "evidence": [{"msg": "farmer-d/logistics/2", "quote": "From: Giron, Darron"}]}]}))
    main(["--corpus", str(corpus), "--out", str(out), "validate"])
    (out / "synthesis.json").write_text(json.dumps({"processes": [
        {"name": "Daily nomination cycle", "description": "merged", "minutes_per_occurrence": 20, "automatable_fraction": 0.5,
         "merged_from": ["0:Nomination confirmation", "0:Nomination follow-up", "0:does not exist"]}]}))
    main(["--corpus", str(corpus), "--out", str(out), "economics", "--threshold", "0.5"])
    o = json.loads((out / "opportunities.json").read_text())["opportunities"][0]
    assert sorted(o["messages"]) == ["farmer-d/logistics/2", "giron-d/sent/1"]
    assert len(o["evidence"]) == 2 and o["merged_unresolved"] == ["0:does not exist"]
    assert o["economics"]["messages_dated"] == 2
    # draft inputs are produced only above threshold and skip opportunities that already have a draft
    main(["--corpus", str(corpus), "--out", str(out), "draft-inputs"])
    assert (out / "draft_inputs" / "daily-nomination-cycle.json").exists()
    (out / "drafts" / "daily-nomination-cycle-sop.md").write_text("---\ntitle: t\nopportunity: Daily nomination cycle\ntype: SOP\n---\nbody")
    (out / "draft_inputs" / "daily-nomination-cycle.json").unlink()
    main(["--corpus", str(corpus), "--out", str(out), "draft-inputs"])
    assert not (out / "draft_inputs" / "daily-nomination-cycle.json").exists()
    main(["--corpus", str(corpus), "--out", str(out), "report"])
    d = json.loads((out / "dashboard.json").read_text())
    assert d["opportunities"][0]["drafts"][0]["type"] == "SOP"
    assert "Daily nomination cycle" in (out / "report.md").read_text()
