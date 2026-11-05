# edit-reel reference

Commands, settings and gotchas for the steps in `SKILL.md`. `KIT` is `G:\My Drive\Claude Code.Locate\_brand\AI Video Editor\remotion-kit`, and `W` is the work folder in this session's scratchpad (for example `<scratchpad>\reel-<topic>`).

## Shell notes (Windows)

- PowerShell doesn't see a new winget install's PATH until restart. Start each command with
  `$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')`
- Set `$env:PYTHONIOENCODING='utf-8'` (captions and descriptions contain emoji and `$`).
- **Don't put multi-line `python -c "..."` in PowerShell.** It mangles quotes and f-strings. Write a `.py` file in the scratchpad and run that. Run Python with `-I`.
- Run anything over about 2 minutes (prep, renders) with `run_in_background`, then wait for the notification. Don't poll.
- FFmpeg can't decode SVG. Check logos in a Remotion still instead.

## Setup

```
mkdir W; copy KIT\* W\remotion\ (src, public, package.json); copy KIT\pipeline\*.py W\
cd W\remotion; npm install --no-fund --no-audit
```
`public/plate_loop.mp4` (the Higgsfield glass background) is git-ignored but sits in KIT\public on Drive. If it's missing, regenerate it (see Higgsfield below).

## Pipeline and the settings to change per reel

| Step | Command | Change first |
|---|---|---|
| Prep | `python -I prep.py "<Raw Footage folder>" W` | — (makes `media/*.mp4|wav`, `clips.json`) |
| Transcribe again | `python -I retranscribe.py W` | `HINT`: the brands, names and figures in this reel |
| Inspect a slice | `python -I segwords.py W\media\<clip>.wav <start> <end>` | — prints words and silences in source time |
| Edit list | `python -I edl.py W` | `SELECT` (clip, start, end, beat) in story order; `OVERRIDE` word timings for cleaned takes; `MAX_GAP` (0.25 default, or what Sam asks) |
| Cut | `python -I aroll.py W` | — makes `aroll.mov` |
| Hidden-repeat scan | `python -I longwords.py W\aroll.wav` | — any ordinary word over 0.55 s is a suspect (`ffmpeg -i aroll.mov -vn -ac 1 aroll.wav` first) |
| Captions | `python -I captions.py W W\remotion\src\data.json` | `REPLACE`, `BRANDS`, `EMPH`, tail length (`TOTAL = END_CARD + 0.3`) |
| Music | `python -I music.py <total s> W\music.wav 92` | BPM if wanted |
| Mix | `python -I audio.py W` | `EVENTS` (time, whoosh/click/tick) on graphic landings |
| Stems (CapCut) | `python -I stems.py W <pack dir>` | — run after `audio.py` |
| SRT and timings (CapCut) | `python -I srt.py W\remotion\src\data.json <pack dir>` | Its `timings.txt` lists PNG overlays, so for a graphics.mov pack, write `timings.txt` by hand |

Copy the cut into Remotion: `ffmpeg -i W\aroll.mov -c:v copy -c:a aac -b:a 256k -movflags +faststart W\remotion\public\aroll.mp4`

## Remotion

- Stills: `npx remotion still src/index.jsx Reel out/s_0300.png --frame=300 --scale=0.4 --log=error`, then tile them with ffmpeg `hstack` and Read the image.
- Preview: `npx remotion render src/index.jsx Reel out/preview.mp4 --codec=h264 --crf=23 --scale=0.5 --muted --concurrency=2`
- Full: `npx remotion render src/index.jsx Reel out/video.mp4 --codec=h264 --crf=16 --muted --concurrency=2 --overwrite --log=error` (about 9–10 minutes for 40 s). **Concurrency 2 is the max**: the default crashed the browser on this machine.
- Mux to spec:
  `ffmpeg -i out/video.mp4 -i W/mix.wav -map 0:v:0 -map 1:a:0 -c:v libx264 -profile:v high -preset slow -b:v 14M -maxrate 16M -bufsize 28M -pix_fmt yuv420p -r 30 -c:a aac -b:a 320k -ar 48000 -movflags +faststart -shortest final.mp4`
- Check: `ffprobe` duration and streams, `ffmpeg -af ebur128=peak=true` (I ≈ −14.0, peak ≈ −1.4), and a contact sheet with `fps=1,scale=150:-2,tile=10x4`.
- CapCut layers:
  - `ReelClean`: same flags as Full, makes `footage_silent.mp4`. Mux in the raw voice from `aroll.mov` as a guide track.
  - `Graphics`: `--codec=prores --prores-profile=4444 --pixel-format=yuva444p10le --image-format=png --muted --concurrency=2`. About 400 MB for 40 s.
  - Magenta backup: `ffmpeg -f lavfi -i color=c=0xff00ff:s=1080x1920:r=30 -i graphics.mov -filter_complex "[0][1]overlay=shortest=1,format=yuv420p" -c:v libx264 -crf 16 graphics_on_magenta.mp4`

## Layout constants (1080 x 1920)

- Safe zones: keep text out of the top 220, bottom 420 and right 120 px.
- Full-frame captions: block bottom at y 1470 (about 76%), clear of the mouth on close selfie framing.
- Split screen: canvas top 864 px (45%), and captions bottom at y 838, sitting above the seam. Footage shifted by `FACE_OFFSET` (−460 for close selfie framing) so the whole face shows.
- Logo pop: `cy` 960 in split, 1250 full. Size 230, held 1.1 s.
- Step cards start at y 300. Dimmed cards collapse to one line, so four steps plus a chip fit above the seam.
- `useSocialFonts()` switches every graphic to TikTok Sans. Big numbers in TikTok Sans need about 138 px (it's wider than the old serif).

## Higgsfield (connector)

- Call `get_preferences` before the first generation. Generate without a project unless asked.
- Quote first with `get_cost: true` and tell Sam the total.
- 3D icons: `gpt_image_2_5`, 1:1, 0.25 credits. Prompt pattern: "Premium 3D render of a single <object> icon made of frosted translucent glass with a soft blue (#007AE8) tint and a subtle cyan rim light, gentle inner glow, three-quarter view, floating, soft contact shadow, clean bright studio lighting, centred with generous margin, plain pure white background, no text, no logos". Then `remove_background` and download the PNG to `public/icons/`.
- Background plate: `kling3_0_turbo`, 9:16, 5 s, 1080p, 10 credits (Seedance 2.5 was 80). Ping-pong it to a seamless 10 s loop: `[0:v]scale=1080:1920,fps=30,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1`.
- Wait with `jobs_wait` (15 s per call) and download results with curl from `result_url`.

## Lessons (2026-11-04, the $200k automation reel)

- **Hidden repeats.** Four false starts survived the first cut because Whisper folded them into one long word ("that" lasting 1.2 s, "promotions" lasting 1.7 s). Always run `longwords.py` and re-transcribe the finished cut.
- **Mis-hearings.** A full-clip transcription leans on context: "go into code" for "going to Claude", and "not going to" for "gonna need". Re-transcribe the exact slice to settle a word. Initial-prompt hints can bias it too, so check against the slice.
- **Words dropped at piece edges.** The word-to-cut mapping assigns each word to the piece it overlaps most. Don't go back to midpoint-only mapping, which dropped the first word of several lines.
- **Sam's style changes from the review rounds:** captions are white TikTok Sans with a black outline (no brand serif, no brush). The graphics stay, but in TikTok Sans with no section titles. Real screenshots for proof, and brands as app-tile logos. The end card was dropped for this reel.
- **Close selfie framing** pushes captions down to about 76% and needs `FACE_OFFSET` in split screens. The checklist asks Sam to leave headroom.
- **4K iPhone clips** take over 10 minutes to prep. The checklist asks for 1080p/30.
