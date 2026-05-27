import csv

# Load anchor text lookup: (broken_url, source_page) -> anchor_text
anchor_lookup = {}
with open(r'G:\My Drive\Claude Code.Locate\clients\MOSIC\broken-links-anchor-text-2026-05-25.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        key = (row['Broken URL'].strip(), row['Source page'].strip())
        anchor_lookup[key] = row['Link / button text on page'].strip()

# Load full audit and merge
rows_out = []
with open(r'G:\My Drive\Claude Code.Locate\clients\MOSIC\broken-links-audit-2026-05-25.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        broken = row['Broken URL'].strip()
        source = row['Source page (linked from)'].strip()
        anchor = anchor_lookup.get((broken, source), '')
        rows_out.append({
            'Priority':             row['Priority'].strip(),
            'Category':             row['Category'].strip(),
            'Broken URL':           broken,
            'Source page':          source,
            'Link / button text':   anchor,
            'Suggested fix':        row['Suggested fix'].strip(),
        })

out_path = r'G:\My Drive\Claude Code.Locate\clients\MOSIC\broken-links-audit-2026-05-25.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['Priority', 'Category', 'Broken URL', 'Source page', 'Link / button text', 'Suggested fix'])
    w.writeheader()
    w.writerows(rows_out)

print(f'Done. {len(rows_out)} rows written to {out_path}')
