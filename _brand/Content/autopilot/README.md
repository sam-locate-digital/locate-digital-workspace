# Content autopilot

Two jobs run on Sam's PC through Windows Task Scheduler. They start Claude Code in the background, so the Claude app doesn't need to be open.

| When | Job | What it does |
|---|---|---|
| Sunday 6pm | Weekly content plan | Plans next week with locate-content and writes the reel scripts. Makes a hand-over folder for every post, already filled in, and pings your phone. |
| Every night 10pm | Nightly content build | Edits any reel whose footage has arrived (edit-reel) and builds any carousel or static whose photos have arrived. Writes the captions (locate-voice) and applies any `changes.md`. Pings your phone at 7am if it made something. |

## Your part

1. **Sunday night:** read the ping, or open `Weeks/<Monday>/plan.md`. The Status table at the top lists every post, its folder and what it needs from you.
2. **Film or take the photos**, then upload them from the Google Drive app into `_brand/Content/_DROP FILES HERE/`. Each post that needs something from you has its own folder there, named with the day and what to drop (for example `03 Tue 10 Nov - Where AI goes first - FILM + 1 SCREENSHOT`). Each one has a READ ME with the shot list and the script. Any file names are fine, and you don't need to tell anyone or tick anything. The nightly build picks a folder up once your last file has been there 2 hours, moves the files to where they belong, and moves the empty folder to `_done`. So whatever is left in `_DROP FILES HERE` is still waiting on you.
3. **Morning:** watch or flick through the result in `Exports/` (reels) or the post's folder (carousels). The caption is next to it.
4. **Changes?** Write them with timestamps in a `changes.md` in the same folder, for example `0:05 cut the repeated line`. They're applied that night as a new version.
5. **Post it.** Optionally change its Status to `posted`.

## Statuses in plan.md

`planned` waiting for your files · `ready` will be built tonight · `building` in progress · `built v1 (date)` done · `failed: reason` stopped (change it back to `planned` to retry) · `hold` skip this one · `posted`

## Run a job now

Open Task Scheduler, find "Locate - Nightly content build" or "Locate - Weekly content plan", and click Run.

## Files

- `plan-week.md`, `build-week.md`: the instructions each job follows. Edit them to change the behaviour, and the change applies from the next run.
- `run.ps1`: the runner. `setup.ps1` copies it to `%LOCALAPPDATA%\LocateAutopilot\`, so run setup again after editing it.
- `setup.ps1`: one-time setup. Right-click it and choose Run with PowerShell. It's safe to re-run.
- Logs and settings (including the private ntfy topic) are in `%LOCALAPPDATA%\LocateAutopilot\`.

## Needs

The PC must be on or asleep and signed in. A locked screen is fine. Google Drive must be running. If the PC was off at the scheduled time, the job runs as soon as you next sign in.
