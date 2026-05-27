"""
Locate Digital — Client Access Guide
Generates a branded .docx using brand.json colours, fonts, and logo.
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.enum.table import WD_TABLE_ALIGNMENT
import copy, os

# ── Brand tokens ─────────────────────────────────────────────────────────────
PRIMARY   = RGBColor(0x00, 0x7a, 0xe8)   # #007ae8
ACCENT    = RGBColor(0xff, 0x59, 0x00)   # #ff5900
INK       = RGBColor(0x0d, 0x0d, 0x0d)   # #0d0d0d
MUTED     = RGBColor(0x63, 0x66, 0x6b)   # #63666b
LINE      = RGBColor(0xe6, 0xe6, 0xe6)   # #e6e6e6
WHITE     = RGBColor(0xff, 0xff, 0xff)
BG_SOFT   = RGBColor(0xfb, 0xfc, 0xff)   # #fbfcff

FONT_HEAD = "Plus Jakarta Sans"
FONT_BODY = "Poppins"

LOGO_WHITE = r"G:\My Drive\Claude Code.Locate\_brand\Logo flat white\Transparent Logo.png"
LOGO_BLUE  = r"G:\My Drive\Claude Code.Locate\_brand\Logo flat blue\Transparent Logo.png"

TAGLINE    = "We don't just market — we locate growth."
FOOTER_TXT = "Locate Digital  ·  locatedigital.io  ·  sam@locatedigital.io"

# ── Helpers ───────────────────────────────────────────────────────────────────

def hex_to_str(r, g, b):
    return f"{r:02X}{g:02X}{b:02X}"

def set_cell_bg(cell, hex_str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_str)
    tcPr.append(shd)

def remove_cell_border(table):
    tbl = table._tbl
    tblPr = tbl.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        tbl.insert(0, tblPr)
    tblBorders = OxmlElement('w:tblBorders')
    for side in ['top','left','bottom','right','insideH','insideV']:
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'none')
        tblBorders.append(el)
    tblPr.append(tblBorders)

def add_divider(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(6)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '4')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), hex_to_str(0xe6, 0xe6, 0xe6))
    pBdr.append(bottom)
    pPr.append(pBdr)

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after  = Pt(4)
    run = p.add_run(text)
    run.bold = True
    run.font.name = FONT_HEAD
    run.font.size = Pt(13)
    run.font.color.rgb = PRIMARY

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after  = Pt(2)
    run = p.add_run(text)
    run.bold = True
    run.font.name = FONT_BODY
    run.font.size = Pt(10.5)
    run.font.color.rgb = INK

def add_body(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    _rich_run(p, text, size=10, color=INK)
    return p

def add_note(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_after = Pt(8)
    # Light blue-tinted background strip via shading
    pPr = p._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), 'EBF5FF')
    pPr.append(shd)
    run = p.add_run(text)
    run.italic = True
    run.font.name = FONT_BODY
    run.font.size = Pt(9.5)
    run.font.color.rgb = MUTED

def _rich_run(p, text, size=10, color=INK, bold=False):
    """Parse **bold** markers and add runs."""
    parts = text.split('**')
    for i, part in enumerate(parts):
        if not part:
            continue
        run = p.add_run(part)
        run.bold = bold or (i % 2 == 1)
        run.font.name = FONT_BODY
        run.font.size = Pt(size)
        run.font.color.rgb = color

def add_numbered(doc, items):
    for item in items:
        p = doc.add_paragraph(style='List Number')
        p.paragraph_format.space_after = Pt(3)
        _rich_run(p, item)

def add_bullet(doc, items):
    for item in items:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        _rich_run(p, item)

def set_doc_fonts(doc):
    """Set default body font for the document."""
    style = doc.styles['Normal']
    style.font.name = FONT_BODY
    style.font.size = Pt(10.5)
    style.font.color.rgb = INK

# ── Document ──────────────────────────────────────────────────────────────────

doc = Document()
set_doc_fonts(doc)

# Margins
section = doc.sections[0]
section.top_margin    = Inches(0)       # header takes the top
section.bottom_margin = Inches(0.8)
section.left_margin   = Inches(1.2)
section.right_margin  = Inches(1.2)

# ── Header band (blue table, logo left, tagline right) ───────────────────────
header_tbl = doc.add_table(rows=1, cols=2)
header_tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
remove_cell_border(header_tbl)

# Set column widths
header_tbl.columns[0].width = Inches(2.8)
header_tbl.columns[1].width = Inches(3.9)

cell_logo = header_tbl.cell(0, 0)
cell_tag  = header_tbl.cell(0, 1)

for cell in [cell_logo, cell_tag]:
    set_cell_bg(cell, '007ae8')
    cell.width = Inches(2.8) if cell is cell_logo else Inches(3.9)

# Logo
p_logo = cell_logo.paragraphs[0]
p_logo.alignment = WD_ALIGN_PARAGRAPH.LEFT
p_logo.paragraph_format.space_before = Pt(14)
p_logo.paragraph_format.space_after  = Pt(14)
p_logo.paragraph_format.left_indent  = Inches(0.25)
if os.path.exists(LOGO_WHITE):
    run = p_logo.add_run()
    run.add_picture(LOGO_WHITE, width=Inches(1.6))

# Tagline
p_tag = cell_tag.paragraphs[0]
p_tag.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p_tag.paragraph_format.space_before = Pt(22)
p_tag.paragraph_format.space_after  = Pt(0)
p_tag.paragraph_format.right_indent = Inches(0.25)
run = p_tag.add_run(TAGLINE)
run.font.name  = FONT_BODY
run.font.size  = Pt(9)
run.font.color.rgb = WHITE
run.italic = True

# Space after header
doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ── Title block ───────────────────────────────────────────────────────────────
p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(4)
p_title.paragraph_format.space_after  = Pt(2)
run = p_title.add_run('Client access guide')
run.bold = True
run.font.name  = FONT_HEAD
run.font.size  = Pt(22)
run.font.color.rgb = INK

p_sub = doc.add_paragraph()
p_sub.paragraph_format.space_after = Pt(10)
run = p_sub.add_run('For new clients — how to grant us access to your accounts')
run.font.name  = FONT_BODY
run.font.size  = Pt(10.5)
run.font.color.rgb = MUTED

add_divider(doc)

# ── Intro ─────────────────────────────────────────────────────────────────────
add_body(doc, "This guide covers exactly how to give Locate Digital access to your accounts. Each section has step-by-step instructions written for someone who doesn't live in these platforms every day.")
add_body(doc, "If you get stuck on any step, send a screenshot to sam@locatedigital.io and we'll sort it out.")

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(10)
run1 = p.add_run('The email to add for all platforms is: ')
run1.font.name = FONT_BODY
run1.font.size = Pt(10.5)
run1.font.color.rgb = INK
run2 = p.add_run('sam@locatedigital.io')
run2.bold = True
run2.font.name = FONT_BODY
run2.font.size = Pt(10.5)
run2.font.color.rgb = PRIMARY

add_divider(doc)

# ── What we need ─────────────────────────────────────────────────────────────
add_h2(doc, 'What we need access to')
add_body(doc, "Depending on what we're working on together, we'll need some or all of the following:")
add_bullet(doc, [
    'Meta (Facebook and Instagram ads)',
    'Google Ads — paid search campaigns',
    'Google Analytics — website traffic data',
    'Google Business Profile — your Google Maps listing',
    'Your CRM or booking system — appointment and patient data (if applicable)',
])
add_body(doc, "You don't need to do all of these at once. We'll tell you which ones apply to your engagement.")
add_divider(doc)

# ── Meta ─────────────────────────────────────────────────────────────────────
add_h2(doc, 'Meta')
add_body(doc, "The central hub for your Facebook page, Instagram account, ad account, and pixel.")
add_note(doc, "Note: If your business doesn't have a Meta Business Manager account yet, go to business.facebook.com and create one before following the steps below. It takes about 5 minutes.")

add_h3(doc, 'Add us to your Business Manager')
add_numbered(doc, [
    'Go to business.facebook.com',
    'Click **Settings** (gear icon, left sidebar)',
    'Under **Users**, click **People**',
    'Click **Add people**',
    'Enter **sam@locatedigital.io**',
    'Set role to **Admin**',
    'Click **Next**, then assign access to your **Ad Account**, **Facebook Page**, and **Instagram Account**',
    'Click **Invite**',
])

add_h3(doc, 'Give us access to your Pixel (if one exists)')
add_numbered(doc, [
    'In Business Manager, go to **Settings → Data sources → Pixels**',
    'Click on your pixel',
    'Click **Add people**, enter **sam@locatedigital.io**, set to **Admin**, click **Save**',
])
add_body(doc, "If you don't have a pixel yet, don't worry — we'll create one and install it.")
add_divider(doc)

# ── Google Ads ────────────────────────────────────────────────────────────────
add_h2(doc, 'Google Ads')
add_body(doc, "There are two ways to do this. Option A is preferred — it keeps your account under your ownership and lets us manage it from our end without needing your login.")

add_h3(doc, 'Option A — Link to our manager account (preferred)')
add_numbered(doc, [
    'Go to ads.google.com',
    'Sign in to your Google Ads account',
    'Click the **tools icon** (wrench) in the top-right corner',
    'Under **Setup**, click **Access and security**',
    'Click the **Managers** tab',
    "Click **+** to send a link request — we'll send you our manager account ID and you enter it here",
    'Click **Send request**',
])
add_body(doc, "We'll accept from our end within 24 hours.")

add_h3(doc, 'Option B — Add as a user directly')
add_numbered(doc, [
    'Go to ads.google.com and sign in',
    'Click the **tools icon** (wrench) → **Access and security**',
    'Click the **Users** tab, then the **+** button',
    'Enter **sam@locatedigital.io**',
    'Set access level to **Admin**',
    'Click **Send invitation**',
])
add_divider(doc)

# ── Google Analytics ──────────────────────────────────────────────────────────
add_h2(doc, 'Google Analytics')
add_body(doc, "Tracks who visits your website, where they come from, and what they do.")
add_numbered(doc, [
    'Go to analytics.google.com',
    'Sign in with the Google account that owns the property',
    'Click the **gear icon** (Admin) in the bottom-left corner',
    'Under the **Property** column, click **Property access management**',
    'Click the blue **+** button in the top-right corner, then **Add users**',
    'Enter **sam@locatedigital.io**',
    'Under Role, select **Editor**',
    'Click **Add**',
])
add_divider(doc)

# ── Google Business Profile ───────────────────────────────────────────────────
add_h2(doc, 'Google Business Profile')
add_body(doc, "Your listing on Google Maps and Google Search — the panel that shows your address, hours, phone number, and reviews.")
add_numbered(doc, [
    'Go to business.google.com',
    'Sign in and select your business',
    'Click **Menu** (three lines, top-left) → **Business Profile settings**',
    'Click **Managers**',
    'Click the **Add** button (person icon with a +)',
    'Enter **sam@locatedigital.io**',
    'Set role to **Manager**',
    'Click **Invite**',
])
add_divider(doc)

# ── CRM ───────────────────────────────────────────────────────────────────────
add_h2(doc, 'CRM or booking system (if applicable)')
add_body(doc, "This only applies if we're pulling appointment or patient data for reporting. We'll let you know if this is relevant to your engagement.")
add_body(doc, "Steps vary depending on what you use. Send us a note on your system and we'll send specific instructions for it.")
add_divider(doc)

# ── How long ──────────────────────────────────────────────────────────────────
add_h2(doc, 'How long does this take?')
add_body(doc, "Most people get through all platforms in 20–30 minutes. The steps look long written out but each one is just a few clicks.")
add_body(doc, "The only thing that can slow it down is if someone else controls the account — an old agency, a web developer, or an IT contact. If that's the case, let us know and we can help you chase the right person.")
add_divider(doc)

# ── Questions ─────────────────────────────────────────────────────────────────
add_h2(doc, 'Questions?')
add_body(doc, "Email sam@locatedigital.io or reply to your onboarding thread. We check daily.")

# ── Footer ────────────────────────────────────────────────────────────────────
footer_section = doc.sections[0]
footer = footer_section.footer
footer.is_linked_to_previous = False
p_foot = footer.paragraphs[0]
p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p_foot.add_run(FOOTER_TXT)
run.font.name  = FONT_BODY
run.font.size  = Pt(8.5)
run.font.color.rgb = MUTED

# ── Save ──────────────────────────────────────────────────────────────────────
output = r"G:\My Drive\Claude Code.Locate\_ops\client-access-guide.docx"
doc.save(output)
print(f"Saved: {output}")
