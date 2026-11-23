#!/usr/bin/env python3
"""Link and normalise every video timestamp in the summaries and slide indexes (policy P13).

ONE form everywhere:  [mm:ss] under an hour, [h:mm:ss] over; ranges [a–b] (en dash); square brackets are part of the
link text; the link opens the video LEAD seconds before the stated start (user, 2026-11-22: 5-10 s so the listener can
get ready):  [\\[16:55–32:00\\]](https://www.youtube.com/watch?v=<id>&t=<seconds>s)

Idempotent. It (1) rewrites already-linked timestamps (any older form: bare, parenthesised, 'a to b', hh:mm:ss) into the
canonical form, then (2) links raw timestamps. Raw forms handled: [mm:ss], [a–b], (a–b), (a to b), the first cell of a table
row, and the Time cell of a slides-index row. Clock times of day (3:00 pm PT) are not touched.
Usage: tools/link_timestamps.py   (edits files in place)"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAD = 8
VID = {"01.national_status_and_passport": "v2N5ESMKI4g",
       "02.national_status_and_right_to_travel": "_-LTnN5BeBs",
       "03.building_freedom_from_the_ground_up": "POZfdI0f4TU"}
T = r"\d{1,2}(?::\d{2}){1,2}"
SEP = r"(?:–|-| to )"


def secs(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def fmt(t):
    n = secs(t)
    h, m, s = n // 3600, n % 3600 // 60, n % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def canon(a, b, vid):
    text = fmt(a) + (f"–{fmt(b)}" if b else "")
    return f"[\\[{text}\\]](https://www.youtube.com/watch?v={vid}&t={max(0, secs(a) - LEAD)}s)"


def normalise(s, vid):
    link = r"\[(?:\\\[)?(" + T + r")(?:" + SEP + r"(" + T + r"))?(?:\\\])?\]\(https://www\.youtube\.com/watch\?v=" + re.escape(vid) + r"&t=\d+s\)"
    s = re.sub(r"\(" + link + r"\)", lambda m: canon(m.group(1), m.group(2), vid), s)      # (range) -> [range]
    return re.sub(link, lambda m: canon(m.group(1), m.group(2), vid), s)


def link_raw(s, vid):
    s = re.sub(rf"\[({T})(?:{SEP}({T}))?\](?!\()", lambda m: canon(m.group(1), m.group(2), vid), s)
    s = re.sub(rf"\(({T})(?:{SEP}({T}))\)(?!\()", lambda m: canon(m.group(1), m.group(2), vid), s)
    s = re.sub(rf"(?m)^\| ({T}) \|", lambda m: f"| {canon(m.group(1), None, vid)} |", s)
    return s


def link_index_raw(s, vid):
    return re.sub(r"(?m)^\| (\d+) \| (\d\d:\d\d:\d\d) \|", lambda m: f"| {m.group(1)} | {canon(m.group(2), None, vid)} |", s)


for folder, vid in VID.items():
    for rel, raw in ((f"{folder}/summary.md", link_raw), (f"{folder}/slides/slides-index.md", link_index_raw)):
        p = ROOT / rel
        a = p.read_text()
        b = raw(normalise(a, vid), vid)
        if a != b:
            p.write_text(b)
        print(f"{rel}: {len(re.findall(r'watch\?v=' + re.escape(vid) + r'&t=', b))} timestamp links")
