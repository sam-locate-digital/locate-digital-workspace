---
name: seo-audit
description: Run a local SEO audit for a service business website. Use when asked to audit SEO, review a website's search performance, check local SEO, assess a Google Business Profile, diagnose poor local rankings, or produce an SEO report for a client. Outputs a structured audit report with prioritised recommendations. Covers technical SEO, on-page, local signals, and Google Business Profile.
---

# SEO audit — local service businesses

Audit a service business website for local search performance. Outputs a structured, priority-ranked report with specific fixes.

Focused on **local service businesses** — those that depend on suburb-based and "near me" search to generate enquiries. Not e-commerce. Not national brands.

## Client context (read first)

Read the client's `CLAUDE.md` from `clients/<name>/CLAUDE.md`. Pull:
- Business name, website URL, locations/suburbs
- Target services and any known keywords
- Active channels (is SEO listed?)
- Known SEO history or issues

If no client is specified, ask which client this is for.

## Inputs (ask only if missing)

- **Website URL** — homepage or specific page to audit
- **Target location** — which suburb(s) or city should rank?
- **Primary service** — what are they trying to rank for?
- **Competitors** — any known sites outranking them? (optional but useful)

## Priority key

🔴 High — direct ranking or lead gen impact, fix first
🟡 Medium — meaningful improvement, fix next sprint
🟢 Low — quick win or minor polish

---

## Audit areas

### 1. Google Business Profile

Highest local SEO impact. Always check this first.

| Item | What to assess |
|---|---|
| Claimed and verified | Is the profile live and actively managed? |
| Business categories | Primary category accurate? Secondary categories added? |
| Business name | Exact match to real name — no keyword stuffing in the name field |
| Address | Formatted correctly, matches website exactly |
| Phone number | Local number present (not 1300 only) |
| Website URL | Points to the right page |
| Business description | Uses target keywords naturally, no promotional language or links |
| Photos | 10+ photos, at least some updated within 6 months |
| Reviews | Volume, recency, are owner responses active? |
| Google Posts | Active? Last post within 2 weeks? |
| Products/Services | Listed with descriptions? |
| Q&A | Seeded with common patient/client questions? |
| Opening hours | Accurate, holiday hours configured? |

### 2. On-page SEO

Check homepage and key service pages.

| Item | What to assess |
|---|---|
| Title tag | 50–60 chars, primary keyword + location + brand |
| Meta description | 150–160 chars, keyword, local signal, click hook |
| H1 | One per page, includes primary keyword |
| H2 structure | Logical hierarchy, secondary keywords present |
| Content depth | Does the page answer what the searcher actually wants? |
| Local signals | Is the target suburb/city mentioned naturally in body copy? |
| Internal links | Are service pages linked from homepage and each other? |
| Image alt text | Keyword-relevant, not "image1.jpg" |
| Schema markup | LocalBusiness schema present? |
| URL slugs | Clean, keyword-relevant, no auto-generated IDs |

Check: are there **separate pages per service** and **separate pages per location** if multi-location? Both are high-value for local service businesses.

### 3. Technical SEO

| Item | What to assess |
|---|---|
| Mobile usability | Passes Google mobile-friendly test |
| Page speed | Core Web Vitals: LCP < 2.5s, CLS < 0.1, INP < 200ms |
| HTTPS | Site loads on https:// |
| Indexing | Is the homepage indexed? (`site:domain.com.au` in Google) |
| Redirects | www → non-www (or vice versa)? HTTP → HTTPS? Both consistent? |
| robots.txt | Not blocking important pages (`domain.com.au/robots.txt`) |
| XML sitemap | Exists and submitted to Search Console (`domain.com.au/sitemap.xml`) |
| Broken links | Internal 404s on key pages |
| Canonical tags | Self-referencing canonicals on service and location pages |

### 4. Local signals

| Item | What to assess |
|---|---|
| NAP consistency | Name, Address, Phone identical across website, GBP, and directories |
| Local citations | Listed on True Local, Yellow Pages, HealthEngine (health clients), Yelp AU |
| Location pages | Separate pages for each suburb/location if multi-location |
| Suburb mentions | Are target suburbs mentioned naturally throughout content? |
| Testimonials on site | Are Google reviews or patient quotes embedded on the website? |
| Google Maps embed | Is a map on the contact or location page? |

---

## Output format

```
# SEO audit — [Business name]
Audited: [Date]
Website: [URL]
Target location: [Suburb / city]
Primary service: [What they're trying to rank for]

---

## Priority findings

🔴 HIGH PRIORITY
[Issue → Impact → Specific fix]

🟡 MEDIUM PRIORITY
[Issue → Impact → Specific fix]

🟢 LOW PRIORITY / QUICK WINS
[Issue → Fix (brief)]

---

## Section breakdown

### Google Business Profile
[Findings per checklist item — note status and specific recommendation]

### On-page SEO
[Key pages checked, findings per item]

### Technical SEO
[Findings from technical checklist]

### Local signals
[Findings from local checklist]

---

## Top 3 actions (do these first)

1. [Most impactful fix — specific and actionable, not generic]
2. [Second most impactful]
3. [Third]

---

## Notes
[Caveats, items needing Search Console access, things to investigate further]
```

## What you can check without tools

- Fetch the URL: check title tag, meta description, H1, body copy, schema (view source)
- Google search `site:domain.com.au` — checks indexing
- Check `domain.com.au/robots.txt` and `domain.com.au/sitemap.xml` directly
- Check Google Business Profile via Google Maps search
- Core Web Vitals: note if Search Console access is needed; or reference PageSpeed Insights URL

## Keep every finding actionable

Never list "title tag too long" without showing what it should say. Never note "no schema" without specifying which schema type and the key fields to populate. A finding without a fix is just a problem list.
