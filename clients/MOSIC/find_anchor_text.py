import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {'User-Agent': 'Mozilla/5.0 (compatible; SEO-audit/1.0)'}

broken_map = {
    'https://www.melbourneosteopathycentre.com.au/?page_id=2177': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/?page_id=2179': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/?page_id=2154': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/about-us/'],
    'https://www.melbourneosteopathycentre.com.au/?page_id=1623': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/about-us/'],
    'https://www.melbourneosteopathycentre.com.au/?page_id=24': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/headaches/'],
    'https://www.melbourneosteopathycentre.com.au/?page_id=2199': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/headaches/'],
    'https://www.melbourneosteopathycentre.com.au/?page_id=2201': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/headaches/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/osteopathy/': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/remedial-massage/': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/myotherapy/': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/services/corporate-health-services/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/exercise-physiology/': ['https://www.melbourneosteopathycentre.com.au/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/corporate-health-services/': ['https://www.melbourneosteopathycentre.com.au/', 'https://www.melbourneosteopathycentre.com.au/about-us/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/exercise-rehabilitation/': ['https://www.melbourneosteopathycentre.com.au/essendon-osteopathy/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/functional-movement-osteopathy/': ['https://www.melbourneosteopathycentre.com.au/our-services-osteopathy/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/podiatry/': ['https://www.melbourneosteopathycentre.com.au/essendon-osteopathy/', 'https://www.melbourneosteopathycentre.com.au/our-services-osteopathy/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/running-analysis/': ['https://www.melbourneosteopathycentre.com.au/essendon-osteopathy/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/bike-fitting-and-analysis/': ['https://www.melbourneosteopathycentre.com.au/essendon-osteopathy/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/golf-injury-and-performance-centre/': ['https://www.melbourneosteopathycentre.com.au/essendon-osteopathy/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/golf-injury-and-performance-centre': ['https://www.melbourneosteopathycentre.com.au/blog/golf/pain-free-golf-5-tips-for-a-smooth-round-for-golfers/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/traditional-chinese-medicine/': ['https://www.melbourneosteopathycentre.com.au/services/needling-accupuncture/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/electro-stimulation-via-acupuncture-electrotherapy/': ['https://www.melbourneosteopathycentre.com.au/services/needling-accupuncture/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/yoga-classes/': ['https://www.melbourneosteopathycentre.com.au/services/corporate-health-services/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/corporate-mat-pilates/': ['https://www.melbourneosteopathycentre.com.au/services/corporate-health-services/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/coaching-and-athlete-development/': ['https://www.melbourneosteopathycentre.com.au/blog/melbourne/swimming-the-fundamentals-of-freestyle-or-front-crawl/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/running-gait-analysis/': ['https://www.melbourneosteopathycentre.com.au/blog/osteopathy/gait-analysis/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/needling-accupuncture/': ['https://www.melbourneosteopathycentre.com.au/blog/osteopathy/dry-needling-for-headaches/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/remedial-message/': ['https://www.melbourneosteopathycentre.com.au/services/traditional-chinese-medicine/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/studio-pilates/': ['https://www.melbourneosteopathycentre.com.au/services/pilates/', 'https://www.melbourneosteopathycentre.com.au/blog/pilates/pilates-equipment-at-mosic/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/pilates-timetable/': ['https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/bodhi-suspension-system/': ['https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/pilates-faq/': ['https://www.melbourneosteopathycentre.com.au/services/pilates/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/timetable/': ['https://www.melbourneosteopathycentre.com.au/services/pilates/pilates-faq/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/pilates/pilates-team/': ['https://www.melbourneosteopathycentre.com.au/blog/pilates/pilates-equipment-at-mosic/'],
    'https://www.melbourneosteopathycentre.com.au/team_group/pilates-instructors/': ['https://www.melbourneosteopathycentre.com.au/services/pilates/pilates-faq/'],
    'https://www.melbourneosteopathycentre.com.au/services/osteopathy/': ['https://www.melbourneosteopathycentre.com.au/blog/osteopathy/headaches-a-pain-in-the-neck/'],
    'https://www.melbourneosteopathycentre.com.au/products/foam-rollers/': ['https://www.melbourneosteopathycentre.com.au/services/health-lifestyle-products/'],
    'https://www.melbourneosteopathycentre.com.au/products/flexi-pillow/': ['https://www.melbourneosteopathycentre.com.au/services/health-lifestyle-products/'],
    'https://www.melbourneosteopathycentre.com.au/how-to-make-the-most-of-your-foam-roller/': ['https://www.melbourneosteopathycentre.com.au/services/health-lifestyle-products/foam-rollers/'],
    'https://www.melbourneosteopathycentre.com.au/our-services/health-lifestyle-products/spiky-balls/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/are-you-experiencing-foot-pain-since-working-from-home/'],
    'https://www.melbourneosteopathycentre.com.au/team/dr-brendan-oloughlin-osteopath/': ['https://www.melbourneosteopathycentre.com.au/blog/osteopathy/running-training-principles-injury-prevention/'],
    'https://www.melbourneosteopathycentre.com.au/team/dr-shane-buntman-osteopath/': ['https://www.melbourneosteopathycentre.com.au/blog/events/5-things-i-wish-i-knew-when-i-started-a-small-business/'],
    'https://www.melbourneosteopathycentre.com.au/team/dr-julia-adams/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/explaining-pain/', 'https://www.melbourneosteopathycentre.com.au/blog/osteopathy/pain-as-a-protector/'],
    'https://www.melbourneosteopathycentre.com.au/team/dr-jake-martin/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/5-healthy-habits-for-getting-back-to-the-office/'],
    'https://www.melbourneosteopathycentre.com.au/team/cassie-robertson/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/why-do-muscles-get-tight/'],
    'https://www.melbourneosteopathycentre.com.au/team/cate-jephcott/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/eating-fat-doesnt-make-you-fat/'],
    'https://www.melbourneosteopathycentre.com.au/our-team/': ['https://www.melbourneosteopathycentre.com.au/blog/dry-needling/dry-needling-versus-acupuncture/', 'https://www.melbourneosteopathycentre.com.au/blog/pilates/pilates-at-home/'],
    'https://www.melbourneosteopathycentre.com.au/our-team-practitioners/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/how-to-quit-coffee/'],
    'https://www.melbourneosteopathycentre.com.au/ask-a-question/': ['https://www.melbourneosteopathycentre.com.au/services/exercise-physiology/', 'https://www.melbourneosteopathycentre.com.au/services/pilates/pilates-faq/'],
    'https://www.melbourneosteopathycentre.com.au/traditional-chinese-medicine/': ['https://www.melbourneosteopathycentre.com.au/blog/health-well-being/10-things-you-should-know-about-acupuncture/'],
    'https://www.melbourneosteopathycentre.com.au/remedial-massage/': ['https://www.melbourneosteopathycentre.com.au/blog/osteopathy/10-tips-to-help-reduce-stress/'],
    'https://www.melbourneosteopathycentre.com.au/pilates/': ['https://www.melbourneosteopathycentre.com.au/blog/pilates/pilates-for-beginners/'],
    'https://www.melbourneosteopathycentre.com.au/pilates-for-beginners/': ['https://www.melbourneosteopathycentre.com.au/blog/pilates/pilates-at-home/'],
    'https://www.melbourneosteopathycentre.com.au/trusting-your-plan-interview-with-melbourne-marathon-runner/': ['https://www.melbourneosteopathycentre.com.au/blog/events/training-for-your-first-triathlon-in-just-4-weeks/'],
    'https://www.melbourneosteopathycentre.com.au/medical-history-explained-workstation-ergonomics/': ['https://www.melbourneosteopathycentre.com.au/blog/osteopathy/medical-history-explained-allergies/'],
    'https://www.melbourneosteopathycentre.com.au/blog/services/coaching-and-athlete-development/': ['https://www.melbourneosteopathycentre.com.au/blog/strength-training/swimming-5-tips-for-beginners/'],
}

page_cache = {}

def get_soup(url):
    if url not in page_cache:
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            page_cache[url] = BeautifulSoup(r.text, 'html.parser')
            print(f'  Fetched: {url}')
        except Exception as e:
            print(f'  ERROR fetching {url}: {e}')
            page_cache[url] = None
    return page_cache[url]

def get_anchor_text(soup, target_href):
    if not soup:
        return '(could not fetch page)'
    target_clean = target_href.rstrip('/')
    matches = []
    for tag in soup.find_all('a', href=True):
        href = tag.get('href', '').rstrip('/')
        if href == target_clean or target_clean.endswith(href) or href.endswith(target_clean.split('/')[-1]):
            text = tag.get_text(strip=True)
            if not text:
                img = tag.find('img')
                text = tag.get('aria-label') or (img.get('alt') if img else '') or '(image/icon link)'
            if text:
                matches.append(text)
    return ' | '.join(dict.fromkeys(matches)) if matches else '(link text not found)'

results = []
print('Fetching pages and finding link/button text...\n')

for broken_url, sources in broken_map.items():
    seen = []
    for src in sources:
        if src not in seen:
            seen.append(src)
    for src in seen[:2]:
        soup = get_soup(src)
        anchor = get_anchor_text(soup, broken_url)
        results.append((broken_url, src, anchor))

out_path = r'G:\My Drive\Claude Code.Locate\clients\MOSIC\broken-links-anchor-text-2026-05-25.csv'
with open(out_path, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Broken URL', 'Source page', 'Link / button text on page'])
    for row in results:
        w.writerow(row)

print(f'\nDone. {len(results)} rows written.')
print(f'Saved to: {out_path}')
