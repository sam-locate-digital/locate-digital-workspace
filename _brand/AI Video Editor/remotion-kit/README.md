# Locate reel kit

The tools that cut and finish a reel in the Locate Reel Style (see `../CLAUDE.md`). They were first used on `Exports/2026-11-04_200k-automation_v1.mp4`, and `src/Reel.jsx` and `src/data.json` are that reel. Treat them as the worked example to copy for the next one.

## Where to run it

Work in a scratch folder on C:, not on Google Drive. The working copies of the footage (about 1.5 GB per reel) and `node_modules` (about 250 packages) would otherwise sync to Drive. Copy this folder there, run `npm install`, and only put the finished MP4 back in `Exports/`.

Expected working-folder layout (`<work>`):

```
<work>/media/          1440x2560 working copies + wav per clip   (prep.py)
<work>/clips.json      silences + Whisper word timings per clip  (prep.py, retranscribe.py)
<work>/edl.json        chosen takes, pause-cut pieces, words     (edl.py)
<work>/aroll.mov       the cut talking footage                   (aroll.py)
<work>/remotion/       this kit; public/aroll.mp4, src/data.json (captions.py)
<work>/music.wav, sfx.wav, mix.wav                               (music.py, audio.py)
```

## Steps

1. `python -I pipeline/prep.py "<Raw Footage folder>" <work>`: makes working copies (auto-rotates iPhone footage), maps silences and transcribes with Whisper `small.en`.
2. `python -I pipeline/retranscribe.py <work>`: transcribes again with domain hints. Edit `HINT` first so product names (GoHighLevel, Claude) come out right. Use `segwords.py <wav> <start> <end>` to check any stretch where takes blur together.
3. Edit `SELECT` in `pipeline/edl.py` to choose the best take of each line, in story order, then run `python -I pipeline/edl.py <work>`. `MAX_GAP` is the longest pause allowed to remain (0.25 s per the style sheet; 0.1 s if Sam asks).
4. `python -I pipeline/aroll.py <work>`: renders the cut. Check it by re-transcribing it and running silencedetect, so no line repeats and no pause over the limit survives.
5. Edit `REPLACE` and `EMPH` in `pipeline/captions.py`, then run `python -I pipeline/captions.py <work> <work>/remotion/src/data.json`.
6. Copy the a-roll in as `public/aroll.mp4`. Edit the `LAYOUT`, `AUTOS`/`STEPS` and proof card values in `src/Reel.jsx` to match the storyboard.
7. Check stills: `npx remotion still src/index.jsx Reel out/s.png --frame=N --scale=0.4`
8. Render: `npx remotion render src/index.jsx Reel out/video.mp4 --codec=h264 --crf=16 --muted --concurrency=2`. Higher concurrency crashed the browser on this machine.
9. `python -I pipeline/music.py <seconds> <work>/music.wav 92`, then `python -I pipeline/audio.py <work>`. Update `EVENTS` in `audio.py` so the sound effects land on the graphics.
10. Mux to spec: H.264 High at 14 Mbps (16 Mbps max), AAC 320 kbps at 48 kHz, `+faststart`. Confirm −14 LUFS, then copy to `Exports/` with a new version number.

## CapCut pack (optional, after the final export)

Render `ReelClean` (footage with the zooms and split framing) and `Graphics` (every graphic, no footage or captions) as a transparent layer with `--codec=prores --prores-profile=4444 --pixel-format=yuva444p10le --image-format=png`. Then overlay that on a solid `0xff00ff` colour with ffmpeg to make `graphics_on_magenta.mp4`, the chroma-key backup in case CapCut ignores the transparency. Each render takes about 10 minutes, and the ProRes file is about 400 MB for 40 s. For a reel whose only overlays are static (screenshots, logos), the lighter `Overlay` still PNGs work instead (pass `--props` with `{"kind":"shot","index":0}` or `{"kind":"logo","logo":"claude"}`). Then run `pipeline/stems.py <work> <pack>` (voice, music and SFX that add up to the final mix) and `pipeline/srt.py <data.json> <pack>` (captions.srt and timings.txt). Add `CAPCUT.md` as the how-to and save the folder as `Exports/<date>_<topic>_capcut/`.

## Lessons from the first reel

- Captions on a close selfie framing go at about 76% height (bottom of the block at y 1470), not 62%, or they cover the mouth.
- In split screen, captions sit in ink just above the seam (bottom at y 838). Footage shifts up by `FACE_OFFSET` so the whole face shows.
- Whisper's first pass can merge a retake into the clean take. Always re-transcribe the finished cut.
- The first caption cue starts fully visible, because frame one is the cover image.
- **Hidden repeats (v2):** Whisper often stretches one word across a false start it doesn't write down ("that" lasting 1.2 s). Run `python -I pipeline/longwords.py <work>/aroll.wav` on every cut. Any ordinary word over 0.55 s is probably a repeated phrase. Check the source slice with `segwords.py`, start the take after the false start, and pin its word timings in `OVERRIDE` in `edl.py`.
- **Logos for brands:** spoken brand names (`BRANDS` in `captions.py`) become logo cues. `LogoPop` shows an iOS-style app tile (`AppTile`) instead of the word. Marks are in `public/logos/`: HighLevel's arrows come from its site SVG, and Claude's from simple-icons 15.0.0. Add a tile in `TILES` in `kit.jsx` for each new brand.
- **Premium layer:** `PremiumCanvas` loops a Higgsfield glass-ribbon plate (Kling 3.0 Turbo, 5 s at 1080p, 10 credits, ping-ponged to 10 s as `public/plate_loop.mp4`, git-ignored, so regenerate or copy it) under the brand grid. The 3D glass icons in `public/icons/` came from `gpt_image_2_5` at 0.25 credits each, background-removed in Higgsfield. Cards use `glass`, entrances de-blur, and the proof card gets a `Sheen` when the count lands.
