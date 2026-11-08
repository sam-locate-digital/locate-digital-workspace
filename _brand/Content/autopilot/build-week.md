# Autopilot: build what's ready (runs nightly at 10pm)

You are running unattended from Windows Task Scheduler. Nobody can answer questions. Where a skill would normally stop to ask (a storyboard, "preview first", a style choice), take its default, carry on, and record the choice under "Autopilot notes" in that week's `plan.md`.

The working directory is the workspace root. Sam's content lives in `_brand/Content/` (read its `CLAUDE.md` first). Paths below are relative to `_brand/Content/`.

## 1. Find the work

- Look at every `Weeks/<Monday>/plan.md` that has a `## Status` table, where `<Monday>` falls between 14 days before today and 7 days after today.
- Go through the table rows in post-day order (earliest first) and decide what each one needs:

| Status | What to do |
|---|---|
| `hold`, `posted`, `failed: ...` | Skip it. |
| `building` | A previous run was cut off (the PC slept or shut down). Treat it as `ready` and start it again, and add a note saying so. |
| `ready` | Build it. |
| `planned` | Build it **if its files have arrived and settled**, as defined below. Otherwise skip it. |
| `built vN ...` | If its folder has a `changes.md`, apply the changes (step 3). Otherwise skip it. |

Sam uploads into **drop folders**, not into the item's own folder. Each row's `Drop folder` column names a folder inside `_DROP FILES HERE/` (or `-` if the item needs nothing from him). Each drop folder holds a `00 READ ME - what to drop.txt` whose `Expected:` and `Moves to:` lines say what should arrive and where it goes. Ignore the READ ME when counting or moving files. Older plans without a Drop folder column use the item's own folder directly.

Files count as **arrived and settled** when:
- **Enough has arrived:** the drop folder holds what the READ ME's `Expected:` line lists. Videos are `.mov`, `.mp4` or `.m4v`. Photos and screenshots are `.jpg`, `.jpeg`, `.png` or `.heic`.
- **It has settled:** the newest file arrived at least 2 hours ago. For each file, take the later of its CreationTime and LastWriteTime. Get these from PowerShell `Get-ChildItem`, because Drive sets CreationTime when a file lands on this PC, and a phone clip's LastWriteTime can be days old. Google Drive may still be uploading anything newer.
- **Fallback:** if some of the expected files are still missing, but at least one video (for a reel) or one photo (for a post) has sat untouched for 24 hours, build with what's there and say what was missing in the Autopilot notes.

**Moving the files in** (do this just before building the item):
1. Move every file except the READ ME from the drop folder to the `Moves to:` folder, using `mv`.
2. For reels, rename screenshots to `1.png`, `2.png`... in the order the READ ME lists them, matching by content and then by capture time. Name journey-reel clips `1.mov`, `2.mov`... in shot-list order.
3. For carousels and statics, name the photos `1.jpg`, `2.jpg`... in the brief's order where you can tell, and otherwise keep upload order.
4. Move the now-empty drop folder (with its READ ME) into `_DROP FILES HERE/_done/`.

Then `_DROP FILES HERE/` only ever shows what is still waiting on Sam.

Do at most **4 items** in one night, earliest post day first. Whatever is left waits for tomorrow night.

## 2. Build each item

Before you start an item, set its Status to `building`. When it finishes, set it to `built v1 (date)`. If it fails, set it to `failed: <reason in under 8 words>` and write the details in the Autopilot notes.

**Reels and journey reels:** use the **edit-reel** skill on the item's `Raw Footage/<folder>` (its Folder column), exactly as if Sam had said "edit the reel in Raw Footage/<folder>".
- Read `notes.md` first. Force-align the captions to the script it names.
- Render the **full-quality export** straight away. Skip the storyboard and the preview step, since time doesn't matter overnight.
- Work in the scratch folder on C: that the run prompt names, never on Google Drive. Copy `remotion-kit/` there as edit-reel says.
- Export to `Exports/<post date>_<slug>_v1.mp4`, bumping the version if that name exists.
- Write the caption with the **locate-voice** skill's caption rules to `Exports/<post date>_<slug>_caption.txt`.

**Carousels and statics:** build them to the spec for that format in the locate-content skill's `references/formats.md` (`$HOME/.claude/skills/locate-content/references/formats.md`). Use the copy in `brief.md` and Sam's photos in `photos/`, converting HEIC as needed. If formats.md names a skill for the format (photo-story-carousel, for instance), use that skill.
- Save the slides as `slide-1.jpg`, `slide-2.jpg` and so on in the item's folder, at the size formats.md gives.
- Write `caption.txt` beside them using locate-voice.
- Look at every finished slide yourself before marking it built. Check for spelling, text inside the safe zones, and no cut-off words.

## 3. Apply changes

When a built item has a `changes.md`:
- **Reel:** use edit-reel's change-request mode with the timestamped notes. Export the next version (`_v2`, `_v3`...) and never overwrite.
- **Carousel or static:** rebuild only the slides that changed, into a `v2/` (`v3/`...) subfolder.
- Then rename `changes.md` to `changes-applied-vN.md` and set Status to `built vN (date)`.

## 4. Record and report

- Under the Status table in each touched `plan.md`, add a line to "Autopilot notes", for example `- 2026-11-10 22:41: built reel 1 v1 (52 s); carousel 2 waiting on photos (3 of 6).`
- Write the phone summary to the file path given in the run prompt:
  - If you built or changed nothing, write exactly `NOTHING`.
  - Otherwise write plain text of 400 characters or less, for example: `Ready to review: AI file notes reel v1 (Tue post), Week 3 carousel (Thu). Still waiting: footage for client onboarding reel. Send changes in a changes.md in the item's folder.`

## Rules

- Never post, schedule or upload anything to Instagram, Facebook or anywhere else.
- Never edit or delete Sam's original clips or photos. The only move allowed is out of the drop folder into the home folder (step 1). Never overwrite an export.
- Only write inside `_brand/Content/`, the scratch folder and the summary file. Don't delete anything (the runner clears old scratch itself). Don't use git.
- This run has a fixed tool list (file tools, ffmpeg, ffprobe, python, whisper, node, npm install, npm run, npx remotion, ls, mkdir, cp, mv, robocopy). If a step needs something else, don't look for a way round it: mark the item `failed: needs <tool>` and explain in the Autopilot notes.
- Follow every rule in `_brand/Content/CLAUDE.md` (the six rules and the safe zones). Sam's own figures are always fine to show, in the captions and on the proof card. Only client testimonials, case studies, client names or client documents need sign-off in `notes.md`..
