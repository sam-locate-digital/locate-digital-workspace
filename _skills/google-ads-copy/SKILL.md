---
name: google-ads-copy
description: Write Google Ads RSA copy for service business clients. Use when asked to write Google ad copy, search ad headlines, RSA copy, Google Ads text, PPC copy, or responsive search ad copy for a client. Outputs a complete Google Ads setup: keywords with match types and reasoning, 15 RSA headlines, 4 descriptions, pinning recommendations, phased bidding strategy, and campaign/ad settings — all with reasoning. Always includes humaniser pass.
---

# Google Ads copy — RSAs for service businesses

Produce a complete Google Ads setup for a service business client: keywords, RSA copy, bidding strategy, and campaign settings. Every recommendation includes a reason — this output is designed to be handed to a client or used to build a campaign from scratch.

## Client context (read first)

Read the client's `CLAUDE.md` from `clients/<name>/CLAUDE.md`. Pull:
- Business name, industry, locations and suburbs
- Primary services and any known target keywords
- Key proof points (years operating, patient/client volume, certifications)
- Google Ads channel status and any existing campaign context

If no client is specified, ask which client this is for.

## Inputs (ask only if missing)

- **Service/campaign** — which service are we targeting?
- **Target keywords** — any known search terms to anchor the ad groups (optional)
- **Locations** — suburb, city, or radius

If only "write Google ads" → ask for the service focus before writing.

---

## Section 1 — Keywords & match types

Organise keywords into ad groups. Service businesses typically need 3–4 ad groups:

1. **Clinic/brand + location** — exact + phrase on the core service + city/suburb queries
2. **Primary condition** — the main pain point or condition the client treats (phrase + exact on the highest-intent combos)
3. **Secondary conditions** — other services or conditions (phrase)
4. **Near me / generic local** — "near me" and location-only variants (phrase)

For each keyword include:
- Keyword text
- Match type: **Exact**, **Phrase**, or **Broad**
- One-sentence reasoning explaining why that match type is right for that query

**Match type guide for local service businesses:**

| Match type | When to use | When to avoid |
|---|---|---|
| **Exact** | Ultra-specific, high-intent queries (service + location + condition). These searchers are ready to book — protect CPC by using exact. | Generic or broad queries where you want to catch variants |
| **Phrase** | Service + condition + location combos where natural variants are valuable. Catches "best X Melbourne", "X near me", "X in CBD" without going too wide. | When the query is so specific that variants add no value |
| **Broad** | Only with Smart Bidding (Target CPA or Maximize Conversions) and 50+ conversions/month. Never at campaign launch. | Any campaign without conversion history — will burn budget |

**"Near me" rule:** Always include `[service] near me` as phrase match. It's consistently the highest-volume modifier in local service search. Phrase match paired with location targeting handles the geography — Google serves it to people near the target location.

**Don't recommend Broad match at launch.** Smart Bidding needs 50+ monthly conversions to work. Without conversion data, Broad + Smart Bidding overspends on irrelevant queries.

---

## Section 2 — Headlines (15)

Hard limits — count every character including spaces:

| Element | Max | Quantity |
|---|---|---|
| Headline | 30 chars | Write 15 |
| Description | 90 chars | Write 4 |

Flag any headline over 30 chars — Ads Manager rejects it. Show character count after each line.

**Headline mix — include every type:**

- **3–4 keyword headlines** — primary keyword or close variant. Must include the main service + location.
- **2–3 location headlines** — city, suburb, "near me". Location signals in headlines improve Quality Score.
- **2–3 benefit/outcome headlines** — what the patient/client actually gets. Avoid vague benefits; be specific.
- **2 CTA headlines** — action-oriented. One for online booking, one for phone.
- **2 trust/proof headlines** — years operating, patient/client volume, credentials, practitioner count.
- **1–2 USP or differentiator headlines** — telehealth, same-day, multi-location, specialist focus.

---

## Section 3 — Descriptions (4)

Write one of each:

1. **Service + outcome** — what the client offers and what the patient/client gets. Specific over vague.
2. **Trust + proof** — volume, years, credentials, location. Specific numbers ("12,000+ patients") beat generic claims.
3. **CTA + booking** — phone number and/or booking URL. This description should always be pinned to position 1 so it always shows.
4. **USP or seasonal** — differentiator, timely angle (EOFY, winter, sport season), or telehealth.

---

## Section 4 — Pinning recommendations

Recommend which headlines to pin and why. Standard pins for local service businesses:
- **Position 1:** Pin the primary keyword headline — core service query must always appear
- **Position 2:** Pin the strongest location headline — local signal on every impression
- **Description 1:** Pin the CTA/contact description — phone number must always show

Note: pinning reduces Ad Strength slightly. If Ads Manager reports "Good" instead of "Excellent" after pinning, test removing the position 2 pin first.

---

## Section 5 — Bidding strategy

Always recommend a phased approach. Explain why each phase exists — Smart Bidding without data performs worse than manual.

**Phase 1 — First 30–60 days:**
- Strategy: Maximize Clicks with a max CPC cap
- CPC cap: base on industry and location competitiveness (AUD 8–15 for most local service businesses in major AU cities)
- Reason: No conversion history yet. Smart Bidding (Maximize Conversions, Target CPA) requires 30–50 conversions/month to work — without data it overspends or underspends unpredictably. Maximize Clicks builds volume, gathers conversion data, and reveals which keywords and headline combinations actually drive bookings.

**Phase 2 — After 50+ conversions (typically month 2–3):**
- Strategy: Maximize Conversions
- Trigger: 50+ monthly conversions for two consecutive months
- Reason: With enough signal, Google optimises bids toward the actions defined in conversion tracking. Don't switch before the threshold — Smart Bidding with thin data actively underperforms manual bidding.

**Phase 3 — Mature campaign (month 4+):**
- Strategy: Target CPA
- CPA range: estimate based on appointment value and margin. Set initial Target CPA 10–20% above observed CPA — too tight causes impression share to collapse.
- Reason: Target CPA enforces a cost ceiling once CPL has stabilised. Set it at the maximum acceptable cost per lead given the client's appointment value and lifetime patient value.

---

## Section 6 — Campaign & ad settings

For every setting, state the recommendation AND the reason. Never list a setting without explaining why.

**Network**
Recommendation: Search Network only at launch. Do not tick Display Network or Search Partners.
Reason: Display Network shows ads on third-party websites and apps — irrelevant for a patient searching for an appointment. Search Partners (Ask.com, YouTube search) add volume at lower intent. Add Search Partners at 60 days if CPC and conversion rate hold up.

**Location targeting**
Recommendation: Radius from each clinic location PLUS explicit suburb targeting.
Reason: Radius targeting catches "near me" queries using device location. Suburb targeting catches explicit suburb queries ("osteopath Carlton") that may fall outside the radius. Use both layers — not one or the other.

**Location options (critical)**
Recommendation: Change from default "Presence or interest" to **"Presence: People in or regularly in your targeted locations"**.
Reason: The default includes people researching the area who live elsewhere — a Sydney resident planning a Melbourne trip. They will not book at a local clinic. This single setting change commonly reduces wasted spend by 10–20% on local campaigns. Always flag this to the client — it's the most commonly missed setting.

**Ad schedule**
Recommendation: Business hours plus early evening. Pause late night.
Reason: Local service bookings cluster during business hours and early evening research windows. Running ads at 2am drives cost without proportional bookings for most service businesses. Adjust based on the specific client's booking patterns once data is available.

**Devices**
Recommendation: All devices, with mobile bid adjustment +20–25%.
Reason: "Near me" and local service searches are 65–75% mobile. Call extension clicks — typically the fastest-converting action for a local service business — only work on mobile. Keep desktop active for CBD/office audiences who search from work computers.

**Conversion tracking (must be live before launch)**
Set up and verify before spending a dollar. Track:
- Phone calls from ads (threshold: 60 seconds — filters out wrong numbers and hang-ups)
- Website form submissions
- Booking page visit or confirmation page
Reason: Without conversion tracking, Smart Bidding is blind, reporting shows clicks not outcomes, and there is no way to calculate ROI for the client. The 60-second call threshold is critical — under 60 seconds is not a real lead.

**Ad rotation**
Recommendation: Optimize — prefer best performing ads.
Reason: RSAs test headline and description combination permutations automatically. Forcing equal rotation shows underperforming combinations as often as winners. "Optimize" lets Google surface the combinations with the highest CTR and conversion rate for each query. Review the combination report monthly.

**Extensions / assets**
Always recommend:
- **Location extension** (linked to Google Business Profile) — shows address and distance. Adds map pin on mobile. Mandatory for local.
- **Call extension** (local number, scheduled during business hours) — one-tap call from mobile. Highest-converting action for most local service businesses.
- **Sitelinks** — link to key service pages, location pages, and booking page.
- **Callout extensions** — short credibility claims: "Same-Week Appointments", "Telehealth Available", "Online Booking", "8 Practitioners".
- **Structured snippets** (Services) — list services: Osteopathy, Back Pain, Sports Injuries, etc.
Reason: Extensions expand ad real estate, improve Quality Score, and give searchers multiple ways to engage. Location + Call are non-negotiable for a local clinic.

**Final URL / display path**
Recommendation: Dedicated landing page per ad group, NOT the homepage. Display path should mirror the ad group topic.
Reason: Homepage has competing CTAs and too many exits. A focused page matching the ad message (back pain ad → back pain landing page) converts 30–50% higher than a homepage for paid traffic. The display path (green text under the headline) signals relevance and improves Quality Score.

---

## AU English and local intent

- Australian spelling: practise not practice, programme not program
- Suburb and city names in headlines and descriptions signal local intent to Google
- "Near me" as a headline phrase is strong for local service searches
- No US-coded phrases, no IRS/401k/ZIP code references

## What to avoid

- Generic filler headlines: "Best Service", "High Quality", "Dedicated Team"
- Repeating the same phrase across 3+ headlines — Ads Manager penalises low variety
- CTAs in descriptions that duplicate a CTA headline (wastes a slot)
- Trailing punctuation on headlines — Ads Manager strips it anyway
- Keyword stuffing in descriptions
- Recommending Broad match to a client without conversion history

## Humaniser pass

Run humaniser on the 4 descriptions. Headlines are too short for deep humaniser logic but scan them for AI vocabulary (exceptional, premier, crucial, dedicated) and forced formality that sounds unlike a real ad. Deliver the cleaned set as final output.
