import re

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/accounting.html', 'r', encoding='utf-8') as f:
    template = f.read()

svg_match = re.search(r'(<svg[^>]+height="44".*?</svg>)', template, re.DOTALL)
LOGO_SVG = svg_match.group(1)

css_match = re.search(r'(<style>.*?</style>)', template, re.DOTALL)
CSS = css_match.group(1)

TICK = '<svg width="12" height="9" viewBox="0 0 12 9" fill="none"><path d="M1 4L4.5 7.5L11 1" stroke="white" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def section(sid, num, title, desc, items):
    count = len(items)
    rows = ''
    for label, note in items:
        rows += f'''    <div class="item" onclick="toggle(this)">
      <div class="item-check">{TICK}</div>
      <div class="item-body">
        <div class="item-label">{label}</div>
        <div class="item-note">{note}</div>
      </div>
    </div>\n'''
    return f'''  <section class="section" id="{sid}">
    <div class="section-head">
      <div class="section-head-top">
        <div class="section-num">{num}</div>
        <h2>{title}</h2>
        <span class="section-progress" id="prog-{sid}">0 / {count}</span>
      </div>
      <p class="section-desc">{desc}</p>
    </div>
{rows}  </section>'''

def make_html(title, meta_desc, h1, p1, p2, market, sections_list, tip, verdicts, js_counts):
    total = sum(js_counts)
    sections_html = '\n'.join(sections_list)
    js_sections = ', '.join([f'{{ id: "s{i+1}", count: {c} }}' for i, c in enumerate(js_counts)])
    verdicts_js = '\n'.join([f'    [{v[0]}, {v[1]}, "{v[2]}"],' for v in verdicts])
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Locate Digital</title>
  <meta name="description" content="{meta_desc}">
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
    <h1>{h1}</h1>
    <p class="hero-sub">{p1}<br><br>{p2}</p>
    <div class="hero-points">
      <div class="hero-point"><div class="hero-point-label">Areas covered</div><div class="hero-point-value">5 categories</div></div>
      <div class="hero-point"><div class="hero-point-label">Items to check</div><div class="hero-point-value">{total} specific actions</div></div>
      <div class="hero-point"><div class="hero-point-label">Time to complete</div><div class="hero-point-value">About 10 minutes</div></div>
      <div class="hero-point"><div class="hero-point-label">Market</div><div class="hero-point-value">{market}</div></div>
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
    <p>Score 19 or above and you are ahead of most local competitors. Below 12 and there are quick wins here that are probably costing you clients every week.</p>
  </div>
{sections_html}
  <div class="progress-wrap">
    <div class="progress-label"><span>Overall progress</span><span id="pct-label">0%</span></div>
    <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
  </div>
  <div class="tip">
    <p><strong>Where to start if you scored under 12:</strong> {tip}</p>
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

# ── BEAUTY SALONS ──────────────────────────────────────────────────────
beauty = make_html(
    title='Digital Presence Checklist — Beauty Salons',
    meta_desc='Attract more bookings and build a loyal client base online. This checklist shows where your salon stands and what to fix first.',
    h1='Beauty salons',
    p1='Most salons are active on Instagram and have a Google listing. That is no longer enough to stand out. The businesses filling their books consistently have the right systems underneath — booking, reviews, local SEO, and targeted advertising working together.',
    p2='This checklist covers <strong>22 items across five areas</strong>, your website, local SEO, social media, client retention, and paid advertising. Work through it honestly. The gaps you find are where your competitors are picking up the bookings you should be getting.',
    market='Melbourne, Victoria',
    sections_list=[
        section('s1', 1, 'Website &amp; online booking',
            'Before a client books, they check your website. For most salons it is also the main place people decide whether to call or move on. A site without online booking, clear pricing, or a portfolio of your work is leaving appointments on the table.',
            [
                ('Mobile-friendly, fast-loading website', 'A website that loads quickly and displays correctly on a phone, where most salon searches happen.'),
                ('Online booking system integrated', 'A booking tool embedded on the website that allows clients to select a service, date, and time without calling.'),
                ('Service menu with clear pricing', 'A full list of services with associated prices, visible without having to contact the salon.'),
                ('Before and after gallery or portfolio', 'A collection of images showing client results, organised by service or style.'),
                ('SSL certificate and HTTPS secure', 'A security certificate that encrypts the connection between a visitor and your website, shown by the padlock in the browser bar.'),
            ]),
        section('s2', 2, 'Local SEO &amp; Google presence',
            'Most local salon searches happen on Google, and the businesses that appear at the top are not always the best — they are the best set up. A complete Google presence is one of the most direct ways to increase bookings from people in your area.',
            [
                ('Google Business Profile fully optimised', 'Your Google listing, including photos, services, opening hours, booking link, and a complete business description.'),
                ('Consistent NAP across all listings', 'Your business name, address, and phone number appearing identically across every online directory and platform.'),
                ('50+ Google reviews with responses', 'The total number of reviews on your Google Business Profile, with a reply from the business on each one.'),
                ('Local keywords on website pages', 'Search terms such as your suburb and service type used naturally throughout your website content and page titles.'),
                ('Listed on Yelp, True Local and directories', 'Your salon listed consistently across general and local business directories.'),
            ]),
        section('s3', 3, 'Social media &amp; content',
            'For beauty businesses, social media is often the first place potential clients look. It acts as a live portfolio. Consistent, high-quality content across Instagram and Facebook is one of the most effective ways to attract and retain clients in this industry.',
            [
                ('Active Instagram and Facebook profiles', 'Regularly updated profiles on both platforms with current work, contact details, and a booking link.'),
                ('Consistent posting schedule (3 times per week minimum)', 'A regular cadence of posts maintained across the week, not just when time allows.'),
                ('Client transformation content and reels', 'Short video content showing before and after results, published as reels or stories.'),
                ('Story highlights covering services, reviews, and FAQs', 'Saved story collections pinned to your Instagram profile covering key information a new visitor would want.'),
                ('Branded hashtag strategy in use', 'A defined set of hashtags used consistently across posts to improve discoverability.'),
            ]),
        section('s4', 4, 'Retention &amp; loyalty marketing',
            'Keeping an existing client costs significantly less than finding a new one. Most salons focus almost entirely on acquisition and underinvest in the systems that keep clients coming back and referring others.',
            [
                ('Email or SMS reminder and follow-up system', 'Automated messages sent before appointments and after visits, managed through your booking software.'),
                ('Loyalty program promoted online', 'A structured rewards program for repeat clients, with details visible on your website and social profiles.'),
                ('Referral program with a clear incentive', 'A formal process for encouraging existing clients to refer friends, with a stated reward for doing so.'),
                ('Re-booking prompt after each appointment', 'A system or process that prompts clients to book their next appointment before or shortly after they leave.'),
            ]),
        section('s5', 5, 'Paid advertising',
            'Organic reach is valuable but limited. Paid advertising lets you reach new clients in your area at the exact moment they are looking, and keeps your salon visible to past visitors who have not yet rebooked.',
            [
                ('Google Ads targeting local search terms', 'Paid search ads that appear when someone in your area searches for a salon or specific service.'),
                ('Meta Ads targeting local clients', 'Paid ads on Facebook and Instagram targeted by suburb, age, and interests relevant to your services.'),
                ('Seasonal promotion campaigns planned', "Paid campaigns built around key dates such as Valentine's Day, Mother's Day, and Christmas."),
                ('Remarketing to previous website visitors', 'Ads shown specifically to people who visited your website but did not book an appointment.'),
            ]),
    ],
    tip='the fundamentals carry the most weight here. A complete Google Business Profile, a steady stream of reviews, and an active Instagram presence will outperform a paid campaign every time for a new or growing salon. Get those right before spending on ads.',
    verdicts=[
        (0, 3, "Work through the checklist above to see your result."),
        (4, 8, "There is a lot of ground to cover. Most of these gaps are fixable within a few months."),
        (9, 12, "Solid foundations in place. The remaining gaps are likely costing you bookings you do not know you are losing."),
        (13, 17, "Good shape overall. A handful of items here could shift your results meaningfully."),
        (18, 20, "Strong presence. You are ahead of most local salons. The remaining items are worth a conversation."),
        (21, 22, "Very strong. Let us talk about where you want to take it from here."),
    ],
    js_counts=[5, 5, 5, 4, 4],
)

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/beauty-salons.html', 'w', encoding='utf-8') as f:
    f.write(beauty)
print('beauty-salons done')

# ── INTERIOR DESIGNERS ─────────────────────────────────────────────────
interior = make_html(
    title='Digital Presence Checklist — Interior Designers',
    meta_desc='Let your portfolio do the selling. This checklist shows where your digital presence stands and what to fix to attract better enquiries.',
    h1='Interior designers',
    p1='Most interior designers have good work and a reasonable Instagram following. The problem is that great work alone does not generate a consistent enquiry pipeline. The designers who stay busy have their digital presence working across multiple channels at once.',
    p2='This checklist covers <strong>23 items across five areas</strong>, your website and portfolio, local SEO, social content, thought leadership, and lead nurture. Work through it honestly. The gaps you find are where potential clients are choosing someone else.',
    market='Melbourne, Victoria',
    sections_list=[
        section('s1', 1, 'Website &amp; portfolio',
            'For an interior designer, the website is the portfolio. It is usually the first and most important thing a potential client looks at before making contact. A site that is slow, hard to navigate, or visually underwhelming will lose that client before they reach the enquiry form.',
            [
                ('Visually strong, mobile-optimised website', 'A professionally designed site that loads quickly and presents your work well on both desktop and mobile.'),
                ('Project pages with before and after details', 'Individual pages for completed projects, each with images, a project description, and the scope of work involved.'),
                ('Separate service pages for residential, commercial, and styling', 'Distinct pages for each service type you offer, rather than a single combined services listing.'),
                ('Clear enquiry process and consultation CTA', 'A defined pathway on the website that tells a visitor exactly how to start working with you.'),
                ('Fast page load speed with optimised images', 'Images compressed and formatted so they load quickly without compromising visual quality.'),
            ]),
        section('s2', 2, 'Local SEO &amp; discovery',
            'High-value design clients often search locally before reaching out. Being visible in those searches, on Google, on Houzz, and on Pinterest, puts you in front of people at the moment they are actively looking for a designer.',
            [
                ('Google Business Profile with project photos', 'A complete and verified Google listing that includes photos of completed projects and a full business description.'),
                ('"Interior designer [city or suburb]" keyword pages', 'Website pages written specifically around your location and service type, targeting local search terms.'),
                ('Houzz profile fully built out', 'A complete profile on Houzz including project photos, business details, reviews, and contact information.'),
                ('Google reviews from past clients', 'Reviews on your Google Business Profile from clients who have worked with you, with a response on each.'),
                ('Pinterest business account active', 'A Pinterest account used to publish project imagery and mood boards, organised into relevant boards by style or room type.'),
            ]),
        section('s3', 3, 'Visual content &amp; social',
            'Interior design is a visual industry. The businesses that attract high-quality enquiries consistently are the ones whose online presence reflects the standard of their work. Social media is less about volume here and more about quality and consistency.',
            [
                ('Instagram portfolio updated consistently', 'An Instagram profile with regular posts showcasing completed projects, work in progress, and design details.'),
                ('Reels showing project reveals and transformation videos', 'Short videos published as reels that show the before and after of a completed space.'),
                ('Pinterest boards organised by style and room type', 'A structured Pinterest account with boards grouped by aesthetic or space type, used to attract clients with specific tastes.'),
                ('Behind-the-scenes process content', 'Content showing the working process, such as sourcing, site visits, and mood board development.'),
                ('Collaboration content with suppliers and builders', 'Posts or stories that feature the tradespeople and suppliers you work with, published to both accounts.'),
            ]),
        section('s4', 4, 'Thought leadership &amp; SEO content',
            'Publishing useful content builds search visibility over time and positions you as the credible choice for a client who is still in the research phase. For high-value projects, clients often spend weeks or months researching before reaching out.',
            [
                ('Blog covering design trends, how-to guides, and room tips', 'Regular articles published on your website covering topics relevant to people planning an interior project.'),
                ('Style quiz or free consultation as a lead magnet', 'A free resource or interactive tool on the website that captures contact details from interested visitors.'),
                ('Video walkthroughs of completed projects', 'Short videos taken inside finished spaces, published on the website and social channels.'),
                ('Houzz ideabooks and articles published', 'Content published directly on Houzz, including ideabooks and written articles relevant to your services.'),
            ]),
        section('s5', 5, 'Lead nurture &amp; referrals',
            'Design projects often have long lead times. A client might enquire months before they are ready to commit. Having systems that stay in touch with warm leads and encourage referrals from past clients is how consistent pipelines are built.',
            [
                ('Email nurture for the consultation-to-quote gap', 'An email sequence that keeps in touch with enquiries who have not yet converted to a paid project.'),
                ('Meta Ads targeting homeowners in your area', 'Paid ads on Facebook and Instagram targeted by location, homeownership status, and renovation-related interests.'),
                ('Past client referral and testimonial strategy', 'A process for requesting testimonials and referrals from completed project clients.'),
                ('Builder, architect, and real estate partnership strategy', 'A structured approach to building referral relationships with complementary professionals.'),
                ('Seasonal campaign around renovation and new home season', 'Marketing activity timed around periods when clients are most likely to be planning a new project.'),
            ]),
    ],
    tip='the fundamentals carry the most weight. A strong website with real project pages, a verified Google Business Profile with reviews, and an active Houzz presence will bring in more enquiries than any paid campaign for most designers. Get those right before spending on ads.',
    verdicts=[
        (0, 3, "Work through the checklist above to see your result."),
        (4, 8, "There is a lot of ground to cover. Most of these gaps are fixable within a few months."),
        (9, 12, "Solid foundations in place. The remaining gaps are likely costing you enquiries you do not know you are losing."),
        (13, 17, "Good shape overall. A handful of items here could shift your pipeline meaningfully."),
        (18, 21, "Strong presence. You are ahead of most local designers. The remaining items are worth a conversation."),
        (22, 23, "Very strong. Let us talk about where you want to take it from here."),
    ],
    js_counts=[5, 5, 5, 4, 5],
)

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/interior-designers.html', 'w', encoding='utf-8') as f:
    f.write(interior)
print('interior-designers done')

# ── LEGAL ──────────────────────────────────────────────────────────────
legal = make_html(
    title='Digital Presence Checklist — Legal Services',
    meta_desc='Win more instructions online — where clients search before they call. This checklist shows where your firm stands and what to fix first.',
    h1='Legal services',
    p1="Most clients search online before they call a lawyer. They compare websites, read reviews, and look at the firm's content before making contact. The practices that consistently win new instructions have invested in making that research process work in their favour.",
    p2='This checklist covers <strong>23 items across five areas</strong>, your website, local SEO, content, lead conversion, and paid advertising. Work through it honestly. The gaps you find are where potential clients are choosing another firm.',
    market='Melbourne, Victoria',
    sections_list=[
        section('s1', 1, 'Website &amp; first impressions',
            'A client searching for legal help has usually already made some kind of decision before they pick up the phone. Your website is where that decision gets confirmed or reversed. Credibility signals, clear practice areas, and an obvious path to contact are what close the gap between a visit and an enquiry.',
            [
                ('Fast, mobile-optimised professional website', 'A website that loads quickly on mobile devices and presents your firm in a professional, credible way.'),
                ('Individual practice area landing pages', 'A dedicated page for each area of law you practise, covering what the service involves and who it is for.'),
                ('Solicitor or barrister bio pages with a photo', 'Individual profile pages for each lawyer at the firm, including a photo, background, and areas of specialisation.'),
                ('Clear and prominent contact and consultation CTA', 'A visible call to action on every page that makes it easy for a visitor to get in touch or book a consultation.'),
                ('Trust signals including awards, memberships, and results', 'Visible indicators of credibility such as Law Institute membership, awards, or notable case outcomes.'),
            ]),
        section('s2', 2, 'Local SEO',
            'Most people searching for a lawyer start on Google. The firms that appear in local results are not always the largest or most experienced — they are the ones that have invested in their local search presence. This is one of the highest-return areas for a legal practice.',
            [
                ('Google Business Profile fully optimised', 'A complete and verified Google listing with photos, practice areas, hours, and a full business description.'),
                ('Practice area and location keyword pages', 'Website pages written around specific combinations of service and location, such as family lawyer in your suburb.'),
                ('50+ Google reviews actively managed', 'Reviews on your Google Business Profile with a response from the firm on each one.'),
                ('Listed on legal directories such as Avvo, Justia, and FindLaw', 'Your firm listed on legal-specific directories with consistent contact details and a complete profile.'),
                ('Schema markup using the LegalService type', 'Structured data added to your website code that helps Google categorise and feature your firm in search results.'),
            ]),
        section('s3', 3, 'Content &amp; authority building',
            'Legal content serves two purposes: it builds trust with people who are not yet ready to call, and it keeps your firm ranking for the searches that matter. Plain-English explainers and FAQ content are particularly effective for attracting and converting research-phase visitors.',
            [
                ('Legal explainer blog written in plain English', 'Regular articles on your website that explain legal concepts and processes in accessible, jargon-free language.'),
                ('FAQ pages for each practice area', 'A page of common questions and answers for each area of law, written to match the way people actually search.'),
                ('Free guide or checklist as a lead magnet', "A downloadable resource relevant to one of your practice areas, offered in exchange for a visitor's contact details."),
                ('Video content including lawyer introductions and Q and As', 'Short videos where lawyers introduce themselves or answer common client questions, published on the website.'),
                ('LinkedIn thought leadership articles', 'Long-form posts published on LinkedIn that share expertise or commentary relevant to your practice areas.'),
            ]),
        section('s4', 4, 'Lead conversion &amp; nurture',
            'Legal decisions are rarely made quickly. A client might research for weeks before making contact. Having systems that respond fast to enquiries and stay in touch with leads over time is how firms convert more of the interest they already generate.',
            [
                ('Automated response to enquiry forms within 5 minutes', 'An automatic reply sent immediately when someone submits a contact form, confirming receipt and next steps.'),
                ('Email nurture sequence for non-immediate leads', 'An automated series of emails sent to enquiries that are not yet ready to proceed, keeping the firm visible over time.'),
                ('Past client referral campaign', 'A structured outreach to past clients designed to encourage referrals, with a clear process for following up.'),
                ('Client newsletter covering relevant legal updates', 'A regular email sent to your client list covering changes in the law or firm news relevant to their situation.'),
            ]),
        section('s5', 5, 'Paid advertising',
            'Legal is one of the highest-intent categories in paid search. People searching for a lawyer are usually ready to act. Paid advertising in this space is expensive, but the value of a single new client makes it viable when campaigns are structured correctly.',
            [
                ('Google Search Ads for high-intent search terms', 'Paid ads that appear when someone searches for a lawyer or legal service in your area.'),
                ('Meta Ads targeting relevant audiences', 'Paid ads on Facebook and Instagram targeted by location, life events, and interests relevant to your practice areas.'),
                ('Geo-targeted campaigns by suburb or court location', 'Campaigns configured to show only to people in specific geographic areas where your clients are based.'),
                ('Remarketing to guide downloaders and website visitors', 'Ads shown to people who have already engaged with your website or downloaded a resource but have not yet made contact.'),
            ]),
    ],
    tip='the highest-impact items here are your Google Business Profile, your review count, and your practice area pages. These are what clients look at first and what Google uses to rank you. Get those right before investing in paid search.',
    verdicts=[
        (0, 3, "Work through the checklist above to see your result."),
        (4, 8, "There is a lot of ground to cover. Most of these gaps are fixable within a few months."),
        (9, 12, "Solid foundations in place. The remaining gaps are likely costing you instructions you do not know you are losing."),
        (13, 17, "Good shape overall. A handful of items here could shift your results meaningfully."),
        (18, 20, "Strong presence. You are ahead of most local firms. The remaining items are worth a conversation."),
        (21, 23, "Very strong. Let us talk about where you want to take it from here."),
    ],
    js_counts=[5, 5, 5, 4, 4],
)

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/legal.html', 'w', encoding='utf-8') as f:
    f.write(legal)
print('legal done')

# ── OSTEOPATHS ─────────────────────────────────────────────────────────
osteo = make_html(
    title='Digital Presence Checklist — Osteopaths &amp; Allied Health',
    meta_desc='Build trust, grow patient enquiries, and fill your appointment book. This checklist shows where your practice stands and what to fix first.',
    h1='Osteopaths &amp; allied health',
    p1='Most patients research a health practitioner online before booking. They check your website, read your reviews, and look at your practitioners before picking up the phone. The practices that consistently attract new patients have their digital presence working across every step of that process.',
    p2='This checklist covers <strong>23 items across five areas</strong>, your website, local SEO, educational content, social media, and patient retention. Work through it honestly. The gaps you find are where patients are choosing another practice.',
    market='Melbourne, Victoria',
    sections_list=[
        section('s1', 1, 'Website &amp; patient experience',
            'Most patients research a health practitioner online before booking. Your website is where that research happens. A site that is hard to navigate, missing online booking, or lacking information about conditions you treat will push patients toward a practice that has those things in place.',
            [
                ('Professional, mobile-optimised website', 'A website that presents the practice clearly on all devices, with easy access to booking, contact details, and practitioner information.'),
                ('Online appointment booking or request form', 'A tool on the website that allows patients to book or request an appointment without needing to call.'),
                ('Conditions treated page with relevant keywords', 'A page or section listing the conditions the practice treats, written with the search terms patients actually use.'),
                ('Practitioner bios with credentials and a photo', 'Individual profile pages for each practitioner including their qualifications, areas of focus, and a professional photo.'),
                ('AHPRA compliant content throughout the site', 'All health claims and testimonials on the website reviewed to ensure they meet AHPRA advertising guidelines.'),
            ]),
        section('s2', 2, 'Local SEO &amp; Google presence',
            'Health searches are highly local. When someone searches for an osteopath or physio, they are usually looking for someone nearby. A well-optimised local search presence is one of the most direct ways to fill appointment slots from new patients.',
            [
                ('Google Business Profile verified and complete', 'A fully completed and verified Google listing including photos, services, opening hours, and a booking link.'),
                ('Review strategy actively managed', 'A consistent process for requesting and responding to Google reviews from patients.'),
                ('Location-specific service pages', 'Website pages written for the suburbs your practice serves, targeting location-based searches.'),
                ('Schema markup using health and medical types', 'Structured data added to the website that helps Google categorise and feature your practice in health-related searches.'),
                ('Listed on Healthengine, HotDoc, and relevant directories', 'Your practice listed on health-specific booking platforms and directories with complete and consistent information.'),
            ]),
        section('s3', 3, 'Authority &amp; trust content',
            'Patients choose practitioners they trust. Educational content builds that trust before a patient has ever set foot in the clinic. It also keeps the practice ranking for the condition and treatment searches that bring in new appointments.',
            [
                ('Blog or educational content published monthly', 'Regular articles on the website covering conditions, treatments, exercises, and health topics relevant to your patient base.'),
                ('FAQ page answering common patient questions', 'A page of questions and answers covering what patients typically ask before their first appointment.'),
                ('Video content including exercises and condition explanations', 'Short videos demonstrating exercises or explaining common conditions, published on the website or social channels.'),
                ('Patient success stories with appropriate consent', 'Written or video accounts from patients describing their experience and outcomes, published with their permission.'),
            ]),
        section('s4', 4, 'Social media',
            'Social media for health practices is less about selling and more about staying visible and building familiarity. Consistent, educational content across the right platforms keeps your practice top of mind for existing patients and discoverable to new ones.',
            [
                ('LinkedIn profile for professional referrals', 'A complete LinkedIn profile for the practice and lead practitioners, used to maintain visibility with GPs and specialists.'),
                ('Facebook page with educational posts', 'An active Facebook page publishing health education content relevant to the conditions you treat.'),
                ('Instagram for behind-the-scenes and health tips', 'An Instagram account used to share practitioner content, clinic updates, and short health tips.'),
                ('Consistent posting and community responses', 'A regular posting schedule maintained across platforms, with replies to comments and messages.'),
            ]),
        section('s5', 5, 'Patient retention &amp; referrals',
            'Acquiring a new patient costs more than keeping an existing one. Practices that retain patients long-term and generate referrals from their existing base have systems in place that make both happen consistently, not just when someone remembers to ask.',
            [
                ('Automated appointment reminder system', 'Automated messages sent to patients before their scheduled appointment via SMS or email.'),
                ('Post-treatment follow-up email or SMS', 'An automated message sent after an appointment checking in with the patient and prompting re-booking.'),
                ('Meta Ads targeting local residents', 'Paid ads on Facebook and Instagram targeted by suburb and health-related interests, used to attract new patients.'),
                ('GP and specialist referral strategy with an online presence', 'A referral page on the website and a LinkedIn presence designed to support relationships with referring practitioners.'),
                ('Email newsletter with health tips and clinic updates', 'A regular email sent to your patient list covering health content relevant to the conditions you treat.'),
            ]),
    ],
    tip='the fundamentals matter most here. A complete Google Business Profile, a consistent review strategy, and online booking will drive more new patient enquiries than almost anything else. Get those in place before investing in paid advertising or more advanced content.',
    verdicts=[
        (0, 3, "Work through the checklist above to see your result."),
        (4, 8, "There is a lot of ground to cover. Most of these gaps are fixable within a few months."),
        (9, 12, "Solid foundations in place. The remaining gaps are likely costing you new patient enquiries."),
        (13, 17, "Good shape overall. A handful of items here could shift your appointment volume meaningfully."),
        (18, 21, "Strong presence. You are ahead of most local practices. The remaining items are worth a conversation."),
        (22, 23, "Very strong. Let us talk about where you want to take it from here."),
    ],
    js_counts=[5, 5, 4, 4, 5],
)

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/osteopaths.html', 'w', encoding='utf-8') as f:
    f.write(osteo)
print('osteopaths done')

# ── RECRUITMENT ────────────────────────────────────────────────────────
recruitment = make_html(
    title='Digital Presence Checklist — Recruitment Agencies',
    meta_desc='Win more clients and attract better candidates with a stronger digital presence. This checklist shows where your agency stands and what to fix first.',
    h1='Recruitment agencies',
    p1='Most recruitment agencies rely heavily on LinkedIn and word of mouth. Those channels work, but they have limits. The agencies that grow consistently have a digital presence that works for both audiences — attracting employer clients and quality candidates at the same time.',
    p2='This checklist covers <strong>22 items across five areas</strong>, your website, local SEO, social presence, CRM marketing, and paid advertising. Work through it honestly. The gaps you find are where your competitors are winning the briefs and the candidates you should be getting.',
    market='Melbourne, Victoria',
    sections_list=[
        section('s1', 1, 'Website &amp; dual audience',
            'Recruitment websites serve two very different audiences at once — employers looking for a partner and candidates looking for a role. A site that does not clearly speak to both, with separate pathways and relevant content for each, tends to convert neither well.',
            [
                ('Separate pathways for employers and candidates', 'Distinct navigation routes and landing pages for each audience, making it clear where each type of visitor should go.'),
                ('Industry and sector specialisation pages', 'Dedicated pages for each sector or discipline you recruit in, outlining your expertise and approach in that area.'),
                ('Consultant profiles with LinkedIn links', 'Individual profile pages for each consultant including their sector focus, background, and a link to their LinkedIn profile.'),
                ('Live job board integrated on the site', 'A current list of active roles hosted on the website, updated regularly and searchable by candidates.'),
                ('Client success stories and placement case studies', 'Examples of successful placements or recruitment projects, published with enough detail to demonstrate your capability.'),
            ]),
        section('s2', 2, 'Local &amp; sector SEO',
            'Employers searching for a recruitment partner and candidates searching for roles both start on Google. Ranking well for the right combination of sector and location is how agencies get found by the clients and candidates that matter most.',
            [
                ('Google Business Profile active and complete', 'A verified Google listing with photos, services, office hours, and a full business description.'),
                ('"Recruitment agency [sector] [city]" keyword pages', 'Website pages targeting specific combinations of sector and location that your ideal clients and candidates would search for.'),
                ('Blog covering hiring guides and salary surveys', 'Regular content published on the website around recruitment topics, with salary data being particularly effective for search and sharing.'),
                ('LinkedIn Company Page active and posting regularly', 'A company page on LinkedIn with regular posts covering industry news, roles, and thought leadership content.'),
                ('Listed on industry directories and job boards', 'Your agency listed on platforms such as Seek, Indeed, and relevant industry directories with consistent contact details.'),
            ]),
        section('s3', 3, 'Social &amp; employer branding',
            'In recruitment, trust is built before a conversation happens. The agencies that win the best clients and attract the best candidates are the ones whose online presence consistently reflects their expertise and culture. LinkedIn is the primary platform, but it works alongside everything else.',
            [
                ('LinkedIn organic strategy for team and company', 'A coordinated approach to content on LinkedIn, with both the company page and individual consultants posting regularly.'),
                ('Candidate success stories published regularly', 'Posts or articles featuring the outcomes of successful placements, with appropriate detail and a quote where possible.'),
                ('Employer brand content aimed at client attraction', "Content that demonstrates understanding of the employer's challenges, such as hiring market insights or sector commentary."),
                ('Job ads formatted for social sharing', 'Active roles written and formatted in a way that makes them easy to share on LinkedIn and other platforms.'),
            ]),
        section('s4', 4, 'Database &amp; CRM marketing',
            "A recruitment agency's database is one of its most valuable assets. The agencies that place faster and retain clients longer are the ones that stay in regular, relevant contact with both candidates and clients — not just when they have a role to fill.",
            [
                ('Candidate email newsletter covering new roles and market tips', 'A regular email sent to active and passive candidates in your database with relevant roles and industry content.'),
                ('Client email nurture covering market insights and hiring tips', 'A regular email sent to existing and prospective clients covering recruitment market data, salary benchmarks, or hiring guides.'),
                ('Automated job alert system for candidates', 'An automated notification sent to registered candidates when a new role matching their profile is listed.'),
                ('Quarterly salary or market report emailed to clients', 'A structured report covering salary benchmarks and market conditions in your sector, sent on a regular cadence.'),
            ]),
        section('s5', 5, 'Paid advertising',
            'Paid advertising in recruitment serves two functions: attracting employer clients and attracting candidates. Both require different platforms and targeting strategies. LinkedIn is typically most effective for hiring managers, while Google and Meta work better for candidate attraction.',
            [
                ('LinkedIn Ads targeting hiring managers and HR leaders', 'Paid ads on LinkedIn targeted by job title, company size, and industry to reach the people who make recruitment decisions.'),
                ('Google Ads for candidate and employer searches', 'Paid search ads appearing when candidates search for roles or employers search for recruitment services in your area.'),
                ('Meta Ads targeting passive candidates and local employers', 'Paid ads on Facebook and Instagram targeted by job title, industry, and location to reach people not actively job searching.'),
                ('Remarketing to employers and candidates who visited the site', 'Ads shown to people who visited your website but did not submit a role brief or register as a candidate.'),
            ]),
    ],
    tip='the items that move the needle fastest are your LinkedIn presence, your sector-specific website pages, and your database marketing. Most agencies underinvest in all three. Get those working well before spending on paid advertising.',
    verdicts=[
        (0, 3, "Work through the checklist above to see your result."),
        (4, 8, "There is a lot of ground to cover. Most of these gaps are fixable within a few months."),
        (9, 12, "Solid foundations in place. The remaining gaps are likely costing you clients and placements."),
        (13, 17, "Good shape overall. A handful of items here could shift your pipeline meaningfully."),
        (18, 20, "Strong presence. You are ahead of most local agencies. The remaining items are worth a conversation."),
        (21, 22, "Very strong. Let us talk about where you want to take it from here."),
    ],
    js_counts=[5, 5, 4, 4, 4],
)

with open('G:/My Drive/Claude Code.Locate/_guides/checklists/recruitment.html', 'w', encoding='utf-8') as f:
    f.write(recruitment)
print('recruitment done')

print('\nAll 5 files complete.')
