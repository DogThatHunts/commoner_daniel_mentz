# Project Policies

Standing rules for this project. Read at the start of each session. Add a new numbered policy whenever the user states one, and record the date and who set it. Policies marked **user-set** are the user's explicit instructions. Policies marked **working convention** were adopted during the first session and can be changed.

## Presentation

**P1. Index tiles use the interview's splash screen** (user-set, 2026-11-22). Each tile on `index.html` shows the interview's own title/splash card.
- If the video opens with a title slide, use it: copy that slide as the tile image (currently `slide-01` in 01 and 03).
- If it has none (for example a gallery-view call), use the video's official YouTube thumbnail, saved at `NN.slug/collateral/thumbnail.jpg`.
- Do not use a mid-talk content slide as the tile.

**P10. Index order is oldest to newest, top to bottom** (user-set, 2026-11-22). Tiles on `index.html` (and rows in `README.md`) run from the earliest to the latest interview, which is also the `NN.` folder order. New interviews are appended at the bottom.

## Content

**P2. Summaries are detailed and slide-illustrated** (user-set, 2026-11-22). Each interview gets a `summary.md` more detailed than the normal workflow summary, with its slides embedded inline at the point they appear, and the full transcript kept in `collateral/`.

**P3. Speakers' claims are attributed, not endorsed** (working convention). Each summary begins with a reader's note and ends with a "Claims worth checking" section. Claims are reported as the speaker's own and are not verified in the summary.

**P4. Audience members are named by first name only,** as given on the call (working convention). Names mangled by auto-transcription are corrected in summaries and left as-is in `transcript.md`, which stays verbatim.

**P5. Titles come from Column D of the Queue sheet** (user-set, 2026-11-22). When the sheet is reachable, use the Column D title for each summary. Currently the titles come from `interview.md`, which was copied from the sheet.

## Files and layout

**P6. One numbered folder per interview** (user-set, 2026-11-22): `NN.slug/` containing `interview.md`, `summary.md`, `summary.html`, `slides/` (with `slides-index.md`) and `collateral/` (`transcript.md`, `video-metadata.json`, and `thumbnail.jpg` when P1 needs it).

**P7. Slide files are named `slide-NN_HH-MM-SS.jpg`** (working convention), where the time is when the slide first appears in the video. The downloaded video and raw frames stay out of the repo.

**P8. `summary.md` is the source of truth** (working convention). `summary.html` is generated from it with pandoc, and `index.html` and `README.md` are updated whenever an interview is added or changes status.

## Publishing

**P9. Repo visibility** (user-set). Private until 2026-11-22, when the user made it **public** and enabled GitHub Pages. Do not change visibility without being asked. The repo scope is this folder only.
