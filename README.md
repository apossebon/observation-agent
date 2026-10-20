# Observation agent

Reads a company's raw email archive (3,240 Enron messages in `corpus/`), works out where the company loses time, proves every claim with a verbatim quote from a specific message, estimates the automation value at a blended $85/hour, drafts the artifacts worth having tomorrow morning, and serves it all on a localhost dashboard.

Claude Code is the runtime. The assignment text is in [`ASSIGNMENT.md`](ASSIGNMENT.md); how the run was driven and where it is most likely wrong is in [`NOTES.md`](NOTES.md).

## Run it

```bash
./run.sh                 # headless: tests → claude -p "/observe" → dashboard on http://127.0.0.1:8765
```
or, inside an interactive Claude Code session in this directory: `/observe`.

No API keys, no package installs: Python 3.11+ standard library at runtime, `pytest` for tests, Claude Code on your subscription for the model stages.

Re-running against an unchanged corpus repeats nothing: `out/state.json` fingerprints every stage, finished batches and drafts are skipped. `./run.sh --force` redoes the model stages; `rm -rf out` is a clean run.

## What happens

| stage | who | input → output |
|---|---|---|
| prepare | code | `corpus/` → `out/messages.json`, `out/batches/batch_NNN.md` (parse, dedupe, date-validate, thread, pack ≤35k tokens) |
| observe | 28 × `observer` subagent, 6 in parallel | one batch → `out/observations/batch_NNN.json` (processes + verbatim quotes); a PostToolUse hook validates each file as it is written |
| validate | code | every quote checked against the raw file; failures dropped and logged → `out/observations_valid.json`, `out/observations_compact.json` |
| synthesize | 1 × `synthesizer` subagent | compact list → `out/synthesis.json` (merged processes, by reference) |
| economics | code | expand references, re-validate, hours & dollars, rank → `out/opportunities.json` |
| draft | N × `drafter` subagent | one opportunity above the threshold → `out/drafts/<slug>-<type>.md` |
| report | code | → `out/report.md`, `out/dashboard.json` |
| serve | code | `python3 -m obsagent serve` → dashboard with drill-through to every cited line |

## Check it yourself

```bash
python3 -m pytest -q                                   # 19 tests, no model
PYTHONPATH=src python3 -m obsagent status              # which stages are done for this corpus
cat out/validation.json | head -40                     # every rejected citation and why
```
Every number on the dashboard shows its formula and inputs; every quote links to `/msg/<id>?line=N`, the raw file with the cited line highlighted. The raw file is `corpus/<id>.`.
