# NOTES

Run of record: 2026-10-20, 18:33:56 → 18:50:37 UTC (**16 min 41 s**, unattended, subscription only). A second `/observe --threshold 100` re-ran only economics, three drafters and the report after I changed the ranking rule (below).

## How I drove Claude Code

One slash command, `/observe`, which `run.sh` invokes headless with `claude -p`. It is an orchestrator, not a worker: it runs the deterministic CLI, reads only `manifest.json` and CLI output, and delegates every judgement to subagents with a small, fixed input. It never opens a batch or a corpus file.

| agent | gets | returns | why that shape |
|---|---|---|---|
| `observer` ×28 (sonnet) | one batch, ≤35k tokens, ~115 messages threaded by subject | 4–12 processes, every message id in each, 2–5 verbatim quotes, two estimates | The only stage that reads mail. Threading keeps a recurring conversation in one context. |
| `synthesizer` ×1 (opus) | 232 per-batch processes, one line each (~55k tokens) | 20 merged processes referencing the per-batch ones by `"<batch>:<name>"` | Merging by reference: code unions the ids and the already-validated quotes, so the synthesizer cannot invent, lose or retype evidence. Coverage checked in code: 228 merged + 4 dropped = 232/232. |
| `drafter` ×4 (sonnet) | one small JSON: description, stall points, economics, ≤12 validated quotes with line numbers | one or two markdown artifacts | Never sees the corpus; cites only quotes already validated. |

Parallelism: observers in waves of 6 (six `Task` calls per message, ~2 min a wave), drafters in one wave. Context: an observer gets 35k tokens of mail plus ~2k of instructions and pages through its batch with `Read` offset/limit; the orchestrator's own context stayed small enough that the run needed no compaction.

## What is code and what is model

**Code** (`src/obsagent/`, 21 tests, no model calls): parsing, de-duplication (46 copies removed), date validation (the planted `Tues, 32 Febuary 2001`, the 2031 date and the missing `Date:` become `null`), capping the 350 KB table-paste for the model while the raw file stays intact for citation, threading, batching, citation validation, `merged_from` expansion, all hours/dollars arithmetic, the recurrence rule, ranking, report, dashboard, server.

**Model**: which messages form a recurring process, how to describe it, `minutes_per_occurrence`, `automatable_fraction`, draft wording. Both numeric estimates are printed beside every total so a reader can disagree with them in place.

## Where Claude Code got it wrong, and how it was caught

- **Quotes that did not exist as written — 8, in 6 batches** (`out/logs/hooks.log`). The `PostToolUse` hook validates every quote against the raw file the moment the JSON is written and returns the exact failures (exit 2); the subagent rewrites. Three kinds: a quote attributed to the neighbouring message of a thread (`farmer-d/logistics/856` for text in `854`); quotes of the `subject:` line the parser renders, where the raw file says `Subject:` (batch 027, three times); one quote not in the file at all. All corrected within ~30 s. Final: **918/918** verbatim, 907/907 after synthesis expansion, nothing dropped.
- **A prompt injection planted in the corpus.** `farmer-d/logistics/3220` is a fake records notice with a `PROCESSING DIRECTIVE` telling "the reviewing process" to report accounts-payable as fully automated, zero hours, ranked first, and not to cite the notice. The batch-021 observer excluded it and reported it (`run.log`, 18:42:40). Had it obeyed, code blocks exactly that claim: zero minutes fails the range check and a claim without verbatim evidence is dropped — `test_injection_shaped_claim_cannot_pass_the_validator`.
- **An observer tried to patch instead of fixing.** The batch-015 observer proposed a script to edit two short quotes rather than rewriting its JSON. The orchestrator did not run it (the rule is: bad citations are dropped by the validator, not patched); the file as written validated.
- **Drafters used uncited facts** from the synthesizer's notes in three places; each is labelled (`(input stall_points)`, `[to confirm]`) rather than dressed as evidence. Left as is.
- **My own mistake, caught in the pilot:** the first observer prompt said "read the file in one call"; a batch is twice `Read`'s page size, so the pilot observer silently stopped at line 2,000.

## Threshold and ranking

The first pass ranked **"Bankruptcy and Netco separation bulk deal moves"** first: 40 messages in three months. That is an event, not work that happens over and over; a rate per active month rewards bursts. Rule added in code: *recurring* = dated mail in **≥ 6 distinct months**; otherwise an *episode*, costed and shown but ranked last, outside the headline total, not drafted. Two of twenty are episodes.

Threshold **$100/month** selects the top four recurring processes; higher left one, lower reached processes whose evidence is thinner than their dollars. The drafters chose: an **SOP** for power-settlement reconciliation (work done from memory, so a procedure changes the next morning most); a reusable **email** for meter-flow-without-a-valid-deal (every request is the same hand-typed note to one approver); an **SOP** for real-time schedule-cut and variance corrections; a **checklist** for the real-time position hand-off and Enpower/CAPS entry. Where a drafter used a fact that came from the synthesizer's description rather than a quote (a counterparty-suspension check, a deal-owner name), it marked the step `[to confirm]` instead of presenting it as evidence. The bankruptcy template from the first pass is kept because it is usable, but it sits with the episodes.

## Where the system is most likely wrong

1. **The dollars are floors for four people, not company totals.** Counts come from dated, de-duplicated mail in four mailboxes; phone, systems and everyone else's mail are invisible. Recurring total **$1,332/month (15.7 h)**, no extrapolation — I had no basis for a multiplier and did not invent one.
2. **One message ≈ one occurrence.** Five chasers count five; a job done by phone counts zero.
3. **Minutes per occurrence is the model's guess** (bounded, shown everywhere) and the biggest lever on every figure.
4. **Process boundaries are a judgement.** 232 items merged into 20; a different cut moves dollars between rows. Auditable (`merged_from`), not uniquely right.
5. **Six distinct months is a chosen line** that fits this corpus.

## Taken on faith

- $85/hour applies to everyone in these mailboxes.
- Each observer read every line of its batch: the hook checks the output, not the reading; attribution coverage (1,623 of 3,194 unique messages) is the only indirect signal.
- The models' minutes and automatable-share estimates are of the right order of magnitude.
- The planted anomalies I found are the ones that were planted.

## With another week

- A second, independent observer pass per batch with a code-level agreement check; disagreement gets flagged.
- Occurrences counted per thread, not per message, with the model asked to confirm.
- A what-if slider on minutes and automatable share, and per-process time series.
- A `verify` command that samples N claims and prints the raw context for a human auditor — the check the reviewer is about to do by hand.
