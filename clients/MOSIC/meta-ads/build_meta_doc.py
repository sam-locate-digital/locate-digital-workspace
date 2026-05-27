from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "mosic-meta-ads-2026-05.docx")

# ── Colours ────────────────────────────────────────────────────────────────────
BLUE   = RGBColor(0x00, 0x7a, 0xe8)
INK    = RGBColor(0x0d, 0x0d, 0x0d)
MUTED  = RGBColor(0x63, 0x66, 0x6b)
RED_HL = RGBColor(0xd4, 0x1c, 0x1c)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GREEN  = RGBColor(0x00, 0x7a, 0x3a)
AMBER  = RGBColor(0xd4, 0x7a, 0x1c)

# ── Data ───────────────────────────────────────────────────────────────────────

AUDIENCES = [
    # (type, name, targeting_detail, reasoning)
    ("Cold",
     "Health & Pain seekers",
     "Interests: back pain, neck pain, osteopathy, physiotherapy, chiropractic, pain management, sports medicine\nAge: 25–55  |  Gender: All  |  Radius: 15 km from Bourke St + 15 km from Essendon",
     "People already signalling health pain awareness in their Facebook/Instagram activity. These interests show intent without being in-market searchers — they engage with health content, follow clinics, or interact with pain-related pages. Strongest cold audience for a clinic."),
    ("Cold",
     "Active & Sport",
     "Interests: running, marathon running, gym, CrossFit, AFL football, injury prevention, health & fitness\nAge: 25–55  |  Gender: All  |  Radius: 15 km from Bourke St + 15 km from Essendon",
     "MOSIC explicitly treats running injuries and sports injuries. This audience is active, health-conscious, and experiences the exact injuries MOSIC treats. Separating it from the health audience lets you test different ad angles — this one leads with sport outcomes, not pain."),
    ("Cold",
     "CBD Professionals",
     "Interests: corporate wellness, workplace health, desk ergonomics OR Job titles: manager, director, professional, executive\nAge: 28–55  |  Location: Melbourne CBD (tighter 5 km radius from Bourke St)\nBehaviour: Commuters, frequent travellers",
     "MOSIC's Bourke St clinic targets desk workers and CBD commuters directly. This audience skews higher income, is time-poor, and values same-week availability — messaging should emphasise convenience and fast outcomes, not price. Narrowing to CBD radius keeps geo precise."),
    ("Cold",
     "Lookalike 1% — Website visitors",
     "Lookalike audience based on website visitors pixel data\n1% similarity  |  Australia  |  Min. 100 seed audience required before activating",
     "A lookalike tells Meta to find people who behave like your existing website visitors. 1% is the tightest match — highest quality. Do NOT activate until the pixel has recorded 100+ website visitors (ideally 500+). Too small a seed produces low-quality lookalikes. Queue this audience now; activate at 30-day mark if pixel volume is sufficient."),

    ("Warm",
     "Website visitors — all pages",
     "Custom audience: website visitors (all pages)\nLookback: 30 days  |  Exclude: existing patients (if email list available)",
     "People who visited the website but didn't book are warm — they know MOSIC exists and had enough interest to click through. 30-day window keeps the list fresh; older visitors have lower conversion probability. Retargeting copy should acknowledge they've been before: 'Still thinking about it?' rather than a cold introduction."),
    ("Warm",
     "Booking page visitors",
     "Custom audience: visited /book-online or /appointments URL\nLookback: 14 days  |  Exclude: confirmed bookings (conversion event)",
     "These people reached the booking page but didn't complete. Highest intent of any warm audience — they got close. 14-day window only because intent fades fast. Ad copy should reduce friction: 'Book takes under 2 minutes' or 'Call us instead on 03 9663 6202'. Exclude anyone who fired the booking confirmation pixel event."),
    ("Warm",
     "Video viewers — 50%+",
     "Custom audience: people who watched 50% or more of any MOSIC video ad\nLookback: 30 days",
     "Watching more than half a video is a strong engagement signal on Meta — average watch-through is under 15%. These people are curious and receptive. Retargeting them with a direct offer (book now, specific service) converts well because you've already done the awareness work. Build this audience from day one even if you don't activate the retargeting campaign immediately."),
    ("Warm",
     "Page engagers",
     "Custom audience: people who engaged with MOSIC Facebook or Instagram page\nLookback: 60 days  |  Includes: likes, comments, shares, profile visits, message senders",
     "Anyone who interacted with MOSIC's social content in the last 60 days. Lower intent than website visitors but warmer than cold. Good for keeping MOSIC top of mind with a follow-up educational post or seasonal angle. 60-day window gives enough volume at a local scale."),
]

VARIANTS = [
    {
        "number": 1,
        "angle": "Social proof — establish scale and local presence",
        "audience": "Cold: Health & Pain seekers, Active & Sport",
        "objective": "Traffic (to landing page) or Lead Gen",
        "primary_text": (
            "12,000 patients. 8 practitioners. Clinics in Bourke St CBD and Essendon. "
            "MOSIC is where Melbourne professionals come when they're done pushing through pain "
            "and want someone to actually fix it."
        ),
        "headline": "MOSIC Melbourne Osteopath",
        "description": "CBD & Essendon clinics",
        "cta": "Learn More",
        "visual": (
            "A practitioner's hands working on a patient's upper back in a clean, warm treatment room. "
            "Patient looks relaxed. Natural window light. No clinical equipment visible — "
            "approachable, not medical."
        ),
        "reasoning": (
            "Cold audiences need a reason to trust before they'll click. "
            "Leading with volume (12,000 patients) and specificity (two named clinics) signals "
            "legitimacy without making claims. 'Done pushing through pain' mirrors exactly how "
            "MOSIC's target — the stoic CBD professional — describes their situation to themselves. "
            "'Learn More' CTA keeps it low-commitment for a first exposure."
        ),
    },
    {
        "number": 2,
        "angle": "Problem/interest hook — desk workers",
        "audience": "Cold: CBD Professionals, Health & Pain seekers",
        "objective": "Traffic or Lead Gen",
        "primary_text": (
            "Your body wasn't built for eight hours at a desk. "
            "Most back and neck pain that CBD workers deal with isn't bad luck. "
            "It's the chair, the screen height, and the commute. "
            "MOSIC looks at what's driving it, not just where it hurts."
        ),
        "headline": "Osteopath in Melbourne CBD",
        "description": "Bourke St & Essendon clinics",
        "cta": "Book Now",
        "visual": (
            "A Melbourne professional at a standing desk, slightly hunched, visible tension in "
            "shoulders. City office or glass building in the background. Real and relatable — "
            "not a posed stock photo. No MOSIC branding needed in the image itself."
        ),
        "reasoning": (
            "The CBD Professional audience is highly specific — they sit at desks, they commute, "
            "they recognise themselves in this copy immediately. 'Not bad luck' reframes their "
            "existing belief (I just have a bad back) into something treatable, which is the "
            "mental shift needed before booking. 'Book Now' CTA works here because the pain "
            "point is active and the audience is local."
        ),
    },
    {
        "number": 3,
        "angle": "Seasonal — AFL + winter timing",
        "audience": "Cold: Active & Sport, Health & Pain seekers",
        "objective": "Traffic or Lead Gen",
        "primary_text": (
            "AFL season, cold mornings, long weeks at the desk. "
            "Every winter we see the same thing at our Bourke St and Essendon clinics. "
            "Runners, gym regulars, and CBD workers who've been putting something off a bit too long."
        ),
        "headline": "MOSIC — Sports & Desk Pain",
        "description": "CBD & Essendon. Book online.",
        "cta": "Book Now",
        "visual": (
            "Someone running along the Yarra in early-morning winter light — overcast, "
            "active wear, Melbourne recognisable in the background. "
            "Alternatively: a footballer strapping their knee on the sideline. "
            "Seasonal and local — should feel like it was shot in Melbourne this week."
        ),
        "reasoning": (
            "Seasonal relevance improves CTR on Meta because it signals the ad was written for "
            "right now, not six months ago. Late May to July is MOSIC's natural peak for sports "
            "injuries and cold-weather desk pain — this ad runs into that demand rather than "
            "trying to create it. 'We see the same thing' positions MOSIC as experienced and "
            "knowing, not salesy."
        ),
    },
    {
        "number": 4,
        "angle": "Retargeting — warm non-converters",
        "audience": "Warm: website visitors + booking page visitors (did not convert)",
        "objective": "Lead Gen / Traffic",
        "primary_text": (
            "Still thinking about it? "
            "Most people wait longer than they should before booking. "
            "Same-week appointments available at our Bourke St CBD and Essendon clinics. "
            "Book online in under 2 minutes or call 03 9663 6202."
        ),
        "headline": "Same-Week Appointments",
        "description": "Book in under 2 minutes.",
        "cta": "Book Now",
        "visual": (
            "Clean, warm clinic interior — reception desk or treatment room. "
            "Welcoming, not clinical. Reinforce that this is a real local business. "
            "Could use a practitioner portrait shot to add a human face."
        ),
        "reasoning": (
            "Retargeting copy should acknowledge proximity to action without being creepy. "
            "'Still thinking about it?' mirrors internal dialogue without saying 'we saw you on "
            "our website'. Removing friction (2 minutes, phone option) addresses the most common "
            "drop-off reason — the booking process feeling like effort. This variant should only "
            "serve to warm audiences; showing it to cold audiences breaks the context."
        ),
    },
]

BIDDING = [
    ("Phase 1 — First 30–60 days",
     "Lowest cost (no bid cap)\nBudget: $30–50/day campaign level (CBO)",
     "Meta's algorithm needs time to exit the learning phase — typically 50 optimisation events per ad set per week. Setting a cost cap too early restricts delivery before the algorithm understands who converts. Lowest cost lets Meta spend freely to gather signal. CBO (Campaign Budget Optimisation) at campaign level lets Meta shift budget toward whichever ad set is performing best, rather than distributing it equally across underperformers."),
    ("Phase 2 — After learning phase (week 3–6)",
     "Cost per result goal\nSet at 20% above observed CPL",
     "Once you have consistent CPL data (cost per lead or cost per click), set a Cost Per Result Goal at 10–20% above your actual observed number. This gives Meta room to find conversions without cutting delivery. For a local osteopath in Melbourne, expect CPL of $15–40 for Lead Gen campaigns (instant form) or $40–80 for Traffic to landing page. Adjust based on actual data — these are benchmarks, not targets."),
    ("Phase 3 — Mature campaigns (month 3+)",
     "Cost cap at target CPL\nSeparate retargeting budget: $10–15/day",
     "Once conversion volume is consistent, a cost cap enforces your CPL ceiling strictly. Set it at your maximum acceptable CPL — Meta will slow delivery if it can't hit it. By month 3, split budget: majority to cold prospecting (acquisition), smaller dedicated budget to warm/retargeting. Retargeting audiences are small at local scale but convert at 2–4x the rate of cold, so even $10/day drives meaningful bookings."),
]

CAMPAIGN_SETTINGS = [
    ("Campaign objective",
     "Leads (instant form) for simplicity\nOR Traffic to dedicated landing page",
     "Leads objective with Meta's instant form reduces friction — users fill in name, phone, and condition without leaving the app. Converts well at local scale. Downside: lead quality can vary (some people submit without real intent). Traffic to a landing page produces fewer but higher-intent leads because the extra click filters out low-commitment users. Recommend starting with Leads for volume, switching to Traffic once you know MOSIC's follow-up capacity."),
    ("Campaign structure",
     "Campaign 1: Cold prospecting (3 ad sets, 3–4 ads each)\nCampaign 2: Retargeting (activate at day 30+)",
     "Keep cold and warm audiences in separate campaigns — they need different budgets, frequency caps, and creative. Mixing them in one campaign causes Meta to favour the cheaper-to-reach warm audience at the expense of prospecting reach. Three ad sets in cold (Health/Pain, Active/Sport, CBD Professional) lets you see which audience converts best before scaling. Don't launch the retargeting campaign until warm audiences are large enough (500+ people per ad set)."),
    ("Ad set budget vs campaign budget",
     "CBO (Campaign Budget Optimisation) — set at campaign level",
     "CBO lets Meta allocate budget dynamically across ad sets based on real-time performance signals. Manual ad set budgets (ABO) force equal or fixed spend regardless of which ad set is actually working. For a new account with no prior data, CBO is safer — Meta finds the path of least resistance while you gather data. Switch individual ad sets to ABO later if you need to lock in minimum spend on a specific audience."),
    ("Placements",
     "Advantage+ placements (recommended for month 1)\nManual month 2+: Facebook Feed, Instagram Feed, Stories, Reels — exclude Audience Network",
     "Advantage+ (formerly automatic placements) lets Meta test across all surfaces and optimise toward your cheapest conversions. For a new account this usually outperforms manual selection. After 30 days, review the placement breakdown report — Audience Network (third-party apps and websites) typically delivers cheap but low-quality traffic for local services. Remove it once you have data confirming this."),
    ("Geography",
     "Radius: 15 km from 140 Bourke St, Melbourne CBD\nRadius: 15 km from 320 Keilor Rd, Essendon\nExclude: areas clearly outside patient catchment (Mornington Peninsula, Geelong)",
     "15 km radius covers the realistic travel distance for a patient booking with a Melbourne clinic — covers CBD, inner suburbs, and the Essendon catchment. Meta's geo works on device location, not billing address, so it will catch people who are physically near the clinic even if they live slightly further away. Exclusions prevent spending on people 60+ km away who will never make the trip."),
    ("Age & gender",
     "Age: 25–55  |  Gender: All\nException: CBD Professional ad set — tighten to 28–52",
     "MOSIC's target is male professionals 25–55 but locking to male-only misses female desk workers and athletes who also book. Keep gender open and let performance data guide any narrowing — if one gender converts at half the rate after 60 days, then consider adjustment. The 25–55 range excludes teenagers (low booking intent) and seniors (different service expectations)."),
    ("Ad schedule",
     "Run all hours (Meta optimises delivery timing)\nException: retargeting ads — pause 11pm–6am",
     "Meta's delivery algorithm already shifts spend toward the hours your audience is most likely to engage — suppressing hours yourself overrides this and can hurt performance. The exception is retargeting: showing 'Still thinking about it?' to someone at 2am feels aggressive. Scheduling retargeting ads during waking hours (7am–10pm) keeps the tone right."),
    ("Pixel & conversion events",
     "Must install BEFORE launch:\n1. PageView (all pages)\n2. ViewContent (service/treatment pages)\n3. InitiateCheckout (booking page load)\n4. Lead / Purchase (booking confirmation page)",
     "The pixel is the foundation of everything — without it, Meta cannot optimise toward conversions, lookalike audiences have no seed data, and retargeting audiences don't build. Install via Meta Business Suite → Events Manager → Add Pixel, then verify events are firing in the Pixel Helper Chrome extension. The booking confirmation page event (Lead or Purchase) is the most critical: this is what tells Meta which users actually became patients, which is what Smart Bidding optimises toward."),
    ("Frequency cap",
     "Cold: 2–3 impressions per person per week\nRetargeting: 5–7 per week",
     "Frequency (how many times the same person sees your ad) is the hidden performance killer on Meta. Cold audiences become 'ad blind' and develop negative sentiment after 3–4 exposures to the same creative. Keep cold frequency under 3/week and rotate creative every 3–4 weeks. Retargeting audiences are smaller so frequency naturally rises — 5–7/week is acceptable because the intent is higher and the exposure window is shorter."),
    ("Creative refresh cadence",
     "Refresh cold creative every 3–4 weeks\nRefresh retargeting creative every 6–8 weeks",
     "Meta's ad fatigue is real and fast at local scale — a small geo means the same people see your ads repeatedly. Watch the 'Frequency' column in Ads Manager; when it crosses 3.0 on cold audiences, swap the primary text or image. Retargeting audiences are smaller so fatigue is slower, but the copy still needs updating quarterly. Keep 2–3 creative variants active at once so Meta can rotate and you always have a fallback when one fatigues."),
]

# ── Helpers ────────────────────────────────────────────────────────────────────

def set_cell_bg(cell, hex_str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_str)
    tcPr.append(shd)


def hdr_row(table, labels, bg="007ae8"):
    for cell in table.rows[0].cells:
        set_cell_bg(cell, bg)
    for cell, label in zip(table.rows[0].cells, labels):
        r = cell.paragraphs[0].add_run(label)
        r.font.bold = True; r.font.color.rgb = WHITE; r.font.size = Pt(9)


def section_heading(doc, text):
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run(text.upper())
    r.font.size = Pt(9); r.font.bold = True; r.font.color.rgb = BLUE
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bot = OxmlElement("w:bottom")
    bot.set(qn("w:val"), "single"); bot.set(qn("w:sz"), "4")
    bot.set(qn("w:space"), "1"); bot.set(qn("w:color"), "007ae8")
    pBdr.append(bot); pPr.append(pBdr)


def add_table(doc, cols, widths, headers):
    t = doc.add_table(rows=1, cols=cols)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    hdr_row(t, headers)
    set_col_widths(t, widths)
    return t


def set_col_widths(table, widths_cm):
    for row in table.rows:
        for i, w in enumerate(widths_cm):
            if i < len(row.cells):
                row.cells[i].width = Cm(w)


def cell_run(cell, text, bold=False, colour=None, size=9, italic=False):
    r = cell.paragraphs[0].add_run(text)
    r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = colour or INK
    return r


def multiline_cell(cell, text, bold=False, colour=None, size=9):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if i == 0:
            r = cell.paragraphs[0].add_run(line)
        else:
            r = cell.add_paragraph().add_run(line)
        r.font.size = Pt(size); r.font.bold = bold
        r.font.color.rgb = colour or INK


def char_colour(chars, limit):
    return RED_HL if chars > limit else MUTED


# ── Build doc ──────────────────────────────────────────────────────────────────

doc = Document()

for section in doc.sections:
    section.top_margin = Cm(2.0); section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.5); section.right_margin = Cm(2.5)

doc.styles["Normal"].font.name = "Calibri"
doc.styles["Normal"].font.size = Pt(10)

# Title
p = doc.add_paragraph()
r = p.add_run("MOSIC — Meta Ads Campaign")
r.font.size = Pt(20); r.font.bold = True; r.font.color.rgb = BLUE

p2 = doc.add_paragraph()
r2 = p2.add_run("Melbourne Osteopathy Sports Injury Centre  ·  May 2026")
r2.font.size = Pt(10); r2.font.color.rgb = MUTED

p3 = doc.add_paragraph()
r3 = p3.add_run(
    "Platform: Facebook + Instagram  ·  Objective: Leads / Traffic  "
    "·  Locations: Bourke St CBD + Essendon  ·  Goal: New patient bookings"
)
r3.font.size = Pt(9); r3.font.color.rgb = MUTED; r3.font.italic = True

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: AUDIENCES
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "1 — Target audiences")

p_note = doc.add_paragraph()
r_note = p_note.add_run(
    "Cold audiences for prospecting. Warm audiences build over time from pixel data — "
    "do not activate warm campaigns until each audience has 500+ people."
)
r_note.font.size = Pt(9); r_note.font.italic = True; r_note.font.color.rgb = MUTED

t_aud = add_table(doc, 4, [2.0, 3.0, 5.0, 7.0],
                  ["Type", "Audience name", "Targeting detail", "Reasoning"])

for atype, name, detail, reason in AUDIENCES:
    row = t_aud.add_row().cells
    c = BLUE if atype == "Cold" else GREEN
    cell_run(row[0], atype, bold=True, colour=c)
    cell_run(row[1], name, bold=True, size=9)
    multiline_cell(row[2], detail, size=8)
    cell_run(row[3], reason, size=8)

set_col_widths(t_aud, [2.0, 3.0, 5.0, 7.0])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: AD VARIANTS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "2 — Ad variants (4)")

p_lim = doc.add_paragraph()
r_lim = p_lim.add_run(
    "Character limits: Primary text — 125 chars visible before 'see more'  "
    "·  Headline — 27 chars before truncation in feed  ·  Description — 30 chars"
)
r_lim.font.size = Pt(9); r_lim.font.italic = True; r_lim.font.color.rgb = MUTED

for v in VARIANTS:
    doc.add_paragraph()
    # Variant header row
    p_vh = doc.add_paragraph()
    r_num = p_vh.add_run(f"Variant {v['number']}  —  ")
    r_num.font.size = Pt(10); r_num.font.bold = True; r_num.font.color.rgb = BLUE
    r_angle = p_vh.add_run(v["angle"])
    r_angle.font.size = Pt(10); r_angle.font.bold = True; r_angle.font.color.rgb = INK

    t_v = doc.add_table(rows=0, cols=3)
    t_v.style = "Table Grid"
    t_v.alignment = WD_TABLE_ALIGNMENT.LEFT

    def var_row(label, value, value_colour=None, value_bold=False, note=None):
        row = t_v.add_row().cells
        set_cell_bg(row[0], "f4f8fd")
        r_l = row[0].paragraphs[0].add_run(label)
        r_l.font.size = Pt(8); r_l.font.bold = True; r_l.font.color.rgb = MUTED
        r_v = row[1].paragraphs[0].add_run(value)
        r_v.font.size = Pt(9); r_v.font.bold = value_bold
        r_v.font.color.rgb = value_colour or INK
        r_n = row[2].paragraphs[0].add_run(note or "")
        r_n.font.size = Pt(8); r_n.font.italic = True; r_n.font.color.rgb = MUTED

    hl_chars  = len(v["headline"])
    desc_chars = len(v["description"])
    pt_chars  = len(v["primary_text"])

    var_row("Audience",     v["audience"],       value_colour=BLUE, value_bold=True)
    var_row("Objective",    v["objective"],       value_colour=GREEN, value_bold=True)
    var_row("Primary text",
            v["primary_text"],
            note=f"{pt_chars} chars {'— over 125 visible limit' if pt_chars > 125 else '— within visible limit' if pt_chars <= 125 else ''}")
    var_row("Headline",
            v["headline"],
            value_colour=RED_HL if hl_chars > 27 else INK,
            note=f"{hl_chars} chars {'⚠ over 27 — will truncate in feed' if hl_chars > 27 else ''}")
    var_row("Description",
            v["description"],
            value_colour=RED_HL if desc_chars > 30 else INK,
            note=f"{desc_chars} chars {'⚠ over 30' if desc_chars > 30 else ''}")
    var_row("CTA button",   v["cta"],            value_colour=BLUE, value_bold=True)
    var_row("Visual direction", v["visual"])
    var_row("Reasoning",    v["reasoning"])

    set_col_widths(t_v, [3.0, 8.0, 6.0])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: BIDDING STRATEGY
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "3 — Bidding strategy")

t_bid = add_table(doc, 3, [4.0, 4.5, 9.0],
                  ["Phase", "Strategy", "Reasoning"])

for phase, strat, reason in BIDDING:
    row = t_bid.add_row().cells
    r_p = row[0].paragraphs[0].add_run(phase)
    r_p.font.size = Pt(9); r_p.font.bold = True
    multiline_cell(row[1], strat, bold=True, colour=BLUE)
    cell_run(row[2], reason, size=8)

set_col_widths(t_bid, [4.0, 4.5, 9.0])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: CAMPAIGN & AD SETTINGS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "4 — Campaign & ad settings")

t_set = add_table(doc, 3, [3.5, 5.0, 9.0],
                  ["Setting", "Recommendation", "Reasoning"])

for setting, rec, reason in CAMPAIGN_SETTINGS:
    row = t_set.add_row().cells
    r_s = row[0].paragraphs[0].add_run(setting)
    r_s.font.size = Pt(9); r_s.font.bold = True
    multiline_cell(row[1], rec, bold=True, colour=BLUE)
    cell_run(row[2], reason, size=8)

set_col_widths(t_set, [3.5, 5.0, 9.0])

# Footer
doc.add_paragraph()
p_foot = doc.add_paragraph()
r_foot = p_foot.add_run(
    "Locate Digital  ·  locatedigital.io  ·  sam@locatedigital.io  ·  Generated May 2026"
)
r_foot.font.size = Pt(8); r_foot.font.color.rgb = MUTED

doc.save(OUTPUT_PATH)
print(f"Saved: {OUTPUT_PATH}")
