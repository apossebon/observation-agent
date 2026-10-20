#!/usr/bin/env bash
# One command, unattended: runs the whole pipeline inside Claude Code and
# leaves the dashboard running on localhost.
#
#   ./run.sh                     normal run (skips finished work)
#   ./run.sh --force             redo the model stages
#   ./run.sh --threshold 300     change the draft threshold ($/month)
#
# Requires: Claude Code on PATH with a subscription login (no API key),
#           Python 3.11+. No other dependencies.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p out/logs
echo "$(date -u +%FT%TZ) run.sh start $*" >> out/logs/run.log

# Deterministic tests first: if these fail, nothing downstream is trustworthy.
PYTHONPATH=src python3 -m pytest -q 2>&1 | tail -1 | tee -a out/logs/run.log

# Hand the run to Claude Code. The /observe command does the orchestration;
# permission mode lets the hook-validated writes under out/ and the python
# calls proceed without prompts.
claude -p "/observe $*" \
  --permission-mode acceptEdits \
  --max-turns 300 \
  --output-format text 2>&1 | tee -a out/logs/claude.log

echo "$(date -u +%FT%TZ) run.sh end" >> out/logs/run.log
echo "Dashboard: http://127.0.0.1:8765/  (restart later with: PYTHONPATH=src python3 -m obsagent serve)"
