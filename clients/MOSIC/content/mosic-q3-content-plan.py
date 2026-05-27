from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# --- Styles ---
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def set_heading(para, text, level=1):
    run = para.add_run(text)
    run.bold = True
    if level == 1:
        run.font.size = Pt(18)
        run.font.color.rgb = RGBColor(0x00, 0x7a, 0xe8)  # Locate blue
    elif level == 2:
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x0d, 0x0d, 0x0d)
    elif level == 3:
        run.font.size = Pt(12)
        run.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)

def add_para(doc, text, bold=False, size=11, color=None, space_before=0, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = color
    return p

def add_table_row(table, cells, bold_first=False):
    row = table.add_row()
    for i, (cell, text) in enumerate(zip(row.cells, cells)):
        cell.text = text
        para = cell.paragraphs[0]
        run = para.runs[0] if para.runs else para.add_run(text)
        run.font.size = Pt(10)
        if bold_first and i == 0:
            run.bold = True

# --- Title ---
title_para = doc.add_paragraph()
title_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
set_heading(title_para, 'MOSIC — Q3 2026 Content Plan', level=1)

sub = doc.add_paragraph()
sub.paragraph_format.space_after = Pt(4)
r = sub.add_run('July · August · September 2026')
r.font.size = Pt(11)
r.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)

meta = doc.add_paragraph()
meta.paragraph_format.space_after = Pt(16)
r2 = meta.add_run('6 blog posts  ·  12 GMB posts  ·  Runs on 7th and 21st each month')
r2.font.size = Pt(10)
r2.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)

# --- Month sections ---
months = [
    {
        'month': 'July',
        'context': 'Peak winter · School holidays (first 2 weeks) · AFL finals race',
        'runs': [
            {
                'date': '7 July',
                'blog': 'Why your back gets worse every winter — the Melbourne desk worker\'s guide',
                'gmb1': 'Cold + sedentary = back pain spiral',
                'gmb2': 'What osteopathy does about winter desk pain',
            },
            {
                'date': '21 July',
                'blog': 'Switching to the gym in winter: why so many Melbourne men pick up new injuries',
                'gmb1': 'Indoor training load vs outdoor patterns — different movement planes, gym overuse',
                'gmb2': 'How MOSIC assesses and treats gym-switch injuries',
            },
        ],
    },
    {
        'month': 'August',
        'context': 'AFL finals series begins · Winter ending · Spring approaching',
        'runs': [
            {
                'date': '7 August',
                'blog': 'AFL finals footy injuries — what\'s actually going wrong and how long it takes to fix',
                'gmb1': 'Weekend warriors back in footy boots for finals — hamstrings, groin, ankles',
                'gmb2': 'Getting seen before the season ends, not after',
            },
            {
                'date': '21 August',
                'blog': 'How to come back to running after winter without getting hurt',
                'gmb1': 'Doing too much too soon when spring arrives',
                'gmb2': 'What MOSIC checks before you ramp up training',
            },
        ],
    },
    {
        'month': 'September',
        'context': 'AFL Grand Final (last Sat) · Father\'s Day (1st Sun) · School holidays (last 2 weeks) · Spring begins',
        'runs': [
            {
                'date': '7 September',
                'blog': 'Getting your body ready for spring sport — a guide for Melbourne\'s office workers',
                'gmb1': 'Winter stiffness + sudden outdoor activity = injury risk',
                'gmb2': 'Spring prep — what a session looks like at MOSIC',
            },
            {
                'date': '21 September',
                'blog': 'After the Grand Final: what a full footy season does to your body (and how to recover)',
                'gmb1': 'Cumulative season load and the post-finals crash',
                'gmb2': 'Transitioning from AFL season into summer — what to do now',
            },
        ],
    },
]

for month_data in months:
    # Month heading
    mh = doc.add_paragraph()
    mh.paragraph_format.space_before = Pt(14)
    mh.paragraph_format.space_after = Pt(2)
    set_heading(mh, month_data['month'], level=2)

    # Context line
    ctx = doc.add_paragraph()
    ctx.paragraph_format.space_after = Pt(10)
    r = ctx.add_run(month_data['context'])
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)
    r.italic = True

    for run in month_data['runs']:
        # Date label
        dh = doc.add_paragraph()
        dh.paragraph_format.space_before = Pt(6)
        dh.paragraph_format.space_after = Pt(4)
        dr = dh.add_run(run['date'])
        dr.bold = True
        dr.font.size = Pt(11)
        dr.font.color.rgb = RGBColor(0x00, 0x7a, 0xe8)

        # Blog
        bp = doc.add_paragraph()
        bp.paragraph_format.left_indent = Inches(0.2)
        bp.paragraph_format.space_after = Pt(3)
        label = bp.add_run('Blog:  ')
        label.bold = True
        label.font.size = Pt(10)
        val = bp.add_run(run['blog'])
        val.font.size = Pt(10)

        # GMB 1
        g1 = doc.add_paragraph()
        g1.paragraph_format.left_indent = Inches(0.2)
        g1.paragraph_format.space_after = Pt(3)
        l1 = g1.add_run('GMB 1:  ')
        l1.bold = True
        l1.font.size = Pt(10)
        l1.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)
        v1 = g1.add_run(run['gmb1'])
        v1.font.size = Pt(10)
        v1.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)

        # GMB 2
        g2 = doc.add_paragraph()
        g2.paragraph_format.left_indent = Inches(0.2)
        g2.paragraph_format.space_after = Pt(8)
        l2 = g2.add_run('GMB 2:  ')
        l2.bold = True
        l2.font.size = Pt(10)
        l2.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)
        v2 = g2.add_run(run['gmb2'])
        v2.font.size = Pt(10)
        v2.font.color.rgb = RGBColor(0x63, 0x66, 0x6b)

# --- Summary table ---
doc.add_paragraph()
sh = doc.add_paragraph()
sh.paragraph_format.space_before = Pt(10)
sh.paragraph_format.space_after = Pt(8)
set_heading(sh, 'Summary', level=2)

table = doc.add_table(rows=1, cols=3)
table.style = 'Table Grid'

# Header row
hdr = table.rows[0].cells
hdr[0].text = 'Date'
hdr[1].text = 'Blog topic'
hdr[2].text = 'Hook'
for cell in hdr:
    for para in cell.paragraphs:
        for run in para.runs:
            run.bold = True
            run.font.size = Pt(10)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), '007ae8')
        shading.set(qn('w:color'), 'auto')
        shading.set(qn('w:val'), 'clear')
        cell._tc.get_or_add_tcPr().append(shading)

rows = [
    ('7 Jul',   'Winter desk pain',                  'Peak cold + sedentary = back pain'),
    ('21 Jul',  'Indoor gym injuries',               'Sport switchers picking up new injuries'),
    ('7 Aug',   'AFL finals footy injuries',         'Weekend warriors back on the pitch'),
    ('21 Aug',  'Return to running after winter',    'Spring ramping = injury risk'),
    ('7 Sep',   'Spring body prep',                  'Winter stiffness meets outdoor activity'),
    ('21 Sep',  'Post-Grand Final recovery',         'End of season, what now'),
]

for i, (date, topic, hook) in enumerate(rows):
    row = table.add_row()
    row.cells[0].text = date
    row.cells[1].text = topic
    row.cells[2].text = hook
    fill = 'f0f7ff' if i % 2 == 0 else 'ffffff'
    for cell in row.cells:
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(10)
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), fill)
        shading.set(qn('w:color'), 'auto')
        shading.set(qn('w:val'), 'clear')
        cell._tc.get_or_add_tcPr().append(shading)

# Column widths
for row in table.rows:
    row.cells[0].width = Inches(1.0)
    row.cells[1].width = Inches(2.8)
    row.cells[2].width = Inches(2.8)

# Save
out = r'G:\My Drive\Claude Code.Locate\clients\MOSIC\content\mosic-q3-2026-content-plan.docx'
doc.save(out)
print(f'Saved: {out}')
