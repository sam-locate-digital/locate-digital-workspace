---
name: edit-tutorial
description: Edits Sam's long-form tutorial footage (talking-head clips plus screen recordings) into a finished 16:9 lesson for Circle, in the Locate hybrid style. It picks the best takes, cuts pauses, fluffs and repeated lines, speeds up silent typing and loading, zooms in on the screen where things happen, and adds Locate-branded lesson title and chapter cards, lower thirds, split frames and key-point cards, an original music bed and sound effects. It mixes to -14 LUFS and exports a 1920x1080 MP4 with a chapter list and .srt/.vtt captions. It also applies timestamped change requests and re-renders only the minutes that changed. Use when Sam says "edit my tutorial", "edit the long video", "edit the footage in Tutorials/Raw Footage/...", "make this into a lesson for Circle", "preview the tutorial" or "change the zoom at 4:12". NOT for vertical reels (edit-reel), scripts (reels-script) or how to film (send Sam to _brand/Tutorials/filming-guide.md).
---

# Edit tutorial

Turns a folder of face clips and screen recordings into a finished Circle lesson. The engine is the kit in `G:\My Drive\Claude Code.Locate\_brand\Tutorials\tutorial-kit\`: a Python pipeline that cuts the footage, plus a Remotion composition driven entirely by one `timeline.json`. This skill is the process and the judgement calls. Exact commands, the `select.json` and `plan.json` formats, and the gotchas are in `$HOME/.claude/skills/edit-tutorial/reference.md`. Read it before step 3.

## Ground rules

- **Sam's own voice only.** Every word in a tutorial is Sam speaking. Never generate, clone, change or dub a voice: no text-to-speech, no AI voiceover, no AI "fixes" to a word, even as a stand-in. If a line is fluffed in every take or missing, tell Sam exactly which line to re-record (a pickup: one short face or screen clip) and drop it into the footage folder.
- **Brand, not social.** Tutorials use the brand fonts (Newsreader and Public Sans), Locate Blue as the one accent, and orange at most once (the end card button). Source of truth: `_brand/brand-guidelines.html`. No burned-in captions by default; Circle gets the .vtt/.srt.
- **Work on C:, never on Google Drive.** Copy the kit to this session's scratchpad (`tut-<topic>/remotion/`) and install there. Only the finished files go to `_brand/Tutorials/Exports/`.
- **Never touch originals.** `Raw Footage/` is read-only. Exports never overwrite: bump `_v1` to `_v2` (finish.py refuses to overwrite).
- **Nothing private on screen.** Circle members see everything. If a client name, email, figure or password shows in a screen recording, `cut` that stretch or ask Sam. Real client results on screen need Sam's written OK in `notes.md`.
- **Verify with tools, then say what you couldn't check.** You can't hear audio or watch motion. Measure loudness, look at stills and contact sheets, and tell Sam to watch it through before posting.
- **Spend nothing without saying so.** The pipeline costs nothing. If a Higgsfield image is wanted (an icon, a thumbnail), quote the credits first.
- **Long renders run in the background.** A 10-minute tutorial renders at about 7 fps, roughly 45 minutes. Never start a full render before the stills and the plan are right.

## Steps

Track the steps with the task list.

### 1. Read the brief
- The folder: `_brand/Tutorials/Raw Footage/<YYYY-MM-DD_topic>/` with `face/`, `screen/`, an optional `extras/` (screenshots and images Sam supplied, each mentioned in `notes.md`) and `notes.md` (title, the section list, brand names, anything to show or hide). The filming guide (`_brand/Tutorials/filming-guide.md`) is what Sam was asked to hand over. If `notes.md` is missing, work the sections out from the transcript and ask only about what is really unclear.
- Sam's request. "Preview first" means a half-size render (`--scale 0.5`) for approval before the full one.
- Which community or course it belongs to (it sets the `kicker`, e.g. "AI Launchpad · Lesson 3"). Ask if it isn't in `notes.md`.

### 2. Set up the workspace
Copy `tutorial-kit/` to `<scratchpad>/tut-<topic>/remotion/` and run `npm install` there in the background. Prep reads the clips straight from Drive.

### 3. Prep and read the transcript
Run `prep.py` with `--hint` set to the brands, people and terms in this video (background: Whisper takes a few minutes per 10 minutes of footage). Then `lines.py` and read `lines.txt` end to end. Expect retakes on camera and "again" on screen.

### 4. Pick the takes (select.json)
- Face clips: the clean take of every line, in story order. The last complete take is usually the keeper. Watch for `RETAKE?` and hidden false starts (a stretched word).
- Screen clips: usually one long take per section. `cut` every flagged mistake (from where it went wrong to where Sam restarts the sentence), `fast` the silent typing, loading and waiting (`(gap Ns)` lines) at 3 to 6x, and `keep` a silent moment that shows a result.
- Give every take a `section` name. The order of sections is the order of the video.
- Run `edl.py`, `base.py` (frame counts must match), then `check_cut.py`. Fix every `REPEAT`, check every `LONG` word with `segwords.py` on the source, and remove stray `PAUSE`s. Repeat until clean.

### 5. Find the zooms
Run `activity.py`, then look at `zooms.jpg` and `screens.jpg`. Keep zooms that land on what Sam is talking about (the field being typed in, the menu just opened, the result), fix focus points that are off, and drop zooms on unimportant changes. Add zooms by hand where Sam says "here" or "this button" and the change was too small to detect. A zoom holds at least 2 s, at 1.4 to 1.9 for most UI; go to 2.2 only for small text.

### 6. Plan the graphics (plan.json)
The hybrid recipe, in order of how much it matters:
1. **Lesson title card** after the hook (2 to 3 s), with the key word brushed.
2. **A chapter card** at the start of every section, matching Sam's section intro line. These become the Circle chapter list, so title them as the viewer would search them.
3. **Zooms** on every screen demo, so the screen is never unreadable on a phone.
4. **Lower thirds** the first time each tool, site or setting is named (with its logo tile if it's a brand: add the real mark to `public/logos/`, never a made-up one).
5. **Split frames** on face pieces that make a point: a stat (counts up), 2 to 4 points, a statement or a screenshot. About one per face piece over 15 s.
6. **Key-point cards** sparingly: the recap, a rule worth screenshotting.
7. **End card** only when there's a clear next step.

Something should change at least every 20 s on screen demos and every 10 s on camera (timeline.py reports the longest unchanged stretch). Run `timeline.py` and fix every `PROBLEM`.

### 7. Check stills
Render 8 to 12 stills at scale 0.4 at the key moments (each card mid-entrance and settled, each split, a zoom held, a label), tile them and look. Fix text running off cards, brushes hitting text below, labels covering the thing being clicked, and zooms that cut off what matters. For a new kind of video, or when Sam asks, publish a storyboard of these stills as an artifact and wait for a yes.

### 8. Render, mix, export
- `node render.mjs` in the background (`--scale 0.5` for "preview first").
- `mix.py` (music `bookends` by default: under the opening and close, a swell on chapter cards, clean under demos).
- `finish.py` to `_brand/Tutorials/Exports/<date>_<topic>_v<N>`. It checks length against the timeline, 1920x1080 H.264 High 30 fps, about -14 LUFS with a true peak around -1.5, writes the chapter list and captions, and makes a contact sheet. Read the contact sheet.

### 9. Change requests
Sam gives a timestamp and the change. Timestamps are in the finished video, which equals cut time (the end card is after the last word). Edit `plan.json` (graphics) or `select.json` (cuts; then edl, base, check_cut again, since everything after a cut shifts), run `timeline.py`, re-render (only changed minutes render again), mix and finish as the next version.

### 10. Leave the kit better
Copy improved code back to `tutorial-kit/` and add new lessons to its README and to `reference.md` here. Don't copy Sam's footage, screenshots or `base.mp4` into the kit. Don't commit unless Sam asks.

## Hand-over message
Say the length, the sections with their times (the chapter list), what was cut or sped up and why, anything you hid for privacy, what couldn't be checked (audio by ear, motion by eye), credits spent (normally none), and the export paths: the MP4, the chapter list and the .vtt to upload to Circle.
