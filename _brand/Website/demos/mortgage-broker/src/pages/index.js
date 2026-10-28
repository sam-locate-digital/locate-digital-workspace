// Homepage (canvas/Main.dc.html)
const { esc, enquire, ICON, photo, contactAside, inlineForm, reviewRail } = require('../partials');
const { IMG, ICONS } = require('../assets');

const SITS = [
  { icon: ICONS.firstHome, title: 'Buying my first home', line: 'Deposits, schemes, pre-approval, and what to do on auction day.', img: IMG.first, alt: 'First home buyers holding their new keys', href: 'first-home.html' },
  { icon: ICONS.nextHome, title: 'Buying my next home', line: 'Buying before you sell, bridging finance and moving your equity.', img: IMG.next, alt: 'A family exploring the backyard of their next home', href: 'next-home.html' },
  { icon: ICONS.refinance, title: 'Refinancing', line: 'Check your rate, cut fees, or free up equity for a renovation.', img: IMG.refi, alt: 'A homeowner relaxed after reviewing his home loan', href: 'refinancing.html' },
  { icon: ICONS.invest, title: 'Investing', line: 'Structuring a loan for your first or next investment property.', img: IMG.invest, alt: 'A woman looking at new townhouses as an investment', href: 'investing.html' },
  { icon: ICONS.selfEmployed, title: 'Self-employed', line: 'Lenders who understand business income, even with a short trading history.', img: IMG.why, alt: 'A Harlow broker talking through loan options with a couple at their dining table', href: 'self-employed.html' },
];
const STEPS = [
  { icon: ICONS.chat, title: 'A free 20-minute chat', body: "Phone, video or at our office. We work out where you stand and what's possible.", img: IMG.s1, alt: 'A woman on a first call with her broker' },
  { icon: ICONS.compare, title: 'We compare lenders for you', body: 'We shortlist loans that fit your situation and show you the trade-offs side by side.', img: IMG.s2, alt: 'A broker comparing loan options at his desk' },
  { icon: ICONS.approval, title: 'Pre-approval in hand', body: 'We handle the application and keep you posted, so you can bid with confidence.', img: IMG.s3, alt: 'A couple reading good news on their phone' },
  { icon: ICONS.settle, title: 'Settled, then reviewed every year', body: 'We line up settlement with your solicitor, then check your loan every year.', img: IMG.s4, alt: 'A couple carrying boxes into their new home' },
];
const WHY = [
  ['Your interests come first, by law.', "Brokers must act in your best interests, and we'll show you why we recommend a loan."],
  ["We show you how we're paid.", "Usually the lender pays us. You'll see the amount before you choose."],
  ['A shortlist, not a sales pitch.', 'We compare <span class="ph">[PLACEHOLDER 30+]</span> lenders and explain the trade-offs side by side.'],
  ['After hours when you need it.', 'Evening video calls and Saturday appointments.'],
  ["We don't disappear after settlement.", "A free loan review every year, so you're not left on an old rate."],
  ['In your language.', 'Appointments in English, Mandarin, Hindi, Gujarati and Vietnamese.'],
];
const FAQ = [
  ['What does a mortgage broker cost?', 'Usually nothing. Lenders pay us a commission when your loan settles, and we\'ll show you how much before you choose. <span class="ph">[PLACEHOLDER: confirm fee policy]</span>'],
  ['How much can I borrow?', "It depends on your income, expenses, debts, deposit and each lender's rules. We'll give you a rough figure in your free chat, then check it properly against real lender rules."],
  ['Will talking to you affect my credit score?', "No. A first chat and estimate don't involve a credit check."],
  ['What deposit do I need?', "Often 5 to 20% of the price, depending on the lender and any scheme you qualify for. We'll check what applies to you."],
  ['When should I refinance?', "When a fixed rate is ending, your rate hasn't been reviewed in a while, or you want to access equity. We'll tell you if it isn't worth it."],
  ['How long does pre-approval take?', 'Often a few days to two weeks, depending on the lender and your paperwork.'],
  ['Do you work with self-employed people?', 'Yes, including sole traders and new businesses. <a href="self-employed.html">See how we help self-employed borrowers</a>.'],
];
const AWARD = '<svg class="aw-mark" width="44" height="40" viewBox="0 0 44 40" fill="none" aria-hidden="true"><path d="M14 36C7 32 3 25 4 16M30 36c7-4 11-11 10-20" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><path d="M6.5 27c-3-.5-4.6-2.6-4.8-5 2.6-.4 4.6 1 5.4 3.4M5 20c-2.8-1.2-3.8-3.6-3.4-6 2.6.2 4.2 2.1 4.4 4.6M5.6 12.8C3.4 10.8 3 8.2 4 6c2.4.9 3.4 3.1 3 5.6M37.5 27c3-.5 4.6-2.6 4.8-5-2.6-.4-4.6 1-5.4 3.4M39 20c2.8-1.2 3.8-3.6 3.4-6-2.6.2-4.2 2.1-4.4 4.6M38.4 12.8c2.2-2 2.6-4.6 1.6-6.8-2.4.9-3.4 3.1-3 5.6" fill="currentColor"/><path d="M22 9.5l2.1 4.3 4.7.7-3.4 3.3.8 4.7-4.2-2.2-4.2 2.2.8-4.7-3.4-3.3 4.7-.7Z" fill="var(--amber)"/></svg>';
const PM = '<span class="pm" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg></span>';

module.exports = (C, R) => {
  const { phone, phoneHref } = C.contact;
  return {
    title: 'Harlow Home Loans | Melbourne mortgage brokers',
    description: 'Melbourne mortgage brokers helping first home buyers, upgraders, refinancers, investors and self-employed borrowers.',
    jsonLd: { '@context': 'https://schema.org', '@type': ['FinancialService', 'LocalBusiness'], name: 'Harlow Home Loans', telephone: '+61355502861', email: C.contact.email, address: { '@type': 'PostalAddress', streetAddress: '[PLACEHOLDER]', addressLocality: '[PLACEHOLDER]', addressRegion: 'VIC', postalCode: '[PLACEHOLDER]', addressCountry: 'AU' }, areaServed: 'Melbourne', openingHours: 'Mo-Fr 08:30-18:00' },
    body: `
<!-- Hero -->
<section class="hero" id="hero" aria-labelledby="hero-h">
<div class="hero-frame on-photo">
${photo({ cls: 'hero-img', src: IMG.hero, alt: 'A couple playing with their toddler in the living room of their new home', width: 1344, height: 752, loading: 'eager' })}
<div class="hero-copy">
<h1 class="h1 hero-in" id="hero-h">Your next <em class="ul">move</em>, made simple.</h1>
<p class="hero-sub hero-in" style="--d: 80ms"><span>Melbourne mortgage brokers.</span><span>We compare <span class="ph">[PLACEHOLDER 30+]</span> lenders and do the legwork, usually at no cost to you.</span></p>
<div class="ctas hero-in" style="--d: 160ms; justify-content: center">
<button type="button" class="btn btn-primary btn-lg" ${enquire({ source: 'Homepage hero' })}>Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="${phoneHref}">Call ${esc(phone)}</a>
</div>
<p class="micro hero-in" style="--d: 240ms"><span>Free 20-minute chat</span><i aria-hidden="true">│</i><span>No credit check</span><i aria-hidden="true">│</i><span>Evening and Saturday times</span></p>
</div>
<div class="wrap hero-stats hero-in" style="--d: 320ms" data-odo-root data-target="${C.stats.settledMillions}">
<div class="stat"><b>4.9 ★</b><span>Google rating, from 280 reviews</span><i>[PLACEHOLDER]</i></div>
<div class="stat"><b><span data-odo aria-hidden="true">$${C.stats.settledMillions}m</span><span class="sr">640 million dollars, placeholder figure</span></b><span>in home loans settled</span><i>[PLACEHOLDER]</i></div>
<div class="stat"><b>30+</b><span>lenders compared</span><i>[PLACEHOLDER]</i></div>
</div>
</div>
</section>

<!-- Situations -->
<section class="band" aria-labelledby="sit-h">
<div class="wrap">
<div class="intro">
<h2 class="h2" id="sit-h">Where are you at?</h2>
<p class="lead">Every situation needs a different loan. Start with yours.</p>
</div>
<div class="sit" data-sit>
<ul class="sit-list">
${SITS.map((s, i) => `<li class="rv fade" style="--d: ${i * 60}ms">
<a class="sit-row${i === 0 ? ' on' : ''}" href="${s.href}">
<img class="sit-ic" src="${s.icon}" alt="" width="240" height="240" loading="lazy">
<b>${s.title}</b>
<p>${s.line}</p>
<span class="arr" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m13 6 6 6-6 6"></path></svg></span>
${photo({ src: s.img, alt: s.alt, width: 1168, height: 876 })}
</a>
</li>`).join('\n')}
</ul>
<div class="sit-photo rv fade" aria-hidden="true">
${SITS.map((s, i) => photo({ cls: i === 0 ? 'on' : '', src: s.img, alt: '', width: 1168, height: 876 })).join('')}
</div>
</div>
</div>
</section>

<!-- How it works -->
<section class="band band-card" aria-labelledby="how-h" data-steps>
<div class="wrap steps">
<div class="step-photo rv focus">
${STEPS.map((st, i) => photo({ cls: i === 0 ? 'on' : '', src: st.img, alt: st.alt, width: 896, height: 1120 })).join('')}
</div>
<div class="rv focus" style="--d: 100ms">
<h2 class="h2" id="how-h">How we <em class="ul">work</em> with you</h2>
<div class="step-list" style="margin-top: 32px">
${STEPS.map((st, i) => `<button type="button" class="step" aria-expanded="${i === 0}" aria-controls="step-body-${i}">
<span class="step-top"><img class="step-ic" src="${st.icon}" alt="" width="240" height="240" loading="lazy"><span class="step-t"><small>Step 0${i + 1}</small>${st.title}</span></span>
<span class="step-b" id="step-body-${i}" style="display: block"${i ? ' hidden' : ''}>${st.body}</span>
<span class="prog" aria-hidden="true" style="display: block"${i ? ' hidden' : ''}><i></i></span>
</button>`).join('\n')}
</div>
<div class="row" style="margin-top: 28px">
<button type="button" class="btn btn-primary" ${enquire({ source: 'How it works' })}>Book a free chat</button>
<a class="textlink" href="${phoneHref}">Or call ${esc(phone)}</a>
</div>
</div>
</div>
</section>

<!-- Reviews -->
<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, { hLead: "Clients who've ", hBrush: 'made', hTail: ' their move' })}
<p style="margin-top: 4px"><a class="textlink" href="reviews.html">Read all reviews ${ICON.arrow16}</a></p>
</div>
</section>

<!-- Why Harlow -->
<section class="band band-w1" aria-labelledby="why-h">
<div class="wrap">
<div class="grid-2" style="align-items: center">
<div class="photo r43 rv fade">
${photo({ src: IMG.why, alt: 'A Harlow broker talking through loan options with a couple at their dining table', width: 1120, height: 840 })}
</div>
<div class="rv fade" style="--d: 80ms">
<h2 class="h2" id="why-h">Advice you can <em class="ul">trust</em></h2>
<p class="lead">The way we work, written down so you can hold us to it.</p>
</div>
</div>
<ol class="olist three" style="margin-top: 48px">
${WHY.map(([b, p], i) => `<li class="rv fade" style="--d: ${i * 60}ms"><span class="n">0${i + 1}</span><b>${b}</b><p>${p}</p></li>`).join('\n')}
</ol>
<div class="awards" aria-labelledby="aw-h">
<h3 class="h3 rv fade" id="aw-h">Awards and recognition</h3>
<ul class="aw-list">${[0, 1, 2, 3].map((i) => `<li class="rv rise" style="--d: ${i * 70}ms">${AWARD}<b>Award name <span class="ph">[PLACEHOLDER]</span></b><p>Awarding body · Year <span class="ph">[PLACEHOLDER]</span></p></li>`).join('')}</ul>
<p class="cap rv fade">Placeholder. Add the broker's real awards here, with the year and awarding body, or remove this row before launch.</p>
</div>
</div>
</section>

<!-- Team -->
<section class="band" aria-labelledby="team-h">
<div class="wrap">
<div class="intro intro-row rv from-l">
<div>
<h2 class="h2" id="team-h">The people you'll <em class="ul">deal</em> with</h2>
<p class="lead">Four of us, one office. You'll talk to the same broker from first chat to settlement.</p>
</div>
<a class="textlink" href="team.html">Meet the team ${ICON.arrow16}</a>
</div>
<div class="photo r32 lift rv from-l" style="--d: 80ms">
${photo({ src: IMG.team, alt: 'The Harlow Home Loans team outside their office', width: 1024, height: 688 })}
</div>
<div class="about-cols">
<div class="rv from-l" style="--d: 120ms">
<b>About us</b>
<p>We're a small, family-run broking team. Since <span class="ph">[PLACEHOLDER 2011]</span> we've helped people across Melbourne buy their first home, move to their next one, refinance and invest.</p>
</div>
<div class="rv from-l" style="--d: 180ms">
<b>Why people choose us</b>
<p>You deal with the same broker from first chat to settlement. We compare <span class="ph">[PLACEHOLDER 30+]</span> lenders, explain the trade-offs in plain English and check your loan every year after it settles.</p>
</div>
</div>
</div>
</section>

<!-- Local band -->
<section class="band band-w3" aria-labelledby="area-h">
<div class="wrap">
<div class="area rv scale">
${photo({ src: IMG.street, alt: 'A tree-lined street of period homes at golden hour', width: 1344, height: 752 })}
<div class="area-copy">
<h2 class="h2" id="area-h">Local to <em class="ul">Melbourne</em></h2>
<p>Meet at our office, at your kitchen table, or on video.</p>
</div>
</div>
</div>
</section>

<!-- FAQ -->
<section class="band band-card" aria-labelledby="faq-h">
<div class="wrap two-col">
<div class="rv fade">
<h2 class="h2" id="faq-h">Questions we <em class="ul">hear</em> a lot</h2>
<p class="lead">Straight answers. If yours isn't here, ask us on a free chat.</p>
</div>
<div class="faq rv fade" style="--d: 80ms">
${FAQ.map(([q, a], i) => `<details name="faq"${i === 0 ? ' open' : ''}><summary>${q}${PM}</summary><p class="ans">${a}</p></details>`).join('\n')}
</div>
</div>
</section>

<!-- Final CTA + enquiry -->
<section class="band band-w2" aria-labelledby="cta-h" id="enquire">
<div class="wrap">
<div class="intro rv rise">
<h2 class="h2" id="cta-h">Let's work out your next <em class="ul">step</em></h2>
<p class="lead">Book a free 20-minute chat. We'll call you back within <span class="ph">[PLACEHOLDER 1 business day]</span>.</p>
</div>
<div class="cta-grid">
<div class="rv rise" style="--d: 60ms">
${inlineForm({ source: 'Homepage form' })}
</div>
${contactAside(C)}
</div>
</div>
</section>`,
  };
};
