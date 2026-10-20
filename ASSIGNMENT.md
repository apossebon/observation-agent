# Build assignment: an observation agent

You are given a company's email archive. Build a system that reads all of it, works out where that company is losing time, proves every claim it makes, and puts the result on a dashboard. It should also act on what it finds rather than only describing it.

Claude Code is the runtime here. The thing you deliver runs inside it and is driven by it. That is the exercise.

## The corpus

A subset of the Enron email archive, 3,240 messages, at `corpus/` in this repo. It is raw. Some messages have no usable date. Some are duplicated. One is enormous. The formatting is inconsistent because it came off a real mail server in 2002.

It is about thirty times larger than a single context window. Everything about this assignment follows from that.

## What it has to do

One command, and the system:

1. Reads every message in the corpus. Not a sample.

2. Identifies the recurring processes at that company: the work that happens over and over, who touches it, how often, and where it stalls.

3. Ranks the automation opportunities. Each one carries an estimate of hours per month and dollars per month at a blended $85/hour.

4. Cites everything. Every process and every opportunity traces back to specific messages, each carrying a verbatim quote. A claim that cannot name its evidence does not ship. I will pull claims at random and check them against the raw files.

5. Acts. For the opportunities above a threshold you choose, produce a drafted artifact someone could use the next morning: a written SOP, a draft email, a checklist, a template. You decide what is worth producing, and you defend that decision in your notes.

6. Serves a dashboard on localhost. Ranked opportunities, the running dollar total, and drill-through on every claim. If I cannot click a number and land on the message it came from, the dashboard is not finished. It should look like something I would put in front of a client president.

## Constraints

- No paid API keys and no API spend, yours or mine. It runs on your Claude Code subscription. Wanting to buy tokens means the design went wrong somewhere.
- A full run completes unattended in under 30 minutes.
- Re-running against an unchanged corpus does not repeat finished work.
- Anything that has to be exactly right is deterministic code rather than a model call. Parsing, deduplication, the hours and dollars arithmetic, citation validation, the server. I will check whether a model was left holding any of it.
- Tests pass without invoking a model at all.
- Python or TypeScript for the deterministic parts.
- Everything runs locally.

## What to send back

- The repo.
- Your `.claude/` directory exactly as you used it. CLAUDE.md, subagents, skills, hooks, slash commands, settings, whatever you built.
- `NOTES.md`, two pages at most. How you drove Claude Code. What you handed to subagents and why. How you budgeted their context. What you ran in parallel. Where Claude Code got it wrong and how you caught it before it reached the output. What you would build next with another week.
- In those notes, tell me where your system is most likely to be wrong, and what it took on faith because you had no way to check it.
- The output of one real run: the report, the dashboard, the run logs, and the drafted artifacts.

Push all of it to your own repo and send me the link.
