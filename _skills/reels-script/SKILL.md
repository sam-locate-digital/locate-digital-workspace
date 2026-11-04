---
name: reels-script
description: Writes Instagram Reels scripts for Sam's own Locate Digital account, aimed at Australian service business owners ($1–3M). Built around a three-layer hook (title card, spoken line, frame-1 visual), list and tutorial formats, and comment-keyword CTAs. Use when Sam asks for a reel, a reel script, hooks, a video idea or IG video content for Sam's own brand. NOT for client social posts (social-post) or written captions/carousels in Sam's voice (locate-voice).
---

# Reels script

Writes short-form video scripts for Sam's Instagram Reels: hook, body, proof, CTA, caption and shot notes.

## When to use
- Sam asks for "a reel", "hook", "script", "IG video", "video idea"
- Output is a Reel, not a long-form video, podcast clip or written post

## References (check before scripting)

**1. Hook library: about 1,000 proven intro hooks**
- Local copy: `$HOME/.claude/skills/reels-script/hooks-flat.txt` (markdown table: hook template | inspo link | brand | notes). Search it for the topic's keywords. It's fast and works offline.
- Live master: Google Sheet "Hooks", file ID `1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4`, read with the Google Drive connector's `read_file_content` tool. It may hold hooks newer than the local copy. If Drive isn't connected, use the local copy and say so once.
- Ignore the `Brand` and `Notes` columns.
- These are opening lines only, not scripts. Pull 5–8 candidates, keep the best 1–3, fill the `[insert X]` blanks, and cite the inspo link so Sam can watch the original.

**2. Files in this skill's folder** (`$HOME/.claude/skills/reels-script/`)
- `swipe-file.md`: reels already studied, with verbatim hooks and why they worked. Start here for structure.
- `trend-log.md`: this week's hooks, formats and audio. Lean the script toward what's spiking now.
- `competitors.md`: accounts being modelled. If a starred (⭐) account covered the topic recently, take a different angle.

If a reference is empty or has nothing relevant, carry on and flag it once at the top: "No [trend/swipe/competitor] data for this yet. Output uses general patterns."

## Audience (always)

**Service business owners as a whole**, turning over one to three million a year. A mix of accountants, lawyers, physios, dentists, osteos, salons, tradies, agencies, consultants and so on.

**Frame broadly. Never niche down to one vertical.** Sam's reach depends on the topic landing with every service business owner, not one trade. Use generic framing ("if you own a service business") or mixed lists ("whether you're a tradie, lawyer or physio"). Vertical-specific scripts are for client work, not Sam's brand.

They're time-poor, sceptical of marketing and often burned by past agencies. They want **leads and revenue**, not vanity metrics.

## Voice
- Australian English, plain marketing, never AI-sounding
- Confident, terse, slightly contrarian
- Like a mate giving advice over a beer, not a LinkedIn guru
- Banned words: synergy, leverage, unlock, deep-dive, game-changer, ecosystem, holistic
- No emojis unless asked
- Never invent proof. Years in business, client results, view counts and dollar figures must be Sam's real numbers. If unknown, leave a `[Sam: real number]` placeholder.

## Inputs (ask only if missing)
- **Topic / angle**, e.g. "Meta ads waste", "GBP optimisation", a recent client win
- Optional: **format** (see Formats below)

If only "make me a reel" is given, propose 3 angles (each with a one-line hook) and let Sam pick before scripting.

---

## The hook: three layers, all in the first 3–4 seconds

Every strong reel studied (see `swipe-file.md`) hooks on three channels at once. **They don't repeat each other.** Each does a different job.

| Layer | Job | Example |
|---|---|---|
| **Title card** (on-screen, stays up 3–10s) | States the outcome or promise, readable on mute | "How I'd get a tradie 20 leads a week" |
| **Spoken hook** (first line of voiceover) | Opens a curiosity gap or names a tension | "If I took over a Brisbane plumber's marketing tomorrow with a grand a month, here's exactly what I'd do." |
| **Frame-1 visual** | Proves or dramatises the claim before a word lands | The full 3-step plan on screen, or a before/after numbers split |

Rules:
- Spoken hook: up to about 20 words, under 4 seconds. Specific beats short.
- Title card: up to 10 words, sentence case, digits for numbers, AU spelling. No all-caps (the Locate Reel Style bans uppercase captions).
- The title card doesn't need to match the voiceover. If they're identical, one layer is wasted.
- **Line 2 must deepen the tension, never reset it.** Give the "because", rule out the obvious answers, or narrow the promise. Never follow the hook with an intro, a name or "so today…".

### Seven hook formulas

Use these alongside the hook library. Never copy a creator's line verbatim.

1. **Failed-fix question.** Name the bad result and the fix they already tried.
   `Why is [bad result] still happening, even after [thing they already tried]?`
   → "Why are your Google Ads still getting clicks and no calls, even after you changed agencies?"
   Line 2 gives the real cause: "Because the agency fixed the ads. Nobody fixed what happens after the click."

2. **Want, but don't want.** A desire plus the fear that stops them, then a number.
   `If you want [desire] but you don't want [feared outcome], here are [N] ways to [fix].`
   → "If you want more bookings from Google but you don't want to pay an agency three grand a month, here are four things to check tonight."

3. **The one thing (and rule out the obvious).** Promise a single answer, then kill the usual suspects.
   `Here's the one thing that decides [result]. And no, it's not [obvious 1], [obvious 2] or [obvious 3].`
   → "Here's the one thing that decides whether your Google Ads make money. And no, it's not your budget, your keywords or your agency."

4. **Compression.** A stakes line, then big input squeezed into tiny output.
   `If you can't [skill], you can't [outcome]. So here's [big input] of [topic] in [small output].`
   → "If your phone doesn't ring, nothing else in your business matters. So here's [Sam: real number] years of lead gen advice in 60 seconds."
   Pair it with a visible timer or a running count on screen.

5. **Start over.** A from-scratch scenario with a constraint.
   `If I [started with constraint] tomorrow, here's exactly what I'd do.`
   → "If I took over a Brisbane plumber's marketing tomorrow with a grand a month, here's exactly what I'd do."
   Show the whole plan on screen in frame 1 so they stay to see each piece.

6. **Insider move.** What the best in a peer group quietly do differently.
   `The [busiest / best] [peer group] are [unexpected thing]. Here's why.`
   → "The busiest accountants in Melbourne aren't posting on Instagram. They're doing this."
   "Did you know…" is allowed only here, and only when what follows is a surprising, true claim, never trivia. Must be true and defensible.

7. **Reframe.** Set up an expected hack, then deliver an unexpected truth.
   `The fastest way to [desire] is [non-hack].`
   → "The cheapest lead you'll ever get is the one who already called you and didn't book."
   Best for quick-hit formats and loop endings.

### Frame-1 visual options (pick one, name it in the output)
- **Comparison split:** two results side by side with real numbers ("BEFORE 3 calls/wk" vs "AFTER 19 calls/wk")
- **The result itself:** the finished thing on screen while Sam talks (dashboard, landing page, the ad)
- **The whole map:** every step of the payoff shown at once, revealed piece by piece later
- **Prop or timer:** a countdown, a stack of invoices, a phone ringing
- **Pattern-interrupt location:** filmed somewhere unexpected for a business reel (on site, in a ute, at the footy). It must still feel natural.
- **Proof screenshot:** Google Ads, GA4, GBP calls or Xero. Blur client names and figures unless Sam has approval.

---

## Formats

| Format | Length | Shape | When |
|---|---|---|---|
| **Quick hit** | ~30s | Hook → one point → loop line | Reframes, contrarian takes, single tips |
| **Value list** | 45–60s | Hook → line 2 → 3–5 named points → proof → CTA | Tips, tools, mistakes, "N ways to…" |
| **Tutorial** | 45–60s | Hook → result shown → steps on screen → CTA | Screen recordings, setups, how-tos |
| **Start-over plan** | 55–60s | Hook → map on screen → levels/steps → CTA | Big-picture "what I'd do" reels |

- Lengths follow the approved Locate Reel Style: 30–60s. Go longer only when Sam says so for that reel.
- Word budget: Sam speaks about 200–240 words a minute after tightening, so a 60s reel holds about 200 words of voiceover and a 30s reel about 100. Count them.
- Something changes every 2–4 seconds: a cut, a punch-in, a new step card, a screenshot.
- **List points must be named and actionable in one line.** Each gets its own step card, digits not "01" ("3 Answer in 5 minutes"). "10 tips for more leads" with vague tips is banned. "7 things in your Google Business Profile costing you calls", each named, is good.
- **Series slot (optional):** a recurring name ("Fix it Friday", "One-minute audit") builds return viewers. Use it only if Sam has started one.

## Script structure (value list / tutorial default)

```
HOOK (0–4s)        title card + spoken hook + frame-1 visual
LINE 2 (4–8s)      deepen the tension: the "because", or rule out the obvious
[MID-ROLL CTA]     optional, ~15–20s, one line: "Comment AUDIT and I'll send you the full checklist."
PAYOFF             the points/steps; title card per point; cut every 2–3s
PROOF              one beat with a real number, screenshot, or "this was built with…"
CTA (last 3–5s)    comment keyword + exactly what they get
```

Quick hit: HOOK → one point with a concrete example → a last line that flows back into the first frame for a replay loop. No keyword CTA needed.

## CTA: comment keyword

The default for value lists, tutorials and start-over plans:
- **One word**, tied to the topic, on the end card's orange button: Comment "audit", "leads", "checklist", "map"
- **Say exactly what they get**: "Comment LEADS and I'll send you all seven, plus the script I use to follow up."
- The freebie must be what the video promised in full form (the checklist, the template, the full list). Note in the output if it doesn't exist yet.
- Optional mid-roll mention at ~15–20s, then repeat at the end.
- Show it on screen: a title card or a mock comment box being typed into.
- **Needs DM automation** (ManyChat or Instagram's own auto-reply). If Sam hasn't set that up, swap to "DM me [WORD] and I'll send it over" and note it in the output.
- Never "follow for more" on its own.

## Proof beat (required for anything over 30s)
One of:
- A real number from Sam's or a client's results (approved, or blurred)
- A screenshot (ad account, call log, GBP insights, GA4)
- Self-proof: "this whole reel was scripted with the method I just showed you"
- Hours/years of work behind it (real figure only)

## Locate Reel Style (approved 2026-11-04): wins on anything visual

Sam's approved edit rules live in `G:\My Drive\Claude Code.Locate\_brand\AI Video Editor\CLAUDE.md`. Read it before writing the Visual column. Where this skill and that file differ, that file wins. The parts that shape a script:
- First word at 0.0s, hook caption on screen in frame one, no logo intro
- Captions 1–3 words, sentence case, no exclamation marks, digits for numbers. Mark one **emphasis word** every 5–8s (it gets the Newsreader italic and blue brush). Put it on the number, the outcome or the turn of the sentence.
- Name graphics by the kit: **series title**, **name tag**, **split screen**, **framework** (steps build one at a time), **proof card** (number counts up, old figure struck in orange), **end card** (a question, an orange button with the keyword, locatedigital.io)
- Locate Blue carries every graphic. Orange appears once, on the end-card button.
- B-roll is real screens, offices and documents with private details blurred. No stock money or handshakes.
- Real client names, figures or documents need Sam's written sign-off before they go on screen.

## Captions and on-screen text
- See the reel style above. In the script, write on-screen text in sentence case and mark the emphasis word in **bold**.
- Real screenshots and photos over icons, emojis or animated graphics
- AU spelling only

---

## Instagram Reels algorithm: what to optimise for

Ranked by weight in 2026:

1. **Sends/shares** (heaviest): the script must trigger "I need to send this to my [partner / business coach / accountant]"
2. **Saves**: lists, checklists and plans get saved
3. **Watch time and completion**: the first 3 seconds stop the scroll; pace holds them. Length isn't the problem; dead air is.
4. **Replays**: quick hits end on a line that loops back to the hook
5. **Comments**: the keyword CTA drives them; otherwise ask one specific question, never "thoughts?"
6. **Likes**: barely matter

Reach killers:
- Watermarks (TikTok/CapCut logos)
- Slow openers ("Hey guys, today I'm going to talk about…")
- "Follow for more" outros
- Reposts without a real re-edit
- Static images, low-motion footage, dead air (the reel style cuts every pause over 0.25s)

## Australian audience targeting (mandatory)

Sam's reach has been drifting offshore. Every script must signal AU, with several signals stacked.

**Voiceover (at least 2 per script)**
- AU regulators/institutions: ATO, ASIC, AHPRA, Fair Work, BAS, GST, EOFY, ABN, super, FBT
- AU tools the audience uses: Xero, MYOB, Hnry, Cliniko, Halaxy, Genie Solutions, ServiceM8
- AU places: Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast, regional ("out west")
- Light Aussie words: "mate", "heaps", "reckon", "Aussie". Never overdo it, never parody.

**Captions and on-screen text**
- AU spelling only: optimise, favour, organisation, behaviour, colour, analyse
- AU dollar framing: "$50K", or "$50K AUD" if ambiguous

**Hashtags (3–5, AU-tilted)**
- Always 1–2 of: `#smallbusinessaustralia` `#ausbusiness` `#aussiebusiness` `#smallbizau` `#australianbusiness`
- Plus 1–3 topical: `#smallbusinessmarketing` `#googleadstips` `#metaads` etc.
- Never spam stacks

**Post time:** AU peaks only: 7–9am, 12–1pm or 7–9pm AEDT. Avoid AU overnight.

**Never use:** IRS, 401k, Walmart, Target, Black Friday framing, "y'all", "buck", US-only software.

---

## Output format

Return in this order:

Save each script to `G:\My Drive\Claude Code.Locate\_brand\AI Video Editor\Scripts\YYYY-MM-DD_topic.md` so the editor can force-align captions to it. Then give Sam the hooks and file links in chat.

1. **Format and length**: e.g. "Value list, ~60s, 195 words"
2. **Hook**
   - Title card: (≤10 words)
   - Spoken hook: (verbatim)
   - Frame-1 visual: (one line)
   - Formula used and the inspo link from the hook library or swipe file
3. **Script table**: one row per beat, so Sam can film and edit straight from it:

   | Time | Voiceover (verbatim) | On-screen text | Visual / cut |
   |---|---|---|---|

   Mark the mid-roll CTA and the proof beat. Voiceover written for the ear, ≥2 AU markers.
4. **CTA**: the keyword, what they get, and whether the freebie exists yet (or the DM fallback)
5. **Caption**: first 90 characters re-state the hook; AU spelling; one specific question; 3–5 hashtags including 1–2 AU-tilted
6. **Shoot notes**: location, framing, B-roll and screenshots to grab (1–3 lines)
7. **Recommended post time**: quick tactical content midday, longer lists and plans in the evening

If Sam asks for variants, give 3 hooks first (each with title card, spoken line and visual, using different formulas), let Sam pick, then script the body.

## Anti-patterns: never do these
- Vague listicles: "10 tips for more leads" with tips that aren't named or actionable
- "Did you know…" followed by trivia (only allowed for the Insider move formula)
- Title card and spoken hook saying the same words
- Line 2 that resets: "Hi, I'm Sam from Locate Digital…"
- Three-act storytelling in a quick hit
- Pitching Locate's services in the first half (the keyword freebie is fine anywhere)
- Invented numbers, years or results
- Over-animated captions, emojis or stock icons
- Jokes about technical topics (dentists don't want root canal gags)

## Maintenance
- Re-check Adam Mosseri's updates and refresh the **algorithm** section every 3 months.
- When Sam shares new reels to study, break them down (vidiQ `watch_shortform_content` works on IG links) and add them to `swipe-file.md`. Add any new hook formula here.
- Hook library links came from a PDF export and some have stray spaces inside them (e.g. `DGLVKBUR6 W0`). Remove the spaces before citing a link.
- Editing this file: never write a dollar sign followed directly by a digit in the body (like a dollar-one figure). Claude Code reads those as argument placeholders and swaps in whatever Sam typed after the command. Write "a grand", "one to three million", or put a letter straight after the digit ("50K").
- Last updated: 2026-11 (hook system rebuilt from 7 studied reels, see `swipe-file.md`).
