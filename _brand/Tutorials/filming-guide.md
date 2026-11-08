# Filming guide: long-form tutorials for Circle

How to record a tutorial so the edit comes out looking like the hybrid style (a talking head that links the sections, real screen demos with zoom-ins, Locate-branded title cards, split frames and lower thirds). Written for someone who has never filmed long-form before. Follow the **recommended setup**; the rest is there if you want it later.

---

## The short version

1. Plan the video as a list of sections, not a script.
2. Record **two kinds of footage, separately**:
   - **Face pieces** on your iPhone: the intro, one short line before each section, and the outro.
   - **Screen pieces** on your PC with OBS, talking through what you're doing as you click.
3. Use **the same clip-on mic** for both, so your voice sounds the same throughout.
4. Drop everything in one folder with a short `notes.md`, and the edit does the rest.

Recording face and screen separately (instead of both at once) is the easiest way to start. Nothing needs syncing, a fluffed demo only means redoing that one section, and you never have to look at the camera and the screen at the same time.

---

## 1. Plan it (15 minutes)

Write a one-page outline. A tutorial that works well on Circle looks like this:

| Part | Length | Recorded on | What you say |
|---|---|---|---|
| Hook | 20–40 s | Face | What they'll be able to do by the end, and why it matters to them |
| What you need | 10–20 s | Face | Accounts, tools or files to have ready |
| Section 1…N | 1–3 min each | Face line, then screen | One face line ("First, we'll connect your inbox."), then the demo |
| Recap | 20–30 s | Face | The 3 things they just learned |
| Next step | 10–20 s | Face | What to do now (post a question in the community, try it, the next lesson) |

Aim for 5–15 minutes in total. If it runs past 15, split it into two lessons.

**Script the face pieces, bullet-point the screen pieces.** Face lines are short, so write them out and read them a couple of times before recording. For the screen demos, just list the steps. Talking it through naturally sounds better than reading.

---

## 2. Gear

**What you probably already have:** an iPhone, a window, a Windows PC.

**Worth buying first (in this order):**
1. **A wireless clip-on mic with a USB-C receiver** (DJI Mic or RØDE Wireless GO type). This makes the biggest difference by far. Plug the receiver into the iPhone for face pieces and into the PC for screen pieces, so both sound identical. Don't use AirPods or the laptop's built-in mic.
2. **A phone tripod with a phone clamp**, tall enough to put the phone at eye level when you're seated.
3. **One soft LED key light** (a panel with a diffuser), if your room is dark or you film at night.

---

## 3. Face pieces (iPhone)

**Camera settings**
- Rear camera (not the selfie camera), **landscape**.
- 4K at 30 fps (Settings → Camera → Record Video). The extra resolution lets the edit punch in without going soft.
- Before you start, tap and hold on your face to lock focus and exposure (AE/AF Lock), so it doesn't pulse while you move.
- Do Not Disturb on, so no notifications or calls interrupt a take.

**Framing**
- Phone at eye level, about 1–1.5 m away.
- Frame from mid-chest up, with a hand's width of space above your head.
- Sit roughly in the centre. The edit makes the split frames, so you don't need to leave space on one side.
- Sit at least 1 m in front of the wall behind you, so the background falls a little soft.

**Light**
- Face a window, or put the key light about 45° to one side and slightly above eye level.
- The background should be a bit darker than your face. A lamp, a shelf or a plant behind you adds depth (both reference videos do this).
- Avoid a bright window behind you and overhead lights only.

**Doing the takes**
- Say each line, pause, and if you fluff it, just start the sentence again. Don't stop recording. The edit picks your best take and cuts the rest, the same way it does for reels.
- Look at the lens, not the screen.
- It's fine to record all face pieces in one go, one after another, in one long clip.

---

## 4. Screen pieces (PC)

**Use OBS Studio** (free, obsproject.com). One-time setup:
- Settings → Video: base and output resolution **the same as your screen** (e.g. 2560x1440, or 1920x1080 on a 1080p screen), **30 fps**. Recording at full resolution keeps text sharp when the edit zooms in.
- Settings → Output: recording format **MP4** (or MKV, then File → Remux Recordings to get MP4).
- Settings → Audio: mic = the clip-on mic receiver. Turn desktop audio off unless the demo has sound you want in it.
- Sources: add **Display Capture** for your main screen.

**Before you hit record**
- Close every app and tab you don't need. Hide the bookmarks bar.
- Turn on Do Not Disturb in Windows, so no pop-ups appear.
- Zoom the browser or app to **125–150%**, so text is readable on a phone.
- Use demo or dummy data. **No client names, emails or figures on screen.** Circle members will see everything.
- Have logins done already, so you're not typing passwords on camera.

**While recording**
- Talk through what you're doing as you do it ("Now I'll click Settings, top right").
- Move the mouse slowly and deliberately. Pause for a second after each click so the edit can zoom in on it.
- Scroll slowly.
- If something goes wrong, pause, say "again", go back a step and redo it. The edit cuts the mistake out.
- One recording per section is easiest. One long recording is fine too, if you pause between sections.

---

## 5. Sound

- Clip the mic mid-chest, about a fist below your chin, away from your collar and clothing that rustles.
- Pick a quiet room with soft things in it (a rug, curtains, a couch). Bare rooms echo.
- Turn off the aircon, fans and anything that hums.
- Stay silent for 5 seconds at the start of each recording. The edit uses that room tone to clean up background noise.

---

## 6. Hand over

Create one folder per tutorial:

```
_brand/Tutorials/Raw Footage/YYYY-MM-DD_topic/
    face/       the iPhone clips (any names)
    screen/     the OBS recordings, named in order: 01_connect-inbox.mp4, 02_...
    extras/     optional: screenshots or images you want shown (see below)
    notes.md
```

**You don't need to make any graphics.** The title cards, chapter cards, name labels, zooms, split frames, counting-up numbers and key-point cards are all built in the edit from what you say. Screenshots of anything you showed on screen are taken straight from your recordings.

Only put something in `extras/` when it **isn't in your screen recordings**: a result from another day, a PDF page, a phone screenshot, a photo, a product mockup. Name each file for what it shows (`inbox-before.png`, `results-dashboard.png`) and mention it in `notes.md` next to the line where it belongs. Same privacy rule as the screen: blur or crop client details first, or say in `notes.md` that the client has OK'd it.

Get iPhone clips onto the PC with the cable (Photos app → Import) or by uploading them to Google Drive from the phone.

`notes.md` only needs:
- The title of the lesson.
- The section list in order (copy it from your outline).
- Brand and product names you say (so they're spelt right and get their logo).
- Anything that must appear on screen: a link, a figure, a download.
- Anything to cut or hide (a client name that slipped onto the screen, for example).

---

## What the edit does with this

So you know what you don't need to worry about while filming:
- Cuts pauses, ums, fluffs and repeated takes.
- Puts a Locate-branded title card at the start of each section.
- Zooms in on the screen where you click, and adds lower-third labels for tools and links.
- Mixes in split frames (you beside the screen) and the occasional mockup or key-point card, so the picture changes regularly.
- Adds a quiet music bed and levels the sound.
- Exports a 1920x1080 MP4 for Circle, plus a section list with timestamps for the lesson description.

---

## Checklist before every recording

- [ ] Mic charged, clipped on and plugged into the right device
- [ ] Do Not Disturb on (phone and PC)
- [ ] Phone landscape, eye level, 4K 30, focus locked on your face
- [ ] Light in front of you, nothing bright behind
- [ ] Screen tidy, browser zoomed, dummy data, logins done
- [ ] 5 seconds of silence at the start
