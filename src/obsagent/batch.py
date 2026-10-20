"""Thread grouping and batch planning.

Messages are grouped into threads by normalised subject so that an observer
subagent sees a recurring conversation together rather than scattered across
batches. Threads are then packed into batches under a fixed token budget.
Token counts are estimated deterministically (chars / 4) — an over-estimate is
fine, it only makes batches smaller.
"""
from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from .parse import Message

CHARS_PER_TOKEN = 4
DEFAULT_BATCH_TOKENS = 35_000
MAX_THREAD_MESSAGES = 60  # a thread larger than this is split


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // CHARS_PER_TOKEN)


def render_message(m: Message) -> str:
    to = ", ".join(m.recipients[:6]) + (" ..." if len(m.recipients) > 6 else "")
    cc = (" | cc: " + ", ".join(m.cc[:4])) if m.cc else ""
    date = m.date[:10] if m.date else "(no usable date)"
    return (
        f"### MSG {m.id}\n"
        f"date: {date} | from: {m.sender} | to: {to}{cc}\n"
        f"subject: {m.subject}\n\n"
        f"{m.clean_body}\n"
    )


def group_threads(messages: list[Message]) -> list[list[Message]]:
    by_subject: dict[str, list[Message]] = defaultdict(list)
    singles: list[list[Message]] = []
    for m in messages:
        if m.subject_norm:
            by_subject[m.subject_norm].append(m)
        else:
            singles.append([m])
    threads: list[list[Message]] = []
    for subj, ms in by_subject.items():
        ms.sort(key=lambda x: (x.date or "9999", x.path))
        for i in range(0, len(ms), MAX_THREAD_MESSAGES):
            threads.append(ms[i : i + MAX_THREAD_MESSAGES])
    threads.extend(singles)
    # chronological by first dated message; undated threads go last, stable by path
    threads.sort(key=lambda t: (min((m.date or "9999") for m in t), t[0].path))
    return threads


@dataclass
class Batch:
    index: int
    message_ids: list[str]
    tokens: int
    text: str


def plan_batches(messages: list[Message], budget_tokens: int = DEFAULT_BATCH_TOKENS) -> list[Batch]:
    batches: list[Batch] = []
    cur_ids: list[str] = []
    cur_text: list[str] = []
    cur_tokens = 0

    def flush():
        nonlocal cur_ids, cur_text, cur_tokens
        if cur_ids:
            batches.append(Batch(len(batches), cur_ids, cur_tokens, "\n".join(cur_text)))
        cur_ids, cur_text, cur_tokens = [], [], 0

    for thread in group_threads(messages):
        rendered = [render_message(m) for m in thread]
        t_tokens = sum(estimate_tokens(r) for r in rendered)
        if cur_tokens and cur_tokens + t_tokens > budget_tokens:
            flush()
        if t_tokens > budget_tokens:  # split an oversized thread message by message
            for m, r in zip(thread, rendered):
                rt = estimate_tokens(r)
                if cur_tokens and cur_tokens + rt > budget_tokens:
                    flush()
                cur_ids.append(m.id); cur_text.append(r); cur_tokens += rt
            continue
        cur_ids.extend(m.id for m in thread)
        cur_text.extend(rendered)
        cur_tokens += t_tokens
    flush()
    return batches


def write_batches(batches: list[Batch], out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    manifest = []
    for b in batches:
        p = out_dir / f"batch_{b.index:03d}.md"
        p.write_text(f"# Batch {b.index:03d} — {len(b.message_ids)} messages, ~{b.tokens} tokens\n\n" + b.text, encoding="utf-8")
        paths.append(p)
        manifest.append({"index": b.index, "file": p.name, "messages": len(b.message_ids), "tokens": b.tokens, "message_ids": b.message_ids})
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    return paths
