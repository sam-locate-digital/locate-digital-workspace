---
name: ram-precinct-post
description: Create Instagram posts for RAM's retail precincts (ASX:REP shopping centres). Use when asked to write a precinct post, RAM social content, shopping centre Instagram post, retailer spotlight, or to batch a month of precinct content. Outputs caption + hashtags + visual direction + Canva template to use, per precinct and content pillar. Local community voice, Australian English, humanizer always on.
---

# RAM precinct post — Instagram content

Create Instagram posts for the **7 retail precincts** under RAM's REIT (ASX: REP). Each precinct is a supermarket-anchored neighbourhood shopping centre with its own **local community voice and brand**. Posts are warm, local, shopper-first — never corporate or investor-facing.

**Platform:** Instagram (feed + Stories direction). **Cadence:** 2–3 posts/week per precinct.

## Step 1 — Read the context (always do this first)

1. `clients/RAM/CLAUDE.md` — engagement, voice rules, the 7 precincts.
2. `clients/RAM/precincts/<precinct>.md` — the specific precinct brief: name, suburb, anchor tenant, retailers, handle, brand colours, local events, parking, hours. **If this file doesn't exist yet, ask Sam to fill the `_TEMPLATE.md` for that precinct first.**
3. Run the `humanizer` skill on every caption before delivery.

Never write a precinct post without its brief. Local specifics (real retailer names, real suburb, real events) are what make these work.

## Step 2 — Pick the content pillar

Every post maps to one of 8 pillars. Rotate them so a precinct's feed has variety. (Calendar in `clients/RAM/sop/`.)

| # | Pillar | What it is | Example |
|---|--------|------------|---------|
| 1 | **Retailer spotlight** | Feature one store/brand in the centre | "Meet [Store] — your go-to for [thing]" |
| 2 | **Food & dining** | Cafes, eateries, fresh food (high IG engagement) | "Coffee run sorted at [Cafe]" |
| 3 | **Offers & deals** | Current promos, sales, value | "On now: [offer] at [store]" |
| 4 | **What's on / events** | Activations, school holidays, community days | "School holiday fun at [Precinct] these [dates]" |
| 5 | **Seasonal moment** | Calendar hooks (Easter, Mother's Day, Christmas, EOFY) | "Sorted for [occasion] at [Precinct]" |
| 6 | **Community & lifestyle** | Local vibe, "your local", people | "Your weekend starts here" |
| 7 | **New & noteworthy** | New tenant, new product, centre news | "Now open: [new store]" |
| 8 | **Convenience & services** | Hours, parking, one-stop, services (chemist, post, banking) | "Everything in one stop — [list]" |

**Default weekly mix (2–3 posts):** one spotlight (pillar 1 or 2), one timely (3, 4 or 5), and if 3rd post, one brand/community (6, 7 or 8).

## Step 3 — Write the post

For each post, output **all four** of these:

### A. Caption
- **Hook first line** — stop the scroll. Specific and local, not generic.
- **2–4 short lines** of body. Plain, warm, Australian. Talk like a friendly local, not a property fund.
- **One clear CTA** — visit, tag a mate, swipe up/link, see you there, check the offer.
- Length: 50–125 words. Instagram rewards tight.
- Emoji: light and natural (1–4), never a wall of them.

### B. Hashtags
- 8–15 total. Mix of:
  - **Local geo** — #<suburb>, #<region>, #<city>shopping, #<suburb>local
  - **Centre brand** — the precinct's own tag
  - **Category** — #shoplocal #supportlocal #[retailtype]
  - **Anchor/seasonal** where relevant
- Put them in a comment-ready block or end of caption per the precinct's convention.

### C. Visual direction
- What the image/Story should show (real photo > stock where possible).
- Shot ideas: storefront, product flatlay, food close-up, people enjoying the space, seasonal styling.
- Note if it's a single image, carousel (and how many frames), or a Reel idea.

### D. Canva template to use
- Name the master template + which precinct skin (e.g. "Template: Retailer Spotlight · Skin: [Precinct]").
- Note the editable fields (headline, store name, photo, offer text, logo).
- See `clients/RAM/sop/post-templates-showcase.html` for the template set.

## Step 4 — Brand & voice rules (non-negotiable)

- **Each precinct sounds local**, like the centre down the road, not a national chain or a REIT.
- **Australian English** always (centre not center, mum not mom, car park not parking lot).
- **Plain and warm.** No corporate-speak ("activation", "asset", "precinct" rarely — call it "the centre" or its name).
- **Humanizer always on** — no AI tells (no "nestled", "vibrant", "elevate your shopping experience", forced rule-of-three, em-dash overuse).
- **Never investor/financial content** — REP unit price, distributions, the fund = RAM's corporate channel, not this. Keep it shopper-facing.
- **No claims you can't back** — don't invent offers, store names, or events. Use the brief, or flag a gap.
- **Respect retailer relationships** — spotlight tone is celebratory; check the brief for any sensitivities.

## Step 5 — Batch mode (for the monthly SOP)

When asked to batch a month for a precinct (or all 7):
1. Pull the content calendar in `clients/RAM/sop/`.
2. For each slot, generate A–D above.
3. Output organised by precinct → week → post, ready to drop into the calendar and Canva.
4. Save to `clients/RAM/content/<precinct>/<YYYY-MM>/`.
5. Flag any slot where the brief lacks the specifics needed (e.g. "no current offer supplied for [Precinct] week 2").

## Output format

```
PRECINCT: [name] · PILLAR: [#/name] · DATE: [date] · PLATFORM: Instagram

CAPTION:
[hook line]
[body]
[CTA]

HASHTAGS:
[8–15 tags]

VISUAL:
[direction + format]

CANVA:
Template: [name] · Skin: [precinct] · Edit: [fields]
```

Run humanizer, then deliver.
