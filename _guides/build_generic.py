import re

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/accounting.html', 'r', encoding='utf-8') as f:
    template = f.read()

svg_match = re.search(r'(<svg[^>]+height="44".*?</svg>)', template, re.DOTALL)
LOGO_SVG = svg_match.group(1)
css_match = re.search(r'(<style>.*?</style>)', template, re.DOTALL)
CSS = css_match.group(1)

TICK = '<svg width="12" height="9" viewBox="0 0 12 9" fill="none"><path d="M1 4L4.5 7.5L11 1" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def make_item(label, note):
    return f'''    <div class="item" onclick="toggle(this)">
      <div class="item-check">{TICK}</div>
      <div class="item-body">
        <div class="item-label">{label}</div>
        <div class="item-note">{note}</div>
      </div>
    </div>'''

def make_section(sid, num, title, desc, items):
    count = len(items)
    rows = '\n'.join([make_item(l, n) for l, n in items])
    return f'''  <section class="section" id="{sid}">
    <div class="section-head">
      <div class="section-head-top">
        <div class="section-num">{num}</div>
        <h2>{title}</h2>
        <span class="section-progress" id="prog-{sid}">0 / {count}</span>
      </div>
      <p class="section-desc">{desc}</p>
    </div>
{rows}
  </section>'''

s1 = make_section('s1', 1, 'Website &amp; credibility',
    'Your website is usually the first place a potential client goes after finding you. It needs to work on mobile, load quickly, and give people enough information to feel confident picking up the phone. Most service business websites fail at least one of these.',
    [
        ('Professional website that works on mobile', 'A site that displays and functions correctly on a smartphone, where the majority of local service searches happen.'),
        ('Clear service pages explaining what you offer', 'Individual or dedicated pages for each service, covering what it involves and who it is for.'),
        ('Team page with photos and credentials', 'A page introducing the people behind the business, with photos, names, roles, and relevant qualifications.'),
        ('Client testimonials or case studies', 'Reviews or outcome stories from past clients, published on the website with enough detail to be credible.'),
        ('A clear call to action on every page', 'A visible next step on each page such as a phone number, contact form, or booking link, that makes it easy to get in touch.'),
        ('Fast page load speed', 'Images and code optimised so the site loads quickly on a standard mobile connection.'),
    ])

s2 = make_section('s2', 2, 'Local SEO &amp; Google presence',
    'When someone nearby searches for a service like yours, Google decides who appears at the top. Most local businesses have never set up the signals that drive that decision. This is one of the most direct ways to generate new enquiries without spending on ads.',
    [
        ('Google Business Profile verified and complete', 'A verified Google listing with photos, services, opening hours, contact details, and a full business description.'),
        ('"[Service] in [suburb]" page on your website', 'A page on your website written for your location and service type, targeting the searches your local clients use.'),
        ('40+ Google reviews with responses on each', 'A volume of reviews on your Google Business Profile that builds credibility, with a reply from the business on every one.'),
        ('Consistent name, address, and phone across directories', 'Your business contact details listed identically across Google, Facebook, and any directory you appear on.'),
        ('Listed on relevant business directories', 'Your business listed on general and industry-specific directories with complete and accurate information.'),
        ('Google Posts published monthly', 'Short updates published directly to your Google Business Profile, keeping the listing active and visible in search.'),
    ])

s3 = make_section('s3', 3, 'Content &amp; visibility',
    'Publishing useful content builds trust with people who are not quite ready to call yet, and keeps you ranking when someone in your area searches for what you do. The businesses that publish consistently are the ones that stay visible between jobs.',
    [
        ('Blog or educational content published regularly', 'Articles on your website covering topics relevant to your clients, such as how-to guides, FAQs, or industry updates.'),
        ('Active presence on one or two social platforms', 'A consistent posting schedule on the platforms where your clients spend time, whether that is Facebook, Instagram, or LinkedIn.'),
        ('Video content introducing the business or team', 'Short videos published on your website or social channels that show who you are and how you work.'),
        ('A lead magnet or free resource', 'A downloadable guide, checklist, or tool offered on the website in exchange for a visitor contact details.'),
        ('Content planned around seasonal or industry peaks', 'A rough schedule of content tied to the times of year when clients are most likely to need your services.'),
    ])

s4 = make_section('s4', 4, 'Lead nurture &amp; client retention',
    'Most service businesses focus almost entirely on getting new clients and underinvest in keeping the ones they have. Retention costs less than acquisition, and a well-looked-after client is also your best source of referrals.',
    [
        ('Email newsletter or update sent regularly', 'A regular email sent to your client list covering relevant tips, updates, or news about your business.'),
        ('Automated follow-up after enquiries', 'An automatic message sent when someone contacts you, confirming receipt and setting expectations for next steps.'),
        ('Referral process or partner strategy in place', 'A structured way to encourage referrals from existing clients or complementary businesses in your area.'),
        ('Onboarding process for new clients', 'A defined sequence of communication that helps new clients understand what to expect and feel confident in their decision.'),
        ('Re-engagement for past clients', 'A process for reaching out to clients who have not been in touch for a defined period, prompting a return visit or enquiry.'),
    ])

s5 = make_section('s5', 5, 'Paid advertising',
    'Organic reach has a ceiling. Paid advertising lets you put your business in front of the right people in your area at the right time. When campaigns are set up correctly, you can measure exactly what each new client costs to acquire.',
    [
        ('Google Ads targeting local search terms', 'Paid ads that appear when someone in your area searches for the service you provide.'),
        ('Meta Ads targeting local residents', 'Paid ads on Facebook and Instagram targeted by suburb, age, and interests relevant to your service.'),
        ('Remarketing to previous website visitors', 'Ads shown specifically to people who visited your website but did not make an enquiry or booking.'),
        ('Conversion tracking set up correctly', 'A system that records when a lead takes a valuable action such as a form submission, call, or booking, so you know which campaigns are working.'),
    ])

sections_list = [s1, s2, s3, s4, s5]
js_counts = [6, 6, 5, 5, 4]
total = sum(js_counts)
sections_html = '\n'.join(sections_list)
js_sections = ', '.join([f'{{ id: "s{i+1}", count: {c} }}' for i, c in enumerate(js_counts)])

verdicts = [
    (0, 4, "Work through the checklist above to see your result."),
    (5, 10, "There is a lot of ground to cover. Most of these gaps are fixable within a few months."),
    (11, 15, "Solid foundations in place. The remaining gaps are likely costing you leads you do not know about."),
    (16, 20, "Good shape overall. A handful of items here could shift your results meaningfully."),
    (21, 24, "Strong presence. You are ahead of most local service businesses. The remaining items are worth a conversation."),
    (25, 26, "Very strong. Let us talk about where you want to take it from here."),
]
verdicts_js = '\n'.join([f'    [{v[0]}, {v[1]}, "{v[2]}"],' for v in verdicts])

html = f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Digital Presence Checklist — Service Businesses | Locate Digital</title>
  <meta name="description" content="How strong is your digital presence? This checklist covers the fundamentals every service business needs to get found, generate leads, and turn marketing spend into something measurable.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
  {CSS}
</head>
<body>
<nav class="nav">
  <a class="nav-logo" href="https://www.locatedigital.io" target="_blank">{LOGO_SVG}</a>
  <div class="nav-right">
    <div class="nav-score-badge">Score: <span id="nav-score">0</span> / <span id="nav-total">0</span></div>
    <a class="nav-cta" href="https://www.locatedigital.io" target="_blank">Book a free call</a>
  </div>
</nav>

<header class="hero">
  <div class="hero-inner">
    <div class="hero-eyebrow">Digital presence checklist</div>
    <h1>Service businesses</h1>
    <p class="hero-sub">
      Most service businesses are invisible online at the exact moment a client is searching for them. They have a website. They might be on Google. But they are missing the things that actually turn a search into a call.<br><br>
      This checklist covers <strong>{total} items across five areas</strong>, website credibility, local SEO, content, client retention, and paid advertising. Work through it honestly. The gaps you find are where your competitors are winning business you should be getting.
    </p>
    <div class="hero-points">
      <div class="hero-point">
        <div class="hero-point-label">Areas covered</div>
        <div class="hero-point-value">5 categories</div>
      </div>
      <div class="hero-point">
        <div class="hero-point-label">Items to check</div>
        <div class="hero-point-value">{total} specific actions</div>
      </div>
      <div class="hero-point">
        <div class="hero-point-label">Time to complete</div>
        <div class="hero-point-value">About 10 minutes</div>
      </div>
    </div>
    <div class="score-pill-wrap">
      <div class="score-pill">Your score so far: <strong id="hero-score">0</strong>&nbsp;/ <span id="hero-total">0</span></div>
      <a class="hero-cta" href="https://www.locatedigital.io" target="_blank">Talk to us about the gaps</a>
    </div>
  </div>
</header>

<main class="main">

  <div class="intro">
    <p>Tick every item that genuinely applies to your business, not what you intend to do, but what is actually live and working right now. That honest number is the one worth talking about.</p>
    <p>Score 21 or above and you are ahead of most local service businesses. Below 12 and there are quick wins here that are probably costing you clients every week.</p>
  </div>

{sections_html}

  <div class="progress-wrap">
    <div class="progress-label"><span>Overall progress</span><span id="pct-label">0%</span></div>
    <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
  </div>

  <div class="tip">
    <p><strong>Where to start if you scored under 12:</strong> the fundamentals carry the most weight. A complete Google Business Profile, a consistent review strategy, and a website that clearly explains what you do and who you serve will generate more enquiries than almost anything else. Get those right before spending on paid advertising.</p>
  </div>

  <div class="score-card">
    <div class="score-card-eyebrow">Your result</div>
    <div class="score-display"><span id="final-score">0</span> / <span id="final-total">{total}</span></div>
    <div class="score-pct" id="score-pct">0% of items complete</div>
    <p class="score-verdict" id="score-verdict">Work through the checklist above to see your result.</p>
    <hr class="score-divider">
    <div class="score-cta-label">Want to know what to fix first?</div>
    <a class="btn-primary" href="https://www.locatedigital.io" target="_blank">Book a free strategy call</a>
  </div>

</main>

<footer>
  <p>&copy; 2026 <a href="https://www.locatedigital.io" target="_blank">Locate Digital</a> — Digital marketing for service businesses.</p>
</footer>

<script>
  const sections = [{js_sections}];
  const total = sections.reduce((a, s) => a + s.count, 0);
  ['hero-total','nav-total','final-total'].forEach(id => {{ const el = document.getElementById(id); if (el) el.textContent = total; }});
  const verdicts = [
{verdicts_js}
  ];
  function getVerdict(score) {{ for (const [min, max, msg] of verdicts) {{ if (score >= min && score <= max) return msg; }} return ""; }}
  function updateScores() {{
    let grand = 0;
    sections.forEach(s => {{
      const sec = document.getElementById(s.id);
      const checked = sec.querySelectorAll('.item.checked').length;
      const progEl = document.getElementById('prog-' + s.id);
      progEl.textContent = checked + ' / ' + s.count;
      progEl.className = 'section-progress' + (checked === s.count ? ' done' : '');
      grand += checked;
    }});
    const pct = Math.round((grand / total) * 100);
    document.getElementById('hero-score').textContent = grand;
    document.getElementById('nav-score').textContent = grand;
    document.getElementById('final-score').textContent = grand;
    document.getElementById('score-pct').textContent = pct + '% of items complete';
    document.getElementById('pct-label').textContent = pct + '%';
    document.getElementById('progress-fill').style.width = pct + '%';
    document.getElementById('score-verdict').textContent = getVerdict(grand);
  }}
  function toggle(el) {{ el.classList.toggle('checked'); updateScores(); }}
  updateScores();
</script>
</body>
</html>'''

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/service-businesses.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done. Total items: {total}')
