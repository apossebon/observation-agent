"""Run state and idempotency.

`out/state.json` records a fingerprint for each completed stage. A stage is
skipped when its input fingerprint is unchanged. The corpus fingerprint is the
sha1 over every file's (path, sha1), so touching any file invalidates the run
while a byte-identical corpus never repeats finished work.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def corpus_fingerprint(pairs: list[tuple[str, str]]) -> str:
    h = hashlib.sha1()
    for path, sha in sorted(pairs):
        h.update(f"{path}:{sha}\n".encode())
    return h.hexdigest()


def file_fingerprint(paths: list[Path]) -> str:
    h = hashlib.sha1()
    for p in sorted(paths):
        h.update(p.name.encode()); h.update(hashlib.sha1(p.read_bytes()).digest())
    return h.hexdigest()


class RunState:
    def __init__(self, out_dir: Path):
        self.path = out_dir / "state.json"
        self.data = json.loads(self.path.read_text()) if self.path.exists() else {"stages": {}}

    def is_done(self, stage: str, fingerprint: str) -> bool:
        s = self.data["stages"].get(stage)
        return bool(s and s.get("fingerprint") == fingerprint and s.get("done"))

    def mark(self, stage: str, fingerprint: str, **info):
        self.data["stages"][stage] = {
            "fingerprint": fingerprint,
            "done": True,
            "at": datetime.now(timezone.utc).isoformat(),
            **info,
        }
        self.save()

    def invalidate_from(self, stage: str, order: list[str]):
        """Drop this stage and every later one (their inputs changed)."""
        if stage in order:
            for s in order[order.index(stage):]:
                self.data["stages"].pop(s, None)
        self.save()

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=1))


STAGES = ["prepare", "observe", "validate", "synthesize", "economics", "draft", "report"]
