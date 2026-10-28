// About us and our team (canvas/Team.dc.html)
const { esc, enquire, photo, ctaBand } = require('../partials');

module.exports = (C, R) => ({
  title: "About us and our team | Harlow Home Loans",
  description: "Harlow Home Loans is a small, family-run mortgage broking team in Melbourne. Meet Claire, Tom, Priya and Mia.",
  active: "about",
  drawerDefaults: {"source":"Team page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap phero-grid">
<div>
<h1 class="h1 hero-in" id="ph-h">A small team that knows Melbourne</h1>
<p class="lead hero-in" style="--d: 80ms">Harlow Home Loans is a family-run broking team helping people across Melbourne since <span class="ph">[PLACEHOLDER 2011]</span>. We're small on purpose: you deal with the same broker from your first chat to settlement, and every year after.</p>
<div class="ctas hero-in" style="--d: 160ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
</div>
<div class="phero-photo" style="aspect-ratio: 3 / 2">${photo({"src":"images/team.jpg","alt":"The Harlow Home Loans team outside their office","width":1024,"height":688,"loading":"eager"})}</div>
</div>
</section>

<section class="band band-card" aria-labelledby="tm-h">
<div class="wrap">
<div class="intro rv focus">
<h2 class="h2" id="tm-h">Meet the <em class="ul">team</em></h2>
<p class="lead">Three brokers and one very organised support lead. Between us we speak five languages.</p>
</div>
<div style="display: grid; gap: 32px; grid-template-columns: repeat(auto-fit, minmax(min(240px, 100%), 1fr))">
${C.team.map((t, i) => `<article class="rv focus" style="--d: ${i * 70}ms; display: flex; flex-direction: column; gap: 6px">
<a href="${t.href}" class="portrait lift" style="display: block; margin-bottom: 12px" aria-label="${esc(t.name)}, view profile">${photo({ src: 'images/' + t.id + '.jpg', alt: t.name, width: 236, height: 295 })}</a>
<b style="font-size: 18px; line-height: 24px; color: #14204A">${esc(t.name)}</b>
<span style="font-size: 16px; line-height: 22px">${esc(t.role)}</span>
<span class="cap">${esc(t.languages.join(', '))}</span>
<div class="row" style="gap: 0 18px; margin-top: 2px">
${t.books ? `<button type="button" class="textlink" ${enquire({ broker: t.id })}>Book with ${esc(t.first)}</button>` : ''}
<a class="textlink" href="${t.href}" style="color: #2E3A5C">Profile</a>
</div>
</article>`).join('\n')}
</div>
</div>
</section>

<section class="band band-w1" aria-labelledby="why-h">
<div class="wrap">
<div class="intro rv fade">
<h2 class="h2" id="why-h">Advice you can <em class="ul">trust</em></h2>
<p class="lead">The way we work, written down so you can hold us to it.</p>
</div>
<ol class="olist two">
<li class="rv fade" style="--d: 0ms"><span class="n">01</span><b>Your interests come first, by law.</b><p>Brokers must act in your best interests, and we'll show you why we recommend a loan.</p></li>
<li class="rv fade" style="--d: 60ms"><span class="n">02</span><b>We show you how we're paid.</b><p>${esc(C.compliance.feePolicy)}</p></li>
<li class="rv fade" style="--d: 120ms"><span class="n">03</span><b>A shortlist, not a sales pitch.</b><p>We compare <span class="ph">[PLACEHOLDER 30+]</span> lenders and explain the trade-offs side by side.</p></li>
<li class="rv fade" style="--d: 180ms"><span class="n">04</span><b>After hours when you need it.</b><p>Evening video calls and Saturday appointments.</p></li>
<li class="rv fade" style="--d: 240ms"><span class="n">05</span><b>We don't disappear after settlement.</b><p>A free loan review every year, so you're not left on an old rate.</p></li>
<li class="rv fade" style="--d: 300ms"><span class="n">06</span><b>In your language.</b><p>Appointments in English, Mandarin, Hindi, Gujarati and Vietnamese.</p></li>
</ol>
</div>
</section>

<section class="band" aria-labelledby="of-h">
<div class="wrap grid-2" style="align-items: center">
<div class="rv rise">
<h2 class="h2" id="of-h">Come and <em class="ul">see</em> us</h2>
<p class="lead">Meet at our office, at your kitchen table, or on video. Whatever's easiest.</p>
<div class="kv" style="margin-top: 24px">
<div><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"></path><circle cx="12" cy="9.5" r="2.5"></circle></svg><span><span class="ph">[PLACEHOLDER street address]</span>, ${esc(C.contact.office)}</span></div>
<div><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path></svg><span>${esc(C.hours)}</span></div>
<div><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10.5 12 4l9 6.5"></path><path d="M5 9.5V20h14V9.5"></path></svg><span>Home visits across Melbourne, by appointment</span></div>
</div>
</div>
<div class="photo r43 rv rise" style="--d: 100ms">${photo({"src":"images/street.jpg","alt":"A tree-lined street of period homes at golden hour","width":1344,"height":752})}</div>
</div>
</section>

${ctaBand(C, {"prefill":{"source":"Team page"}})}`,
});
