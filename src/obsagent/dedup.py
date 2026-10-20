"""Deterministic de-duplication.

Two messages are duplicates when, after normalisation, they share the same
sender, subject and authored body. This catches the same email stored in the
sender's "sent" folder and in a recipient's inbox (different Message-IDs, same
content). Exact Message-ID collisions are caught as well.

The first occurrence (in sorted path order) is kept as canonical; the others
are recorded so a citation to a dropped duplicate can be redirected.
"""
from __future__ import annotations

import hashlib
from .parse import Message, normalize_ws


def content_key(m: Message) -> str:
    key = "|".join([m.sender, m.subject_norm, normalize_ws(m.clean_body).lower()[:4000]])
    return hashlib.sha1(key.encode("utf-8")).hexdigest()


def dedupe(messages: list[Message]) -> tuple[list[Message], dict[str, str]]:
    """Return (unique_messages, alias_map) where alias_map maps dropped id -> kept id."""
    seen_content: dict[str, str] = {}
    seen_msgid: dict[str, str] = {}
    kept: list[Message] = []
    aliases: dict[str, str] = {}
    for m in sorted(messages, key=lambda x: x.path):
        ck = content_key(m)
        canonical = seen_content.get(ck)
        if canonical is None and m.message_id:
            canonical = seen_msgid.get(m.message_id)
        if canonical is not None:
            aliases[m.id] = canonical
            continue
        seen_content[ck] = m.id
        if m.message_id:
            seen_msgid[m.message_id] = m.id
        kept.append(m)
    return kept, aliases
