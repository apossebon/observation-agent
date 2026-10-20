#!/usr/bin/env bash
# PostToolUse hook (Write|Edit). Receives the tool call as JSON on stdin.
# Validates observer/synthesizer JSON the moment it is written: schema, batch
# membership, and every quote against the raw corpus. Exit 2 => the problems
# are fed back to the agent that wrote the file, which fixes and rewrites it.
cd "$(dirname "$0")/../.." || exit 0
PYTHONPATH=src exec python3 -m obsagent check
