---
name: edit-reel
description: Edits Sam's raw talking-head footage into a finished Instagram/TikTok reel in the Locate reel style, end to end. It picks the best take of each line, cuts pauses and hidden repeated false starts, adds word-timed white outlined TikTok Sans captions, glass-canvas motion graphics (split screens, step cards, a count-up proof card, 3D glass icons, app-tile logos for named brands, real screenshots), an original music bed and sound effects, mixes to -14 LUFS and exports 1080x1920 to the Exports folder. It can also make a CapCut pack of layers and apply timestamped change requests to an existing reel. Use when Sam says "edit my reel/video", "edit the footage in Raw Footage/...", "turn these clips into a reel", "re-render", "change the graphic at 0:12", "preview first", or asks for a CapCut pack. NOT for writing scripts (reels-script), planning content (locate-content) or downloading reference reels.
---

# Edit reel

Turns a folder of raw clips into a finished reel that follows Sam's approved style. The engine is the kit in `G:\My Drive\Claude Code.Locate\_brand\Content\remotion-kit\`: Remotion graphics plus a Python pipeline. This skill is the process and the judgement calls around it. Exact commands, script settings and known gotchas are in `$HOME/.claude/skills/edit-reel/reference.md`. Read it before step 3.

## Ground rules

- **The rulebook wins.** Read `_brand/Content/CLAUDE.md` at the start of every edit. It holds the current style (captions, graphics, colour, pacing, sound, safe zones, export spec). If it disagrees with this skill, follow the rulebook. Sam's words for a specific reel beat both.
- **Work on C:, never on Google Drive.** Copy the kit to this session's scratchpad (`reel-<topic>/remotion/`) and install there. Only the finished files go back to Drive.
- **Never touch originals.** `Raw Footage/` is read-only. Exports never overwrite: bump `_v1` → `_v2`.
- **Verify with tools, then say what you couldn't check.** You can't hear audio. Measure it, then tell Sam to listen before posting.
- **Spend nothing without saying so.** Higgsfield credits: quote with `get_cost` first and state the total. Never reuse other creators' footage, music or graphics from `References/`; those reels are for style only.
- **Real client figures on screen need written sign-off.** If `notes.md` doesn't confirm it, remind Sam once.

## Steps

Track the steps with the task list, and run long jobs (prep, renders) in the background.

### 1. Read the brief
- The reel folder: `Raw Footage/<YYYY-MM-DD_topic>/` with clips, screenshots and `notes.md`. If there's no `notes.md`, work out the brands, numbers and call to action from the transcript, and ask Sam only about what really is ambiguous.
- The script, if `notes.md` names one in `Scripts/` (or one matches by date and topic). With a script, captions follow its words.
- Sam's request. "Preview first" means a half-size preview before the full render. Note any one-off overrides, such as a 0.1 s pause cut instead of the 0.25 s default.

### 2. Set up the workspace
Copy `remotion-kit/` to the scratchpad and run `npm install` there (Remotion stays pinned to 4.0.537). Copy the clips' paths, not the clips. Prep reads them straight from Drive.

### 3. Prep and transcribe
Run `prep.py` (1440x2560 working copies, silence map, Whisper `small.en`), then `retranscribe.py` with `HINT` set to this reel's brands, names and numbers. Read each clip's word timeline. Expect retakes.

### 4. Pick the takes
- Choose the clean take of every line, in story order. The last complete take is usually the keeper. Put them in `SELECT` in `edl.py`.
- **Assume hidden false starts.** Whisper stretches one word across a restart it doesn't write down. For any take that looks long, check the slice with `segwords.py`, start the take after the restart, and pin its word timings in `OVERRIDE`.
- Run `edl.py` then `aroll.py`. Then verify the cut three ways: silencedetect shows no pause over the limit, `longwords.py` flags no ordinary word over 0.55 s, and a re-transcription reads every line exactly once. Repeat until all three pass.

### 5. Storyboard (only when it helps)
Skip it for routine reels, since the style is locked. Make one when the format is new, there's a lot of graphics or Sam asks. Use real frames from the cut with the planned overlays, beat by beat, and publish it as an artifact. List the points Sam must confirm (unclear words, names, figures).

### 6. Captions
Set `REPLACE` (house style: digits, Australian spelling, confirmed words), `BRANDS` (spoken product names, which become logo tiles instead of captions) and `EMPH` in `captions.py`, then run it into `remotion/src/data.json`. Check the cue list for missing first words, split numbers ("3 / months") and one-word flashes.

### 7. Graphics timeline
Edit `remotion/src/Reel.jsx` (the worked example is the $200,000 automation reel):
- `LAYOUT`: alternate full-frame wide (100%) and punch (118%) with split-screen stretches, so something changes every 2–4 s.
- `SHOTS`: Sam's screenshots in `public/shots/`, timed to when each result is mentioned.
- `STEPS`: one card per step, timed to its key word. Brand chips use `AppTile`. No section titles.
- The `ProofCard` figure and count timing, `FloatIcon` placement, and `LogoPop` positions.
- Logos: add a new brand's mark to `public/logos/` and `TILES` in `kit.jsx`. Use the brand's own site or simple-icons, never a made-up logo.
- New 3D icons, if needed: Higgsfield `gpt_image_2_5` in the same frosted-glass prompt style (0.25 credits each), then `remove_background`.

Render 8–10 stills at key frames (scale 0.4), tile them, and look. Fix overlaps, captions on the mouth, and text running into icons before any full render.

### 8. Render, mix, export
- "Preview first": render half size and wait for Sam.
- Full: `music.py` (length = data total) → `audio.py` (set `EVENTS` to the graphic landings) → Remotion render (`--concurrency=2`) → mux to spec.
- Check duration, H.264 High 1080x1920 30 fps, −14 LUFS with a true peak around −1.5, and a one-frame-per-second contact sheet. Frame one must show the hook caption.
- Save to `Exports/<date>_<topic>_v<N>.mp4`.

### 9. CapCut pack (when asked)
Render `ReelClean` and `Graphics` (transparent ProRes 4444). Make `graphics_on_magenta.mp4`, run `stems.py` and `srt.py`, write `timings.txt`, and copy the kit's `CAPCUT.md` in as the guide. Save the folder as `Exports/<date>_<topic>_v<N>_capcut/`. Check that the stacked layers match the export.

### 10. Change requests
Sam gives a timestamp, an element and the change. Edit that piece only (text, timing, removal, a swapped file), check a still, re-render and export as the next version. If the change is a style preference meant for every reel, update the rulebook and the `locate-reel-style` memory as well.

### 11. Leave the kit better
Copy improved code (`kit.jsx`, pipeline scripts) back to `remotion-kit/`. Add any new lesson to its README and to `reference.md` here. Don't copy client screenshots into the kit, since `.png` files are tracked by git. Don't commit unless Sam asks.

## Hand-over message
Say what the export contains (length, the main beats, where graphics and logos land), what changed from the brief and why, what couldn't be checked (audio by ear, the CapCut import), credits spent, and the export path.
