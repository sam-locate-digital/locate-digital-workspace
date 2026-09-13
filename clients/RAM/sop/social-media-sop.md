# RAM precincts — social media SOP

The repeatable process for running Instagram across all 7 retail precincts. Built to be **batched monthly**, so you produce a full month for every centre in one focused sitting instead of scrambling daily.

- **Platform:** Instagram (feed + Stories)
- **Cadence:** 2–3 posts per precinct per week (~14–21/week, ~60–90/month total)
- **Voice:** each precinct as its own local community brand (see `clients/RAM/CLAUDE.md`)
- **Tools:** `ram-precinct-post` skill (copy) · Canva brand templates (design) · a scheduler (Meta Business Suite / Later / Metricool) for publishing

---

## The monthly rhythm (the whole loop)

Run this once a month. Aim to have next month fully built and approved before the 1st.

### Week before month start

**1. Gather inputs (by the 20th).**
For each precinct, collect from the centre manager / RAM contact:
- Current and upcoming offers/promos
- Events / school-holiday activities / activations
- New tenants, store news, trading-hour changes
- Fresh photos (storefronts, food, events)

Chase anything missing. The brief in `clients/RAM/precincts/<precinct>.md` lists who supplies what.

**2. Plan the calendar (1–2 hrs).**
Open `clients/RAM/sop/content-calendar.xlsx`. For each precinct, fill the month's slots using the pillar rotation (below). Slot the timely stuff (offers, events, seasonal) to real dates first, then fill gaps with evergreen (spotlights, community, convenience).

**3. Generate the copy (batch — 1–2 hrs).**
Run the `ram-precinct-post` skill in batch mode: "Batch [Month] for [precinct]" (or all 7). It outputs caption + hashtags + visual direction + which Canva template, per slot. Saves to `clients/RAM/content/<precinct>/<YYYY-MM>/`.

**4. Design the graphics (2–3 hrs).**
In Canva, open the master template set. For each post, duplicate the right template, apply the precinct skin, drop in the photo + text from the generated brief. Export at 1080×1080 (feed) / 1080×1920 (Stories).

**5. Approval.**
Send the month's posts (copy + visuals) to the RAM/centre approver. One batch, one round of edits. Lock it.

**6. Schedule.**
Load everything into the scheduler, set dates/times, queue Stories. Done for the month.

### Through the month
- **Reactive posts** — react to anything live (a flash sale, weather, a viral local moment) outside the batch. Keep it light.
- **Engagement** — reply to comments/DMs, like local tags, repost shopper content (with permission). 15 min/precinct/week.
- **Stories** — lighter, more frequent: behind-the-scenes, polls, repost retailer content, "what's on today".

---

## Pillar rotation (keeps each feed varied)

Eight pillars (full detail in the `ram-precinct-post` skill). A simple weekly pattern at 3 posts/week:

| Post | Lean | Pull from pillars |
|------|------|-------------------|
| **Post 1** | Spotlight | Retailer spotlight · Food & dining |
| **Post 2** | Timely | Offers · What's on · Seasonal |
| **Post 3** | Brand/community | Community & lifestyle · New & noteworthy · Convenience |

At 2 posts/week, run Post 1 + Post 2 and rotate Post 3 in every other week.

Across a month, every precinct should hit: spotlights, food, at least one offer, one event/seasonal, and one community/convenience. Don't repeat the same pillar back to back.

---

## Roles & responsibilities

| Who | Does |
|-----|------|
| **You (Locate)** | Calendar, copy, design, scheduling, engagement, monthly report |
| **RAM / centre managers** | Supply offers, events, store news, photos; approve the monthly batch |
| **Retailers** | Source material for spotlights (via centre managers) |

---

## Quality bar (check before approval)

- [ ] Sounds local and warm, not corporate. Australian English.
- [ ] Real store names, real offers, real dates — nothing invented.
- [ ] Humanizer run — no AI tells.
- [ ] One clear CTA per post.
- [ ] On-brand Canva template, correct precinct skin, photo looks good on a phone.
- [ ] No investor/financial content (that's REP's corporate channel).
- [ ] Hashtags: local + brand + category, 8–15.

---

## Monthly reporting (to RAM)

Once a month, a simple report per precinct: posts published, reach/impressions, engagement rate, follower growth, top post. Use `_skills/monthly-report/` as the base. Keep it plain — what worked, what's next.

---

## Files

- Precinct briefs: `clients/RAM/precincts/<precinct>.md` (one per centre)
- Content calendar: `clients/RAM/sop/content-calendar.xlsx`
- Post template designs: `clients/RAM/sop/post-templates-showcase.html`
- Generated content: `clients/RAM/content/<precinct>/<YYYY-MM>/`
- The skill: `ram-precinct-post` (in `~/.claude/skills/`)
