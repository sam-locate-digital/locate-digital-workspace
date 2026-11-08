---
name: monthly-report-narrative
description: Write the narrative, insights, anomaly flags, and recommendations for a client's monthly performance report. Reads the generated report.md or accepts pasted data tables. Produces client-facing commentary per active channel plus a prioritised action list. Humaniser pass mandatory. Use when writing the monthly report, adding commentary to data tables, or reviewing a client's month.
---

# Monthly report narrative

Takes the structured data from `generate.py` output (or pasted numbers) and writes the human commentary that turns tables into a client-ready report.

**Input:** `reports/YYYY-MM/report.md` path, or paste the data directly.
**Output:** `reports/YYYY-MM/narrative.md` — ready to slot into the report.

---

## Step 1 — Load context

Read CLAUDE.md (already loaded if running from the client folder). Extract:

- Client name and industry
- Active channels (only write sections for channels with data)
- Baseline metrics at onboarding — used to judge whether current numbers are good or bad
- Goal for the engagement (if set)
- Average job/appointment/loan value (needed to translate volume into revenue impact)

---

## Step 2 — Get the data

**Priority order:**
1. If the user says "reports/2026-05" or gives a month, look for `reports/YYYY-MM/report.md` in the current client folder. Read it.
2. If `report.md` not found, check for the most recent file under `reports/` automatically.
3. If neither exists, ask: "Paste the data tables, or confirm the report path."

Once you have the data, read every table and KPI line. Pull:
- This month's value and prior month's value for every metric
- Calculated deltas where not already present
- Channel breakdown (organic vs paid vs direct etc.)
- Any segmentation data (by location, by practitioner, by ad group, etc.)

---

## Step 3 — Flag anomalies first

Before writing prose, identify every metric that warrants attention. Classify each:

| Flag | Threshold | Examples |
|---|---|---|
| 🔴 Critical | >25% drop vs prior month, or zero where >0 expected | Conversions dropped to 0, sessions down 30% |
| 🟡 Watch | 10–25% change either direction (unexpected) | Bounce rate up 15%, CPA up 18% |
| 🟢 Win | Meaningful positive movement or record metric | Best month for new patients, CPL below target |

Rules:
- A drop during a known seasonal period (school holidays, public holidays, summer) is still flagged but includes the likely cause
- A 30% increase is flagged too — unsustained spikes need explaining
- Zero conversions is always 🔴 regardless of percentage
- Over-budget spend is always 🔴
- Under-delivery (budget not spent) is 🟡 if >15% unspent

---

## Step 4 — Write the narrative

Produce each section below. Only include sections for channels with actual data. Skip sections with no data rather than writing "not available".

---

### Section 1: Executive summary

3–4 sentences. Lead with the most important number or movement, then the second-most important, then overall direction.

Rules:
- Name specific numbers: "sessions fell from 1,240 to 1,085, down 12.5%"
- Say what caused it if known; say "under investigation" if unknown — never be vague
- If it was a good month, say so directly
- If something needs immediate action, say so here — don't bury it in section 5
- No filler openers: never start with "This month saw…" or "It was a busy month"

Example pattern (adapt to the actual data):
> "Sessions were down 12% in April — standard post-school-holiday softness, in line with the same period last year. New patients held steady at 47 despite the lower traffic, which suggests the booking page conversion rate improved. Google Ads cost per lead came in at 34 dollars, back within target after the March spike. One priority: the campaign for [service] hit zero conversions last week — see recommendations."

---

### Section 2: Channel-by-channel insights

One subsection per active channel. Write 2–4 sentences per channel.

**Website (GA4)**
- Sessions, users, engagement rate vs prior month
- Which channel drove the movement (organic up? paid down? direct flat?)
- Top landing page changes — is the homepage still eating traffic that should go to service pages?
- Any conversion goal completions to note

**Google Ads**
- Impressions, clicks, CTR vs prior month
- Spend vs budget (underspent or overspent)
- Cost per conversion vs target
- Which campaign or ad group is performing / underperforming
- Quality Score or Ad Strength changes if available

**Meta Ads**
- Reach, CPM, click-through rate
- Lead form completions or landing page conversions
- Cost per result vs target
- Which audience or creative is leading; which is fatiguing (frequency >3.5 is a warning sign)
- Learning phase status if a campaign is new

**SEO (organic)**
- Organic session trend
- Any notable ranking movements (if Search Console data is available)
- Pages gaining or losing organic traffic
- GBP calls or direction requests if tracked

**Cliniko / CRM / bookings**
- New patients or leads vs prior month and vs onboarding baseline
- Appointments held, cancelled, no-show rate
- By-location breakdown if there are multiple sites
- By-practitioner if relevant (e.g. a practitioner was away — this explains a dip)

**Email (if active)**
- Send volume, open rate, click rate vs industry benchmark (~25% open, ~2.5% click for health/services)
- Conversions or revenue attributed

---

### Section 3: Anomaly log

List every flagged metric from Step 3 in a tight table. Be specific.

Format:
```
| Flag | Metric | This month | Prior month | Change | Likely cause |
|---|---|---|---|---|---|
| 🔴 | Conversions — Search campaign | 0 | 14 | –100% | Conversion tag fired incorrectly — confirm in GA4 |
| 🟡 | CPA — Brand campaign | AUD 62 | AUD 48 | +29% | Competitor activity on brand terms — check auction insights |
| 🟢 | New patients | 52 | 41 | +27% | April new-patient landing page went live 5 Apr |
```

"Likely cause" column: give a specific hypothesis or say "cause unknown — investigate". Never leave it blank.

---

### Section 4: Recommendations

Exactly 5 recommendations. Prioritised: most urgent first.

Each recommendation must be:
- **Specific** — "Add [exact keyword] as a negative keyword in the Search campaign" not "review keywords"
- **Actionable** — something that can be done in the next 2 weeks
- **Tied to a number** — reference the metric it addresses

Format:
```
1. **Fix conversion tracking before next spend cycle** — zero conversions recorded in the Search campaign last week despite 340 clicks. Check the GA4 tag fires on the thank-you page. Until this is confirmed, pause Smart Bidding and revert to Max Clicks to avoid the algorithm optimising on ghost data.

2. ...
```

Rules:
- No generic advice ("improve ad copy", "increase budget", "post more content")
- No more than 5 — prioritise ruthlessly
- If it's a structural fix (like conversion tracking), it always goes first
- If everything is healthy, recommendations focus on next growth lever — not invented problems

---

### Section 5: Month-over-month scorecard

A single clean table covering all key metrics. This goes at the end of the narrative and also works as a standalone summary.

```
| Metric | This month | Prior month | Change | Status |
|---|---:|---:|---:|---|
| Sessions | 1,085 | 1,240 | –12.5% | 🟡 |
| New patients | 52 | 41 | +26.8% | 🟢 |
| Google Ads spend | AUD 1,840 | AUD 1,800 | +2.2% | 🟢 |
| Google Ads CPA | AUD 34 | AUD 42 | –19% | 🟢 |
| Meta CPL | AUD 28 | — | — | New |
...
```

Include every metric with a prior-month comparison. Mark new channels with "New" in the Change column.

---

## Step 5 — Humaniser pass

Before outputting anything, apply humaniser rules:
- No em dashes — use commas or periods
- No AI vocabulary: crucial, pivotal, delve, underscore, foster, showcase, vibrant, testament, landscape (abstract)
- Sentence case throughout
- Vary sentence length — short punchy sentences mixed with longer ones
- No generic closings: "this sets us up well for next month", "exciting times ahead"
- No signposting: "let's look at", "here's what the data shows"
- Australian English: "optimise" not "optimize", "recognised" not "recognized"

---

## Step 6 — Write the file

Save to `reports/YYYY-MM/narrative.md` in the client's folder.

Print the path and a brief summary:
```
✓ Narrative written: clients/MOSIC/reports/2026-05/narrative.md

Anomalies: 1 🔴  2 🟡  1 🟢
Key finding: Conversion tracking broken in Search campaign — action needed before next billing cycle.
Recommendations: 5 (conversion fix, negative keyword list, new Meta audience test, GBP post schedule, landing page CTA update)
```

---

## Rules

- Write to the actual data. If a metric moved 3% and there's no context suggesting that's unusual, don't flag it.
- Never invent causes. If you don't know why something moved, say "cause unknown — needs investigation".
- Never imply the agency caused a bad result without evidence. But also never hide it if the data suggests an agency action caused a problem.
- The narrative is client-facing. Write as if the client will read it — clear, respectful, no jargon without explanation.
- Financial clients: don't name or imply specific financial outcomes from marketing data. Report lead volume, cost per lead, website behaviour — not "this will result in X loans funded".
- Health clients: AHPRA applies — no clinical outcome claims in commentary (e.g. don't write "more patients getting treatment for X condition" — just "new patient volume").
- If data is missing for a section (e.g. GA4 access not yet granted), note it once and skip the section — don't write filler.
