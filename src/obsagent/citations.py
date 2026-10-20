"""Citation validation — deterministic, no model.

A citation is `{"msg": "<message id>", "quote": "<verbatim text>"}`. It is
valid when the message exists in the corpus (aliases of dropped duplicates are
redirected to the kept copy) and the quote, after whitespace collapsing, is a
case-sensitive substring of the raw file's text. The line number of the first
match is recorded so the dashboard can jump to it.

Anything that fails is removed and logged. A process left with no valid
citations is removed entirely — a claim that cannot name its evidence does not
ship.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

_WS = re.compile(r"\s+")
MIN_QUOTE_CHARS = 12
MAX_QUOTE_CHARS = 400


def _norm(s: str) -> str:
    return _WS.sub(" ", s).strip()


@dataclass
class Citation:
    msg: str
    quote: str
    line: int | None = None
    ok: bool = False
    reason: str = ""


@dataclass
class ValidationReport:
    checked: int = 0
    valid: int = 0
    rejected: list[dict] = field(default_factory=list)
    processes_dropped: list[str] = field(default_factory=list)

    def summary(self) -> dict:
        return {
            "checked": self.checked,
            "valid": self.valid,
            "rejected": len(self.rejected),
            "processes_dropped": self.processes_dropped,
        }


class CorpusIndex:
    """Raw text of every message, keyed by id, with duplicate aliases."""

    def __init__(self, corpus_root: Path, ids: list[str], aliases: dict[str, str]):
        self.root = corpus_root
        self.ids = set(ids)
        self.aliases = aliases
        self._cache: dict[str, str] = {}

    def resolve(self, msg_id: str) -> str | None:
        msg_id = msg_id.strip().rstrip(".")
        if msg_id in self.ids:
            return msg_id
        return self.aliases.get(msg_id)

    def raw(self, msg_id: str) -> str:
        if msg_id not in self._cache:
            self._cache[msg_id] = (self.root / (msg_id + ".")).read_text("utf-8", errors="replace")
        return self._cache[msg_id]


def find_quote(raw: str, quote: str) -> int | None:
    """Return 1-based line number of the first line where the quote starts, or None."""
    q = _norm(quote)
    if not q:
        return None
    # Fast path: exact substring in raw.
    pos = raw.find(quote.strip())
    if pos < 0:
        # Whitespace-insensitive match: build a regex that allows any whitespace run.
        pattern = r"\s+".join(re.escape(tok) for tok in q.split(" "))
        m = re.search(pattern, raw)
        if not m:
            return None
        pos = m.start()
    return raw.count("\n", 0, pos) + 1


def validate_citation(index: CorpusIndex, c: dict) -> Citation:
    cit = Citation(msg=str(c.get("msg", "")), quote=str(c.get("quote", "")))
    resolved = index.resolve(cit.msg)
    if not resolved:
        cit.reason = "unknown message id"; return cit
    cit.msg = resolved
    if len(_norm(cit.quote)) < MIN_QUOTE_CHARS:
        cit.reason = "quote too short"; return cit
    if len(cit.quote) > MAX_QUOTE_CHARS:
        cit.reason = "quote too long"; return cit
    line = find_quote(index.raw(resolved), cit.quote)
    if line is None:
        cit.reason = "quote not found verbatim"; return cit
    cit.line, cit.ok = line, True
    return cit


def validate_processes(index: CorpusIndex, processes: list[dict], report: ValidationReport, source: str = "") -> list[dict]:
    """Validate the `evidence` list of each process in place; drop processes with none left."""
    kept: list[dict] = []
    for p in processes:
        good = []
        for raw_c in p.get("evidence", []) or []:
            report.checked += 1
            c = validate_citation(index, raw_c)
            if c.ok:
                report.valid += 1
                good.append({"msg": c.msg, "quote": c.quote, "line": c.line})
            else:
                report.rejected.append({"source": source, "process": p.get("name"), "msg": c.msg, "quote": c.quote[:120], "reason": c.reason})
        # message ids claimed for frequency counting must exist too
        msgs = []
        for mid in p.get("messages", []) or []:
            r = index.resolve(str(mid))
            if r and r not in msgs:
                msgs.append(r)
        for c in good:
            if c["msg"] not in msgs:
                msgs.append(c["msg"])
        if not good:
            report.processes_dropped.append(f"{source}:{p.get('name')}")
            continue
        p = dict(p); p["evidence"] = good; p["messages"] = msgs
        kept.append(p)
    return kept
