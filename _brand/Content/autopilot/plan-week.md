# Autopilot: plan the week (runs Sunday 6pm)

You are running unattended from Windows Task Scheduler. Nobody can answer questions. Where a skill would normally stop to ask Sam something, make the sensible choice, carry on, and write the choice under "Autopilot notes" in the week's `plan.md`.

The working directory is the workspace root. Sam's Instagram content lives in `_brand/Content/` (read its `CLAUDE.md` first). Paths below are relative to `_brand/Content/`.

## 1. Pick the week

- The target week is the **first Monday after today**. Call it `<Monday>` (format `YYYY-MM-DD`).
- If `Weeks/<Monday>/plan.md` already exists **and** already has a `## Status` table, stop. Write the summary `Week of <Monday> was already planned. Nothing changed.` and finish.

## 2. Plan it

- Use the **locate-content** skill to plan the week starting `<Monday>`, exactly as Sam would run it by hand. It reads `insights-log.md`, `profile.md` and everything in `Research/` (swipe file, reference accounts, competitors, trend log, hook library). Let it choose the mix of reels, carousels, static images and journey reels.
- For every reel (talking-head or journey), use the **reels-script** skill to write the script into `Scripts/<post date>_<slug>.md`. Put the words to emphasise in **bold**, as edit-reel expects.
- `plan.md` goes in `Weeks/<Monday>/plan.md` in whatever shape locate-content normally uses.

## 3. Add the Status table

Add this section to the **top** of `plan.md`, under the title. The nightly build reads it and updates it, so keep the exact column order and the status words.

```
## Status

**Where to put your files:** `_brand/Content/_DROP FILES HERE/`. There's one folder per post that needs something from you, named with the day and what to drop, plus a READ ME with the shot list and script. Upload into it and leave it. The nightly build (10pm) picks it up once your last file has been there 2 hours. Change a status to `hold` to skip a post.

| # | Post day | Format | Topic | Folder | Needs from you | Drop folder | Status |
|---|---|---|---|---|---|---|---|
| 1 | Tue 10 Nov | Reel | AI file notes | Raw Footage/2026-11-10_ai-file-notes | Film the script (about 45 s), 2 screenshots | 01 Tue 10 Nov - AI file notes - FILM + 2 SCREENSHOTS | planned |
| 2 | Sat 14 Nov | Static | Hook quote | Weeks/2026-11-09/hook-quote | nothing | - | ready |

### Autopilot notes
- (one line per choice made or problem met, newest first, each starting with the date)
```

- Formats: `Reel`, `Journey reel`, `Carousel` or `Static`.
- Status is `planned` when Sam must supply something, or `ready` when the post needs nothing from him (a designed carousel with no photos, say).
- "Folder" is the item's home: where its notes, brief and finished files live. "Drop folder" is where Sam uploads, inside `_DROP FILES HERE/`.

## 4. Make the folders

Every post gets a **home folder** with everything already filled in. Every post that needs something from Sam also gets a **drop folder**, so he only ever opens one place.

**Home folders** (the nightly build reads these; Sam doesn't need to open them):
- Reels and journey reels: `Raw Footage/<post date>_<slug>/notes.md`, in the format from `Reel checklist.md` (Script, Brands mentioned, Screenshots, Numbers to show, Call to action, Pause cut 0.25 s default, Anything to skip or keep, `Figures on screen: yes`, and `Client sign-off (only for testimonials, case studies, client names or client documents): not needed`, or `needed` if the reel uses one), plus a `## Shot list`.
- Carousels and statics: `Weeks/<Monday>/<slug>/brief.md` with the slide-by-slide copy, the numbered list of photos needed, the format spec from locate-content's `references/formats.md`, and a draft caption. Create an empty `photos/` folder inside it when photos are needed.
- End each notes.md and brief.md with `## Hand-over` and the line `Upload to _DROP FILES HERE/<drop folder name>/ from the Google Drive app. That's it.` (or `Nothing needed from you.`), so a home folder never tells Sam to drop files in it directly.

**Drop folders:** `_DROP FILES HERE/<NN> <Ddd d Mmm> - <Short topic> - <WHAT>/`
- `NN` is the row number, padded to two digits, so the folders sort in posting order.
- `WHAT` is in capitals and is all Sam needs to read: `FILM`, `FILM + 1 SCREENSHOT`, `FILM + 2 SCREENSHOTS`, `FILM + SCREEN CLIP`, `4 CLIPS`, `1 PHOTO`, `6 PHOTOS` and so on.
- Example: `_DROP FILES HERE/03 Tue 10 Nov - Where AI goes first - FILM + 1 SCREENSHOT/`
- Inside it, write one plain-text file, `00 READ ME - what to drop.txt`, with Windows line endings. It holds:
  1. `WHAT TO DROP IN THIS FOLDER`, then a bullet list of every clip, screenshot or photo, in order, with how long each clip runs or what each shot shows.
  2. The lines: `Upload straight into this folder from the Google Drive app. Any file names are fine.` / `The nightly build (10pm) picks it up once your last file has been here 2 hours,` / `moves everything to where it belongs, and this folder moves to _done.`
  3. `Expected: <n> video(s)[, <n> screenshot(s)]` or `Expected: <n> photo(s)`. Leave optional extras out of the count.
  4. `Moves to: <home folder, or its photos/ subfolder>`.
  5. For reels: a divider, then `SCRIPT (the master copy is Scripts/<file>.md)` and the full script text, so Sam can read it on his phone while filming.
- Don't create a drop folder for posts that need nothing.

Never overwrite a file or folder that already exists. If a name is taken, add `-2`.

## 5. Phone summary

Write the summary to the file path given in the run prompt, as plain text of 350 characters or less. Sam reads it as a phone notification, for example:

`Week of 9 Nov: 2 reels, 1 carousel, 1 static. Film: AI file notes (45 s), client onboarding (30 s). Photos: 6 from your week for Thu. Everything is in Weeks/2026-11-09/plan.md`

## Rules

- Never post, schedule or upload anything to Instagram, Facebook or anywhere else.
- Only write inside `_brand/Content/` (including `_DROP FILES HERE/`) and the summary file. Don't delete anything, and don't use git.
- This run has a fixed tool list (file tools, web search and fetch, ls, mkdir, cp, mv, python). If a step needs something else, skip that step and note it in the Autopilot notes rather than looking for a way round it.
- Follow the voice and style rules in the skills and in `_brand/Content/CLAUDE.md` (Australian spelling, no emoji, no exclamation marks).
