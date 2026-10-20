---
name: market-research
description: Research a client's industry and market landscape — size, growth, trends, regulatory environment, target audience/customer segments, demand signals, and pricing benchmarks. Produces a pitch-quality HTML report with markdown backup. Use when onboarding a new client, before writing a proposal, planning a campaign strategy, or when Sam says "market research", "research the market for [client]", "what's the market like for [client]", "industry overview", or "market landscape". Typically runs before competitor-research to establish industry context.
---

# Market research

Pulls publicly available industry and market data for a client's sector and produces a pitch-quality landscape report. Sets the context that competitor-research, ad copy, and landing page strategy build on — this answers "what's the market doing," competitor-research answers "what are specific rivals doing."

**Output:** `assets/market-research-YYYY-MM.html` (+ `.md` backup)

**Sequencing:** run this before `competitor-research` when doing both for a client. Market research establishes industry size, trends, and audience context; competitor-research then does the head-to-head deep-dive. Each also works standalone.

---

## Step 1 — Load context

Read CLAUDE.md (already loaded if running from the client folder). Extract:

- Client name, industry/vertical, and specific services offered
- Service area (suburb/city/state/national) — Australia is the default market unless CLAUDE.md says otherwise
- Any existing target audience notes or personas
- Client's positioning and proof points

If the industry/vertical isn't clear, ask: "What industry/vertical should I research for [client]? Any specific geography (suburb/city/state/national)?"

Confirm before proceeding: "Researching the [industry] market in [location]. Any specific angle or decision this needs to inform?"

---

## Step 2 — Research

Work through each area below. Run searches in parallel where possible. Some will come up empty — note the gap and move on rather than stalling.

### 2a — Industry size & growth

Search: `"[industry]" market size Australia [year] OR "[industry]" industry report IBISWorld OR statista`. Check abs.gov.au for business counts or employment data if relevant.

Extract: market size ($), growth rate (CAGR/YoY), number of businesses, employment. Note the source and year for every figure — anything older than 2 years gets flagged as dated, not presented as current.

### 2b — Trends shaping the industry

Search: `"[industry]" trends 2026 Australia` and `"[industry]" disruption OR "market shift" Australia`.

Extract 3–5 trends actually reshaping the industry (technology, consumer behaviour, regulation, new entrants). Only include trends with a clear marketing implication — a trend with no bearing on how the client should market itself isn't worth a slot.

### 2c — Regulatory & structural factors

Only for licensed/regulated industries (finance, health, legal, trades, real estate). Search: `"[industry]" regulation Australia [year] change`.

Note licensing requirements, compliance shifts, or structural barriers shaping competition. Skip this section entirely for unregulated industries rather than padding it.

### 2d — Target audience & customer segments

Search: `"[industry]" customer demographics OR "buyer persona" Australia`. Cross-check against any customer data already in the client's CLAUDE.md or site.

Build 2–3 segments: who buys, what triggers the purchase decision, price sensitivity, typical research/buying journey length. Ground each in evidence — search behaviour, review language, industry data — not invention.

### 2e — Demand signals & seasonality

Search for third-party summaries citing Google Trends or industry search-demand data: `"[service/product]" search trend Australia`. Trends itself often won't fetch directly — use industry reports or news that cite the data instead.

Note whether demand is growing/flat/declining, and any seasonality (spikes tied to time of year, weather, tax periods, etc.). This directly informs budget pacing and campaign timing.

### 2f — Pricing benchmarks

Search: `"[industry]" pricing OR cost OR rates Australia [year]`, plus any industry-specific comparison sites (same approach as competitor-research's rate-comparison step).

Note the typical price range, what drives variation, and where the client's own pricing sits if known.

### 2g — Local market context

Only if the client serves a specific city/region rather than nationally. Search `"[industry]" [suburb/city] market OR demand OR competition`.

Note local population/demographic drivers and anything geography-specific (new housing developments for trades, local demographic shifts for health services, etc.).

---

## Step 3 — Build the report

All sections mandatory unless data is genuinely unavailable — note the gap rather than omitting silently. Regulatory (Section 4) and local context (Section 8) are the two sections it's normal to skip when not applicable.

### Section 1: Executive snapshot

3–4 stat callouts (market size, growth rate, number of competitors/businesses, one demand signal). One paragraph framing the opportunity or challenge this creates for the client.

### Section 2: Industry size & growth

Full detail from 2a, every figure sourced and dated.

### Section 3: Trends shaping the industry

3–5 trends from 2b, each with a one-line "what this means for [client]" implication.

### Section 4: Regulatory & structural factors

From 2c. Omit entirely if not applicable.

### Section 5: Target audience & customer segments

2–3 segments from 2d as profile cards: who they are, purchase trigger, price sensitivity, objections.

### Section 6: Demand signals & seasonality

From 2e — a plain read on which months are high/low demand and the growth/flat/decline trend, with the timing implication spelled out.

### Section 7: Pricing landscape

From 2f — typical range, what drives variation, where the client sits.

### Section 8: Local market context

From 2g. Omit if the client operates nationally.

### Section 9: Strategic implications

4–5 bullets translating the research into direct action — channel choice, messaging angle, budget pacing, or targeting. Each tied to a specific finding above; no generic advice.

---

## Step 4 — Humanizer pass

Same rules as competitor-research:
- No em dashes — commas or periods
- No AI vocabulary: crucial, pivotal, delve, underscore, foster, showcase, vibrant, testament, landscape (used as metaphor)
- Sentence case headings
- Australian English
- Concrete claims over hedged ones — "demand peaks in spring for renovation-driven trades" not "demand may see some seasonal variation"

---

## Step 5 — Output

1. **HTML report** — `assets/market-research-YYYY-MM.html`
   - Branded cover page (dark navy, client name, date, prepared by Locate Digital)
   - Stat callouts, segment profile cards, sourced figures with citation footnotes
   - Pitch-ready: a non-marketer should read the executive snapshot and strategic implications and understand the opportunity
   - Open in browser after saving

2. **Markdown backup** — `assets/market-research-YYYY-MM.md`
   - Plain text version, used for search, diffing, and loading into future sessions

Print on completion:
```
✓ Market research saved:
  assets/market-research-YYYY-MM.html (pitch report)
  assets/market-research-YYYY-MM.md (backup)

Industry: [industry] | Market size: [$X, Y% growth]
Key trend: [one sentence]
Top opportunity: [one sentence]
Next step: run competitor-research for head-to-head positioning gaps
```
