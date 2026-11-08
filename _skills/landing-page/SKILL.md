---
name: landing-page
description: Write or audit a landing page for a service business client. Use when asked to write a landing page, review a landing page, build a campaign page, improve a page that isn't converting, or assess landing page copy for a client. Two modes: WRITE (generate copy from scratch) or AUDIT (review existing copy). Lead generation focused for local service businesses in Australia.
---

# Landing page — service businesses

Write or audit landing page copy for service business clients. Goal: phone calls, form submissions, or online bookings. Not product purchases or sign-ups.

## MOSIC reference template

For MOSIC pages, use `mosic-template.html` (in this skill's own folder) as the base. It matches the WPBakery site exactly — colors, fonts, button styles, responsive layout. Copy and adapt sections; don't rebuild from scratch.

## Client context (read first)

Read the client's `CLAUDE.md` from `clients/<name>/CLAUDE.md`. Pull:
- Business name, locations, services
- Target audience
- Key proof points (years, volume, credentials)
- Primary CTA destination (phone, form, booking link)
- Voice/tone notes

If no client is specified, ask which client this is for.

## Mode: WRITE or AUDIT

Ask if not clear from the prompt.

---

## Mode: WRITE

### Inputs (ask only if missing)

- **Service** — which specific service is this page for?
- **Traffic source** — Google Ads, Meta Ads, or organic? (Paid traffic needs stronger hooks — less patience)
- **Primary CTA** — phone call, form, or online booking?
- **One specific proof point** — patient/client count, a credential, years operating, a real outcome

### Page sections — follow this order

**1. Hero**
Must answer "Is this for me?" within 3 seconds.

```
H1: [Service] in [Location] — specific, not clever
    Example: "Osteopath in Melbourne CBD — Book Same-Day"
    Example: "Back Pain Treatment — Bourke Street Clinic"

Subheadline: [Who you help] + [what you do for them] — 1–2 sentences
    Example: "We help Melbourne CBD professionals get out of pain and back to sport, faster."

Primary CTA button: specific action, not "Submit"
    Example: "Book Online" / "Call 03 9663 6202" / "Get a Free Consult"

Social proof bar (directly under CTA):
    [Star rating] | [Review count] | [Years operating or patient volume]
    Example: ★★★★★ 4.9 · 120 Google Reviews · 15 years in Melbourne CBD
```

**2. Problem section**
Name the pain. Specifically. Make them feel understood.
- 2–3 short paragraphs or a simple bullet list
- Write it in the patient/client's words, not clinic language
- No "many people suffer from..." — be specific to this audience

**3. Service section**
What you do and how it helps. Three parts:
1. What the service is (plain English, no jargon without a plain explanation)
2. What happens in a typical session
3. What they can expect after

Present as 2–3 paragraphs or a "How it works" 3-step layout. Keep it practical.

**4. Trust section**
Give them a reason to choose you over the next Google result.
- Practitioner credentials and years of experience
- Patient/client volume or a landmark number
- 1–2 Google review excerpts (first name + suburb)
- Clinic photos reference (faces build more trust than empty rooms)

**5. Mid-page CTA**
Don't make them scroll to the bottom to act.
```
[Repeated CTA button — same text as hero]
"Or call [phone number] — open [hours]"
```

**6. FAQ section**
3–5 questions that reduce friction. Real objections, not "what is osteopathy?"
Examples: "How many sessions will I need?" / "Do I need a referral?" / "Is it covered by private health?"

**7. Closing CTA**
```
[One-sentence restatement of the core promise]
[CTA button]
[Phone number]
[Address(es) with Google Maps link]
[Hours]
```

### Copy rules

- Short paragraphs — 3 sentences max per paragraph, then a line break
- No section with more than 4 paragraphs without a visual break (button, image, pull-quote, or list)
- Never open with "Welcome to [business]"
- Local suburb signals in at least the hero and trust section
- AU English throughout
- Medical/legal disclaimer rules apply (see below)

### Output format

Deliver the full page copy structured by section with:
- Suggested headings (H1, H2, H3)
- Body copy per section
- CTA button text
- Notes on imagery or trust elements to include

Run humaniser on all copy before delivering the final version.

---

## Mode: AUDIT

### Inputs

- **URL** — the page to review
- **Traffic source** — how is traffic arriving?
- **Conversion goal** — what should the visitor do?
- **Current conversion rate** — if known

### What to check

Fetch the page. Go section by section:

| Section | What to look for |
|---|---|
| Above the fold | Does the H1 name the service clearly? Is there a visible CTA without scrolling? Mobile load fast? |
| Hero copy | Specific to this audience, or generic? Does the subheadline explain the benefit? |
| Social proof | Review count, rating, or specific number present? Is it near the top or buried at the bottom? |
| Problem/service copy | In the visitor's language? Or clinic/jargon language? |
| Trust signals | Credentials, volume, reviews — specific and credible, or vague? |
| CTA mechanics | How many clicks to convert? Is the phone number visible on mobile? Is the form short (3–5 fields max)? |
| Mobile experience | Does it work properly on a phone screen? |
| Local signals | Are suburb/city names in the copy? |
| Page speed | Loads in under 3 seconds? Note if not measurable directly. |

### Audit output format

```
# Landing page audit — [Business]
URL: [page]
Traffic source: [source]
Conversion goal: [action]

## Overall verdict
[1 paragraph: biggest strengths and biggest gap. What's costing them conversions?]

## Section findings

### [Section name]
Status: 🔴 / 🟡 / 🟢
Finding: [what's wrong or what's working]
Recommendation: [specific rewrite or change — not generic advice]

[Repeat for each section]

## Top 3 fixes
1. [Most impactful change — with specific rewrite if applicable]
2. [Second]
3. [Third]
```

For any section rated 🔴, include a rewritten version of the copy.

---

## Medical and professional services

**Health clients** (osteos, physios, dentists): no outcome guarantees. Never "cures", "eliminates", or "guaranteed relief". Use "may help", "commonly used to treat", "many patients report". AHPRA compliance applies.

**Legal/accounting clients**: no specific legal or tax advice on the page. General service descriptions only. Direct to a consult.

---

## Humaniser pass (always last)

Run humaniser on the full page copy before delivering. Focus on:
- Removing AI vocabulary (seamless, exceptional, dedicated, holistic)
- Breaking up sentences that all run the same length
- Making it sound like a real business wrote it for real patients/clients

Deliver the humanized version as final output.
