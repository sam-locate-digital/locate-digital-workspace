# edit-tutorial reference

Commands, file formats and gotchas for the steps in `SKILL.md`. `KIT` is `G:\My Drive\Claude Code.Locate\_brand\Tutorials\tutorial-kit`, and `W` is the work folder in this session's scratchpad (for example `<scratchpad>\tut-<topic>`). The kit's README has the same steps with the folder map.

## Shell notes (Windows)

- Use the Bash tool with forward slashes, or PowerShell; set `PYTHONIOENCODING=utf-8` if a print fails on a symbol.
- Run Python with `-I`. Write multi-line Python to a `.py` file in the scratchpad instead of `python -c`.
- Background anything over about 2 minutes (prep, base on long footage, renders, check_cut) with `run_in_background`, and wait for the notification.
- FFmpeg here has no default font config: don't use `drawtext` without a `fontfile`.

## Setup

```
mkdir -p W/remotion && cp -r KIT/. W/remotion/
cd W/remotion && npm install --no-audit --no-fund        # background; Remotion 4.0.537
```
Every pipeline script runs from `W/remotion` as `python -I pipeline/<script>.py W ...`.

## Pipeline

| Step | Command | Notes |
|---|---|---|
| Prep | `prep.py "<Raw Footage folder>" W --hint "..."` | `face/` and `screen/` subfolders; loose files are sorted by shape. `--redo` re-transcribes. Face clips fill 2560x1440; screens keep their aspect ratio |
| Transcript | `lines.py W [clip]` | Writes `W/lines.txt` |
| Slice check | `segwords.py W/media/<clip>.wav <start> <end>` | Words and silences in source time |
| Edit list | `edl.py W` | Reads `W/select.json` |
| Cut | `base.py W [--jobs 4]` | Pieces cached in `W/pieces/`. Hard-links `base.mp4` into `W/remotion/public/` |
| Check the cut | `check_cut.py W [--max-pause 0.7]` | REPEAT / LONG / PAUSE |
| Zoom finder | `activity.py W` | `zooms_suggested.json`, `zooms.jpg`, `screens.jpg` |
| Timeline | `timeline.py W` | Reads `W/plan.json`, writes `W/remotion/src/timeline.json` |
| Still | `npx remotion still src/index.jsx Tutorial out/s.png --frame=N --scale=0.4 --log=error` | Tile with ffmpeg `hstack`/`vstack`, then Read |
| Render | `node render.mjs [--scale 0.5] [--concurrency 4] [--chunk 60] [--force]` | `out/video.mp4` or `out/preview.mp4`, no audio |
| Mix | `mix.py W [--lufs -14]` | Makes `music.wav` itself (music.py, seamless loop) |
| Finish | `finish.py W "<Exports>/<date>_<topic>_v<N>"` | MP4, `_chapters.txt`, `.srt`, `.vtt`, `W/contact.jpg` |

## select.json

```json
{
  "max_gap": {"face": 0.3, "screen": 0.6},
  "select": [
    {"clip": "face_IMG_2001", "in": 0.0, "out": 21.4, "section": "hook"},
    {"clip": "screen_01_connect", "in": 2.0, "out": 184.0, "section": "connect",
     "cut": [[61.2, 74.8]], "fast": [[90.0, 118.5, 5]], "keep": [[150.2, 152.0]], "gap": 0.8}
  ],
  "override": {"face_IMG_2001@0.0": [["First", 0.12, 0.40]]}
}
```
- Clip ids are `face_<file stem>` and `screen_<file stem>` (spaces and symbols become `-`).
- `in`/`out` are source seconds. Start a take just before its first word; end it after the last word, or after the result on screen settles.
- `cut` the whole mistake: from the start of the line that went wrong to the start of the restarted line.
- `fast` only silent stretches (its sound is dropped). 3 to 6x reads as "skipping ahead". Over 8x looks like a glitch.
- `max_gap` 0.3 s on camera keeps it tight but natural; 0.6 s on screen lets clicks land. Raise `gap` on a take where Sam pauses on purpose.
- `override` fixes a take's word timings when Whisper merged a false start (find them with `segwords.py`).

## plan.json

The kit README has the full key table. Times: seconds, `"section:<name>"`, `"end:<name>"` with `+`/`-` offsets, or `"<word or phrase>@<seconds>"`.

```json
{
  "title": "Connect Claude to your inbox", "kicker": "AI Launchpad · Lesson 3",
  "intro": {"at": "end:hook", "dur": 2.6, "em": "inbox", "sub": "About 20 minutes to set up"},
  "chapters": [{"section": "connect", "title": "Connect your inbox", "em": "inbox"}],
  "zooms": [{"s": 31.2, "e": 36.0, "x": 0.72, "y": 0.18, "z": 1.8}],
  "labels": [{"at": "claude.ai@20", "dur": 4, "text": "claude.ai", "sub": "Free plan works", "logo": "claude"}],
  "splits": [{"at": "hours@5", "e": "end:hook", "side": "right",
              "panel": {"kind": "stat", "value": 12, "suffix": " hrs", "label": "saved every week"}}],
  "cards": [{"at": "section:recap", "dur": 6, "kind": "points", "title": "Recap",
             "items": [{"text": "Connect once", "at": "connect@400"}, "Write the prompt", "Check the first summary"]}],
  "end": {"title": "Try it on this week's enquiries", "button": "Post your result in the community", "dur": 4},
  "music": "bookends",
  "replace": {"summarize": "summarise", "inquiry": "enquiry"}
}
```
- Zoom `x`/`y` are the focus centre as a fraction of the screen picture (not the 1920x1080 frame). The `zooms.jpg` blue box shows what a suggestion will show.
- A zoom that starts within 1.2 s of the previous one's end pans straight across instead of zooming out and in.
- Splits need face footage under their whole span. The face card is 820x952 px on the side opposite the panel.
- Cards and chapter cards cover the video but not the voice: time them over a line that says the same thing.
- `face.fy` (0.4) is the face's height in frame; lower it (0.3) if a punch-in crops the forehead.

## Remotion and render

- The composition is `Tutorial` (1920x1080, 30 fps). `src/Tutorial.jsx` picks the layout per frame; `src/tkit.jsx` holds the brand pieces (Canvas, ChapterCard, TitleCard, LowerThird, panels, EndCard, AppTile).
- New logo tile: drop the brand's real mark as `public/logos/<name>-mark.svg` (from the brand's site or simple-icons), and add its tile colour to `TILE_BG` in `tkit.jsx` if it isn't white.
- Screenshots for image panels go in `W/remotion/public/shots/`. Two sources: copy Sam's files from the footage folder's `extras/`, or grab a still from a screen recording at the moment it shows the thing (`ffmpeg -ss <t> -i W/media/<clip>.mp4 -frames:v 1 W/remotion/public/shots/<name>.png`, then crop to the screen box). Sam never has to make graphics; ask for an `extras/` file only when the thing isn't in any recording.
- Render speed on Sam's PC: about 7 fps at concurrency 4 (a 10-minute tutorial is about 45 minutes; a half-size preview is roughly half that). Concurrency 6 was no faster. If the browser crashes, use `--concurrency 2`.
- Chunks are cached by content (code, assets, the timeline items inside the chunk, base.mp4). A change to `tkit.jsx` or `Tutorial.jsx` re-renders everything; a change to one label re-renders one minute. `--force` ignores the cache.
- Output is tagged BT.709 limited range (`colorSpace: 'bt709'`). Remotion's default was full-range bt470bg.

## Gotchas found in the test build

- Whisper stretches a first word over the silence before it. edl.py places words by overlap, so they don't vanish.
- Whisper splits "$200,000" into "$200" ",000". edl.py joins them, and the captions follow.
- lines.py flags `RETAKE?` when a line starts like one of the last six. Spoken "again", "redo" and "take two" are flagged `AGAIN`.
- activity.py ignores changes under 4 connected blocks (the cursor) and treats a change over 30% of the screen as a new page. A single panel appearing counts as a zoom if it covers 3% or more of the screen.
- timeline.py catches overlapping cards, splits on screen footage, missing logos and images, and words that are never said. Fix every PROBLEM before rendering.
