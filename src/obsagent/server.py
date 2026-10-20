"""Localhost dashboard — Python stdlib only.

Routes:
  /                      the dashboard (ranked opportunities, running total, drill-through)
  /api/dashboard         out/dashboard.json
  /api/message/<id>      raw text + metadata of one corpus message
  /msg/<id>?line=N       raw message page with the cited line highlighted
  /drafts/<file>         a drafted artifact (markdown, rendered as text)
"""
from __future__ import annotations

import html
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

STATIC = Path(__file__).parent / "static"


def make_handler(corpus: Path, out: Path):
    index = json.loads((out / "messages.json").read_text("utf-8"))
    known = {m["id"]: m for m in index["messages"]}
    aliases = index["aliases"]

    def resolve(mid: str):
        mid = mid.strip("/").rstrip(".")
        return mid if mid in known else aliases.get(mid)

    class H(SimpleHTTPRequestHandler):
        def log_message(self, fmt, *args):  # quieter
            pass

        def _send(self, body: bytes, ctype="text/html; charset=utf-8", code=200):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            u = urlparse(self.path)
            p = u.path
            if p in ("/", "/index.html"):
                return self._send((STATIC / "dashboard.html").read_bytes())
            if p == "/api/dashboard":
                return self._send((out / "dashboard.json").read_bytes(), "application/json")
            if p.startswith("/api/message/"):
                mid = resolve(p[len("/api/message/"):])
                if not mid:
                    return self._send(b'{"error":"unknown message"}', "application/json", 404)
                raw = (corpus / (mid + ".")).read_text("utf-8", errors="replace")
                return self._send(json.dumps({"id": mid, "meta": known[mid], "raw": raw}).encode(), "application/json")
            if p.startswith("/msg/"):
                mid = resolve(p[len("/msg/"):])
                if not mid:
                    return self._send(b"unknown message", "text/plain", 404)
                line = int((parse_qs(u.query).get("line") or ["0"])[0] or 0)
                return self._send(render_message_page(corpus, mid, known[mid], line).encode())
            if p.startswith("/drafts/"):
                f = (out / "drafts" / Path(p).name)
                if not f.exists():
                    return self._send(b"not found", "text/plain", 404)
                return self._send(render_draft_page(f).encode())
            if p == "/report.md":
                return self._send((out / "report.md").read_bytes(), "text/markdown; charset=utf-8")
            return self._send(b"not found", "text/plain", 404)

    return H


def render_message_page(corpus: Path, mid: str, meta: dict, line: int) -> str:
    raw = (corpus / (mid + ".")).read_text("utf-8", errors="replace")
    rows = []
    for i, l in enumerate(raw.split("\n"), 1):
        cls = ' class="hit" id="hit"' if i == line else ""
        rows.append(f"<tr{cls}><td class=n>{i}</td><td><pre>{html.escape(l) or ' '}</pre></td></tr>")
    return f"""<!doctype html><html><head><meta charset=utf-8><title>{html.escape(mid)}</title>
<style>
body{{font:14px/1.45 ui-sans-serif,system-ui;margin:0;background:#f6f7f9;color:#1b1f24}}
header{{background:#0f2a43;color:#fff;padding:14px 22px}} header a{{color:#9fd0ff}}
.meta{{font-size:12px;opacity:.85;margin-top:4px}}
table{{border-collapse:collapse;width:100%;background:#fff}} td{{vertical-align:top;padding:0 10px}}
td.n{{color:#999;text-align:right;width:44px;user-select:none;font:12px ui-monospace,monospace;padding-top:2px}}
pre{{margin:0;white-space:pre-wrap;word-break:break-word;font:13px ui-monospace,SFMono-Regular,Menlo,monospace}}
tr.hit{{background:#fff3b0;outline:2px solid #e2a800}}
</style></head><body>
<header><a href="/">← back to dashboard</a> &nbsp; <b>{html.escape(mid)}</b>
<div class=meta>{html.escape(meta.get('date') or meta.get('date_raw') or 'no usable date')} · from {html.escape(meta.get('sender',''))} · {html.escape(meta.get('subject',''))}
 · raw file: corpus/{html.escape(mid)}. ({meta.get('size',0)} bytes){' · cited line ' + str(line) if line else ''}</div></header>
<table>{''.join(rows)}</table>
<script>var h=document.getElementById('hit');if(h)h.scrollIntoView({{block:'center'}});</script>
</body></html>"""


def render_draft_page(f: Path) -> str:
    return f"""<!doctype html><html><head><meta charset=utf-8><title>{html.escape(f.name)}</title>
<style>body{{font:15px/1.55 ui-sans-serif,system-ui;max-width:860px;margin:30px auto;padding:0 20px;color:#1b1f24}}
a{{color:#0b57d0}} pre{{white-space:pre-wrap;background:#fff;border:1px solid #e3e6ea;padding:18px;border-radius:8px}}</style>
</head><body><a href="/">← back to dashboard</a><h2>{html.escape(f.name)}</h2><pre>{html.escape(f.read_text('utf-8'))}</pre></body></html>"""


def serve(corpus: Path, out: Path, host="127.0.0.1", port=8765):
    handler = make_handler(corpus, out)
    srv = None
    for p in range(port, port + 10):  # a stale server from an earlier run may still hold the port
        try:
            srv = ThreadingHTTPServer((host, p), handler); port = p; break
        except OSError:
            continue
    if srv is None:
        raise SystemExit(f"[obsagent] no free port in {port}-{port + 9}")
    print(f"[obsagent] dashboard at http://{host}:{port}/  (Ctrl-C to stop)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
