# Waypoint

Running log of progress in this project. Newest entries on top. Read [POLICIES.md](POLICIES.md) first each session, and add to it when the user states a new policy.

## 2026-11-22: restart point (end of session 1)

**State: three detailed, slide-illustrated summaries are published, all approved by the user.**
- **Index page (live):** https://dogthathunts.github.io/commoner_daniel_mentz/index.html
- **Repo (public, GitHub Pages on):** https://github.com/DogThatHunts/commoner_daniel_mentz, branch `main`. It is a nested git repo rooted at this folder (`law_sovereignty/daniel_mentz/01.DanielMentzSummariesFromCommoner/`); the parent `law_sovereignty` repo does not track `daniel_mentz/`.
- The repo is public (user, 2026-11-22), so it includes the verbatim transcripts. The Status Awakening PDF is **not** in the repo (too large; the book is linked to the publisher at https://www.sacredhonoref.com).
- Policies P1 to P13 are in `POLICIES.md` (P1 is superseded by P11).

| # | Folder | Video | Slides | Source resolution | Status |
|---|---|---|---|---|---|
| 01 | `01.national_status_and_passport` | `v2N5ESMKI4g` | 32 | 480p | Approved |
| 02 | `02.national_status_and_right_to_travel` | `_-LTnN5BeBs` | 6 | 360p | Approved |
| 03 | `03.building_freedom_from_the_ground_up` | `POZfdI0f4TU` | 18 | 720p | Approved |

### What exists
- `index.html` (a card per interview, oldest to newest, tiles from `collateral/thumbnail.jpg`) and `README.md` (text index with status).
- Each `NN.slug/` folder: `interview.md` (queue-sheet row: ID, YouTube URL, title, dates, Drive transcript link), `summary.md` and `summary.html`, `slides/` (`slide-NN_HH-MM-SS.jpg` plus `slides-index.md`), `collateral/` (`transcript.md` verbatim, `video-metadata.json`, `thumbnail.jpg`).
- `tools/link_timestamps.py` links and normalises every video timestamp (P13).
- `tools/build_html.sh` renders `summary.md` to `summary.html` (pandoc, with `tools/style.css`). Pages are **light-only** (no device dark mode), the column is 1100 px wide (text stays 820 px), and every slide image opens the full-size file in a new tab.
- Queue sheet: Google Sheet `1gws-Nmp5YFnMWK6oZgcEDkVL8SPMwhVWmBf_xZcaS9w`, tab "Queue". The `interview.md` files for 01 and 03 had been swapped at the start of the session and were corrected.
- Each summary has links from the shared citation register (re-linked 2026-11-22 after the register merge), a reader's note, and a "Claims worth checking" section. The checks include opinion-text findings for *Jones*, *Valentine*, *Kitchens*, *Slater* and *Belmont* (01) and the DD Form 2168 note (03).

### Done this session (details, in case something needs redoing)
- **Shared citation command (2026-11-22, later in session 1): built.** `python -m publisher.cite_cli run <summary.md> --project daniel_mentz` (from `transcription-agent`; recipe under "How to run the citation pass") links from the register, applies `summary.citation-overrides.json` (none exist yet), and writes a private report to `_citation-register/pending/reports/` (committed there). Plan and status: `_citation-register/CITATION_PROCESS_PLAN.md`. A dry run on 01, 02 and 03 changes nothing; reports show 3, 1 and 7 unresolved items (the held items already in `TBD_later.md`). Three linker bugs found in this project were fixed with tests (bold "commissioner" no longer links to *Lane-Wells*; DD Form 2168 no longer read as an IRS form; "Section 11/14" self-references stay plain). User decision: leave the *Lane-Wells* record's one-word short form "Commissioner" as it is for now.
- **Citation linking: merged and re-linked (2026-11-22).** The register merge was done by `_citation-register/tools/apply_daniel_mentz_2026-11-22.py` (validate OK; pending files moved to `pending/merged/`; register commit `9ac627a`, pushed to the private `citation-register` repo on the user's instruction). The summaries were re-linked (01: 59 links, 02: 10, 03: 9). Still unlinked on purpose or not found (all logged in the register's `TBD_later.md`, "2026-11-22 daniel_mentz held items"): Ralph M. Brown Act (needs a state-statutes category), inpowermovement.org (needs the user's approval), DD Form 2168, travel.state.gov (403), the Hummel book, the Juries and Secret Financials videos, bare *Miranda*, and "INA §101(a)(21)" (the section resolver has no rule for "INA"). Linker feedback for `transcription-agent` is in that TBD file. When the linker or register changes, re-run the citation pass (recipe below) and the scripts in `tools/`.
- **Timestamps linked to the video, 8 s early, in one form everywhere: DONE (policy P13).** All 178 timestamps in the three summaries and the three `slides-index.md` files are links of the form `[mm:ss]` / `[h:mm:ss]` / `[a–b]` (brackets are part of the link text; ranges use an en dash; link on the start time; `t` = start minus 8 s), checked by script; only clock times of day (03's schedule caption) stay plain. `tools/link_timestamps.py` is idempotent and rewrites older forms into this one: run it after writing or editing any summary, then `tools/build_html.sh`.

### Next up
**Nothing is blocking.** Both repos (`commoner_daniel_mentz` and `_citation-register`) are clean and pushed.
1. **`.md` links on GitHub Pages (watch only).** Pages serves `transcript.md` and `slides-index.md` as `text/markdown`, so a browser may download them instead of showing them. The user says it is fine so far (2026-11-22); only act if it becomes a problem (render them as HTML, or link to the github.com view).
2. **Next revision: remove the "Project policies" link** from `index.html` (line 35, `<a href="POLICIES.md">Project policies</a>`; user, 2026-11-22). The `README.md` line 20 pointer to `POLICIES.md` is a separate item: leave it unless the user says otherwise. Not done yet; do it with the next change to the site.
3. **Citation process, remaining steps (plan file above):** C per-document manifest, D `triage.py` in the register, later `cite refresh`; register categories `state_statutes` / `dd_forms` / `court_rules` when the first verified record exists (Ralph M. Brown Act, DD Form 2168 are waiting). No Mentz work is blocked on these.
4. **Possible additions:** `04.` and later interviews in the same layout (follow the recipe below); a tile for this project on `../../_index_hub/index.html` (separate repo).

### Parked (user, 2026-11-22; do not work on these until the user raises them)
- **Request for originals.** A request to Clint Griess (Commoner Law Group) and Daniel Mentz (Sacred Honor) for the slide decks and any higher-resolution recordings was drafted; the user will send it. It also asks whether they are comfortable with their slides shown publicly and whether they want a credit line. The text is not in the repo (a personal message). If files arrive, replace the slide JPEGs under the same filenames and rebuild the HTML.
- **Their email addresses: not found.** Checked: both organizations' contact pages (forms only; `chenowith52@gmail.com` on commonerlaw.com is a placeholder in a typo-suggester script, not a contact), the three video descriptions, web search (nothing), and `stealth_vision/03.CommunicationWithDanielMentzEMail/NationalStatusInquiry.pdf` (addressed to Daniel through the Sacred Honor site; no email). The Gmail connector needs `/mcp` re-authentication before I can search the user's mailbox for earlier correspondence. Other routes: the contact forms; Daniel's monthly member call; the Commoner Law Group YouTube channel's About tab (behind a captcha).

### Facts worth keeping
- **Slide resolution is a limit of the source, not a bug.** YouTube's best formats (confirmed 2026-11-22 with default yt-dlp clients and the pipeline's cookies) are 480p for 01, 360p for 02 and 720p for 03, exactly the sizes already extracted. No cropping and no upscaling (user). If originals arrive, 01 slide 21 was captured at 41:26 (2486 s) although it is named 41:08; every other slide was captured 2 s after the time in its filename.
- **YouTube bot check:** after a burst of downloads, YouTube refused every request from this host for a while ("Sign in to confirm you're not a bot"), even with the pipeline's cookies (`transcription-agent/secrets/yt_cookies.txt`). It cleared on its own. The pipeline's `web_embedded,mweb` options expose only a 360p format; the default clients list more. Download one video at a time, and delete any copy of the cookies file from the scratchpad afterwards.
- **Pipeline code is separate:** the linker and resolver live in `transcription-agent/publisher/` (`citations.py`, `register_loader.py`, `citation_scan.py`, `citation_verify.py`); the register is `_citation-register/` (private; proposals go in `pending/`, never straight into `register.json`).
- Audience members appear by first name only (P4). Names mangled by the auto-transcripts are corrected in the summaries and left as-is in `transcript.md`.

### How a new interview is processed (for 04+)
1. Read the folder's `interview.md`: row ID, YouTube URL, title, Drive transcript link.
2. Download the transcript with `mcp__claude_ai_Google_Drive__download_file_content` and compact it into about 45-second paragraphs to read.
3. Download the video to the scratchpad, one video at a time: `yt-dlp -f 'bv*[height<=720]+ba/b[height<=720]' --merge-output-format mp4 --write-info-json`. Quote the format string, because zsh globs the brackets. The `info.json` supplies chapters, the description, the upload date and the thumbnail URL.
4. Locate slide segments with a coarse contact sheet (`fps=1/60`, `tile`). Then run `select='gt(scene,0.03)'` inside those segments, extract the frame 2 s after each cut, build contact sheets, and pick the distinct slides. For gallery-view calls scene detection alone is noisy.
5. Save the YouTube thumbnail as `collateral/thumbnail.jpg` (P11). Write `summary.md`, run `tools/build_html.sh`, generate `slides-index.md`, update `README.md` and `index.html` (appended at the bottom, P10), commit and push.

### How to run the citation pass (P12)
From `~/Projects/transcription-agent`: `mac-poller/.venv/bin/python -m publisher.cite_cli run <folder>/summary.md --project daniel_mentz` (dry run; add `--apply` to write). It prints what needs the user (ambiguous, unresolved, suspected false positives, linker gaps) and writes the full private report to `_citation-register/pending/reports/`. Resolve each miss (the register's resolver, CourtListener citation lookup by reporter cite, pages opened in Chrome), write proposals to `_citation-register/pending/daniel_mentz_<date>.json`, and let the user merge. Hand corrections go in `summary.citation-overrides.json` beside the summary. Then run `tools/link_timestamps.py` and `tools/build_html.sh`.

Tools used: `yt-dlp`, `ffmpeg`, `pandoc` (in `/opt/homebrew/bin`), `gh` (logged in as DogThatHunts), and Chrome through the claude-in-chrome tools.
