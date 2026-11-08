# Content: Locate reel style and Instagram workspace

This folder (formerly `AI Video Editor`, combined with `social-media` on 2026-11-05) is the one home for Sam's Instagram content: planning, research, scripts, footage, editing and exports. The skills that use it stay in `_skills/` (`locate-content`, `reels-script`, `edit-reel`). Every edit follows the **Locate Reel Style** below. Sam approved it on 2026-11-04. Only break a rule when Sam says so for a particular reel.

- Visual sheet: [locate-reel-style.html](locate-reel-style.html), also published at https://claude.ai/artifact/Npa53by2cxT7U26kvazboQ
- Brand source of truth: `../brand-guidelines.html` (colours, fonts, voice)
- Built from the 5 reference reels in `References/` (style inspiration only; never reuse their footage, music or graphics)

## Folders

- `_DROP FILES HERE/`: the **only folder Sam uploads to**. It holds one folder per post that needs his footage or photos, named `NN Ddd d Mmm - Topic - WHAT` (e.g. `03 Tue 10 Nov - Where AI goes first - FILM + 1 SCREENSHOT`), each with a READ ME listing the shots and the script. The nightly build moves the files to the post's home folder (`Raw Footage/...` or `Weeks/.../photos/`) and moves the empty folder to `_done/`.
- `profile.md`: @locatingsam bio, pinned posts, highlights and intro reel plan (`locate-content`)
- `insights-log.md`: what earns follows, winning Trial Reels hooks (`locate-content` reads it every week)
- `Weeks/`: one folder per week, named by the Monday (`YYYY-MM-DD/`), holding `plan.md` plus that week's carousel slides and images. Images are git-ignored.
- `autopilot/`: the scheduled content jobs (Sunday 6pm plan, nightly 10pm build) that run Claude Code from Windows Task Scheduler. The Status table at the top of each `Weeks/<Monday>/plan.md` drives them. See `autopilot/README.md`.
- `Research/`: `swipe-file.md` (studied reels), `reference-accounts.md`, `competitors.md`, `trend-log.md` and `hooks-flat.txt` (the hook library)
- `Scripts/`: reel scripts from the `reels-script` skill, named `YYYY-MM-DD_topic.md`. Force-align captions to these.
- `Raw Footage/`: source clips, one folder per reel (`YYYY-MM-DD_topic/`) holding the clips, any screenshots and a `notes.md` (script, brands, numbers, call to action, pause cut, client sign-off). Read `notes.md` first. Never edit or delete originals.
- `Reel checklist.md`: Sam's filming and hand-over checklist. When Sam says "preview first", render a half-size preview for approval before the full-quality export.
- `References/`: inspiration reels and their `.info.json` files.
- `Exports/`: finished reels, named `YYYY-MM-DD_topic_v1.mp4`. Bump the version number. Never overwrite.
- Media and `node_modules` are git-ignored (see `.gitignore`). Scripts, configs and notes are tracked.

## Tools

These are installed globally: FFmpeg (Gyan build), yt-dlp, and openai-whisper in the main Python 3.12. Remotion is installed per project (`npm install` inside that reel's project folder) when a reel needs motion graphics. Use Whisper word timestamps for caption timing, and force-align them to the script text when there is one.

The whole process is packaged as the **`/edit-reel` skill** (`_skills/edit-reel/`). Use it for every edit, re-render, change request and CapCut pack. Start every edit from `remotion-kit/`: the Remotion graphics kit (Remotion 4.0.537) plus the Python pipeline that preps footage, cuts pauses, builds captions, makes original music and mixes to −14 LUFS. Its README has the steps and the lessons from the first reel. Copy it to a scratch folder on C: to work, and never install `node_modules` on Drive.

## The six rules

1. **Talk from frame one.** First word at 0.0 s and the hook caption on screen in frame one. No logo intro, no "hey guys".
2. **Change something every 2–4 s.** A cut, punch-in or graphic. Never more than 4 s on an unchanged frame.
3. **1–3 words per caption.** Word-timed, white TikTok Sans with a plain black outline, centred low on the frame. One key word every 5–8 s is set in Newsreader italic with the blue brush underline (Sam, 2026-11-05: keep the serif keyword for now; may change later).
4. **One accent colour.** Locate Blue for any brand touch. Orange appears once at most, on a call to action.
5. **Premium graphics in a social font.** Use the v2/v4 look: frosted glass canvas with a light grid, split screens, step cards, a proof card with count-up, floating 3D glass icons and app-tile logos. Every graphic is in TikTok Sans, never the brand fonts. Show real proof as the actual screenshot on the canvas, and no section titles like "How to set it up" (Sam, 2026-11-04: asked for v2's graphics back after trying a no-graphics v3).
6. **−14 LUFS, voice first.** Clean voice, quiet instrumental bed, a soft click when a graphic lands.

## Captions and type

| | |
|---|---|
| Caption | TikTok Sans 800 (TikTok's platform font), 68 px on a 1080 frame, white with a plain black outline about 5 px wide. Social reels use standard platform fonts, not the brand fonts (Sam, 2026-11-04). |
| Emphasis | One key word every 5–8 s, on the number, the outcome or the turn of the sentence: Newsreader 600 italic, 100 px, white with a soft shadow, and the blue brush sweeping under it in 0.35 s. Any setup words sit on the same line, in TikTok Sans (60 px, outlined). Lines over 20 or 24 characters step down (84/52 or 72/46 px) so the pair stays on one line, low on the frame and clear of the mouth. Kit style `keyword` (the house default). Take the words from the script's **bold** words. |
| Chunking | 1–3 words, at most 2 lines and 18 characters a line. Spoken brand names (GoHighLevel, Claude) show as an app-tile logo instead of a caption. |
| Position | Centred, bottom of the text block at about 76% height (y ≈ 1470 px), clear of the mouth on close selfie framing and above Instagram's bottom zone |
| Entrance | 0.12 s fade, scale 94% → 100%. No bounce, typewriter or colour-per-word karaoke. |
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

- Length 30–60 s, except **short journey reels** (approved 2026-11-04): 5–15 s of real footage with one or two lines of on-screen text and little or no talking, planned by the `locate-content` skill. They skip the talking-90% rule and the end card, but keep the caption type, safe zones, one accent colour and no emoji. Visual change every 2.5–3.5 cuts per 10 s, average shot no longer than 4 s, talking at least 90% of the runtime.
- Speech at natural speed, 1.1× at most. Aim for about 200–240 words a minute after tightening.
- Cut every pause longer than 0.25 s and keep natural breaths.
- Two framings from one clip: wide 100% and punch 118%. Alternate them on jump cuts and punch in on emphasis lines. Use a slow push from 100% to 105% on takes longer than 6 s.
- Use hard cuts only. Graphics enter in 0.2 s (slide up 40 px and fade, ease-out) and leave on a cut. No spin, glitch, zoom-blur or whip pan.
- B-roll: real screens, real offices and real documents with private details blurred. No stock footage of money, handshakes or people pointing at laptops.
- Beat structure (45 s example): hook 0–3 s → setup and credibility 3–10 s → the useful bit, one idea at a time, 10–40 s → CTA end card for the last 3–5 s.

## Motion graphics kit (build as reusable Remotion components)

> **Current social build (v4, 2026-11-04):** `remotion-kit/src/Reel.jsx` is the template. Call `useSocialFonts()` so every piece below renders in TikTok Sans instead of Newsreader and Public Sans. Use `SocialCaption` (white, black outline), `PremiumCanvas` (Higgsfield glass plate), `StepCard` and `ProofCard` (frosted glass), `Shot` for real screenshots on the canvas, `FloatIcon` (3D glass icons in `public/icons/`) and `LogoPop` app tiles. Leave out section titles. The font names in the list below are the brand versions and only apply outside social reels.

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

Tracked uppercase captions. Inter, Poppins or Montserrat (social reels use TikTok Sans). Emoji, exclamation marks or hype words. Rainbow or colour-per-word captions. More than one orange element. Flashy transitions. Stock cash or handshake shots. Voice faster than 1.1×. Logo intros. 01/02 numbering. Client testimonials, case studies, client names or client documents on screen without written sign-off. (Sam's own figures and results, like $200,000, are fine: show them in the captions and on the proof card.)
