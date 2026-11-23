# Project Policies

Standing rules for this project. Read at the start of each session. Add a new numbered policy whenever the user states one, and record the date and who set it. Policies marked **user-set** are the user's explicit instructions. Policies marked **working convention** were adopted during the first session and can be changed.

## Presentation

**P1. Superseded by P11.** (Originally: tiles use the interview's own splash screen.)

**P11. Index tile graphics come from the Queue sheet's linked graphic** (user-set, 2026-11-22). Each tile on `index.html` uses the graphic linked on that interview's row of the Queue sheet, which is the video's YouTube thumbnail. Save it as `NN.slug/collateral/thumbnail.jpg` (fetch `https://i.ytimg.com/vi_webp/<id>/maxresdefault.webp` and convert to JPEG) and point the tile at it. Use another image only when the user calls out an exception for that interview.

**P10. Index order is oldest to newest, top to bottom** (user-set, 2026-11-22). Tiles on `index.html` (and rows in `README.md`) run from the earliest to the latest interview, which is also the `NN.` folder order. New interviews are appended at the bottom.

## Content

**P2. Summaries are detailed and slide-illustrated** (user-set, 2026-11-22). Each interview gets a `summary.md` more detailed than the normal workflow summary, with its slides embedded inline at the point they appear, and the full transcript kept in `collateral/`.

**P3. Speakers' claims are attributed, not endorsed** (working convention). Each summary begins with a reader's note and ends with a "Claims worth checking" section. Claims are reported as the speaker's own and are not verified in the summary.

**P4. Audience members are named by first name only,** as given on the call (working convention). Names mangled by auto-transcription are corrected in summaries and left as-is in `transcript.md`, which stays verbatim.

**P5. Titles come from Column D of the Queue sheet** (user-set, 2026-11-22). Use the title already in each folder's `interview.md`, which is copied from the sheet; the user dropped the idea of re-checking it against Column D (2026-11-22).

**P12. Citations are linked from the shared register** (working convention, adopted 2026-11-22 with the user's approval). Run the register's own linker (`transcription-agent/publisher/citations.py` with `_citation-register/register.json`) on each `summary.md`. Review the diff before applying: remove any false positive by hand, and reword self-references such as "Section 11" so the linker cannot read them as statutes. Resolve every miss automatically first (the register's resolver, CourtListener citation lookup by reporter cite, and pages opened in Chrome for sites that block scripts), then write the result to `_citation-register/pending/daniel_mentz_<date>.json`. The user reviews and merges. Never merge into `register.json` from here, and never invent a URL.

## Files and layout

**P6. One numbered folder per interview** (user-set, 2026-11-22): `NN.slug/` containing `interview.md`, `summary.md`, `summary.html`, `slides/` (with `slides-index.md`) and `collateral/` (`transcript.md`, `video-metadata.json`, and `thumbnail.jpg` when P1 needs it).

**P7. Slide files are named `slide-NN_HH-MM-SS.jpg`** (working convention), where the time is when the slide first appears in the video. The downloaded video and raw frames stay out of the repo.

**P8. `summary.md` is the source of truth** (working convention). `summary.html` is generated from it with pandoc, and `index.html` and `README.md` are updated whenever an interview is added or changes status.

**P13. Timestamps link to the video, 8 seconds early** (user-set, 2026-11-22: "5 to 10 sec before the actual time stated so the listener can get ready"). Every video timestamp in a summary (slide captions, section headings and ranges such as `[16:55–32:00]`, the first column of Q&A tables) and in each `slides-index.md` is a link to `https://www.youtube.com/watch?v=<id>&t=<seconds>s`, where seconds is the stated time minus 8. One form everywhere: the link text is the time in square brackets, `[mm:ss]` under an hour and `[h:mm:ss]` over, and ranges use an en dash, `[16:55–32:00]` (no parentheses, no "to"). The link goes on the start time. Run `tools/link_timestamps.py` after writing or editing a summary: it is idempotent, rewrites any older form into this one, and links raw timestamps. Clock times of day (such as a schedule's "3:00 pm PT") are not video timestamps and stay plain.

## Publishing

**P9. Repo visibility** (user-set). Private until 2026-11-22, when the user made it **public** and enabled GitHub Pages. Do not change visibility without being asked. The repo scope is this folder only.
