---
name: reels-script
description: Writes Instagram Reels scripts and hooks for Locate Digital — daily posting to attract service business owners ($1–3M).
---

# Reels script

Writes short-form video scripts (hook + body + CTA + caption) for Sam's daily Instagram Reels.

## When to use
- Sam asks for "a reel", "hook", "script", "IG content", "video idea"
- Output is a Reel — not a long-form video, podcast clip, or tweet

## References (always check before scripting)

**1. Hook library — live Google Sheet (primary source)**
- Read via `mcp__claude_ai_Google_Drive__read_file_content` with `fileId: 1QQVgwaiPaGfGMgqJ4q65k0BXYv5BkiOfva8HIf2XDj4`
- ~1000 **intro hooks only** — these are the first-3-second opening line of a reel, not full scripts
- **Ignore the `Brand` and `Notes` columns** — use any hook regardless of those values
- Use the `Inspo link` column to study the original viral reel that proved the hook
- File is ~150k chars: if truncation occurs, read in 30k-char chunks via `offset`/`limit` and keyword-search for the requested topic
- Pull 5–8 candidate hooks → pick 1–3 strongest → fill in the `[insert X]` blanks with topic specifics → reference the inspo link in output
- If Drive isn't connected, prompt Sam to run `/mcp` and authenticate, then proceed with general hook patterns

**2. Local files in `_skills/reels-script/`**
- **`trend-log.md`** — current-week hook/format/audio signals. Tilt the script toward what's spiking now.
- **`competitors.md`** — accounts being modelled. If a starred (⭐) competitor recently covered the topic, take a different angle.
- **`swipe-file.md`** — sheet pointer + manual quick captures.

If a reference is empty or has no relevant entries, proceed but flag once at the top: "No [trend/swipe/competitor] data for this niche yet — output uses general patterns."

## Audience (always)

**Service business owners as a whole** — $1–3M revenue range. Mix of accountants, lawyers, physios, dentists, osteos, salons, tradies, agencies, consultants, etc.

**Frame broadly, never niche down to a single vertical.** Sam's reach strategy depends on the topic resonating across all service-biz operators, not one trade. Use generic framing ("if you own a service business") or mixed-vertical lists ("whether you're a tradie, lawyer, or physio") for variety. Vertical-specific scripts are for client work only — not Sam's own brand.

They're time-poor, sceptical of marketing, often burned by past agencies. They want **leads and revenue**, not vanity metrics.

## Voice
- Australian English, plain marketing — never AI-sounding
- Confident, terse, slightly contrarian
- Speak like a mate giving advice over a beer, not a LinkedIn guru
- Banned words: synergy, leverage, unlock, deep-dive, game-changer, ecosystem, holistic
- No emojis unless explicitly requested

## Inputs (ask only if missing)
- **Topic / angle** — e.g. "Meta ads waste", "GBP optimisation", a recent client win
- Optional: **format** (talking head, b-roll voiceover, screen recording, text-on-black)

If only "make me a reel" is given → propose 3 angles, let Sam pick before scripting.

## Instagram Reels algorithm — what to optimise for

Ranked by weight in 2026:

1. **Sends/shares** (heaviest) — script must trigger "I need to send this to my [partner / business coach / accountant]"
2. **Saves** — list/checklist/framework content gets saved
3. **Watch-through %** — first 3 seconds stop the scroll; sweet spot 7–21s, hard ceiling 45s for tutorials
4. **Replays** — last frame should flow back into first frame for natural loops
5. **Comments** — ask one specific question, not "thoughts?"
6. **Likes** — barely matters, ignore

Reach killers:
- Watermarks (TikTok / CapCut logos) → use original or strip
- Slow openers ("Hey guys, today I'm going to talk about…")
- "Follow for more" CTAs (kills shares)
- Reposts without meaningful re-edit
- Static images, low-motion footage

## Australian audience targeting (mandatory)

Sam's reach has been drifting offshore (US/EU views). Every script must signal AU to the algorithm so reach skews local. Bake the following in — not just one, multiple signals stacked.

**Voiceover (include at least 2 per script)**
- AU regulators / institutions: ATO, ASIC, AHPRA, Fair Work, BAS, GST, EOFY, ABN, super, FBT
- AU software / tools the audience actually uses: Xero, MYOB, Hnry, Cliniko, Halaxy, Genie Solutions, ServiceM8
- AU place names: Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast, regional ("out west", "down south")
- Light Aussie words: "mate", "heaps", "reckon", "fair dinkum" (sparingly), "Aussie" — never overdo, never parodic

**Captions + on-screen text**
- AU English spelling only: optimise, favour, organisation, behaviour, colour, analyse — never US
- AU dollar framing — "$50K" with AU context, or "$50K AUD" if ambiguity matters

**Hashtags (3–5, AU-tilted)**
- Always include 1–2 of: `#smallbusinessaustralia` `#ausbusiness` `#aussiebusiness` `#smallbizau` `#australianbusiness`
- Plus 1–3 topical: `#smallbusinessmarketing` `#googleadstips` `#metaads` etc.
- Never spam stacks (`#love #life #instagood`) — kills credibility and dilutes geo signal

**Posting time (recommend in output)**
Post at AU peak windows only — algorithm learns where engagement comes from:
- 7–9am AEDT
- 12–1pm AEDT
- 7–9pm AEDT
Avoid posting in AU overnight — that hits US/EU prime time and is where the offshore drift comes from.

**Never use**
- US references: IRS, 401k, Walmart, Target, Black Friday-coded framing
- US-coded slang ("y'all", "buck", "soccer mom")
- US-only software examples (QuickBooks USA, etc.)

## Hook patterns (use as templates, never copy verbatim)

> Lead with the live Sheet hooks. These local examples are fallback only when the Sheet isn't accessible. Frame examples for **service businesses broadly**, not single verticals.

**Pattern interrupt**
- "Stop running Google Ads. Here's what to do instead."
- "Your bookkeeper is leaving $80K on the table and doesn't know it."

**Curiosity gap**
- "The reason your business isn't growing has nothing to do with your marketing."
- "There's one mistake every Aussie service business makes on Meta — costing them clients every week."

**Direct callout**
- "If you own a service business doing under $2M, watch this."
- "Aussie business owners — this 12-second test tells you if your Google Ads are wasting money."

**Specificity / proof**
- "$47K from one email. Here's the exact subject line."
- "We turned off 60% of this client's keywords. Bookings went up 3x."

**Contrarian**
- "Posting daily on Instagram won't grow your business. This will."
- "SEO isn't dead. Your strategy is."

**Negative bias**
- "Don't hire a marketing agency until you've checked these 3 things."
- "5 ways your Meta ads are quietly bleeding money before EOFY."

## Script structure (sub-30s default)

```
HOOK (0–3s)      — one pattern from above; on-screen text matches voiceover word-for-word
SETUP (3–7s)    — establish stakes; why this matters RIGHT NOW
PAYOFF (7–25s)  — the actual insight; 1–3 specific points, never abstract
CTA / LOOP (last 2s) — either a clear next step OR a line that loops back to the hook
```

For tutorials (30–45s): expand PAYOFF into 3 numbered steps. Never exceed 45s.

## Output format

Always return:

1. **Hook** — single line (≤12 words) pulled or adapted from the Sheet, exactly what they hear/read in first 3s. Cite the inspo link from the Sheet so Sam can study the original.
2. **On-screen text** — frame-by-frame if it differs from voiceover. AU spelling only.
3. **Voiceover script** — verbatim, written for the ear not the eye. Must include ≥2 AU markers (regulator/brand/place/word).
4. **Caption** — first 90 chars hook above-the-fold; AU English spelling; include one specific question; 3–5 hashtags including 1–2 AU-tilted (#smallbusinessaustralia, #ausbusiness, etc.)
5. **B-roll / visual notes** — 1–2 lines on what to shoot
6. **Estimated length** — in seconds
7. **Recommended post time** — one of: 7–9am / 12–1pm / 7–9pm AEDT (pick based on topic — quick tactical content midday, longer educational evening)

If Sam asks for variants → give 3 hook options first, let him pick, then script the body.

## Anti-patterns — never do these
- Generic "10 tips for…" listicles
- "Did you know…" openers
- Three-act storytelling in sub-30s clips
- Selling / pitching in the first half
- "Follow for more" outros
- Vague claims without a number, name, or example
- Trying to be funny when the topic is technical (dentists don't want jokes about root canals)

## Maintenance
Algorithm signals shift. Re-check Adam Mosseri's quarterly updates and update the **algorithm** section every 3 months. Last updated: 2026-05.
