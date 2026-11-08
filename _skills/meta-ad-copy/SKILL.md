---
name: meta-ad-copy
description: Write a complete Meta (Facebook/Instagram) ads setup for service business clients. Use when asked to write Facebook ads, Instagram ads, Meta ad copy, paid social copy, or ad creative copy for a client. Outputs a full campaign setup: target audiences with reasoning, ad variants (primary text, headline, description, CTA, visual direction) for cold and retargeting, phased bidding strategy, and campaign/ad settings — all with reasoning. Always runs humanizer before delivery.
---

# Meta ad copy — complete campaign setup for service businesses

Produce a complete Meta ads setup for a service business client: audiences, ad copy variants, bidding strategy, and campaign settings. Every recommendation includes a reason — designed to be handed to a client or used to build a campaign from scratch.

## Client context (read first)

Read the client's `CLAUDE.md` from `clients/<name>/CLAUDE.md`. Pull:
- Business name, industry, locations
- Services to prioritise
- Target audience (who they serve, demographics)
- Key proof points (years operating, patient/client count, credentials)
- Voice/tone notes
- Active channels (to understand if Meta is new or existing)

If no client is specified, ask which client this is for.

## Inputs (ask only if missing)

- **Campaign goal** — new patient/client acquisition, awareness, retargeting, or a specific service?
- **Budget** — daily or monthly? Shapes the campaign structure recommendation.
- **Any creative assets** — existing photos, video, or building from scratch?

If only "write Meta ads" → propose 2–3 angles based on client services, let Sam pick before writing the full output.

---

## Section 1 — Target audiences

Build audiences across two tiers. Always document both even if only cold is active at launch — warm audiences need to start accumulating pixel data from day one.

**Cold audiences (prospecting):**
Build 2–3 cold ad sets targeting people who don't know the business yet. For local service businesses:

- **Interest-based** — people engaging with content related to the client's conditions or services (back pain, running, osteopathy, physiotherapy, corporate wellness, etc.). Strongest cold audience for a health or professional services clinic.
- **Behaviour/demographic** — job titles, commuter behaviour, age range, income proxies. Useful for service businesses with a clear professional demographic (e.g. CBD desk workers).
- **Audience-specific interests** — if the client treats athletes, target sport interests. If they serve tradespeople, target trade-related interests. Separate from the general health audience so different ad angles can be tested independently.
- **Lookalike 1%** — queue but do not activate until the pixel has recorded 500+ website visitors. Too small a seed produces low-quality lookalikes.

**Warm audiences (retargeting — activate at 30 days+):**
- **All website visitors** (30-day window) — people who know the business but didn't convert. Copy should acknowledge proximity without being explicit about tracking.
- **Booking/contact page visitors** (14-day window, exclude confirmed conversions) — highest intent. Remove friction in the copy: fast booking, phone alternative.
- **Video viewers 50%+** (30-day window) — strong engagement signal. Follow up with a direct offer.
- **Page engagers** (60-day window) — broader warm pool. Good for top-of-mind content.

For each audience include:
- Audience name
- Targeting details (interests, behaviours, demographics, geo, age)
- Reasoning — why this audience for this client, what to emphasise in copy

**Geography rule for local service businesses:** Use radius targeting (15 km from each location is a reliable starting point) rather than city-level targeting. City-level includes people too far to travel. Exclude areas clearly outside the patient/client catchment.

**Do not activate warm campaigns until each audience has 500+ people.** Meta needs volume to optimise delivery — too small an audience causes ad fatigue, inflated CPMs, and erratic results.

---

## Section 2 — Ad variants

Write one variant per audience type, plus a dedicated retargeting variant. Minimum 3 variants; 4 is better (cold × 3 angles + retargeting × 1).

**Character limits:**

| Element | Visible limit | Hard max |
|---|---|---|
| Primary text | 125 chars before "see more" in feed | 5,000 |
| Headline | 27 chars before truncation in feed | 255 |
| Description | 30 chars | 255 |

Write primary text to ~125 chars for cold audiences. Warm and retargeting can run longer (200–250 chars) — these people are already familiar, they'll read more.

Every headline must work standalone at 27 chars. Count it.

**For each variant include:**
- Angle (one-line description of the approach)
- Target audience (which cold or warm segment)
- Campaign objective (Leads, Traffic, or Awareness)
- Primary text
- Headline (with char count)
- Description (with char count)
- CTA button
- Visual direction (specific — subject, mood, composition; not "professional photo of clinic")
- Reasoning — why this angle for this audience, what psychological trigger it uses

**Ad patterns for service businesses:**

*Problem/solution — cold*
Name the pain specifically. Then offer the fix. Works best when the audience has already signalled the pain through their interests.
"Your body wasn't built for eight hours at a desk. Most back and neck pain CBD workers deal with isn't bad luck. It's the chair, the screen height, and the commute."

*Social proof — cold or warm*
Specific numbers beat vague claims. Pull from client CLAUDE.md — patient/client volume, years, practitioners.
"12,000 patients. 8 practitioners. Two clinics in Melbourne."

*Seasonal/local — cold*
Tie to a real moment: EOFY, AFL, marathon season, winter, school holidays. Seasonal relevance improves CTR because it signals the ad was written for right now.
"AFL season, cold mornings, long weeks at the desk. Every winter we see the same thing at our clinics."

*Outcome-first — cold*
Lead with the result, not the service. Speak to where the patient/client wants to be, not where they are.
"Back at the gym in 3 sessions. That's what most of our running injury patients tell us."

*Retargeting — warm non-converters*
Acknowledge proximity to action without referencing tracking. Remove friction. Include a direct phone number as an alternative to the online booking path.
"Still thinking about it? Same-week appointments available. Book online in under 2 minutes or call [number]."

**Retargeting copy rule:** Only show retargeting variants to warm audiences. Showing "Still thinking about it?" to a cold audience who has never heard of the business breaks the context entirely and damages brand perception.

---

## Section 3 — Bidding strategy

Always recommend a phased approach. Meta's algorithm needs time and data to exit the learning phase before Smart Bidding can work effectively.

**Phase 1 — First 30–60 days:**
- Strategy: Lowest cost (no bid cap), CBO at campaign level
- Budget starting point: AUD 30–50/day for a local service business in a major AU city
- Reason: The learning phase requires approximately 50 optimisation events per ad set per week. Setting a cost cap or ROAS target before accumulating that data restricts delivery and extends the learning phase. CBO (Campaign Budget Optimisation) lets Meta shift budget toward whichever ad set performs best in real time, rather than distributing budget equally across underperformers.

**Phase 2 — After learning phase (week 3–6):**
- Strategy: Cost Per Result Goal set 10–20% above the observed CPL
- Expected CPL benchmarks: AUD 15–40 for Lead Gen (instant form), AUD 40–80 for Traffic to landing page
- Reason: Once CPL data is consistent, a Cost Per Result Goal guides Meta's bidding without enforcing a hard ceiling. The 10–20% buffer above observed CPL gives the algorithm room to find conversions — setting it too tight slows delivery. These are benchmarks; actual CPL depends on audience quality, creative, and landing page.

**Phase 3 — Mature campaigns (month 3+):**
- Strategy: Cost cap at target CPL for cold; separate retargeting budget
- Retargeting budget: AUD 10–15/day (small audiences convert at 2–4× cold rate)
- Reason: Cost cap enforces the maximum acceptable CPL strictly once performance has stabilised. Split budget at this point: majority to cold prospecting (acquisition), dedicated smaller budget to warm/retargeting. Retargeting is small but high-converting at local scale — underfunding it wastes the warm audiences built over the first two months.

---

## Section 4 — Campaign & ad settings

For every setting, state the recommendation AND the reason.

**Campaign objective**
Recommendation: Leads (instant form) for volume; Traffic to dedicated landing page for higher-intent leads.
Reason: Meta's instant form reduces friction — users complete a form without leaving the app. This produces more leads at lower cost but quality can vary (some low-commitment submissions). Traffic to a landing page filters out low-intent users via the extra click — fewer leads but higher booking rate. Start with Leads for volume; switch to Traffic once the client's follow-up process is confirmed and conversion tracking is live on the landing page.

**Campaign structure**
Recommendation: Campaign 1 (cold prospecting, 2–3 ad sets). Campaign 2 (retargeting, activate at day 30+). Keep cold and warm in separate campaigns.
Reason: Mixing cold and warm audiences in one campaign causes Meta to favour the cheaper-to-reach warm audience, cannibalising the prospecting budget. Separate campaigns allow independent budget control, frequency caps, and creative. Don't launch the retargeting campaign until each warm audience has 500+ people — too small an audience causes extreme frequency and ad fatigue.

**Campaign budget vs ad set budget**
Recommendation: CBO (Campaign Budget Optimisation) at campaign level.
Reason: CBO dynamically allocates budget across ad sets based on real-time performance signals. Manual ad set budgets (ABO) force fixed spend regardless of which ad set is actually working. For a new account with no prior data, CBO is safer. Switch individual ad sets to ABO later if a specific audience needs a guaranteed minimum spend.

**Placements**
Recommendation: Advantage+ placements for month 1. Manual from month 2 — Facebook Feed, Instagram Feed, Stories, Reels. Exclude Audience Network after 30 days.
Reason: Advantage+ lets Meta test across all surfaces and optimise toward cheapest conversions — generally outperforms manual selection for new accounts. After 30 days, review the placement breakdown report. Audience Network (third-party apps and websites) consistently delivers cheap but low-quality traffic for local service businesses. Remove it once you have data confirming this pattern.

**Geography**
Recommendation: Radius targeting from each clinic location (15 km is a reliable starting point). Exclude areas clearly outside the patient/client catchment.
Reason: Meta's geo targeting uses device location, not billing address — 15 km captures people who are physically accessible to the clinic. City-level targeting is too broad for a local service business. Exclusions prevent spending on people who will never make the journey, which is wasted budget at a local scale.

**Age and gender**
Recommendation: Match the client's actual target demographic. Keep gender open unless strong performance data justifies narrowing.
Reason: Locking to a single gender misses a portion of the converting audience without data to support the exclusion. Let performance data guide narrowing after 60 days. Age range should exclude demographics the client doesn't serve or that have significantly lower booking intent.

**Ad schedule**
Recommendation: Run all hours for cold (Meta optimises delivery timing automatically). Retargeting ads: pause 11pm–6am.
Reason: Meta's delivery algorithm shifts spend toward the hours your audience is most likely to engage — suppressing hours overrides this optimisation and can hurt performance. The exception is retargeting: showing "Still thinking about it?" at 2am feels intrusive. Scheduling retargeting during waking hours keeps the tone appropriate.

**Pixel and conversion events**
Must be installed and verified BEFORE launching any campaign. Track:
1. PageView (all pages)
2. ViewContent (service/treatment pages)
3. InitiateCheckout (booking page load)
4. Lead or Purchase (booking confirmation page)
Reason: The pixel is the foundation of everything on Meta. Without it, Smart Bidding cannot optimise toward conversions, lookalike audiences have no seed data, and retargeting audiences don't build. The booking confirmation event is the most critical — this is what tells Meta which users became actual patients or clients. Install via Meta Business Suite → Events Manager, then verify all events are firing using the Meta Pixel Helper Chrome extension before spending a dollar.

**Frequency cap**
Recommendation: Cold audiences — 2–3 impressions per person per week. Retargeting — 5–7 per week.
Reason: Frequency is the hidden performance killer on Meta at local scale. Small geo means the same people see your ads repeatedly. Cold audiences develop negative sentiment and become ad-blind above 3 impressions/week — watch the Frequency column in Ads Manager and rotate creative when it crosses 3.0. Retargeting audiences are smaller so frequency naturally rises; 5–7/week is acceptable because intent is higher and the exposure window is shorter.

**Creative refresh cadence**
Recommendation: Cold creative — refresh every 3–4 weeks. Retargeting — refresh every 6–8 weeks.
Reason: Ad fatigue is faster at local scale than national. Keep 2–3 creative variants active simultaneously so Meta can rotate and a fresh fallback is always ready. When frequency crosses 3.0 on cold audiences, swap the primary text or lead image even if CTR looks fine — fatigue shows in frequency data before it shows in click metrics.

---

## What to avoid in ad copy

- Vague claims: "high quality service", "dedicated professionals", "passionate team"
- Generic openers: "Are you looking for...", "Do you struggle with..."
- Superlatives without proof: "best", "leading", "premier"
- More than one exclamation mark per variant
- Em dashes — replace with commas or periods
- US references, non-AU framing
- Medical outcome guarantees for health clients — use "may help", "commonly used to treat", "many patients find"
- Showing retargeting copy to cold audiences

## Humanizer pass (always last)

Run humanizer on all variants. Focus on:
- Removing AI vocabulary (crucial, seamless, exceptional, pivotal, dedicated)
- Making primary text sound like a real marketer or business owner wrote it
- Varying sentence length in longer primary text blocks
- Checking headlines read naturally at 27 chars — not cut-off mid-word or thought

Deliver humanized variants as the final output.
