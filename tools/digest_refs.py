#!/usr/bin/env python3
"""Expand cross-interview timestamp tokens in digest/summary.md (policy P13, P14).

Write  {01@42:02}  or  {02@1:09:45–1:19:00}  in the digest; this script rewrites each token, in place, to
  01 [\\[42:02\\]](https://www.youtube.com/watch?v=<id>&t=<seconds minus 8>s)
(the interview number as plain text, then the canonical linked time). Idempotent: expanded links are left alone, so
rerun it after any edit. Interview numbers and video ids come from tools/link_timestamps.py's table."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAD = 8
VID = {"01": "v2N5ESMKI4g", "02": "_-LTnN5BeBs", "03": "POZfdI0f4TU"}
T = r"\d{1,2}(?::\d{2}){1,2}"


def secs(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def fmt(t):
    n = secs(t)
    h, m, s = n // 3600, n % 3600 // 60, n % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def expand(m):
    n, a, b = m.group(1), m.group(2), m.group(3)
    if n not in VID:
        raise SystemExit(f"unknown interview {n} in token {m.group(0)}")
    text = fmt(a) + (f"–{fmt(b)}" if b else "")
    return f"{n} [\\[{text}\\]](https://www.youtube.com/watch?v={VID[n]}&t={max(0, secs(a) - LEAD)}s)"


p = ROOT / "digest" / "summary.md"
s = p.read_text()
out = re.sub(rf"\{{(\d\d)@({T})(?:[–-]({T}))?\}}", expand, s)
if out != s:
    p.write_text(out)
print(f"digest/summary.md: {out.count('youtube.com/watch?v=')} timestamp links; {len(re.findall('[{][0-9][0-9]@', out))} tokens left")
