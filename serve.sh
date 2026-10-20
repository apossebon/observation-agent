#!/usr/bin/env bash
# Start (or restart) the dashboard in the background on http://127.0.0.1:8765/
cd "$(dirname "$0")"
PORT="${1:-8765}"
mkdir -p out/logs
if [ -f out/server.pid ] && kill -0 "$(cat out/server.pid)" 2>/dev/null; then
  kill "$(cat out/server.pid)"; sleep 0.5
fi
PYTHONPATH=src setsid nohup python3 -m obsagent serve --port "$PORT" > out/logs/server.log 2>&1 < /dev/null &
echo $! > out/server.pid
sleep 1
cat out/logs/server.log
