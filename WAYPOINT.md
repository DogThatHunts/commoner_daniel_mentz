# Waypoint

Running log of progress in this project. Newest entries on top. Read [POLICIES.md](POLICIES.md) first each session, and add to it when the user states a new policy.

## 2026-11-22: restart point (end of session 1)

**State: three detailed, slide-illustrated summaries are published, all approved by the user.**
- **Index page (live):** https://dogthathunts.github.io/commoner_daniel_mentz/index.html
- **Repo (public, GitHub Pages on):** https://github.com/DogThatHunts/commoner_daniel_mentz, branch `main`. It is a nested git repo rooted at this folder (`law_sovereignty/daniel_mentz/01.DanielMentzSummariesFromCommoner/`); the parent `law_sovereignty` repo does not track `daniel_mentz/`.
- The repo is public (user, 2026-11-22), so it includes the verbatim transcripts. The Status Awakening PDF is **not** in the repo (too large; the book is linked to the publisher at https://www.sacredhonoref.com).
- Policies P1 to P12 are in `POLICIES.md` (P1 is superseded by P11).

| # | Folder | Video | Slides | Source resolution | Status |
|---|---|---|---|---|---|
| 01 | `01.national_status_and_passport` | `v2N5ESMKI4g` | 32 | 480p | Approved |
| 02 | `02.national_status_and_right_to_travel` | `_-LTnN5BeBs` | 6 | 360p | Approved |
| 03 | `03.building_freedom_from_the_ground_up` | `POZfdI0f4TU` | 18 | 720p | Approved |

### What exists
- `index.html` (a card per interview, oldest to newest, tiles from `collateral/thumbnail.jpg`) and `README.md` (text index with status).
- Each `NN.slug/` folder: `interview.md` (queue-sheet row: ID, YouTube URL, title, dates, Drive transcript link), `summary.md` and `summary.html`, `slides/` (`slide-NN_HH-MM-SS.jpg` plus `slides-index.md`), `collateral/` (`transcript.md` verbatim, `video-metadata.json`, `thumbnail.jpg`).
- `tools/build_html.sh` renders `summary.md` to `summary.html` (pandoc, with `tools/style.css`). Pages are **light-only** (no device dark mode), the column is 1100 px wide (text stays 820 px), and every slide image opens the full-size file in a new tab.
- Queue sheet: Google Sheet `1gws-Nmp5YFnMWK6oZgcEDkVL8SPMwhVWmBf_xZcaS9w`, tab "Queue". The `interview.md` files for 01 and 03 had been swapped at the start of the session and were corrected.
- Each summary has links from the shared citation register (01: 43, 02: 6, 03: 8), a reader's note, and a "Claims worth checking" section. The checks include opinion-text findings for *Jones*, *Valentine*, *Kitchens*, *Slater* and *Belmont* (01) and the DD Form 2168 note (03).

### Next up (in order)
1. **Re-link citations: blocked until the register is updated.** Two pending files sit unmerged and uncommitted in the private repo `_citation-register/pending/`: `daniel_mentz_2026-11-22.json` (01) and `daniel_mentz_02_03_2026-11-22.json` (02, 03). `register.json` lacks all their records, so a linker re-run adds nothing new (checked 2026-11-22; the only difference is the "commissioner" false positive, removed by hand in 02). **Open question for the user:** will they merge, or should I merge using the register's own process (a dated `tools/apply_*.py`, `tools/validate_register.py`, move the files to `pending/merged/`, commit, no push until the user has seen it)? Then re-run the linker on all three, show the diff, apply, rebuild HTML, commit and push. Linker feedback is in the pending files: case search limited to Supreme Court (add reporter-cite lookup via CourtListener citation-lookup), "commissioner" false positive, "Section N" self-references, "INA" unknown, DD forms treated as IRS forms. Dry-run recipe is under "How to run the citation pass" below.
2. **Link every timestamp to its video** in all three `summary.md` files (slide captions, section headings, Q&A table times) as `https://www.youtube.com/watch?v=<id>&t=<seconds>s`, and in the Time column of each `slides/slides-index.md`. Then update the sentence in each summary that says timestamps can be opened by adding `&t=<seconds>`, rebuild the HTML, commit and push.
3. **Check titles against Column D** of the Queue tab (policy P5). The titles for 02 and 03 are whatever `interview.md` contained. My search of Queue rows A1:D1000 did not turn up the Mentz row IDs, so the rows may be further down the sheet.
4. **View the rendered pages.** The light-only change and the click-through slides were measured in Chrome (slide widths) but not looked at by the user on a device set to dark mode. Also check tables and captions.
5. **`.md` links on GitHub Pages.** Pages serves `transcript.md` and `slides-index.md` as `text/markdown`, so a browser may download them instead of showing them. Render them as HTML, or link to the github.com view.
6. **Possible additions:** `04.` and later interviews in the same layout (follow the recipe below); a tile for this project on `../../_index_hub/index.html` (separate repo).

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
The scratch scripts are gone; they are short. In a Python session using `transcription-agent/mac-poller/.venv/bin/python` (set `CITATION_REGISTER_PATH` to the register folder, use `PYTHONDONTWRITEBYTECODE=1`, add `transcription-agent` to `sys.path`): load the register with `publisher.register_loader.load_register()`, build rules with `build_register_rules(reg)`, run `publisher.citations.linkify(md, register_rules=rules)` on a copy of `summary.md`, and show the diff. Run `publisher.citation_scan.scan(linked, reg)` for the misses (it flags italic slide captions as unknown; ignore those). Resolve misses by reporter cite with CourtListener's citation-lookup API (token in `transcription-agent/.env`), open opinion pages and sites that block scripts in Chrome to confirm the name, court and date, and reword any "Section N" self-reference so the linker cannot read it as a statute. Write the findings to `_citation-register/pending/daniel_mentz_<date>.json`.

Tools used: `yt-dlp`, `ffmpeg`, `pandoc` (in `/opt/homebrew/bin`), `gh` (logged in as DogThatHunts), and Chrome through the claude-in-chrome tools.
