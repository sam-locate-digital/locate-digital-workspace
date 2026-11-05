# Swipe file: hook library and studied reels

## Master source: live Google Sheet

**Title:** Hooks
**File ID:** `1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4`
**Open:** https://docs.google.com/spreadsheets/d/1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4/edit
**Local copy:** `hooks-flat.txt` in this folder (snapshot from May 2026, searchable offline)

The Sheet holds ~1000 **intro hooks**: the first-3-second opening lines of a reel, not full scripts. Most use fill-in-the-blank patterns (`[insert X]`) so they adapt to any topic.

### Columns to use
- **Hook**: the intro line template
- **Inspo link**: Instagram/TikTok URL of the reel that went viral with that hook (watch it to study the original)

### Columns to ignore
- **Brand** and **Notes**

### How the skill reads it

1. Search `hooks-flat.txt` for keywords from the topic first. It's fast and works offline.
2. For hooks added since the snapshot, read the Sheet with the Google Drive connector's `read_file_content` tool and the file ID above. It's large (~150k chars), so read in ~30k-char chunks if it truncates.
3. Pull 5–8 candidates, keep the strongest 1–3, fill the `[insert X]` blanks, and cite the inspo link in the output.

### If Drive isn't connected
Use the local copy and say once that the live Sheet wasn't checked.

---

## Studied reels (full breakdowns)

Reels Sam picked to model, broken down hook-first. The hook formulas in the `reels-script` skill come from these. When adding one, use this template:

```
### [creator] — [topic] — studied [YYYY-MM-DD]
- Link:
- Length / format:
- Title card:
- Spoken hook (verbatim):
- Line 2:
- Frame-1 visual:
- Formula: (one of the seven in the reels-script skill, or a new one)
- Structure:
- CTA:
- Steal this: 1–2 lines
```

---

### Content Principles skill — "Skill of the Week" — studied 2026-11-04
- Link: https://www.instagram.com/reel/DeeroIoRpnr/
- Length / format: ~61s, talking head with split-screen motion graphics, cut every 1.5–2.5s
- Title card: "500 hours of short form, in one claude skill"
- Spoken hook: "Why is AI so bad at writing content despite all of the YouTube videos on viral hooks that you've fed it?"
- Line 2: "Well, it's because all Claude actually takes from those videos is the steps." Gives the cause straight away.
- Frame-1 visual: Meme collage with AI logos as heads on top, creator below, a typewriter-head figure typing
- Formula: Failed-fix question
- Structure: problem → diagnosis (copies steps, misses the thinking) → fix (teach principles) → series intro → the asset → use cases → proof (1.8M views, +15.3K followers in 30 days) → CTA
- CTA: "Comment the word SKILL and I'll send it over", with "I shouldn't even be doing this" urgency
- Steal this: name the thing they've already tried in the hook ("despite…"). A recurring series name. An analytics screenshot as proof.

### Cindy Zhu — design effects from GitHub repos — studied 2026-11-04
- Link: https://www.instagram.com/p/DcxV37-CJOC/
- Length / format: ~62s, talking head with UI cards and meme inserts over the speaker, cut every 1.5–3s
- Title card: "How to create Advanced Design Effects using Claude & Github"
- Spoken hook: "Did you know that the best designers these days use GitHub as their asset library?"
- Line 2: "If you've ever seen those insane visual effects online and thought 'how does one even achieve that?'" Names the viewer's own reaction.
- Frame-1 visual: The finished effects shown on cards under her face
- Formula: Insider move
- Structure: hook → relatable "how do they do that" → why it's possible now → "4 repos you can steal" → #1–#4, one line each with a demo → objection killer ("you don't have to code any of this") → CTA
- CTA: "Follow me and comment Repo, and I'll send you all four links and exactly how to use them."
- Steal this: show the end result in frame 1. Each list item gets a name, one line and a visual. Kill the main objection right before the CTA.

### Rooftop creator — "the one thing" for Instagram growth — studied 2026-11-04
- Link: https://www.instagram.com/p/C8QFlapP9YW/
- Length / format: ~67s, talking head across many locations, cut every 2–3s, yellow keyword highlight in captions
- Title card: none, word-by-word captions only
- Spoken hook: "Here is the one thing you need to know if you actually wanna blow up on Instagram."
- Line 2: "And no, it's not what niche you're in, it's not what captions are above your head, and it's not knowing which creator to copy next."
- Frame-1 visual: Standing on a rooftop ledge, low angle against the sky. It's a pattern interrupt, then the script jokes about it.
- Formula: The one thing (and rule out the obvious)
- Structure: hook → rule out 3 obvious answers → reveal ("who your viewer is") → mid-roll CTA at ~20s with the Google Doc shown → examples → why it works → mindset shift (8 billion vs 100K) → repeat CTA
- CTA: "Comment viewer and I'll send you this entire guide for free." Said at 0:21 and again at the end.
- Steal this: ruling out the obvious answers holds attention right up to the reveal. Show the freebie on screen when it's first mentioned.

### Mino Lee — 7 ways to un-slop AI editing — studied 2026-11-04
- Link: https://www.instagram.com/p/De0yEPUN0RQ/
- Length / format: ~66s, handheld walk-and-talk on a city street, real-life B-roll (buying a hot dog), static native-style pop-ups
- Title card: "SLOP" (282 views) vs "VIRAL" (495K views) split
- Spoken hook: "If you want to start editing with Claude, but you don't want your videos to look like AI vibe-coded slop, these are seven ways to un-slop your AI editing."
- Line 2: "And yeah, this video was completely edited by Claude." The video is its own proof.
- Frame-1 visual: Side-by-side view counts, bad vs good
- Formula: Want, but don't want
- Structure: hook + self-proof → #1 → mid-roll CTA at ~18s → #2–#7, each a concrete instruction → final CTA tied to #7
- CTA: Two keywords: "slop" (mid-roll, for the skill) and "Claude" (end, for the MCP)
- Steal this: a numbers comparison in frame 1. Make the reel itself the demo. Plain 2–3 word captions, real screenshots, no animated icons.

### Alex Hormozi — 15 years of sales advice in 60 seconds — studied 2026-11-04
- Link: https://www.instagram.com/p/DfS9tS4IcP6/
- Length / format: ~49s, single take on a white backdrop, LED countdown timer on the desk
- Title card: "15 YEARS OF SALES ADVICE IN 60 SECONDS" (red banner), then a white card per point ("#1 NO DISCOUNTS")
- Spoken hook: "If you can't sell anything, you can't make money. So here's 15 years of sales advice in 60 seconds."
- Line 2: Straight into #1. No setup, because the timer is the tension.
- Frame-1 visual: He hits a countdown timer starting at 01:00
- Formula: Compression
- Structure: stakes + promise → 11 rapid one-sentence rules, each with a 2–3 word title card
- CTA: none. Built for saves and shares.
- Steal this: a stakes line before the promise. A physical timer as a retention device. Short title card per point.

### Alex Hormozi — starting over with $0 — studied 2026-11-04
- Link: https://www.instagram.com/p/DfFZ_AYIMTO/
- Length / format: ~134s, seated talking head with dense animated infographics, cut every 1.5–3s
- Title card: "HOW I WOULD START OVER IF I HAD $0 TO MY NAME" plus the 3-level circular map
- Spoken hook: "If I woke up with zero dollars tomorrow and wanted to be a millionaire, here's what I would do in 2026."
- Line 2: "Step one: I'd determine these three things…" Straight into the plan.
- Frame-1 visual: The whole 3-level roadmap on screen at once
- Formula: Start over
- Structure: scenario → Level 1 (3 steps) → Level 2 (5 steps) → Level 3 (4 steps) → "I know that was a lot" → CTA
- CTA: "Comment MAP below and get a personalised business scaling roadmap for free in under 30 seconds", with the tool shown on screen
- Steal this: show the full map in frame 1 so they stay to see it filled in. Add the current year to make it feel fresh. "I know that was a lot" sets up the freebie.

### Chris Williamson ft. Alex Hormozi — becoming worthy of success — studied 2026-11-04
- Link: https://www.instagram.com/p/De-Tn1fRH7g/
- Length / format: ~97s podcast clip, multi-camera angle switches every 4–8s, no B-roll
- Title card: "How To Become Worthy Of Success" (white pill, first 10s)
- Spoken hook: "The fastest way to attract what you want in life is to deserve it."
- Line 2: "By doing so much work, it becomes unreasonable not to achieve it."
- Frame-1 visual: Podcast studio, which signals authority
- Formula: Reframe
- Structure: aphorism → expansion → guest's matching view ("volume negates luck") → emotional close (have a quest)
- CTA: none. Built for shares, saves and the full episode.
- Steal this: "the fastest way to X is [not a hack]" sets up a hack and flips it. Works best for quick hits and mindset content.

---

### @aiwithremy — "I banned AI slop at my company" (Skill of the Week) — studied 2026-11-04
- Link: https://www.instagram.com/reel/DeO1JDpx2Lc/
- Length / format: ~76s, talking head with polished UI graphics, cut every 1–3s. 744K plays, 13.9K comments.
- Title card: "SKILL of the week" series card at ~0:31 (no separate opening title)
- Spoken hook: "The biggest problem with using AI to build websites is that even if you give it great references, it still comes out looking like AI slop."
- Line 2: Names the exact clichés (purple gradients, italic serif headlines, cream "old money" backgrounds). It proves the creator sees what the viewer sees.
- Frame-1 visual: AI app logos popping up around the creator's hands
- Formula: Failed-fix question (stated as a problem)
- Structure: problem → named clichés → stakes ("the best product in the world won't be taken seriously") → testing proof (12 tools tested, 11 marked slop on a graphic) → series intro → the fix and who made it → how to use it → own-use proof ("mandatory for my whole team") → CTA
- CTA: comment "SKILL", delivered standing on the couch as a pattern interrupt
- Steal this: credibility from testing, not results. A recurring series card. Naming the specific clichés the viewer already dislikes.

### @tahlia.kennedy — "I quit my dream job" — studied 2026-11-04
- Link: https://www.instagram.com/reel/DfO5RjLTDqt/
- Length / format: ~40s, single talking-head take sitting on the floor at home, with a picture-in-picture clip. 183K plays (a near-identical version got 10.5K).
- Title card: "I quit my dream job." (white pill, top, the whole reel)
- Spoken hook: "So, I just quit my dream job to build something of my own full time."
- Line 2: "And it's probably been one of the hardest decisions I've ever had to make."
- Frame-1 visual: casual, unpolished home setting, direct eye contact
- Formula: Story (the decision, stated plainly)
- Structure: decision → why it was hard → real clip of the moment (picture-in-picture) → who's in the creator's corner → "follow along on this journey"
- CTA: soft follow-along
- Steal this: the story structure for journey reels. The paradox in the hook ("dream job" + "quit"). A real clip instead of describing the feeling. Posting two versions and keeping the winner.

---

## Quick captures (manual)

Reels spotted in the wild that aren't in the Sheet yet. Migrate to the master Sheet weekly.

```
### [creator handle] — [YYYY-MM-DD]
- Link:
- Hook (verbatim):
- Format: talking head / b-roll VO / text-on-black / screen rec / split-screen
- Why it worked: 1–2 lines
```

_(none yet)_
