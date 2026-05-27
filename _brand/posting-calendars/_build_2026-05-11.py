"""Build Locate Digital reels posting calendar for week of 2026-05-11.
Uses brand tokens from _brand/brand.json. Output: 2026-05-11_reels-week.docx.
"""
import json
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BRAND = json.loads(Path(r"G:/My Drive/Claude Code.Locate/_brand/brand.json").read_text(encoding="utf-8"))
PRIMARY = BRAND["colours"]["primary"].lstrip("#")
SEMI_BLACK = BRAND["colours"]["ink"].lstrip("#")
DARK_GREY = BRAND["colours"]["muted"].lstrip("#")
ORANGE = BRAND["colours"]["accent"].lstrip("#")
HEAD_FONT = BRAND["fonts"]["heading"]["family"]
BODY_FONT = BRAND["fonts"]["body"]["family"]

def hex_rgb(h):
    return RGBColor(int(h[0:2],16), int(h[2:4],16), int(h[4:6],16))

def set_cell_bg(cell, hex_colour):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_colour)
    tc_pr.append(shd)

def set_run(run, font=BODY_FONT, size=10.5, bold=False, colour=SEMI_BLACK):
    run.font.name = font
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii","w:hAnsi","w:cs","w:eastAsia"):
        rFonts.set(qn(attr), font)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = hex_rgb(colour)

def add_heading(doc, text, size=22, colour=PRIMARY, space_before=18, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    set_run(r, font=HEAD_FONT, size=size, bold=True, colour=colour)
    return p

def add_para(doc, text, size=10.5, bold=False, colour=SEMI_BLACK, space_after=4, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    set_run(r, size=size, bold=bold, colour=colour)
    r.italic = italic
    return p

def add_label_value(doc, label, value, label_colour=PRIMARY):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f"{label}  ")
    set_run(r1, size=10.5, bold=True, colour=label_colour)
    r2 = p.add_run(value)
    set_run(r2, size=10.5, colour=SEMI_BLACK)
    return p

def add_block_label(doc, label):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(label.upper())
    set_run(r, font=HEAD_FONT, size=9.5, bold=True, colour=PRIMARY)

def add_bullet(doc, text, size=10.5):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(1)
    r = p.add_run(text)
    set_run(r, size=size, colour=SEMI_BLACK)

def add_quoted_block(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    set_run(r, size=10.5, colour=SEMI_BLACK)
    r.italic = True

def add_divider(doc):
    p = doc.add_paragraph()
    p_pr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), PRIMARY)
    pbdr.append(bottom)
    p_pr.append(pbdr)

# ---------- DOCUMENT ----------
doc = Document()
for s in doc.sections:
    s.top_margin = Cm(2.0)
    s.bottom_margin = Cm(2.0)
    s.left_margin = Cm(2.2)
    s.right_margin = Cm(2.2)

# Set default style
normal = doc.styles["Normal"]
normal.font.name = BODY_FONT
normal.font.size = Pt(10.5)

# COVER
add_heading(doc, "Reels Posting Calendar", size=26, space_before=0, space_after=2)
add_heading(doc, "Locate Digital — Week of Mon 11 → Sun 17 May 2026", size=12, colour=DARK_GREY, space_before=0, space_after=14)
add_para(doc, "Audience: Aussie service-business owners ($1–3M revenue). Broad framing — never single-vertical.", size=10.5, colour=DARK_GREY)
add_para(doc, "Goal this week: pull views back to AU. Stack 3+ AU markers in every script.", size=10.5, colour=DARK_GREY, space_after=10)
add_divider(doc)

# EXTRA AU LEVERS
add_heading(doc, "Extra AU levers — apply every post this week", size=15)
levers = [
    "Stack 3+ AU markers per script. Mix one regulator/scheme (ASIC, AHPRA, Fair Work, ACCC, modern award, payroll tax, WorkCover, super) + one AU tool (Xero, MYOB, Hnry, Cliniko, Halaxy, ServiceM8, Tradify, simPRO, Employment Hero, Deputy) + one AU place name.",
    "Geo-tag every post with a Melbourne, Sydney or Brisbane location — your suburb, a CBD, a known venue.",
    "First comment = a second hashtag block, all AU-tilted (#australianbusiness #aussiesmallbiz #ausbiz #smallbizaustralia #aussieentrepreneur). Pin it.",
    "Reply to first 5 comments within 30 minutes — but only AU accounts. Skip non-AU early commenters; their engagement teaches the algorithm wrong.",
    "Engage 10 minutes before posting — like + comment on 5–10 AU service-biz accounts to warm the AU audience graph.",
    "Hard NO on overnight posting (10pm–6am AEDT). That window is US/EU prime time and is where the offshore drift compounds.",
    "Caption opener in AU English within first 10 chars (e.g. \"Aussie business owners —\"). The algorithm reads the caption hard for geo.",
    "Drop in an AU brand name where it fits naturally — Bunnings, Officeworks, Telstra, Australia Post, hipages — these don't exist in the US and tag content as local instantly.",
]
for l in levers:
    add_bullet(doc, l)

add_divider(doc)

# ---------- SCRIPTS ----------
scripts = [
    {
        "day": "Monday 11 May 2026",
        "time": "Post 7–9am AEDT",
        "topic": "Google Ads waste audit",
        "pattern": "Specificity / proof",
        "format": "Talking head + screen recording of Google Ads dashboard",
        "hook": "We just found $14K of wasted Google Ads spend in 20 minutes.",
        "inspo": "https://www.instagram.com/reel/DGLVKBUR6W0/",
        "onscreen": [
            "0–3s: WE FOUND $14K of WASTED Google Ads spend",
            "3–7s: 20 minutes. Melbourne service biz.",
            "7–25s (animated bullets): Search terms = junk · Bidding on competitor brand · No location exclusions · Match types too broad",
            "Last 2s: Want yours audited?",
        ],
        "vo": (
            "We just found $14,000 of wasted Google Ads spend for a Melbourne service business — in twenty minutes. "
            "Here's how. Step one — pulled their search terms report. Half the clicks were people searching for unrelated stuff. "
            "Step two — they were bidding on three competitor brand names with no exclusions, paying premium for clicks that never converted. "
            "Step three — no Australia-only location targeting set, so they were burning budget on overseas clicks too. "
            "Step four — broad match keywords with no negative list. "
            "If your Google Ads in Xero are showing the spend but not the results, send this to your bookkeeper and your marketing person."
        ),
        "au_markers": "Melbourne · Australia · Xero",
        "caption": (
            "Aussie business owners — $14K of wasted Google Ads spend in 20 minutes. Most of you are bleeding money the same way. "
            "What's the last thing you audited in your Ads account?\n\n"
            "#smallbusinessaustralia #ausbusiness #googleadstips"
        ),
        "broll": "Talking-head close-up for hook (3s). Cut to screen rec scrolling Google Ads search-terms report with sensitive bits blurred. Cut back to talking head for CTA.",
        "length": "≈28 seconds",
    },
    {
        "day": "Tuesday 12 May 2026",
        "time": "Post 12–1pm AEDT",
        "topic": "Stop boosting posts on Meta",
        "pattern": "Contrarian",
        "format": "Text-on-black with VO + brief Ads Manager screen recording",
        "hook": "Stop boosting posts on Meta. It's the most Aussie way to waste $2K a month.",
        "inspo": "https://www.instagram.com/p/DGaYM9PIO9b/",
        "onscreen": [
            "0–3s: STOP boosting posts.",
            "3–7s: = $2,000/month gone",
            "7–22s: What to do instead — 1. Use Ads Manager · 2. Pick a real objective (leads / conversions) · 3. Build an actual audience",
            "Last 2s: Save this. Use Monday.",
        ],
        "vo": (
            "Stop boosting posts on Meta. It's the most Aussie way I know to waste two grand a month. "
            "The boost button picks the cheapest objective — page engagement. That's why you get heaps of likes from Sydney, Brisbane, Manila, "
            "and zero leads. Open Ads Manager instead. Pick a real objective — leads or conversions. Build an audience around your actual service area. "
            "Run it for at least seven days before you touch anything. That's how you stop torching budget on a button that was designed for big brands, "
            "not for you running a service business out of a Bunnings carpark on your lunch break."
        ),
        "au_markers": "Aussie · Sydney · Brisbane · Bunnings",
        "caption": (
            "Aussie business owners — the boost button is the fastest way to lose $2K a month on Meta. Real campaigns live in Ads Manager. "
            "What's the most you've ever spent boosting a post?\n\n"
            "#smallbusinessaustralia #ausbusiness #metaads"
        ),
        "broll": "Bold text-on-black for first 7s. Cut to brief Ads Manager screen rec for the 'what to do instead' section. Loop final frame back to STOP graphic.",
        "length": "≈25 seconds",
    },
    {
        "day": "Wednesday 13 May 2026",
        "time": "Post 7–9pm AEDT",
        "topic": "Google Business Profile fixes",
        "pattern": "Direct callout",
        "format": "Screen recording of GBP dashboard intercut with talking head",
        "hook": "Sydney, Melbourne, Brisbane service businesses — your GBP is costing you 5 calls a week.",
        "inspo": "https://www.instagram.com/p/DDCdiwNO6cO/",
        "onscreen": [
            "0–3s: Sydney. Melbourne. Brisbane.",
            "3–7s: Your GBP is costing you 5 calls a week.",
            "7–27s (red-cross checklist): No Q&A populated · Photos older than 3 months · No services listed · No weekly post · Reviews ignored",
            "Last 2s: Fix one tonight.",
        ],
        "vo": (
            "Sydney, Melbourne, Brisbane service businesses — your Google Business Profile is costing you about five booked calls every week. "
            "Here's why. Most of you have no Q and A populated, so when someone searches 'do you bulk bill' or 'do you take new clients' Google can't answer for you. "
            "Your photos are older than three months. You haven't listed your actual services. You don't post weekly. And every single review sits there with no reply. "
            "Fix one of those tonight while you're watching telly. Then go reply to your last ten reviews — the algorithm reads response rate like Google's own version of hipages."
        ),
        "au_markers": "Sydney · Melbourne · Brisbane · hipages",
        "caption": (
            "Aussie business owners — your Google Business Profile is the most ignored marketing channel you own. "
            "Five booked calls a week sit on the table. Which one of these are you guilty of?\n\n"
            "#smallbusinessaustralia #ausbusiness #googlebusinessprofile"
        ),
        "broll": "Mock GBP dashboard screen rec — highlight each ✗ point with a red ring as it's mentioned. Cut to talking-head close-up for the CTA.",
        "length": "≈30 seconds",
    },
    {
        "day": "Thursday 14 May 2026",
        "time": "Post 7–9am AEDT",
        "topic": "5 Meta ads mistakes",
        "pattern": "Negative bias",
        "format": "Talking head + animated on-screen list",
        "hook": "5 things to never do in Meta ads — most Aussie owners get #3 wrong.",
        "inspo": "https://www.instagram.com/reel/DG2_ufDxNQJ/",
        "onscreen": [
            "0–3s: 5 things to NEVER do in Meta ads",
            "3–7s: 1. Don't boost posts",
            "7–11s: 2. Don't run 1 ad set forever",
            "11–15s: 3. Don't make claims the ACCC will fine you for",
            "15–19s: 4. Don't skip retargeting",
            "19–23s: 5. Don't run with no Pixel",
            "Last 2s: Which one are you guilty of?",
        ],
        "vo": (
            "Five things you should never do in your Meta ads — most Aussie owners get number three wrong. "
            "One — don't boost posts. Use Ads Manager. "
            "Two — don't run the same ad set for six months thinking it's still working. Refresh creative every fortnight. "
            "Three — don't make outcome claims the ACCC will fine you for. 'Guaranteed results', 'we're number one in Perth' — that's a please-fine-me sign on your account. "
            "Four — don't skip retargeting. Most of your sales are people who saw you twice. "
            "Five — don't run a single dollar without the Meta Pixel installed properly. "
            "If you're guilty of more than two of these, mate, your ad budget is a charity donation."
        ),
        "au_markers": "Aussie · ACCC · Perth · mate",
        "caption": (
            "Aussie business owners — these five Meta ads mistakes are costing you bookings every week. The ACCC angle catches everyone off guard. "
            "Which one are you guilty of?\n\n"
            "#smallbusinessaustralia #ausbusiness #metaads"
        ),
        "broll": "Talking head intercut with bold on-screen list animation — each number flashes on. Final frame loops back to '5 things to NEVER do' graphic so it replays.",
        "length": "≈28 seconds",
    },
    {
        "day": "Friday 15 May 2026",
        "time": "Post 12–1pm AEDT",
        "topic": "Marketing spend hidden in Xero",
        "pattern": "Pattern interrupt",
        "format": "Screen recording of Xero (mock data) + voiceover",
        "hook": "Your bookkeeper is missing $8K of marketing spend in Xero right now.",
        "inspo": "https://www.instagram.com/reel/DH_Y1jnsjde/",
        "onscreen": [
            "0–3s: $8K of marketing missing in Xero",
            "3–7s: Right now. Your bookkeeper missed it.",
            "7–25s: Where it's hiding → 'Software subscriptions' · 'Bank fees' (it's Stripe) · 'Office supplies' (it's Canva) · 'Cost of sales'",
            "Last 2s: Re-code it. Reports fix themselves.",
        ],
        "vo": (
            "Your bookkeeper is missing about eight grand of marketing spend in Xero right now. Here's where it's hiding. "
            "Half your ad spend is coded as 'software subscriptions'. Your Stripe fees on lead-gen funnels are sitting in 'bank fees'. "
            "Canva, Adobe, Hootsuite — all coded as 'office supplies'. Your sponsored email blasts through Cliniko or MYOB add-ons are buried in 'cost of sales'. "
            "Move them all into a clean 'marketing — paid ads' and 'marketing — software' account. Then your monthly P&L finally shows you what you actually spend. "
            "And next time someone asks for your true cost per lead, you can answer in ten seconds — not ten emails to your accountant."
        ),
        "au_markers": "Xero · Cliniko · MYOB",
        "caption": (
            "Aussie business owners — your real marketing spend in Xero is probably 30% bigger than you think. "
            "Re-code it once, reports fix forever. What's the biggest line you've found buried?\n\n"
            "#smallbusinessaustralia #ausbusiness #xerotips"
        ),
        "broll": "Screen rec of Xero chart of accounts (mock data). Highlight each misallocated line with a coloured block as it's named. Cut to talking head for CTA.",
        "length": "≈30 seconds",
    },
    {
        "day": "Saturday 16 May 2026",
        "time": "Post 7–9pm AEDT",
        "topic": "Email old leads — what to actually say",
        "pattern": "Curiosity gap",
        "format": "Text-on-black + mock Gmail composer typing the template",
        "hook": "Everyone tells you to email old leads. Nobody tells you what to say.",
        "inspo": "https://www.instagram.com/reel/DC2pqKUpy7C/",
        "onscreen": [
            "0–3s: Everyone says: 'email your old leads'",
            "3–7s: Nobody tells you what to actually write.",
            "7–25s (Gmail mockup typing letter by letter): SUBJ: \"{First name}, did you ever sort it?\" · We chatted about {service} back in {month}. · Did you ever get it sorted? Either way, no pressure. · If you're still keen — happy to grab a quick chat next week.",
            "Last 2s: Save this. Send Monday.",
        ],
        "vo": (
            "Everyone tells you to email your old leads. Nobody tells you what to actually say. Save this template. "
            "Subject line — first name, did you ever sort it? "
            "Body — three short lines. We chatted about whatever service back in March. Did you ever get it sorted? Either way, no pressure. "
            "If you're still keen, happy to grab a quick chat next week. "
            "That's it. No pitch. No discount. No 'I just wanted to follow up' opener. "
            "We tested this on a Cliniko list of three hundred old enquiries down in Geelong last month — twelve replies, four bookings. "
            "Send it Monday morning, eight AM, no later."
        ),
        "au_markers": "Cliniko · Geelong · AU spelling (enquiries, organisation)",
        "caption": (
            "Aussie business owners — your old leads aren't dead, they just need the right opener. "
            "Save this and send it Monday. What's the longest you've waited to re-email a cold list?\n\n"
            "#smallbusinessaustralia #ausbusiness #emailmarketing"
        ),
        "broll": "Text-on-black for first 7s. Cut to mock Gmail composer typing template letter by letter — natural typing pace. Final frame: 'SAVE THIS' so it loops.",
        "length": "≈30 seconds",
    },
    {
        "day": "Sunday 17 May 2026",
        "time": "Post 7–9pm AEDT",
        "topic": "Sunday-night planning — 5 fixes before Monday",
        "pattern": "Direct callout",
        "format": "Calm talking head (cuppa in shot) + on-screen checklist",
        "hook": "Aussie service businesses — 5 marketing fixes for Sunday night, before Monday hits.",
        "inspo": "https://www.instagram.com/reel/DE9tW4dyxlJ/",
        "onscreen": [
            "0–3s: Sunday night.",
            "3–7s: 5 fixes before Monday.",
            "7–25s (numbered checklist): 1. Reply to last 10 GBP reviews · 2. Pause any ad with CTR < 1% · 3. Refresh top 3 service-page photos · 4. Email last week's no-shows · 5. Block 30 mins for content Tues",
            "Last 2s: One a week. Compounds fast.",
        ],
        "vo": (
            "Aussie service business owners — it's Sunday night, kettle's on, here are five marketing fixes you can do before Monday. "
            "One — reply to your last ten Google Business Profile reviews. Even a thanks. "
            "Two — open Meta or Google Ads, pause anything with a click-through rate under one percent. "
            "Three — swap the top three photos on your most-visited service page. "
            "Four — email everyone who didn't show last week, no charge, just a 'want to rebook'. "
            "Five — block thirty minutes Tuesday morning to film one piece of content. "
            "Don't do all five. Do one. Same one every Sunday for a month and your numbers in Perth, Brisbane or wherever you're trading will start moving on their own."
        ),
        "au_markers": "Aussie · Perth · Brisbane · AU spelling",
        "caption": (
            "Aussie business owners — Sunday night, five fixes, none take longer than 15 minutes. "
            "Pick one. Which one are you actually going to do tonight?\n\n"
            "#smallbusinessaustralia #ausbusiness #smallbusinessmarketing"
        ),
        "broll": "Lower-energy lighting, calm pacing. Talking head with a cuppa in shot for warmth. Cut to on-screen list as each item is read. Last frame loops back to '5 fixes before Monday'.",
        "length": "≈30 seconds",
    },
]

for s in scripts:
    add_heading(doc, s["day"], size=18, space_before=14, space_after=2)
    # meta line
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(f"{s['time']}   ·   {s['topic']}   ·   Pattern: {s['pattern']}   ·   Format: {s['format']}")
    set_run(r, size=10, colour=DARK_GREY)
    r.italic = True

    add_block_label(doc, "Hook (≤12 words)")
    add_quoted_block(doc, s["hook"])
    add_label_value(doc, "Inspo:", s["inspo"], label_colour=DARK_GREY)

    add_block_label(doc, "On-screen text")
    for line in s["onscreen"]:
        add_bullet(doc, line)

    add_block_label(doc, "Voiceover")
    add_para(doc, s["vo"], size=10.5, space_after=4)
    add_label_value(doc, "AU markers stacked:", s["au_markers"], label_colour=DARK_GREY)

    add_block_label(doc, "Caption")
    add_para(doc, s["caption"], size=10.5, space_after=4)

    add_block_label(doc, "B-roll / visual notes")
    add_para(doc, s["broll"], size=10.5, space_after=4)

    add_label_value(doc, "Length:", s["length"], label_colour=DARK_GREY)

    add_divider(doc)

# Final hashtag template page-end
add_heading(doc, "Reusable templates", size=15, space_before=14)
add_block_label(doc, "Caption opener (first 90 chars, above the fold)")
add_quoted_block(doc, "Aussie business owners — [hook in plain words]. [one-line payoff]. [single specific question, e.g. \"What's the one thing you'd fix this week?\"]")
add_block_label(doc, "Hashtag block (in caption, 3–5)")
add_quoted_block(doc, "#smallbusinessaustralia #ausbusiness #[topical e.g. googleadstips / metaads / smallbusinessmarketing]")
add_block_label(doc, "Pinned first comment")
add_quoted_block(doc, "#australianbusiness #aussiesmallbiz #ausbiz #smallbizaustralia #aussieentrepreneur")

# Footer note
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(18)
r = p.add_run(BRAND.get("footer", "Locate Digital — locatedigital.io"))
set_run(r, size=8.5, colour=DARK_GREY)
r.italic = True

out_path = Path(r"G:/My Drive/Claude Code.Locate/_brand/posting-calendars/2026-05-11_reels-week.docx")
doc.save(out_path)
print(f"WROTE: {out_path}")
print(f"SIZE: {out_path.stat().st_size} bytes")
