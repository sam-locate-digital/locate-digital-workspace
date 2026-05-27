from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "mosic-google-ads-rsa-2026-05.docx")

# ── Brand colours ──────────────────────────────────────────────────────────────
BLUE    = RGBColor(0x00, 0x7a, 0xe8)
INK     = RGBColor(0x0d, 0x0d, 0x0d)
MUTED   = RGBColor(0x63, 0x66, 0x6b)
RED_HL  = RGBColor(0xd4, 0x1c, 0x1c)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
BG_SOFT = RGBColor(0xf4, 0xf8, 0xfd)

# ── Data ───────────────────────────────────────────────────────────────────────

KEYWORDS = [
    # (ad_group, keyword, match_type, reasoning)
    ("1 — Osteopath + Location",
     "osteopath Melbourne CBD",       "Phrase",
     "Captures variants like 'best osteopath Melbourne CBD' and 'CBD osteopath open now'. High intent, location-specific."),
    ("1 — Osteopath + Location",
     "osteopath Melbourne CBD",       "Exact",
     "Exact match on the core query ensures highest-intent searches always trigger the ad. Bids can be set higher than phrase."),
    ("1 — Osteopath + Location",
     "osteopath Bourke Street",       "Exact",
     "Ultra-specific query — anyone typing this is ready to book. Exact only; no need for phrase variants here."),
    ("1 — Osteopath + Location",
     "osteopath Essendon",            "Phrase",
     "Catches 'osteopath near Essendon', 'Essendon North osteopath'. Phrase gives reach without losing local relevance."),
    ("1 — Osteopath + Location",
     "osteopath near me",             "Phrase",
     "'Near me' is the highest-volume modifier in local service search. Phrase match paired with location targeting handles geography correctly."),
    ("1 — Osteopath + Location",
     "osteopathy Melbourne",          "Phrase",
     "Service-noun variant ('osteopathy' vs 'osteopath'). Different searcher vocabulary, same intent. Phrase to catch location modifiers."),

    ("2 — Back Pain",
     "back pain treatment Melbourne", "Phrase",
     "Condition + treatment intent + location. Phrase captures 'back pain treatment Melbourne CBD', 'best back pain treatment Melbourne'."),
    ("2 — Back Pain",
     "back pain osteopath Melbourne", "Exact",
     "All three signals in one query: condition, service, location. Anyone typing this is ready to book — use exact to protect CPCs."),
    ("2 — Back Pain",
     "back pain Melbourne",           "Phrase",
     "Shorter query, slightly earlier in research journey. Phrase match to catch 'lower back pain Melbourne', 'chronic back pain Melbourne'."),
    ("2 — Back Pain",
     "osteopath for back pain",       "Phrase",
     "Alternative search pattern — service first, condition second. Different from location-first queries but same high intent."),

    ("3 — Sports & Running Injuries",
     "sports injury treatment Melbourne", "Phrase",
     "Condition + treatment + location. Phrase captures sport-specific variants: 'AFL sports injury Melbourne', 'running sports injury treatment'."),
    ("3 — Sports & Running Injuries",
     "running injury Melbourne",          "Phrase",
     "MOSIC explicitly treats running injuries. Melbourne Marathon training season drives this query mid-year. Phrase to catch 'running knee injury Melbourne' etc."),
    ("3 — Sports & Running Injuries",
     "sports osteopath Melbourne",        "Phrase",
     "Service + audience + location. Targets people who identify as athletes rather than general pain sufferers — different ad copy angle."),

    ("4 — Neck Pain & Desk Workers",
     "neck pain treatment Melbourne",     "Phrase",
     "Mirrors the back pain structure. Phrase to capture 'neck pain specialist Melbourne', 'neck pain physio Melbourne' (competitor terms)."),
    ("4 — Neck Pain & Desk Workers",
     "neck pain osteopath",               "Phrase",
     "Service + condition without location. Works because location targeting handles geography — useful for catching searches without a city modifier."),
    ("4 — Neck Pain & Desk Workers",
     "work injury Melbourne",             "Phrase",
     "MOSIC lists work injuries as a service. CBD professional audience is high-value. Phrase to capture 'work-related injury Melbourne', 'workplace injury treatment'."),
]

HEADLINES = [
    ("Osteopath Melbourne CBD",        "Keyword"),
    ("Back Pain Treatment Melbourne",  "Keyword"),
    ("Osteopath Bourke Street",        "Keyword"),
    ("Sports Injury Osteopath",        "Keyword"),
    ("CBD Osteopath Near You",         "Location"),
    ("Essendon Osteopathy Clinic",     "Location"),
    ("Melbourne CBD & Essendon",       "Location"),
    ("Back Pain Relief Fast",          "Benefit"),
    ("Neck Pain? We Can Help",         "Benefit"),
    ("Same-Week Appointments",         "Benefit"),
    ("Book Online Today",              "CTA"),
    ("Call for Same-Day Booking",      "CTA"),
    ("8 Experienced Practitioners",    "Trust"),
    ("12,000+ Melbourne Patients",     "Trust"),
    ("Telehealth Also Available",      "USP"),
]

DESCRIPTIONS = [
    ("Back pain. Neck pain. Sports injuries. Bourke St CBD and Essendon clinics.",
     "Service + outcome", 74),
    ("12,000+ patients seen by 8 Melbourne osteopaths. Clinics in Bourke St CBD and Essendon.",
     "Trust + proof", 87),
    ("Book online or call 03 9663 6202. Same-week appointments at our CBD and Essendon clinics.",
     "CTA + booking", 89),
    ("For desk workers, runners, and weekend athletes. Telehealth appointments also available.",
     "USP", 88),
]

PINNING = [
    ("Position 1",    "Headline 1 — Osteopath Melbourne CBD",
     "Primary keyword must always appear. Anchors the ad to the core service query — every impression should see this."),
    ("Position 2",    "Headline 5 — CBD Osteopath Near You",
     "Local signal reinforces geo relevance. Pairing keyword (pos 1) + location (pos 2) covers both intent and geography in the first visible line."),
    ("Description 1", "Description 3 — Book online or call 03 9663 6202…",
     "Phone number must always show. CTA with direct contact details drives calls — MOSIC's highest-converting action. Don't let Google rotate this out."),
]

BIDDING = [
    ("Phase 1 — First 30–60 days",
     "Maximize Clicks  ·  Max CPC cap: $10",
     "No conversion history exists yet. Google's Smart Bidding (Maximize Conversions, Target CPA) requires 30–50 conversions per month to work properly — without data it will overspend or underspend unpredictably. Maximize Clicks with a CPC cap gathers volume, builds conversion history, and reveals which keywords and ad combinations actually drive bookings. The $10 cap prevents any single click from blowing the daily budget on a competitive term."),
    ("Phase 2 — After 50+ conversions",
     "Maximize Conversions",
     "Once there's enough conversion signal, switch to Maximize Conversions. Google will optimize bids toward the actions you've defined (calls, form fills, bookings) rather than just clicks. Don't switch before hitting ~50 conversions — Smart Bidding with thin data actively performs worse than manual bidding. Trigger: when monthly conversions consistently exceed 50 for two consecutive months."),
    ("Phase 3 — Mature campaign (4+ months)",
     "Target CPA  ·  Estimated CPA: $40–$80",
     "Once CPA stabilises, set an explicit target. For a Melbourne CBD osteopath, a first appointment is worth $90–$150+ (and lifetime patient value is multiples of that), so a CPA of $40–$80 leaves strong margin. Set the initial Target CPA at 10–20% above your actual observed CPA to give Smart Bidding room to move — tightening too fast causes impression share to collapse."),
]

CAMPAIGN_SETTINGS = [
    ("Network",
     "Search Network only",
     "Do not tick 'Display Network' or 'Search Partners' at launch. Display Network shows ads on websites and apps — irrelevant for a patient searching for an appointment. Search Partners (Ask.com, YouTube search, etc.) add volume at lower intent. Start Search only; add Search Partners after 60 days if CPC and conversion rate hold up."),
    ("Location targeting",
     "Radius: 10 km from each clinic (140 Bourke St CBD + 320 Keilor Rd Essendon)\n+ Explicit suburbs: Melbourne CBD, Carlton, Fitzroy, South Yarra, Docklands, North Melbourne, Moonee Ponds, Ascot Vale, Essendon, Essendon North",
     "Radius targeting catches 'near me' queries automatically — Google uses the searcher's device location against the radius. Suburb targeting catches explicit suburb queries ('osteopath Carlton') that might fall outside the radius. Use both layers together, not one or the other."),
    ("Location options",
     "Presence: People in or regularly in your targeted locations",
     "Default is 'Presence or interest' — this includes people researching Melbourne who live elsewhere (e.g. a Sydney resident planning a trip). A patient in Sydney will not book at MOSIC. Changing to 'Presence' ensures only local searchers see the ads. This single setting change commonly reduces wasted spend by 10–20% on local campaigns."),
    ("Ad schedule",
     "Monday–Saturday: 7 am–7 pm\nSunday: 8 am–1 pm (or paused)",
     "Osteopath bookings happen during business hours and early-evening research windows. Saturday mornings are high-intent (sport injury recovery over the weekend). Sunday late night/evening browsing rarely converts to appointments — it's leisure browsing, not booking intent. Running ads outside these windows drives cost without proportional bookings."),
    ("Devices",
     "All devices  ·  Mobile bid adjustment: +20–25%",
     "'Near me' and local service searches are 65–75% mobile. Call extension clicks — MOSIC's fastest conversion path — only exist on mobile. Keeping desktop/tablet active captures CBD professionals searching from work computers (relevant for this target). The +20–25% mobile bid adjustment ensures competitive position on the placements most likely to convert without abandoning desktop entirely."),
    ("Conversion tracking",
     "Must be live BEFORE launch:\n1. Phone calls from ads (threshold: 60 seconds)\n2. Website form submissions\n3. Online booking page visit / confirmation page",
     "Without conversion tracking, Smart Bidding is blind, reporting shows clicks but not outcomes, and there's no data to prove ROI to the client. Phone calls over 60 seconds filter out wrong numbers and hang-ups — under 60 seconds is not a real lead. Set this up in Google Ads → Tools → Conversions, and verify it's firing before spending a dollar."),
    ("Ad rotation",
     "Optimize: Prefer best performing ads",
     "RSAs are designed to test headline and description combinations automatically. Forcing equal rotation defeats the point — it shows underperforming combinations the same number of times as winners. 'Optimize' lets Google surface the combinations with the highest CTR and conversion rate based on the query, device, and audience. Review the combination report monthly to see which headlines appear most often."),
    ("Extensions / Assets",
     "Required: Location, Call, Sitelinks, Callout, Structured Snippets",
     "Location extension (linked to MOSIC Google Business Profile): shows address and distance under the ad — critical for local. Adds map pin on mobile.\nCall extension (03 9663 6202, scheduled Mon–Sat 8am–6pm): one-tap call from mobile. Highest-converting action for a clinic.\nSitelinks: Back Pain Treatment, Neck Pain, Sports Injuries, Book Online, Bourke St Clinic, Essendon Clinic — each linking to a relevant page.\nCallout extensions: 'Same-Week Appointments', 'Telehealth Available', '8 Practitioners', 'Online Booking'.\nStructured snippets (Services): Osteopathy, Running Injuries, Work Injuries, Corporate Health, Neck Pain, Back Pain.\nExtensions expand ad real estate, improve Quality Score, and give searchers multiple ways to engage without clicking the main ad."),
    ("Final URL / Display path",
     "Final URL: dedicated landing page per ad group (not homepage)\nDisplay path: /back-pain-treatment or /sports-injury-melbourne",
     "The homepage has too many exits and competing calls to action. A focused landing page matching the ad's message (back pain ad → back pain page) significantly improves conversion rate — typically 30–50% higher than sending paid traffic to a homepage. The display path (the green text under the headline) should mirror the ad group's topic to reinforce relevance and improve Quality Score."),
]

AD_STRENGTH_NOTE = (
    "15 unique headlines across 6 distinct types (keyword, location, benefit, CTA, "
    "trust, USP) with 4 varied descriptions covering service, proof, CTA, and audience. "
    "Should score Excellent in Ads Manager. Pinning position 1 and description 1 slightly "
    "reduces combination flexibility — remove pins if Ads Manager reports Good instead of "
    "Excellent after 2 weeks of data."
)

# ── Helpers ────────────────────────────────────────────────────────────────────

def set_cell_bg(cell, hex_str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_str)
    tcPr.append(shd)


def hdr_row(table, labels, bg_hex="007ae8"):
    hdr = table.rows[0].cells
    for cell in hdr:
        set_cell_bg(cell, bg_hex)
    for cell, label in zip(hdr, labels):
        p = cell.paragraphs[0]
        r = p.add_run(label)
        r.font.bold = True
        r.font.color.rgb = WHITE
        r.font.size = Pt(9)


def section_heading(doc, text):
    doc.add_paragraph()
    p = doc.add_paragraph()
    r = p.add_run(text.upper())
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = BLUE
    # bottom border
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "007ae8")
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p


def body_run(para, text, bold=False, colour=None, size=9, italic=False):
    r = para.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = colour or INK
    return r


def set_col_widths(table, widths_cm):
    for row in table.rows:
        for i, w in enumerate(widths_cm):
            if i < len(row.cells):
                row.cells[i].width = Cm(w)


def add_table(doc, cols, col_widths, header_labels):
    t = doc.add_table(rows=1, cols=cols)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    hdr_row(t, header_labels)
    set_col_widths(t, col_widths)
    return t


# ── Build document ─────────────────────────────────────────────────────────────

doc = Document()

for section in doc.sections:
    section.top_margin    = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

doc.styles["Normal"].font.name = "Calibri"
doc.styles["Normal"].font.size = Pt(10)

# Title
p = doc.add_paragraph()
r = p.add_run("MOSIC — Google Ads RSA Copy")
r.font.size = Pt(20); r.font.bold = True; r.font.color.rgb = BLUE

p2 = doc.add_paragraph()
r2 = p2.add_run("Melbourne Osteopathy Sports Injury Centre  ·  May 2026")
r2.font.size = Pt(10); r2.font.color.rgb = MUTED

p3 = doc.add_paragraph()
r3 = p3.add_run(
    "Campaign: Google Search  ·  Services: Osteopathy, back pain, neck pain, sports injuries  "
    "·  Locations: Bourke St CBD + Essendon  ·  Goal: Lead gen (calls + bookings)"
)
r3.font.size = Pt(9); r3.font.color.rgb = MUTED; r3.font.italic = True

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: KEYWORDS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "1 — Keywords & match types")

t_kw = add_table(doc, 4, [3.5, 5.0, 2.0, 6.0],
                 ["Ad group", "Keyword", "Match type", "Reasoning"])

prev_group = None
for ag, kw, match, reason in KEYWORDS:
    row = t_kw.add_row().cells
    # Shade alternate ad groups for readability
    if ag != prev_group:
        prev_group = ag
    row[0].paragraphs[0].add_run(ag).font.size = Pt(8)
    r_kw = row[1].paragraphs[0].add_run(kw)
    r_kw.font.size = Pt(9); r_kw.font.bold = True
    r_mt = row[2].paragraphs[0].add_run(match)
    r_mt.font.size = Pt(9)
    r_mt.font.color.rgb = (
        RGBColor(0x00, 0x7a, 0xe8) if match == "Exact" else
        RGBColor(0x00, 0x7a, 0x3a) if match == "Phrase" else
        RGBColor(0xd4, 0x7a, 0x1c)
    )
    row[3].paragraphs[0].add_run(reason).font.size = Pt(8)

set_col_widths(t_kw, [3.5, 5.0, 2.0, 6.0])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: HEADLINES
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "2 — Headlines (15)  ·  max 30 characters each")

p_note = doc.add_paragraph()
body_run(p_note, "Any headline shown in red exceeds 30 chars and will be rejected by Ads Manager.",
         colour=MUTED, italic=True)

t_hl = add_table(doc, 4, [1.0, 8.5, 2.5, 1.5],
                 ["#", "Headline", "Type", "Chars"])

for i, (text, htype) in enumerate(HEADLINES, 1):
    chars = len(text)
    over  = chars > 30
    row   = t_hl.add_row().cells
    row[0].paragraphs[0].add_run(str(i)).font.size = Pt(9)
    r = row[1].paragraphs[0].add_run(text)
    r.font.size = Pt(9)
    if over: r.font.color.rgb = RED_HL; r.font.bold = True
    row[2].paragraphs[0].add_run(htype).font.size = Pt(9)
    cr = row[3].paragraphs[0].add_run(str(chars))
    cr.font.size = Pt(9)
    if over: cr.font.color.rgb = RED_HL; cr.font.bold = True

set_col_widths(t_hl, [1.0, 8.5, 2.5, 1.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: DESCRIPTIONS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "3 — Descriptions (4)  ·  max 90 characters each")

t_desc = add_table(doc, 4, [1.0, 9.5, 2.5, 1.5],
                   ["#", "Description", "Type", "Chars"])

for i, (text, dtype, chars) in enumerate(DESCRIPTIONS, 1):
    over = chars > 90
    row  = t_desc.add_row().cells
    row[0].paragraphs[0].add_run(str(i)).font.size = Pt(9)
    r = row[1].paragraphs[0].add_run(text)
    r.font.size = Pt(9)
    if over: r.font.color.rgb = RED_HL; r.font.bold = True
    row[2].paragraphs[0].add_run(dtype).font.size = Pt(9)
    cr = row[3].paragraphs[0].add_run(str(chars))
    cr.font.size = Pt(9)
    if over: cr.font.color.rgb = RED_HL; cr.font.bold = True

set_col_widths(t_desc, [1.0, 9.5, 2.5, 1.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: PINNING
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "4 — Pinning recommendations")

t_pin = add_table(doc, 3, [2.5, 5.0, 9.5],
                  ["Slot", "Pin to", "Reasoning"])

for slot, pin_to, reason in PINNING:
    row = t_pin.add_row().cells
    row[0].paragraphs[0].add_run(slot).font.size = Pt(9)
    r = row[1].paragraphs[0].add_run(pin_to)
    r.font.size = Pt(9); r.font.bold = True
    row[2].paragraphs[0].add_run(reason).font.size = Pt(9)

set_col_widths(t_pin, [2.5, 5.0, 9.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5: BIDDING STRATEGY
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "5 — Bidding strategy")

t_bid = add_table(doc, 3, [4.0, 4.0, 9.5],
                  ["Phase", "Strategy", "Reasoning"])

for phase, strat, reason in BIDDING:
    row = t_bid.add_row().cells
    r_p = row[0].paragraphs[0].add_run(phase)
    r_p.font.size = Pt(9); r_p.font.bold = True
    r_s = row[1].paragraphs[0].add_run(strat)
    r_s.font.size = Pt(9); r_s.font.bold = True; r_s.font.color.rgb = BLUE
    row[2].paragraphs[0].add_run(reason).font.size = Pt(9)

set_col_widths(t_bid, [4.0, 4.0, 9.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6: CAMPAIGN & AD SETTINGS
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "6 — Campaign & ad settings")

t_set = add_table(doc, 3, [3.5, 5.0, 9.5],
                  ["Setting", "Recommendation", "Reasoning"])

for setting, rec, reason in CAMPAIGN_SETTINGS:
    row = t_set.add_row().cells
    r_s = row[0].paragraphs[0].add_run(setting)
    r_s.font.size = Pt(9); r_s.font.bold = True
    # Recommendation may have newlines — split and add runs
    for j, line in enumerate(rec.split("\n")):
        if j == 0:
            r_r = row[1].paragraphs[0].add_run(line)
        else:
            r_r = row[1].add_paragraph().add_run(line)
        r_r.font.size = Pt(9); r_r.font.bold = True; r_r.font.color.rgb = BLUE
    row[2].paragraphs[0].add_run(reason).font.size = Pt(8)

set_col_widths(t_set, [3.5, 5.0, 9.5])

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 7: AD STRENGTH & NOTES
# ═══════════════════════════════════════════════════════════════════════════════
section_heading(doc, "7 — Ad strength note")
p_as = doc.add_paragraph()
body_run(p_as, AD_STRENGTH_NOTE, size=9)

# Footer
doc.add_paragraph()
p_foot = doc.add_paragraph()
r_foot = p_foot.add_run(
    "Locate Digital  ·  locatedigital.io  ·  sam@locatedigital.io  ·  "
    "Generated May 2026"
)
r_foot.font.size = Pt(8); r_foot.font.color.rgb = MUTED

# Save
doc.save(OUTPUT_PATH)
print(f"Saved: {OUTPUT_PATH}")
