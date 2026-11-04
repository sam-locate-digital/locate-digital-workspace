# AI Video Editor: Locate reel style

This folder is where Sam does all video editing and social posting. Every edit follows the **Locate Reel Style** below. Sam approved it on 2026-11-04. Only break a rule when Sam says so for a particular reel.

- Visual sheet: [locate-reel-style.html](locate-reel-style.html), also published at https://claude.ai/artifact/Npa53by2cxT7U26kvazboQ
- Brand source of truth: `../brand-guidelines.html` (colours, fonts, voice)
- Built from the 5 reference reels in `References/` (style inspiration only; never reuse their footage, music or graphics)

## Folders

- `Scripts/`: reel scripts from the `reels-script` skill, named `YYYY-MM-DD_topic.md`. Force-align captions to these.
- `Raw Footage/`: source clips. Never edit or delete originals.
- `References/`: inspiration reels and their `.info.json` files.
- `Exports/`: finished reels, named `YYYY-MM-DD_topic_v1.mp4`. Bump the version number. Never overwrite.
- Media and `node_modules` are git-ignored (see `.gitignore`). Scripts, configs and notes are tracked.

## Tools

These are installed globally: FFmpeg (Gyan build), yt-dlp, and openai-whisper in the main Python 3.12. Remotion is installed per project (`npm install` inside that reel's project folder) when a reel needs motion graphics. Use Whisper word timestamps for caption timing, and force-align them to the script text when there is one.

## The six rules

1. **Talk from frame one.** First word at 0.0 s and the hook caption on screen in frame one. No logo intro, no "hey guys".
2. **Change something every 2–4 s.** A cut, punch-in or graphic. Never more than 4 s on an unchanged frame.
3. **1–3 words per caption.** Word-timed, centred at 62% height. One Newsreader italic emphasis word with a blue brush every 5–8 s.
4. **One accent colour.** Locate Blue carries every graphic. Orange appears once, on the end-card call to action.
5. **Graphics live on a light grid.** Soft white canvas, faint grid, white cards with real numbers. No dark tech panels.
6. **−14 LUFS, voice first.** Clean voice, quiet instrumental bed, a soft click when a graphic lands.

## Captions and type

| | |
|---|---|
| Caption | Public Sans 800, 64 px on a 1080 frame. White with a soft shadow (0 4px 18px rgba(0,0,0,.5)) on footage, ink #0D0D0D on the canvas. |
| Setup line | Public Sans 600, 52 px, directly above an emphasis word |
| Emphasis | Newsreader 600 italic, 112 px. Blue #007AE8 brush sweeps under it in 0.35 s. Put it on the number, the outcome or the turn of the sentence. |
| Chunking | 1–3 words, at most 2 lines and 18 characters a line |
| Position | Centred, bottom of the text block at 62% height (y ≈ 1190 px) |
| Entrance | 0.14 s fade, scale 92% → 100%. No bounce, typewriter or colour-per-word karaoke. |
| Writing | Sentence case, Australian spelling, digits for numbers ($2,850, 9 days), no emoji, no exclamation marks |

Brush SVG (viewBox `0 0 200 28`, preserveAspectRatio none, width 108% of the word, offset −4%):
`M3 19 C 28 11, 96 5, 190 2 C 196 1, 200 4, 197 8 C 186 10, 120 13, 60 17 C 38 19, 18 21, 9 25 C 3 27, 0 22, 3 19 Z`

## Colour

- Locate Blue `#007AE8`: brush, name tag, step numerals, chart lines, highlight marker (blue at 14% opacity, never yellow)
- Cyan `#75DFEE`: canvas corner glow and guide lines only, never text
- Orange `#FF5900`: end-card button only, once per reel. It may also strike through an old figure on a proof card.
- Canvas: `#FBFCFF` with a `#E6E6E6` grid (54 px squares at 1080 wide). Cards are white with a #E6E6E6 border, 32 px radius and a soft blue-tinted shadow.
- Ratio: about 60% neutral and footage, 30% blue, 6% cyan, 4% orange
- Footage: natural, clean grade with true skin tones and no heavy LUT

## Cuts, zooms and pacing

- Length 30–60 s. Visual change every 2.5–3.5 cuts per 10 s, average shot no longer than 4 s, talking at least 90% of the runtime.
- Speech at natural speed, 1.1× at most. Aim for about 200–240 words a minute after tightening.
- Cut every pause longer than 0.25 s and keep natural breaths.
- Two framings from one clip: wide 100% and punch 118%. Alternate them on jump cuts and punch in on emphasis lines. Use a slow push from 100% to 105% on takes longer than 6 s.
- Use hard cuts only. Graphics enter in 0.2 s (slide up 40 px and fade, ease-out) and leave on a cut. No spin, glitch, zoom-blur or whip pan.
- B-roll: real screens, real offices and real documents with private details blurred. No stock footage of money, handshakes or people pointing at laptops.
- Beat structure (45 s example): hook 0–3 s → setup and credibility 3–10 s → the useful bit, one idea at a time, 10–40 s → CTA end card for the last 3–5 s.

## Motion graphics kit (build as reusable Remotion components)

1. **Series title**: recurring segment name in the first 2 s, Public Sans 800 + Newsreader italic with the brush. The name is still to be chosen by Sam; "AI fix of the week" is a placeholder.
2. **Name tag**: shown on each speaker's first appearance for 3 s. Name in a blue pill (Public Sans 700, white), role on a white pill (Newsreader 400).
3. **Split screen**: graphic in the top 45% on the canvas, speaker in the bottom 55%
4. **Framework**: full-screen canvas. Steps build one at a time as they're said, with Newsreader 600 numerals in blue, single digits (1, 2, 3, never 01).
5. **Proof card**: white UI card. The number counts up over 0.8 s in Newsreader 600 blue. The old figure is muted with an orange strike. Optional blue tick chip.
6. **End card**: last 3–4 s on the canvas. A Newsreader question, an orange button with one keyword (e.g. Comment "notes"), and locatedigital.io. Sam keeps talking over it.

## Music and sound

- Mix to −14 LUFS integrated, true peak no higher than −1 dBTP
- Voice: noise removal, 80 Hz high-pass, light compression, a little presence at 3–5 kHz
- Music: instrumental only (soft piano, warm lo-fi or minimal electronic), 85–110 BPM, about 20 dB under the voice and ducked further during speech. Licensed or from Instagram's library, one track per reel. It lifts slightly under the end card and ends on the last frame so the loop is clean.
- SFX: soft click when a card lands, low whoosh into a full-screen graphic, small tick when a count-up stops. At most one every 4 s, never on caption words, no cash registers or airhorns.

## Export and safe zones

- 1080 × 1920, 9:16, 30 fps, H.264 High at 12–16 Mbps, MP4. Audio AAC 48 kHz 320 kbps.
- Keep text out of the top 220 px, bottom 420 px and right 120 px
- Cover image: frame one (the hook caption)

## Never

Tracked uppercase captions. Inter, Poppins or Montserrat. Emoji, exclamation marks or hype words. Rainbow or colour-per-word captions. More than one orange element. Flashy transitions. Stock cash or handshake shots. Voice faster than 1.1×. Logo intros. 01/02 numbering. Real client names, figures or documents on screen without written sign-off.
