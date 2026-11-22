# Waypoint

Running log of progress in this project. Newest entries on top.

## 2026-11-22

**State: all three summaries drafted and pushed. 01 is approved. 02 and 03 await review.**

### What exists
- Repo: https://github.com/DogThatHunts/commoner_daniel_mentz (**private**), branch `main`, one commit (`001d75a`). It is a nested git repo rooted at this folder, `law_sovereignty/daniel_mentz/01.DanielMentzSummariesFromCommoner/`. The parent `law_sovereignty` repo does not track `daniel_mentz/` (it shows as untracked there).
- `index.html` is a landing page with a card per interview. `README.md` is the text index with a status column.
- Each interview folder contains `interview.md` (queue-sheet row: ID, YouTube URL, Column D title, dates, transcript Drive link), `summary.md` and `summary.html`, `slides/` (JPEGs named `slide-NN_HH-MM-SS.jpg` plus `slides-index.md`), and `collateral/` (`transcript.md` verbatim, `video-metadata.json`).

| # | Folder | Video | Slides | Status |
|---|---|---|---|---|
| 01 | `01.national_status_and_passport` | `v2N5ESMKI4g` | 32 | Approved |
| 02 | `02.national_status_and_right_to_travel` | `_-LTnN5BeBs` | 6 | Draft, awaiting review |
| 03 | `03.building_freedom_from_the_ground_up` | `POZfdI0f4TU` | 18 | Draft, awaiting review |

- The queue sheet is Google Sheet `1gws-Nmp5YFnMWK6oZgcEDkVL8SPMwhVWmBf_xZcaS9w`, tab "Queue". Transcripts come from the Drive links in each `interview.md`.
- The `interview.md` files for 01 and 03 were swapped this session (they had the wrong videos). They are correct now.

### Decisions made
- The summaries are more detailed than the normal workflow. They have timestamped sections and slides embedded inline. Each ends with a **reader's note** and a **"Claims worth checking"** section. The speakers' claims are attributed to them and not verified. This was added because the user plans to share publicly.
- Slides: scene-change detection with ffmpeg, then manual selection from contact sheets. In gallery-view calls (02, 03) only the screen-shared segments are slides. Raw frames and the downloaded video were kept out of the repo (they lived in the scratchpad).
- Audience members appear by first name only. Names mangled by the auto-transcripts were corrected in the summaries and left as-is in `transcript.md`.
- Repo is private for now. The user wants to share publicly later.

### Open items / next session
0. **Planned for next session: link the timestamps back to the videos.** Make every timestamp in the summaries (slide captions, section headings, Q&A table times) a clickable YouTube link at that moment, using `https://www.youtube.com/watch?v=<id>&t=<seconds>s`. Video IDs: 01 `v2N5ESMKI4g`, 02 `_-LTnN5BeBs`, 03 `POZfdI0f4TU`. Do it in `summary.md` for all three, regenerate `summary.html`, and apply the same to the Time column in each `slides/slides-index.md`. The summaries currently say timestamps can be opened by adding `&t=<seconds>`; update that sentence once they are links.
1. **Get the user's feedback on 02 and 03** and revise. Likely points: the tone and length of the "Claims worth checking" sections, and whether the 03 summary should say more about the Exit & Build promotion.
2. **Column D titles:** The titles used for 02 and 03 are whatever `interview.md` already contained. I did not check them against Column D of the Queue tab. My search of Queue rows A1:D1000 did not turn up the Mentz row IDs, so the rows may be further down the sheet.
3. **Going public:** `gh repo edit DogThatHunts/commoner_daniel_mentz --visibility public --accept-visibility-change-consequences`. Offer GitHub Pages so `index.html` works online. Note the HTML pages load slide images by relative path, so they must stay beside `slides/`. `transcript.md` and `slides-index.md` links open as plain text locally.
4. **Slide quality:** the 02 source video is 360p max, so its slide images are low-resolution. 01 and 03 are 480p and 720p.
5. **Quick checks not yet done:** I never viewed the rendered `index.html` and `summary.html` pages myself. Look at them for table or caption problems.
6. **Possible additions:** `04.` and later interviews, using the same layout (the user said there may be more). Add a tile for this project to `../../_index_hub/index.html` (the shared landing page), which is a separate repo.

### How a new interview was processed (to repeat for 04+)
1. Read the folder's `interview.md`: row ID, YouTube URL, title, Drive transcript link.
2. Download the transcript with `mcp__claude_ai_Google_Drive__download_file_content` and compact it into about 45-second paragraphs to read.
3. Download the video to the scratchpad: `yt-dlp -f 'bv*[height<=720]+ba/b[height<=720]' --merge-output-format mp4 --write-info-json`. Quote the format string, because zsh globs the brackets. The `info.json` supplies chapters, the description and the upload date.
4. Locate slide segments with a coarse contact sheet (`fps=1/60`, `tile`). Then run `select='gt(scene,0.03)'` inside those segments, extract the frame 2 s after each cut, build contact sheets, and pick the distinct slides. For gallery-view calls, scene detection alone is noisy.
5. Write `summary.md`, render `summary.html` with `pandoc -f gfm --standalone` plus the shared CSS, and swap the `summary.md` links for `summary.html`. Generate `slides-index.md`, update `README.md` and `index.html`, then commit and push.

Tools used: `yt-dlp`, `ffmpeg`, `pandoc` (all in `/opt/homebrew/bin`), and `gh` (logged in as DogThatHunts).
