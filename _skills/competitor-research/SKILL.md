---
name: competitor-research
description: Research 2-3 competitors for a client and produce a structured brief covering positioning, messaging, ads, SEO presence, reviews, and social. Identifies gaps the client can exploit. Produces pitch-quality HTML output. Saves to assets/competitor-research-YYYY-MM.html. Use when onboarding a new client, planning a campaign, writing ad copy, or when Sam says "research competitors", "look into competitors", or "what are [client]'s competitors doing".
---

# Competitor research

Pulls publicly available data on 2–3 competitors and produces a pitch-quality brief. Informs ad copy, landing page strategy, and channel decisions.

**Output:** `assets/competitor-research-YYYY-MM.html` (+ `.md` backup)

---

## Step 1 — Load context

Read CLAUDE.md (already loaded if running from the client folder). Extract:

- Client name, industry, and primary services — note each service specifically
- Competitor list (already recorded at onboarding — see Competitors section)
- Target audience and client's own positioning
- Client's proof points — what they can credibly claim

If no competitors are listed in CLAUDE.md, ask: "Which competitors should I research? (2–3 URLs or names)"

Confirm the list before proceeding: "Researching: [list]. Any changes?"

---

## Step 2 — Research each competitor

Run all competitor research in parallel. For each competitor, work through all sources below. Some will fail — handle each gracefully rather than stopping.

### 2a — Homepage

Fetch the homepage. Extract:
- Main headline and subheadline (exact copy)
- Value propositions — what do they lead with?
- Primary CTA (exact text + destination)
- Trust signals (years operating, volume stats, awards, certifications)
- Lead capture mechanism — rate calculator? Online application? Phone only? Single "contact us"?
- Pricing visibility — are rates or fees shown at all?
- Overall tone (corporate/casual/clinical/warm)

**If the homepage blocks access (403, expired certificate, JS-heavy):** don't retry. Search `[competitor name] home page headline value proposition` and extract from search snippets instead. Note the fallback was used.

### 2b — Product pages for the client's primary services

This is the most important research step. For each of the client's primary services, check whether the competitor offers it and how they position it.

For each client service:
1. Run `site:[competitor-domain] "[service name]"` to confirm whether the page exists
2. If it exists, fetch it and extract: headline, key messages, target borrower description, any rates or fees, CTA
3. If the site: search returns nothing, the product is likely not offered — note it as "not offered (confirmed)"

**Why this matters:** product gaps are often the most actionable finding. In the Brighten research, this step revealed that none of three competitors offered bridging loans — the market leader actively redirected those enquiries away. That single finding reshaped the entire strategic recommendation.

### 2c — Broker or partner portals

Many lenders and service businesses run a separate partner/broker portal (e.g. broker.resimac.com.au, broker.redzed.com). These often contain the real product specs — loan-to-value ratios, maximum loan sizes, which products are available, income verification requirements.

If the consumer site is thin or blocked, search `broker.[competitor-domain]` or `[competitor name] broker portal products`. Fetch if accessible.

### 2d — Rates via comparison sites

Competitors rarely publish rates on their own sites. Comparison sites often do it for them.

Search: `[competitor name] home loan rates finder.com.au OR canstar.com.au OR money.com.au`

Extract: advertised rates, comparison rates, product names. Note the source and date.

**Applicable to:** financial services (mortgages, insurance, loans), utilities, any regulated industry with rate/price obligations.

### 2e — Reviews

Fetch the competitor's listing on Product Review AU directly:
`https://www.productreview.com.au/listings/[competitor-slug]`

Extract: overall star rating, total review count, and — critically — the specific language customers use in positive and negative reviews. Exact phrases are more useful than paraphrasing.

Also search `[competitor name] reviews trustpilot` as a second source.

If no reviews are found on either platform, note it explicitly. Absence of consumer reviews is itself a meaningful data point (often signals a broker-only or wholesale model with no direct customer relationships).

### 2f — Industry news and market data

Search `[competitor name] originations OR "market share" OR "settlement volume" site:theadviser.com.au OR site:brokernews.com.au OR site:mpamag.com.au`

This surfaces financial data and strategic moves that competitors don't publish on their own sites — origination volumes, growth rates, award wins, strategic shifts, partnerships. Useful for competitive matrix scoring and market context.

Also run one search for industry-wide context: `[industry] non-bank OR independent market share growth Australia 2025 2026`

### 2g — Social media

Search for the competitor's Instagram and Facebook handles. Note follower count if surfaced in search snippets (Instagram profile pages often render follower count in the meta description). If not findable via search, note "manual check required" and provide the likely handle to check.

Note: follower counts are hard to get programmatically — don't spend multiple attempts. One search is enough; then move on.

### 2h — Meta Ad Library

Do not attempt to WebFetch the Meta Ad Library. It is a JavaScript app and will not render via automated fetch.

For every competitor, note: "Meta Ad Library — manual check required: facebook.com/ads/library/?active_status=all&ad_type=all&country=AU&q=[competitor-name]"

If any campaign information is available from other sources (press releases, industry news, the competitor's own site), note it here instead.

---

## Step 3 — Build the report

Produce all sections below. The product gap matrix and opportunities sections are mandatory. Skip individual sections only if data is genuinely unavailable — note it rather than omitting silently.

---

### Section 1: Market context

2–3 sentences on the industry growth environment. Use data from Step 2f. Frame the competitive analysis in terms of market dynamics — is the sector growing? Consolidating? Is direct digital acquisition underinvested?

Include 3–4 key stats as callout figures (industry growth rate, market share, best available rate, any notable volume figures from competitors).

---

### Section 2: Competitive matrix

Score each competitor across these 8 dimensions on a 1–5 scale. Also score the client (current state). Base every score on specific evidence from the research.

| Dimension | What to score |
|---|---|
| Messaging clarity | Is their positioning specific and ownable, or generic? |
| Direct digital acquisition | Do they have a functioning direct funnel, or is it broker/wholesale only? |
| Consumer reviews and trust | Volume and quality of public reviews |
| Product breadth (direct) | How many of their products are marketed directly to consumers? |
| Speed/turnaround claim | Do they publish a specific approval or response time? |
| Pricing transparency | Are rates or fees shown anywhere on their site? |
| Online tools and UX | Rate calculator, online application, account access quality |
| Social media presence | Follower count, posting frequency, engagement |

For each score, note the evidence: "3 — broad, emotional messaging" or "1 — broker only, no consumer journey confirmed."

---

### Section 3: Product gap matrix

A table with every product the client offers as a row, and each competitor as a column.

Mark each cell:
- ✓ — confirmed offered and marketed
- ✗ — confirmed not offered
- Partial — offered with conditions (e.g. self-employed only, capped at $X)

**How to confirm a gap:** don't assume. Use the site: search from Step 2b to confirm absence. "Not found in site search" is more reliable than "not mentioned on homepage."

Highlight any product the client offers that no competitor offers — this is the most actionable gap.

---

### Section 4: Per-competitor deep-dives

One section per competitor. Include:

**Positioning** — one sentence: who they target and how.

**Key messages** — exact copy from their site, not paraphrased.

**Product deep-dive** — for each of the client's primary services: does the competitor offer it, how do they position it, what are the terms/limits?

**Lead capture and funnel** — how does a consumer actually enquire? Rate tool, online application, phone, broker pathway? Grade the friction level.

**Reviews** — star rating, volume, specific customer quotes for both positive and negative themes.

**Digital and social footprint** — what paid and organic presence is confirmed?

**Gaps and weaknesses** — specific gaps, not general observations. "They have no speed claim" not "their positioning could be stronger."

---

### Section 5: Website scorecards

Grade each competitor's homepage on these 6 criteria using A/B/C/D:

| Criterion | What to assess |
|---|---|
| Headline clarity | Is the headline specific and audience-targeted, or generic? |
| Rates visible | Are any rates or fees shown on the homepage or linked product pages? |
| Lead capture | Is there a calculator, rate check, or online application? Or just a contact form? |
| Social proof | Reviews, testimonials, volume stats — visible and credible? |
| Speed claim | Is a specific turnaround time published anywhere? |
| Mobile UX | Does the page function well on mobile (check via content structure if page is accessible)? |

A = strong, B = adequate, C = weak, D = absent or broken.

---

### Section 6: Keyword battleground

A table of 6–10 high-intent search terms relevant to the client's primary services. For each term:
- Intent level (High / Medium)
- Which competitors have a page or known presence for this term
- The opportunity level for the client

Focus on terms where the client has a product but competitors don't — these are the highest-value, lowest-competition opportunities.

---

### Section 7: Opportunities

5 prioritised opportunities. Each must be:
- Tied to specific evidence from the research ("Pepper Money redirects bridging loan enquiries to personal loans — confirmed from their resources page")
- Specific about what the client should do ("Build a dedicated bridging loan landing page and launch Google Ads on [term]")
- Realistic given the client's current capabilities and budget

Order by impact and ease of execution. Number 1 should be the single fastest path to differentiation.

---

### Section 8: Strategic recommendation

A clear, named strategic recommendation. One paragraph on what position the client should own and why the research supports it. Followed by 3–5 specific actions with timeframes (immediate / 3–6 months).

Do not hedge. The recommendation should read like advice from a senior strategist, not a summary of findings.

---

## Step 4 — Humanizer pass

Before outputting, apply humanizer rules:
- No em dashes — use commas or periods
- No AI vocabulary: crucial, pivotal, delve, underscore, foster, showcase, vibrant, testament, landscape (abstract)
- Sentence case headings
- Australian English
- Say "their headline is generic" not "their messaging lacks differentiation"
- Say "Pepper Money redirects bridging enquiries to personal loans" not "Pepper Money appears to not offer bridging loan products at this time"

---

## Step 5 — Output

Produce both files:

1. **HTML report** — `assets/competitor-research-YYYY-MM.html`
   - Branded cover page (dark navy, client name, date, prepared by Locate Digital)
   - All 8 sections with visual formatting: stat boxes, matrix tables, scoring dots, colour-coded product gap matrix, sentiment boxes, opportunity cards
   - Pitch-ready: a non-marketer should be able to read the executive summary and the strategic recommendation and know exactly what to do next
   - Open in browser after saving

2. **Markdown backup** — `assets/competitor-research-YYYY-MM.md`
   - Plain text version of the same content
   - Used for search, diffing, and loading into future sessions

Print on completion:
```
✓ Competitor research saved:
  assets/competitor-research-YYYY-MM.html (pitch report)
  assets/competitor-research-YYYY-MM.md (backup)

Competitors covered: [list]
Key finding: [one sentence — the single most actionable insight]
Critical gap found: [yes/no — product the client offers that no competitor offers]
Opportunities: [N flagged]
Manual checks needed: [Meta Ad Library for X, Y, Z — links provided in report]
```

---

## Rules

- **Product gaps are the most valuable finding.** Always confirm whether each competitor offers the client's primary services — don't assume. Use site: searches to verify absence.
- **Exact quotes beat paraphrasing.** "Need really helpful loan options? That's us." is more useful than "they use approachable language."
- **Absence of reviews is data.** No Product Review AU listing usually means broker-only or wholesale distribution — note what it implies about their business model.
- **Meta Ad Library always requires manual check.** Never attempt to WebFetch it. Just provide the direct URL in the report.
- **Blocked sites don't stop the research.** If a competitor blocks direct access (403, expired cert, JS-heavy), fall back to search snippets + industry news. Note the fallback was used.
- **Comparison sites publish what competitors won't.** For financial services clients, always check finder.com.au, canstar.com.au, and money.com.au for rate data competitors hide on their own sites.
- **Broker portals reveal real product specs.** Many financial services and B2B companies maintain a separate broker/partner portal with full product documentation. Check for it.
- **Never fabricate.** If data isn't found, say so. "Not found — manual check recommended" is always acceptable.
- **Opportunities must cite evidence.** "No competitor offers bridging loans — confirmed via site: searches on all three" not "there may be an opportunity in bridging loans."
- **The strategic recommendation should name a position.** Not "Brighten should consider differentiating on speed" but "Brighten should own bridging loans in the direct digital channel — it is uncontested."
