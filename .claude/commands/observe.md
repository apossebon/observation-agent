---
description: Run the full observation pipeline over corpus/ (prepare → observe → validate → synthesize → economics → draft → report) and serve the dashboard.
argument-hint: [--threshold DOLLARS_PER_MONTH] [--force]
allowed-tools: Bash(PYTHONPATH=src python3 *), Bash(python3 *), Bash(./serve.sh *), Bash(mkdir *), Bash(echo *), Bash(cat *), Bash(ls *), Read, Write, Task
---

Run the whole pipeline end to end, unattended. Arguments: `$ARGUMENTS` (optional `--threshold N`, default 100; optional `--force` to redo model stages even if outputs exist).

You are the orchestrator. Deterministic work is done by `python3 -m obsagent …`; judgement is delegated to subagents with small, fixed inputs. Never read a batch file or the corpus yourself — your context is for coordination. Every stage appends to `out/logs/run.log` as shown below.

## 0. Setup
```
mkdir -p out/logs out/observations out/drafts
echo "$(date -u +%FT%TZ) run start args=$ARGUMENTS" >> out/logs/run.log
PYTHONPATH=src python3 -m obsagent prepare 2>&1 | tee -a out/logs/run.log
```
`prepare` is idempotent: an unchanged corpus is detected by fingerprint and skipped.

## 1. Observe (parallel)
Read `out/batches/manifest.json` (it is small). For every batch index N that has no `out/observations/batch_NNN.json` (or all of them if `--force`), launch an `observer` subagent with exactly this prompt:

> Read `out/batches/batch_NNN.md` and write `out/observations/batch_NNN.json`.

Launch them in waves of 6 (six Task calls in one message), wait for the wave, then launch the next. Append `observed NNN` lines to `out/logs/run.log` as they finish. Do not read the observation files yourself.

## 2. Validate
```
PYTHONPATH=src python3 -m obsagent validate --strict 2>&1 | tee -a out/logs/run.log
```
If it reports `missing batches`, re-launch observers for those batches only (at most two retries), then validate again. Rejected citations are logged in `out/validation.json`; they are dropped, not fixed.

## 3. Synthesize
Launch one `synthesizer` subagent with the prompt:

> Read `out/observations_compact.json` and write `out/synthesis.json`.

(Skip if `out/synthesis.json` exists and `--force` was not given.)

## 4. Economics
```
PYTHONPATH=src python3 -m obsagent economics --threshold <N> 2>&1 | tee -a out/logs/run.log
```

## 5. Draft (parallel)
```
PYTHONPATH=src python3 -m obsagent draft-inputs
```
prints a JSON list of slugs that need a draft. For each slug launch a `drafter` subagent (all in one wave if ≤ 8) with the prompt:

> Read `out/draft_inputs/<slug>.json` and write the artifact file(s) it asks for under `out/drafts/`.

Economics is re-run whenever the threshold or the synthesis changes; the observers and the synthesizer are not. Opportunities marked `"recurring": false` (episodes) are never drafted.

## 6. Report and serve
```
PYTHONPATH=src python3 -m obsagent report 2>&1 | tee -a out/logs/run.log
PYTHONPATH=src python3 -m obsagent status | tee -a out/logs/run.log
echo "$(date -u +%FT%TZ) run end" >> out/logs/run.log
```
Then start the dashboard in the background and tell the user the URL:
```
./serve.sh
```

## Final message
Report, in under ten lines: messages read / unique / duplicates, batches observed, citations checked vs valid at each stage, number of recurring opportunities and episodes, recurring total $/month, drafts written, and the dashboard URL. Mention anything that was retried or dropped.
