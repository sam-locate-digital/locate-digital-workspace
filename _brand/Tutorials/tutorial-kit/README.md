# Locate tutorial kit

Turns a folder of face clips and screen recordings into a finished 16:9 tutorial for Circle, in the hybrid style: you on camera for the hook, section intros and recap; real screen demos that zoom in where things happen; Locate-branded title and chapter cards, lower thirds, split frames and key-point cards; an original music bed under the opening and close. The `/edit-tutorial` skill drives it. How to film for it: `../filming-guide.md`.

`src/timeline.json` and `examples/` are the test tutorial it was built on (2026-11-06): two vertical reel clips standing in for face footage, plus a synthetic 16:10 screen recording with a fluffed line and a silent loading stretch. The kit never generates a voice: every word in a real tutorial is Sam's.

## Where to run it

On C:, never on Google Drive. Copy this folder to `<work>/remotion/`, run `npm install` there (Remotion pinned to 4.0.537), and run every script from `<work>/remotion/`. Only the finished files go back to `../Exports/`.

```
<work>/media/            2560x1440 working copies + 48 kHz wav per clip      prep.py
<work>/clips.json        kind, size, silences, Whisper words per clip        prep.py
<work>/lines.txt         readable timed transcript with retake flags          lines.py
<work>/select.json       the takes, cuts, speed-ups (you write it)            -> edl.py
<work>/edl.json          frame-exact pieces, segments, sections, words        edl.py
<work>/pieces/           cached encoded pieces                                base.py
<work>/base.mp4, base.wav  the cut (2560x1440, no graphics) and the voice     base.py
<work>/zooms_suggested.json, zooms.jpg, screens.jpg                          activity.py
<work>/plan.json         the graphics plan (you write it)                     -> timeline.py
<work>/remotion/src/timeline.json                                             timeline.py
<work>/remotion/out/video.mp4                                                 render.mjs
<work>/mix.wav           voice + music + sound effects at -14 LUFS            mix.py
```

## Steps

1. `python -I pipeline/prep.py "<raw folder>" <work> --hint "brand names, people, terms"`: working copies, silence map, Whisper `small.en` with the hint. Raw folder holds `face/` and `screen/`.
2. `python -I pipeline/lines.py <work>`: the transcript in timed lines. `RETAKE?` and `AGAIN` mark restarts and spoken "again"s; `(gap Ns)` marks long silences (on screen pieces, candidates for `fast`).
3. Write `<work>/select.json` (see `examples/select.json`): takes in story order, each with a `section`. On screen takes, `cut` removes a fluffed stretch, `fast` speeds up silent typing or loading (`[a, b, 4]` = 4x, sound dropped), `keep` holds a silent moment that matters, `gap` changes the pause limit.
4. `python -I pipeline/edl.py <work>` then `python -I pipeline/base.py <work>`. base.py prints the frame count against the EDL; they must match.
5. `python -I pipeline/check_cut.py <work>`: re-transcribes the cut. Fix every `REPEAT`, check every `LONG` word with `segwords.py` on the source, and fix stray `PAUSE`s. Repeat 3 to 5 until clean.
6. `python -I pipeline/activity.py <work>`: zoom suggestions where the screen changes, with `zooms.jpg` (the blue box is what each zoom will show) and `screens.jpg` (what's on screen every 6 s).
7. Write `<work>/plan.json` (see `examples/plan.json` and the table below), then `python -I pipeline/timeline.py <work>`. Fix every `PROBLEM`. Watch "longest unchanged stretch": over about 20 s, add a zoom, label or split.
8. Stills: `npx remotion still src/index.jsx Tutorial out/s.png --frame=N --scale=0.4`. Check cards, splits, labels and zooms before rendering.
9. `node render.mjs` (add `--scale 0.5` for a preview). One-minute chunks, cached by content, so after a change only the minutes that changed render again.
10. `python -I pipeline/mix.py <work>`, then `python -I pipeline/finish.py <work> "<Exports>/<date>_<topic>_v<N>"`.

## plan.json

| Key | What it makes |
|---|---|
| `title`, `kicker` | Lesson title and the small blue line above it ("AI Launchpad · Lesson 3") |
| `intro` `{at, dur, sub, em}` | Lesson title card, usually right after the hook. `em` = the word the blue brush underlines |
| `chapters` `[{section, title, em, dur}]` | "Part 2 of 5" card at the start of a section (2.6 s default). Also the chapter list for Circle |
| `zooms` `[{s, e, x, y, z}]` or `"auto"` | Screen zoom: focus x/y as a fraction of the screen, z 1.3 to 2.2. Hold at least 2 s |
| `labels` `[{at, dur, text, sub, logo}]` | Lower third, bottom left. `logo` = a file `public/logos/<logo>-mark.svg` |
| `splits` `[{at, e, side, panel}]` | You shrink into a card on one side, a panel on the other. Face footage only |
| `cards` `[{at, dur, kind, ...}]` | Full-frame key-point card over your voice |
| `end` `{title, button, url, dur}` | End card after the last word (adds its seconds). The orange button is the one orange in the video |
| `music` | `bookends` (default), `under` or `off` |
| `face` `{punch, fx, fy, min, max}` | Punch-in zoom (1.14), face centre, and how often wide/punch alternate (5-11 s) |
| `screen` `{inset}` | How much of the frame the un-zoomed screen window fills (0.9) |
| `replace` | Caption spelling fixes, e.g. `{"summarize": "summarise"}` |

Panels (for `splits` and `cards`): `points` `{title, items}` (items can carry their own `at`), `statement` `{text, em, sub}`, `stat` `{value, prefix, suffix, label}` (numbers count up), `image` `{src, caption}` (file in `public/shots/`).

Times: seconds in the cut, `"section:s2"`, `"end:s2"` (plus `+1.5` / `-0.5`), or `"word@40"` (the first time a word or phrase is said at or after 40 s).

## Lessons from the test build (2026-11-06)

- Whisper stretches a first word across the silence before it ("I" over 0.0-0.58 s). edl.py matches words to pieces by overlap, not midpoint, or the first word vanishes from the captions.
- Whisper splits money ("$200" ",000"); edl.py joins them.
- Render speed is about 7 fps at 1080p with concurrency 4 (concurrency 2 was about 6 fps; 6 gained nothing). A 10-minute tutorial is about 45 minutes, so always check stills first and use the chunk cache for changes.
- Remotion's default output was tagged full-range bt470bg; `colorSpace: 'bt709'` in render.mjs fixes it.
- Back-to-back full cards must cut card to card, or the video flashes between them. A split's panel must leave before the face grows back.
- Screen recordings are padded into the 2560x1440 base; Remotion shows only the box, so 16:10 laptop screens work.
