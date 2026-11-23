#!/usr/bin/env python3
"""Link every video timestamp in the summaries and slide indexes to YouTube, LEAD seconds early (user, 2026-11-22: 5-10 s so the listener can get ready).
Idempotent: only unlinked timestamps are changed. Usage: tools/link_timestamps.py   (run from anywhere; edits files in place)
Patterns handled:  [mm:ss] / [h:mm:ss] / [a–b] in prose and headings;  '| mm:ss |' first table cell;  slide-index '| N | hh:mm:ss |'."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAD = 8
VID = {"01.national_status_and_passport": "v2N5ESMKI4g",
       "02.national_status_and_right_to_travel": "_-LTnN5BeBs",
       "03.building_freedom_from_the_ground_up": "POZfdI0f4TU"}
T = r"\d{1,2}(?::\d{2}){1,2}"


def secs(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def url(vid, t):
    return f"https://www.youtube.com/watch?v={vid}&t={max(0, secs(t) - LEAD)}s"


def link_text(s, vid):
    # [mm:ss] or [a–b] (not already followed by '(')
    s = re.sub(rf"\[({T})((?:–|-)({T}))?\](?!\()",
               lambda m: f"[\\[{m.group(1)}{m.group(2) or ''}\\]]({url(vid, m.group(1))})", s)
    # parenthesised ranges: (00:00–02:25) and (04:42 to 53:45)
    s = re.sub(rf"\(({T})((?:–|-| to )({T}))\)(?!\()",
               lambda m: f"([{m.group(1)}{m.group(2)}]({url(vid, m.group(1))}))", s)
    # first table cell
    s = re.sub(rf"(?m)^\| ({T}) \|", lambda m: f"| [{m.group(1)}]({url(vid, m.group(1))}) |", s)
    return s


def link_index(s, vid):
    return re.sub(r"(?m)^\| (\d+) \| (\d\d:\d\d:\d\d) \|",
                  lambda m: f"| {m.group(1)} | [{m.group(2)}]({url(vid, m.group(2))}) |", s)


for folder, vid in VID.items():
    for rel, fn in ((f"{folder}/summary.md", link_text), (f"{folder}/slides/slides-index.md", link_index)):
        p = ROOT / rel
        a = p.read_text()
        b = fn(a, vid)
        if a != b:
            p.write_text(b)
        print(f"{rel}: {len(re.findall(r'watch\?v=' + re.escape(vid) + r'&t=', b))} timestamp links")
