---
name: client-onboarding
description: Onboard a new Locate Digital client. Creates the full client workspace — folder structure, CLAUDE.md with all context, .env template, memory folder, and base settings file. Use when adding a new client, setting up a new client workspace, or when Sam says "onboard [client]", "set up [client]", or "new client". Runs a structured interview first, then creates everything in one pass. Nothing is created until the interview is complete.
---

# Client onboarding

Set up a complete client workspace for Locate Digital. One skill run = one client ready to work in.

**Output:**
```
clients/<name>/
├── CLAUDE.md                      ← full client context
├── .env                           ← API key template for active channels
├── .gitignore
├── .claude/
│   └── settings.local.json        ← base permissions
├── memory/
│   └── sessions/
├── reports/
└── [channel folders — active channels only]
    ├── meta-ads/
    ├── google-ads/
    ├── content/
    ├── landing-pages/
    └── assets/
```

---

## Step 1 — Interview

Ask all of this before creating any files. Group the questions — 3 rounds, each small enough to answer in one message. Extract anything already provided upfront and only ask for genuine gaps.

**Round 1 — Business basics**
1. Business name and folder name to use (no spaces — e.g. MOSIC, Smith-Legal, BrightSmile)
2. Industry: accountant, lawyer, physio, dentist, osteopath, salon, or other?
3. Location(s) — full address per location
4. Phone number(s) and website URL
5. Key contact name and email
6. Number of practitioners or staff (if relevant)
7. Years in business

**Round 2 — Marketing & audience**
8. Services offered — full list, then which to prioritise
9. Target audience — ideal patient/client: age range, occupation, location, what brings them in, what they care about
10. Current marketing channels (before Locate Digital) — what's already running?
11. Channels Locate Digital is taking on — new vs existing
12. Tools and CRMs in use — practice management, email platform, booking system
13. Competitors — 1 to 3 names or URLs
14. Voice and tone — any strong preferences, or TBD?
15. Primary goal — new patients/clients, retention, awareness, or a specific number target?
16. Reporting cadence — monthly or fortnightly?
17. Monthly ad spend budget (approximate is fine)

**Round 3 — Discovery & access**
18. Current monthly lead or enquiry volume (approximate — establishes the baseline)
19. Average appointment or job value ($)
20. Anything that's worked well in marketing before? Anything that's flopped?
21. Current Google review count and star rating
22. Existing assets: clinic/team photos? Video? Brand guidelines or logo files?
23. Email list size (if email is in scope)
24. Who controls access to their Google account, Meta Business Manager, and website? (Needed to request access)

If any answer is unknown, mark it TBD — don't skip the field.

---

## Step 2 — Check for existing folder

Before creating anything:
```bash
ls "G:/My Drive/Claude Code.Locate/clients/<name>" 2>/dev/null
```
If the folder exists, stop and flag it. Do not overwrite without explicit confirmation from Sam.

---

## Step 3 — Create folder structure

```bash
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/reports"
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/memory/sessions"
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/.claude"
```

Then create `memory/projects.md` with a stub entry so `/wrapup` can update it immediately:

```markdown
# Projects

## <name>

**Status:** Active
**Onboarded:** YYYY-MM-DD
**Pending:**
- Fill in TBDs from CLAUDE.md
- Send access request to [contact]
- Confirm .env credentials once access granted
```

Channel folders — only for active or in-scope channels:
```bash
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/meta-ads"       # Meta Ads
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/google-ads"      # Google Ads
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/content"         # Content creation
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/landing-pages"   # Landing pages
mkdir -p "G:/My Drive/Claude Code.Locate/clients/<name>/assets"          # Creative assets
```

---

## Step 4 — Write CLAUDE.md

Populate every field from the interview. Use TBD for unknowns — never invent values.

```markdown
# [BUSINESS NAME] — Client Context

Onboarded: [YYYY-MM-DD]

## Business
- **Industry:** [industry]
- **Locations:** [full address per location]
- **Phone:** [number(s)]
- **Website:** [URL]
- **Staff:** [practitioner/staff count]
- **Years operating:** [years or "established YYYY"]
- **Scale:** [appointments/month or client volume — from interview]
- **Key contact:** [name, email]

## Services
Primary (prioritise in all copy and campaigns):
- [service 1]
- [service 2]

Secondary:
- [service 3]
- [service 4]

## Target audience
[2–3 sentences. Specific: age, occupation, location, what brings them in, what they care about.
Example: "Male professionals 25–55 in Melbourne CBD and Essendon. Desk workers and weekend athletes
who push through pain longer than they should. They book when something stops them functioning,
not as a preventative measure. Value speed, competence, and not being talked down to."]

## Channels
| Channel | Status | Notes |
|---|---|---|
| Google Ads | [Active / Setting up / Not in scope] | [context] |
| SEO | [Active / Setting up / Not in scope] | [context] |
| Meta Ads | [Active / Setting up / Not in scope] | [context] |
| Google Business Profile | [Active / Needs work / Not in scope] | [context] |
| Email | [Active / Setting up / Not in scope] | [platform] |
| Social (organic) | [Active / Setting up / Not in scope] | [platforms] |

## Tooling & integrations
| Tool | Purpose | Status |
|---|---|---|
| [Cliniko / Halaxy / Jane / etc.] | Practice management / CRM | [API key in .env / TBD] |
| GA4 | Website analytics | [Property ID in .env / TBD] |
| Google Ads | Paid search | [Customer ID in .env / TBD] |
| Meta Business Manager | Paid social | [Ad account ID in .env / TBD] |
| [Email platform] | Email marketing | [API key in .env / TBD] |

## Baseline metrics (at onboarding — [month YYYY])
Document before touching anything. Used to prove ROI.
- Monthly new patients/clients: [~N/month]
- Monthly enquiries/leads: [~N/month]
- Average appointment/job value: [$X]
- Conversion rate (leads → bookings): [X% or TBD]
- Google reviews: [N reviews, X.X stars]
- Monthly website sessions: [N or TBD — pull from GA4 once access granted]
- Current ad spend (if any): [$X/month on [platform]]
- Current cost per lead (if known): [$X or TBD]

## Proof points
- [Years operating, e.g. "Operating since 2012"]
- [Volume, e.g. "12,000+ patients treated"]
- [Staff, e.g. "8 qualified osteopaths"]
- [Credentials, awards, affiliations — if known]

## Competitors
- [Competitor 1 — URL]
- [Competitor 2 — URL]
- [Competitor 3 — URL]

## What's worked / what hasn't
Worked: [any channels or tactics that have generated results — from client interview]
Hasn't worked: [anything they've tried that flopped — avoid repeating these]

## Existing assets
- Photos: [clinic photos / team photos / treatment photos — yes/no/TBD]
- Video: [yes/no/TBD]
- Brand guidelines: [yes/no/TBD — if yes, note location]
- Logo files: [yes/no/TBD — if yes, note location in assets/]
- Email list: [N subscribers or TBD]
- Testimonials/reviews available for use: [yes/no/TBD]

## Voice & tone
[Notes on how the client communicates. Flag TBD if not discussed — update after reviewing their
existing website copy, social posts, or email examples. Key things to capture: formal vs casual,
clinical/technical vs plain language, any phrases they use or hate.]

## Compliance & restrictions
[Industry-specific advertising rules. See compliance notes in this skill for defaults per industry.
Fill in any client-specific restrictions discussed.]

## Engagement scope
What Locate Digital is responsible for:
- [e.g. Google Ads management]
- [e.g. Monthly performance report]
- [e.g. Fortnightly content: blog + GMB]

Not in scope (to prevent scope creep):
- [e.g. Website development]
- [e.g. Email campaign copywriting]

## Account access
| Platform | Access granted | Notes |
|---|---|---|
| Google Analytics 4 | [Yes / Pending / Not needed] | |
| Google Ads | [Yes / Pending / Not needed] | |
| Meta Business Manager | [Yes / Pending / Not needed] | |
| Google Business Profile | [Yes / Pending / Not needed] | |
| [CRM] | [Yes / Pending / Not needed] | |
| Website / CMS | [Yes / Pending / Not needed] | |

## Reporting
- Cadence: [monthly / fortnightly]
- Format: [HTML + PPTX / doc / TBD]
- Output path: `reports/YYYY-MM/`
- Sent to: [contact name, email]

## Goals
[1–2 sentences with a specific target where possible.
Example: "Grow new patient volume from ~48/month to 70+/month within 6 months via Google Ads
optimisation and SEO improvements. Secondary: reduce cost per new patient below 60 dollars."]

## Notes
- API keys and credentials in `.env` (gitignored)
- [Any other context]
```

---

## Step 5 — Write .env template

Only include sections for active or planned channels. Comment out tools not yet in use.

```bash
# ── Google (GA4 + Google Ads) ───────────────────────────────────────────────
GA4_PROPERTY_ID=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_REFRESH_TOKEN=

# Google Ads (activate when customer ID confirmed):
GOOGLE_ADS_DEVELOPER_TOKEN=
GOOGLE_ADS_CUSTOMER_ID=

# ── Meta Ads ────────────────────────────────────────────────────────────────
META_ACCESS_TOKEN=
META_AD_ACCOUNT_ID=
META_PIXEL_ID=

# ── Practice management CRM ─────────────────────────────────────────────────
# Cliniko:
CLINIKO_API_KEY=
CLINIKO_SHARD=
# Halaxy: HALAXY_API_KEY=
# Jane: JANE_API_KEY=

# ── Email ───────────────────────────────────────────────────────────────────
# Mailchimp: MAILCHIMP_API_KEY= / MAILCHIMP_AUDIENCE_ID=
# Klaviyo:   KLAVIYO_API_KEY=
```

---

## Step 6 — Write .gitignore

```
.env
*.env
.env.*
```

---

## Step 7 — Write settings.local.json

Replace `[CLIENT-DOMAIN]` with the actual domain (e.g. `melbourneosteopathycentre.com.au`).

```json
{
  "permissions": {
    "allow": [
      "Bash(python *)",
      "Bash(PYTHONIOENCODING=utf-8 python *)",
      "WebFetch(domain:[CLIENT-DOMAIN])",
      "WebSearch",
      "Skill(startup)",
      "Skill(wrapup)",
      "PowerShell(Start-Process *)",
      "Read(//g/My Drive/Claude Code.Locate/_brand/**)"
    ]
  }
}
```

---

## Step 8 — Compliance notes by industry

Add the relevant block to the CLAUDE.md compliance section.

**Health (osteopath, physio, dentist, GP, psychologist)**
AHPRA advertising guidelines apply. Key rules:
- No testimonials that reference a clinical outcome ("fixed my back", "cured my pain")
- No before/after clinical comparisons
- No "best", "leading", "most experienced" claims without substantiation
- No outcome guarantees ("will fix", "eliminates", "cures")
- Approved language: "may help", "commonly used to treat", "many patients find", "our practitioners treat"
- Pricing claims must be accurate and include all mandatory fees (e.g. initial consult vs follow-up)

**Legal**
Legal Services Council advertising rules apply:
- No "best", "leading", "expert" without substantiation
- No misleading cost claims or "no win no fee" without full conditions
- Must not create unrealistic expectations of outcome
- Victoria: Legal Profession Uniform Law applies

**Accounting / financial planning**
ASIC advertising standards and Australian Financial Services licence obligations:
- No implied financial advice in general marketing
- "General information only — not financial advice" disclaimer on any content that could be construed as advice
- No specific return or outcome promises

**Salon / beauty / aesthetics**
TGA advertising code if any treatments involve therapeutic devices or claims:
- No therapeutic claims for cosmetic treatments unless TGA-approved
- "Results may vary" required on before/after imagery

**All clients — Privacy Act**
Australian Privacy Principles (APPs) apply to any client data used in reporting:
- Don't include identifiable patient/client data in reports
- Aggregated/anonymised data only in dashboards and month reports
- API integrations must comply with the client's privacy policy

---

## Step 9 — Access request

After creating files, produce a short access request summary Sam can send or read out to the client:

```
Hi [contact],

To get started, we'll need access to the following accounts:

□ Google Analytics 4 — add sam@locatedigital.io as Editor
□ Google Ads — we'll share our MCC account ID for you to link (or add sam@locatedigital.io as Admin)
□ Meta Business Manager — add sam@locatedigital.io as Admin on the Ad Account and Pixel
□ Google Business Profile — add sam@locatedigital.io as Manager
□ [CRM] — API key or read-only user access
□ Website / CMS — [developer contact or login details for relevant section]

Once these are granted, we can pull your baseline numbers and get the first report set up.
```

Only include platforms relevant to the engagement scope.

---

## Step 10 — Confirmation summary

```
✓ Client onboarded: [Business name]
  Folder: clients/<name>/

Files created:
  ✓ CLAUDE.md
  ✓ .env (template — fill in API keys before running data scripts)
  ✓ .gitignore
  ✓ .claude/settings.local.json
  ✓ memory/sessions/
  ✓ reports/
  [✓ meta-ads/ / google-ads/ / content/ / landing-pages/ / assets/]

TBDs to resolve:
  — [Fields marked TBD in CLAUDE.md]
  — [.env sections needing API keys]
  — [Access requests outstanding]

Compliance flag: [industry — e.g. "AHPRA rules apply — see CLAUDE.md compliance section"]

Quick wins to tackle in session 1:
  [Based on the interview, identify 2–3 immediate opportunities. Examples:]
  — Google Business Profile incomplete or not actively managed → high-impact, low-effort fix
  — No conversion tracking on existing Google Ads → fix before next spend
  — Meta Pixel not installed → install before any Meta campaign planning
  — Review count low → set up a review request process
  — No dedicated landing pages for paid traffic → identify highest-value service to build first
  — Existing ads running with no negative keywords → audit for wasted spend

Next steps:
  1. Send access request to [contact name]
  2. Fill in .env once access is granted
  3. Pull baseline metrics (GA4, Google Ads, GBP)
  4. Run /startup from clients/<name>/ to confirm context loads
```

---

## Rules

- Never create files until the interview is complete
- Never invent values — TBD for anything unknown
- Never store actual credentials in the skill output — .env is always a template
- If a client folder already exists at the path, stop before overwriting anything
- Folder names: no spaces, use abbreviation or CamelCase (MOSIC, SmithLegal, BrightSmile)
- Quick wins must be based on what was actually learned in the interview — don't list generic items that don't apply
