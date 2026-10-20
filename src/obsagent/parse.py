"""Deterministic email parsing.

Every message in the corpus becomes a `Message` record. Nothing in here calls a
model. The raw file text is kept verbatim so that citations can be validated
against it later; a separate `clean_body` is produced for the model to read.
"""
from __future__ import annotations

import email
import hashlib
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from email import policy
from email.utils import parsedate_to_datetime, getaddresses
from pathlib import Path
from typing import Iterable

# Dates outside this window are treated as unusable (the corpus is 1999-2002).
MIN_YEAR, MAX_YEAR = 1998, 2003

_QUOTE_SPLIT = re.compile(
    r"^\s*(-{3,}\s*Original Message\s*-{3,}|-{3,}\s*Forwarded by .*?-{3,}|"
    r"From:\s.*?\nSent:\s.*?\n|_{10,}|>{1,}\s)",
    re.M | re.S,
)
_SUBJECT_PREFIX = re.compile(r"^\s*((re|fw|fwd)\s*:\s*)+", re.I)
_WS = re.compile(r"\s+")


@dataclass
class Message:
    id: str                 # stable id: relative path without trailing dot, e.g. "giron-d/sent/795"
    path: str               # path relative to corpus root
    sha1: str               # sha1 of raw bytes
    mailbox: str            # top-level folder (owner of the mailbox)
    folder: str             # second-level folder
    message_id: str
    date: str | None        # ISO 8601 UTC, None when missing/invalid
    date_raw: str
    sender: str
    recipients: list[str]
    cc: list[str]
    subject: str
    subject_norm: str       # lower, prefixes stripped, whitespace collapsed
    body: str               # full body text as stored in the file
    clean_body: str         # body with quoted/forwarded tails removed
    truncated: bool = False
    size: int = 0
    extra: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def normalize_subject(subject: str) -> str:
    s = _SUBJECT_PREFIX.sub("", subject or "")
    return _WS.sub(" ", s).strip().lower()


def normalize_ws(text: str) -> str:
    return _WS.sub(" ", text or "").strip()


def parse_date(raw: str | None) -> str | None:
    if not raw:
        return None
    try:
        dt = parsedate_to_datetime(raw)
    except Exception:
        return None
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    if not (MIN_YEAR <= dt.year <= MAX_YEAR):
        return None
    return dt.astimezone(timezone.utc).isoformat()


def _addresses(value: str | None) -> list[str]:
    if not value:
        return []
    return sorted({a.strip().lower() for _, a in getaddresses([value]) if a.strip()})


def split_quoted(body: str) -> tuple[str, str]:
    """Split the body into (authored part, quoted/forwarded tail)."""
    m = _QUOTE_SPLIT.search(body)
    if not m:
        return body.strip(), ""
    return body[: m.start()].strip(), body[m.start():].strip()


def strip_quoted(body: str) -> str:
    return split_quoted(body)[0]


QUOTED_TAIL_CHARS = 2500


def clean_for_model(body: str, max_body_chars: int) -> tuple[str, bool]:
    """Authored text in full, plus a capped slice of the quoted/forwarded tail.

    Forwarded mail is often the only content of a message ("FYI" + a forward),
    so the tail cannot be dropped outright; it is capped so one long forward
    cannot crowd out a batch.
    """
    head, tail = split_quoted(body)
    truncated = False
    if len(tail) > QUOTED_TAIL_CHARS:
        tail = tail[:QUOTED_TAIL_CHARS] + "\n[... quoted tail truncated by parser ...]"
        truncated = True
    text = (head + "\n\n" + tail).strip() if tail else head
    if len(text) > max_body_chars:
        text = text[:max_body_chars] + "\n[... truncated by parser ...]"
        truncated = True
    return text, truncated


def parse_file(path: Path, corpus_root: Path, max_body_chars: int = 6000) -> Message:
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    msg = email.message_from_string(text, policy=policy.compat32)
    rel = path.relative_to(corpus_root).as_posix()
    parts = rel.split("/")
    body = msg.get_payload()
    if isinstance(body, list):  # multipart (not expected in this corpus)
        body = "\n".join(p.get_payload() for p in msg.walk() if not p.is_multipart())
    body = body or ""
    clean, truncated = clean_for_model(body, max_body_chars)
    return Message(
        id=rel.rstrip("."),
        path=rel,
        sha1=hashlib.sha1(raw).hexdigest(),
        mailbox=parts[0],
        folder=parts[1] if len(parts) > 2 else "",
        message_id=(msg.get("Message-ID") or "").strip(),
        date=parse_date(msg.get("Date")),
        date_raw=(msg.get("Date") or "").strip(),
        sender=(_addresses(msg.get("From")) or [""])[0],
        recipients=_addresses(msg.get("To")),
        cc=_addresses(msg.get("Cc")),
        subject=normalize_ws(msg.get("Subject") or ""),
        subject_norm=normalize_subject(msg.get("Subject") or ""),
        body=body,
        clean_body=clean,
        truncated=truncated,
        size=len(raw),
        extra={"x_from": msg.get("X-From", ""), "x_to": msg.get("X-To", "")},
    )


def iter_corpus_files(corpus_root: Path) -> Iterable[Path]:
    return sorted(p for p in corpus_root.rglob("*") if p.is_file())


def parse_corpus(corpus_root: Path, max_body_chars: int = 6000) -> list[Message]:
    return [parse_file(p, corpus_root, max_body_chars) for p in iter_corpus_files(corpus_root)]
