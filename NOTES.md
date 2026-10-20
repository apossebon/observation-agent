# NOTES

## How I drove Claude Code

The whole run is one slash command, `/observe` (`.claude/commands/observe.md`), which `run.sh` invokes headless with `claude -p`. The command is an orchestrator, not a worker: it runs the deterministic CLI (`python3 -m obsagent …`), reads only `manifest.json` and CLI output, and delegates every judgement to subagents with a fixed, small input. It never opens a batch file or a corpus file; its own context stays at a few thousand tokens for the whole run.

Three subagents, each with a single-purpose prompt and `Read`+`Write` only:

| agent | gets | returns | why that shape |
|---|---|---|---|
| `observer` ×28 (sonnet) | one batch file, ≤35k tokens, ~110 messages threaded by subject | `batch_NNN.json`: 4–12 processes, every message id that belongs to each, 2–5 verbatim quotes each, two estimates | The only stage that reads mail. Threading by subject means a recurring conversation lands in one observer rather than being split across contexts. |
| `synthesizer` ×1 (opus) | `observations_compact.json` (~25k tokens: one line per per-batch process, two sample quotes) | `synthesis.json`: merged processes referencing per-batch ones by `"<batch>:<name>"` | Merging by reference is what keeps this stage small and honest: code unions the message ids and the already-validated quotes, so the synthesizer cannot invent or lose evidence while copying. |
| `drafter` ×N (sonnet) | one `draft_inputs/<slug>.json` (description, stall points, economics, ≤12 validated quotes with line numbers) | one or two markdown artifacts | Never sees the corpus; everything it writes traces to quotes already validated. |

Parallelism: observers in waves of 6 (six `Task` calls per message), drafters in one wave. Validation, economics and report run between waves as cheap CLI calls.

Context budget per observer: 35k tokens of batch + ~2k of instructions + output. Below the point where sonnet starts skimming; I tested 50k batches and the observer's attributions got thinner in the second half.

## What is code and what is model

Code: parsing, de-duplication (normalised sender+subject+body), date validation (two planted bad dates and one in 2031 become `null`), threading, batch packing, citation validation, `merged_from` expansion, all hours/dollars arithmetic, ranking, threshold, report, dashboard, server. All of it under `tests/` (19 tests, no model).

Model: which messages form a recurring process, how to describe it, `minutes_per_occurrence`, `automatable_fraction`, draft wording. Both numeric estimates are shown next to every total on the dashboard so a reader can disagree with them in place.

## Where Claude Code got it wrong, and how it was caught

- **Quotes that were paraphrases.** Early observer drafts "cleaned up" punctuation or merged two sentences. The PostToolUse hook (`check_observation.sh` → `obsagent check`) validates every quote against the raw file the moment the JSON is written and returns the exact failures (exit 2); the subagent fixes and rewrites. Final-run hook log: `out/logs/hooks.log`. Anything still wrong at the end is dropped by `obsagent validate`, never shown.
- **Citing the parser's header line.** Observers quoted `date: … | from: …`, which is not in the raw file. Caught by the same hook; the prompt now says so explicitly.
- **Reading only the first 2,000 lines.** Claude Code's `Read` pages at 2,000 lines; a batch is ~4,000. The first pilot observer silently stopped early. Fixed in the prompt (page with offset/limit until empty) and visible in the attribution counts.
- **Message ids from the wrong batch.** An observer cited an id it remembered from the subject line of a forwarded mail. The hook rejects ids outside the batch.
- **Synthesizer copying ids.** The first synthesizer version copied hundreds of ids by hand and dropped some. Replaced by `merged_from` references expanded in code.

## Threshold and the artifacts

Threshold: **$_____ / month**. Rationale: …

Artifacts produced: …

## Where the system is most likely wrong

1. **Frequency is undercounted and skewed to four people.** Occurrences are counted from dated, de-duplicated messages in four mailboxes. Work that happened by phone, in a system, or in mailboxes we do not have is invisible. No extrapolation is applied, so the dollar figures are floors for these four people, not company totals.
2. **Minutes per occurrence is the model's guess.** It is bounded (1–480) and shown everywhere, but it is the single largest lever on every dollar figure.
3. **Process boundaries are a judgement.** Two observers can split one process or merge two; the synthesizer reconciles, but a merge decision moves dollars between rows.
4. **Duplicate detection is content-based.** Near-duplicates with different trailing signatures survive; the inflation is small (46 exact duplicates were removed) but non-zero.
5. **Subject threading mis-groups mail with blank subjects** (107 messages); those are read as singletons.

## Taken on faith

- That the $85/hour blended rate applies to everyone in these mailboxes.
- That a message is a reasonable proxy for one occurrence of a process.
- That the observer read every line of its batch (the hook checks the output, not the reading; attribution coverage is the only indirect signal).
- That sonnet's estimates of minutes and automatable share are of the right order of magnitude.

## With another week

- A second, independent observer pass per batch and a code-level agreement check, so a process reported by only one pass is flagged.
- Occurrence counting from thread structure rather than message count (one occurrence = one thread), with the model asked to confirm.
- Per-person time series on the dashboard, and a "what if" slider on minutes and automatable share.
- A `verify` command that samples N claims and prints the raw context for a human auditor — the thing the reviewer is about to do by hand.
