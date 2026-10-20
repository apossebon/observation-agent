#!/usr/bin/env bash
# SubagentStop hook: one timestamped line per finished subagent, for the run log.
cd "$(dirname "$0")/../.." || exit 0
mkdir -p out/logs
python3 - <<'PY' >> out/logs/subagents.log
import json, sys, datetime
try:
    d = json.load(sys.stdin)
except Exception:
    d = {}
print(datetime.datetime.now(datetime.timezone.utc).isoformat(), "subagent stop",
      d.get("agent_type") or d.get("subagent_type") or "", d.get("agent_id") or d.get("session_id") or "")
PY
exit 0
