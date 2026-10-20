# Observation agent — project rules for Claude Code

Build an evidence-backed picture of where a company loses time, from its raw email archive in `corpus/`, and serve it as a dashboard. Claude Code is the runtime; `python3 -m obsagent` is the deterministic toolbox it drives.

## The one command
`/observe [--threshold N] [--force]` (interactive) or `./run.sh` (headless, same thing). Everything else in this file exists to make that command correct, cheap and repeatable.

## Division of labour — do not blur it
- **Code decides anything that must be exactly right**: parsing, de-duplication, dates, batching, citation validation, the hours/dollars arithmetic, ranking, the report, the server. All in `src/obsagent/`, all covered by `tests/` which never call a model.
- **Models decide only what needs judgement**: what counts as a recurring process, how to describe it, the two estimates (`minutes_per_occurrence`, `automatable_fraction`), and the wording of drafts. Every model output is JSON or markdown that code validates before it is used.
- A claim without a verbatim, validated quote does not reach the report. The validator (`obsagent validate`, `obsagent economics`, and the PostToolUse hook) drops it and logs it in `out/validation*.json`.

## Context budget
- The corpus is ~1.7M raw tokens; after parsing it is ~0.96M, packed into batches of ≤35k tokens (`out/batches/`). One `observer` subagent reads one batch and nothing else.
- The orchestrator (the `/observe` command) never opens a batch or a corpus file. It reads only `manifest.json`, CLI output and small JSON.
- The `synthesizer` reads only `out/observations_compact.json` (~20–30k tokens). It merges by reference (`merged_from`); code expands references into message ids and quotes.
- `drafter` subagents read one `out/draft_inputs/<slug>.json` each.

## Idempotency
`out/state.json` records a fingerprint per stage. `prepare` skips an unchanged corpus; `validate`/`economics`/`report` skip unchanged inputs; `/observe` skips batches that already have an observation file and opportunities that already have a draft. `--force` redoes model stages. Deleting `out/` is a clean run.

## Layout
```
corpus/                 raw Enron maildir subset (read-only input)
src/obsagent/           parse, dedup, batch, cache, citations, economics, report, server, cli
tests/                  pytest, no model calls:  python3 -m pytest -q
.claude/agents/         observer, synthesizer, drafter
.claude/commands/       /observe
.claude/hooks/          check_observation.sh (PostToolUse validator), log_subagent.sh
out/                    run outputs: batches/, observations/, synthesis.json, opportunities.json,
                        drafts/, report.md, dashboard.json, logs/, validation*.json, state.json
NOTES.md                how the run was driven, what was wrong, what was taken on faith
```

## Conventions
- Python 3.11+, standard library only at runtime; `pytest` for tests. Run from the repo root with `PYTHONPATH=src`.
- Message ids are the corpus path without the trailing dot: `giron-d/sent/795` ↔ `corpus/giron-d/sent/795.`
- Quotes are matched whitespace-insensitively but case-sensitively against the raw file; 12–400 characters.
- Money is always `dated_messages / active_months × minutes / 60 × automatable_fraction × $85`, shown with its inputs.
- Do not install packages, do not call external APIs, do not touch `corpus/`.
