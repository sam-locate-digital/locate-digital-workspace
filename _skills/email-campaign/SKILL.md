---
name: email-campaign
description: Write a complete email campaign for a Locate Digital client. Produces a full campaign document — every email in the sequence with send timing, 3 subject line variants, preview text, and body copy. Use when Sam asks to write an email campaign, email sequence, nurture series, reactivation campaign, welcome sequence, newsletter, or follow-up email for any client. Also triggers on "email for [client]", "write emails for [client]", or "draft a [campaign type] campaign".
---

# Email campaign

Write a complete, ready-to-use email campaign for a Locate Digital client. One skill run = one campaign document, fully written.

---

## Step 1 — Load client context

Read the client's `CLAUDE.md` before writing a single word. Extract:

- Business name, industry, locations
- Target audience (age, occupation, what brings them in)
- Primary services to push
- Tone and voice notes (if set)
- Proof points (years operating, patient volume, practitioners, awards)
- Compliance flags (industry — health, legal, accounting, etc.)
- Goal (default: drive bookings)

If no CLAUDE.md exists or key fields are TBD, ask Sam to fill the gaps before continuing. Don't write on assumptions.

---

## Step 2 — Confirm campaign type

If Sam hasn't specified, ask which campaign type:

| Type | When to use |
|---|---|
| **Welcome sequence** | New patient/client enquires or books for the first time |
| **Reactivation — lapse** | Patients who haven't booked in 3–6+ months |
| **Reactivation — DNF** | Patients who dropped off mid-treatment plan |
| **Monthly newsletter** | Regular send to full active list |
| **Post-appointment follow-up** | After a visit — review request, rebook nudge, care tip |

Also confirm:
- **Sending platform** (Cliniqapps, Mailchimp, Klaviyo, other — affects formatting notes)
- **Any specific offer or hook** to lead with (if none, the skill will write without one)

---

## Step 3 — Write the campaign

### Output format

Save the completed campaign as a markdown document at:
```
clients/<name>/content/<YYYY-MM>/email-campaign-<type>.md
```

Every campaign document follows this structure:

```
# [Client name] — [Campaign type] email campaign
Date: [YYYY-MM-DD]
Platform: [platform or TBD]
Goal: [primary goal]
Audience segment: [who receives this]

---

## Campaign overview
[2–3 sentences: what this campaign does, why it works for this client]

---

## Email [N] — [Name]
**Send:** [timing, e.g. "Immediately on sign-up" / "Day 3" / "Day 7"]
**Audience:** [segment note if different from campaign-level]

**Subject lines (pick one — or A/B test 1 vs 2):**
- A: [subject line]
- B: [subject line]
- C: [subject line — most experimental]

**Preview text:** [60–90 characters]

**Body:**

[Full email copy]

---
[Repeat for each email]
```

---

## Campaign blueprints

### Welcome sequence (3–5 emails)

Goal: convert a new enquiry or first booking into a retained patient who refers others.

| Email | Send timing | Purpose | Length | Style |
|---|---|---|---|---|
| 1 — Welcome | Immediately | Warm confirmation, set expectations | 150–200 words | Plain text |
| 2 — About us | Day 2–3 | Build trust, introduce the team/clinic | 200–250 words | Plain text |
| 3 — What to expect | Day 5–7 | Reduce first-visit anxiety, practical info | 150–200 words | Plain text |
| 4 — Social proof | Day 10–14 | Reviews, outcomes language, confidence builder | 150–200 words | Plain text |
| 5 — Soft rebook nudge | Day 21–28 | Invite them to book their next session | 100–150 words | Plain text |

**Tone:** Warm, personal, human. Reads like it's from the practitioner or front desk — not a broadcast.

---

### Reactivation — lapse (3 emails)

Goal: get a patient who has gone quiet to rebook. The window is 3–6 months since last visit.

| Email | Send timing | Purpose | Length | Style |
|---|---|---|---|---|
| 1 — "We miss you" | Day 0 | Low pressure check-in, remind them you exist | 100–130 words | Plain text |
| 2 — Value reminder | Day 7 | Remind them of progress made / what they were treating | 120–150 words | Plain text |
| 3 — Final nudge | Day 14 | Light urgency, clear CTA, easy out | 80–100 words | Plain text |

**Tone:** Human and direct. Never guilt-trip. The reader should feel like the clinic noticed their absence and genuinely wants to help, not like they're being chased for revenue.

---

### Reactivation — DNF (3–4 emails)

Goal: re-engage a patient who stopped treatment before completing a plan. These patients often feel embarrassed about dropping off — remove that barrier.

| Email | Send timing | Purpose | Length | Style |
|---|---|---|---|---|
| 1 — No judgement check-in | Day 0 | Acknowledge the gap, make it easy to come back | 120–150 words | Plain text |
| 2 — Outcome reminder | Day 5 | Reconnect them with what they were working toward | 130–160 words | Plain text |
| 3 — Practical re-entry | Day 10 | Make booking feel simple and low-friction | 100–120 words | Plain text |
| 4 — Soft close | Day 18 | Final touch — no hard sell | 80–100 words | Plain text |

**Tone:** Non-judgemental and warm. Acknowledge that life gets in the way. Don't imply they've failed — imply they've just paused.

---

### Monthly newsletter (1 email)

Goal: stay top-of-mind, deliver value, and include a soft booking CTA.

**Structure:**
1. **Opening hook** — one punchy sentence or question (not "Welcome to our newsletter")
2. **Main content block** — one useful, relevant topic (health tip, seasonal advice, new service, practitioner spotlight). 150–200 words.
3. **Soft CTA** — "If this sounds like something you're dealing with, we have availability this month" → book link
4. **Secondary item** (optional) — short clinic update, Google review request, or upcoming closure notice

**Length:** 300–400 words total
**Style:** Lightly branded — clean layout with a header, but body reads like a human wrote it

---

### Post-appointment follow-up (1–2 emails)

Goal: collect a review, encourage rebooking, and reinforce the value of the visit.

| Email | Send timing | Purpose | Length | Style |
|---|---|---|---|---|
| 1 — Thank you + review request | 24–48 hours post-visit | Warm thanks, Google review ask | 100–130 words | Plain text |
| 2 — Rebook nudge (optional) | 2–3 weeks post-visit | Remind them when their next session would typically fall | 80–100 words | Plain text |

**Tone:** Personal and warm. The review ask should never feel transactional — frame it as helping others find the clinic, not helping the clinic's SEO.

---

## Writing rules

### Subject lines
Write 3 per email — all tested against each other on the same list or rotated over time.

- **A** — direct, benefit-led ("Your next appointment — when you're ready")
- **B** — curiosity or question ("Been a while — how are you going?")
- **C** — most experimental — pattern interrupt, personalisation token, or unexpected angle

Keep subject lines under 50 characters where possible. Mobile previews cut off at 40.

Never use:
- Clickbait with no payoff
- All caps
- Excessive punctuation (!!!, ???)
- Spam triggers: "FREE", "Act now", "Limited time offer"

### Preview text
Always write it. Never leave it blank or repeat the subject line. It's 60–90 characters and should extend the subject line's thought — not summarise the email.

### CTAs
Every email has one primary CTA. One. Not three buttons and a link list.

- Booking emails: "Book online" or "Book your next session" → link to booking page
- Review emails: "Leave us a Google review" → direct Google review link
- Newsletter: "Book an appointment this month" or "Reply and let us know"

Make the CTA a button where the platform supports it. In plain text, use a full URL on its own line.

### Tone by email type
| Type | Tone |
|---|---|
| Welcome | Warm, excited, personal |
| Reactivation | Human, low-pressure, zero guilt |
| Newsletter | Helpful, conversational, slightly informal |
| Post-appointment | Grateful, brief, not salesy |

### Length
Shorter is almost always better. If you can cut a sentence without losing meaning — cut it. Long emails get scrolled past on mobile.

### What to avoid
- "We're excited to share..." — just share it
- "Don't hesitate to reach out" — no one says this
- "We hope this email finds you well" — delete immediately
- Outcome guarantees: "This will fix your back" / "You'll be pain-free" — never, for any industry
- Fabricated testimonials or invented proof points
- Misleading urgency ("Only 2 spots left" when there aren't)

---

## Compliance (all industries)

Regardless of client industry, never write:

- Outcome guarantees ("will cure", "eliminates", "fixes")
- Fabricated or implied testimonials
- Misleading pricing or offer claims
- False urgency or scarcity

For **health clients** (osteo, physio, dentist, GP, chiro): use "may help", "commonly used to treat", "many patients find". No before/after outcome language.

For **legal clients**: no implied outcome predictions. No "we'll win your case" framing.

For **financial/accounting clients**: no specific return or outcome promises. Add "general information only" where content could be construed as advice.

---

## Finalise and deliver

After writing the full campaign:

1. Save the file to `clients/<name>/content/<YYYY-MM>/email-campaign-<type>.md`
2. Print a short summary:

```
✓ Campaign written: [type] — [client name]
  Emails: [N]
  File: clients/<name>/content/<YYYY-MM>/email-campaign-<type>.md

Emails in this campaign:
  1. [Email name] — send [timing]
  2. [Email name] — send [timing]
  ...

Compliance notes: [any flags raised — or "none"]

Before sending:
  — Replace [BOOKING LINK] with the actual URL
  — Replace [REVIEW LINK] with the Google review URL
  — Confirm send timing matches what the platform supports
  — Proofread practitioner names and service names against CLAUDE.md
```
