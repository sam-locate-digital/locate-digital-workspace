# Formats in the weekly mix

Specs for every format `locate-content` plans. Reels with talking go through `reels-script`. This file covers what the skill writes itself, and how each reel type should be briefed to `reels-script`.

## Design tokens (all static posts)

- Size: 1080 × 1350 (4:5) for carousels and single images
- Canvas `#FBFCFF` with a faint `#E6E6E6` grid, white cards with a `#E6E6E6` border and 32 px radius
- Type: Public Sans (body, 600–800) and Newsreader (italic emphasis word with the blue brush underline, numerals). Sam chose on 2026-11-05 to keep the serif keyword with the underline for now; it may change later, so don't switch it without being asked. Not Poppins, Inter or Montserrat. (`_brand/brand.json` still lists Poppins; it's out of date. `_brand/brand-guidelines.html` and the reel style are the source.)
- Locate Blue `#007AE8` for every accent. Orange `#FF5900` once per post at most, on the last slide's CTA.
- Sentence case, digits for numbers, Australian spelling, no emojis or exclamation marks
- Real screenshots and real photos of Sam (`_brand/photos/`, `_brand/Content/Weeks/`) over icons and stock

---

## 1. Teaching reel (3 a week)

Brief `reels-script` with: the topic, the format (value list or tutorial), the area (AI or marketing), and any real screen or setup Sam can show. Ask for the main hook plus 2 trial hooks.

Good topics are one job done properly: "4 prompts that write a file note in 2 minutes", "the 3 fields your enquiry form actually needs", "how I get Claude to chase missing documents".

## 2. Series episode (1 a week)

Brief `reels-script` with: "Series episode, AI fix of the week" plus the fix.
- Series title card in the first 2 seconds (reel style motion kit #1)
- Shape: the problem in one line → the fix → show it working on a real screen → who it's for → "Follow for next week's fix."
- 45–60 s
- Same title card, same opening line pattern, every week. Consistency is what makes people follow for the next one.

## 3. Short journey reel (2 a week)

Written here. 5–15 seconds of real footage with one or two lines of on-screen text. No voiceover, or one spoken line at most. These are cheap to make and reach far: the reference accounts got 59K–473K plays from 5–10 second reels like this.

**Shapes that work:**
- **Milestone line:** "Today was my first full week running Locate." Over footage of the moment.
- **Routine list:** a stacked list over walking or desk footage, e.g. "5:30am start / Gym / Two client sessions / Built an enquiry summariser / Home by 6". (Remy's "8h sleep / iced americano / Claude…" reel did 59K in 5 seconds.)
- **Grid:** "Every day / once a week / once a month" with small photos of each habit. (Jun's version did 322K.)
- **POV line:** "POV: your AI assistant drafted 14 file notes while you were at lunch." Only if it's true.

**Rules:**
- The on-screen line is the hook. It must be specific and true. Use Sam's real week.
- Footage is real: early starts, the desk, client-session prep (no client details), the gym-to-desk routine, Melbourne streets. No family.
- Text: sentence case, Public Sans, in the safe zone (not the top 220 px, bottom 420 px or right 120 px).
- Quiet instrumental or a trending audio from Instagram's library.
- Caption carries the story: 40–100 words in `locate-voice`'s register, present tense, ending on what's next. Optional "Follow along" line.
- Trial hooks: 2 alternative on-screen lines.

## 4. Story reel (1 a week)

Brief `reels-script` with: "Story reel" plus the moment. Structure (from Tahlia's "I quit my dream job", 183K plays):
1. **The decision**, said plainly in the first line, also on the title card: "I left my corporate job to build an AI training firm."
2. **Why it was hard or what was at stake**, in one or two lines. Real, not dramatic.
3. **Show, don't tell:** a real clip or photo from the moment (the last day, the first client session, the empty new desk).
4. **What keeps it moving:** who's backing Sam, or what's next this week.
5. **Invite:** "Follow along if you want to see where this goes."

30–45 s, talking head in a casual real setting, calm pace. No "what I got wrong" framing and no comeback arcs.

---

## 5. Carousels (3 a week)

### 5a. Teaching carousel: built to be saved
6–8 slides on the light grid canvas.
1. **Cover:** the hook (10 words max, a `reels-script` formula) and a short subline. One emphasis word in Newsreader italic with the blue brush.
2. **Why it matters:** the tension in one or two lines ("Most enquiry forms lose the client before the first call.")
3–6. **One step per slide:** a short heading with a blue numeral (1, 2, 3, never 01) and one or two sentences, plus a real screenshot or the exact prompt in a white card.
7. **Recap:** the steps as a checklist.
8. **Last slide:** "Save this for your next team meeting", "Follow for more fixes like this", or the comment keyword. Orange button only here.

### 5b. Prompt carousel
Same layout. Each middle slide is one copy-ready prompt in a white card, with one line on when to use it. Example: "5 prompts for cleaner file notes". The prompts must be ones Sam has actually tested.

### 5c. Story or journey carousel (photo story)
Matches the 2 November carousels in `_brand/Content/Weeks/2026-11-02/`: full-bleed real photos of Sam, one bold headline line and a short white subline near the bottom, one beat per slide, 5–7 slides. Build with the `photo-story-carousel` skill.
- Slide 1 states the decision or moment ("I left my corporate job to build an AI training agency. This is why.")
- The middle slides move through the story, one photo and one line each
- The last slide is where it's heading, plus "Follow the journey"

Those slides currently use Poppins with a yellow headline, which the reel style rules out for video. Keep the look consistent with what's already posted unless Sam decides to move it to Public Sans and Locate Blue.

---

## 6. Single image (2 a week)

### 6a. Claim card
One true, slightly uncomfortable line on the canvas, e.g. "Most firms don't need an AI tool. They need someone to set up the one they already pay for." One emphasis word with the brush. The caption explains it in 40–100 words and ends on the practical consequence.

### 6b. Real photo + journey caption
A real photo of Sam working (studio headshot, a client session, the laptop, the office). The caption's first line is the hook; the rest is present-tense journey in `locate-voice`'s register. 60–120 words.
