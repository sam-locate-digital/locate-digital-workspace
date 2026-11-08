// Claire Harlow, principal broker (canvas/Claire.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Claire Harlow, principal broker | Harlow Home Loans",
  description: "Meet Claire Harlow, principal mortgage broker at Harlow Home Loans.",
  active: "about",
  drawerDefaults: {"broker":"claire","source":"Claire Harlow profile"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap profile">
<div class="portrait phero-photo" style="max-width: 420px; aspect-ratio: 4 / 5">${photo({"src":"images/claire.jpg","alt":"Claire Harlow, principal broker","width":250,"height":312,"loading":"eager"})}</div>
<div>
<a class="backlink hero-in" href="team.html"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>All of the team</a>
<h1 class="h1 hero-in" id="ph-h" style="margin-top: 8px">Claire Harlow</h1>
<p class="lead hero-in" style="--d: 60ms; margin-top: 8px; color: #14204A; font-weight: 600">Principal broker</p>
<p class="lead hero-in" style="--d: 120ms">Claire started Harlow Home Loans in <span class="ph">[PLACEHOLDER 2011]</span> after <span class="ph">[PLACEHOLDER years]</span> in bank lending, because she wanted to sit on the client's side of the table. She grew up in Melbourne, still lives in <span class="ph">[PLACEHOLDER suburb]</span>, and has a soft spot for first home buyers who think they're years away.</p>
<div class="hero-in" style="--d: 180ms; margin-top: 24px; display: grid; gap: 18px">
<div><p class="cap" style="margin-bottom: 8px">Specialities</p><div class="tags"><span class="tag">First home buyers</span><span class="tag">Self-employed borrowers</span><span class="tag">Family guarantees</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Languages</p><div class="tags"><span class="tag">English</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Credentials</p><p class="small">Member of <span class="ph">[PLACEHOLDER MFAA or FBAA]</span> · <span class="ph">[PLACEHOLDER qualifications]</span> · Credit Representative <span class="ph">[PLACEHOLDER]</span></p></div>
</div>
<div class="ctas hero-in" style="--d: 240ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book with Claire</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
</div>
</div>
</section>

<section class="band band-card" aria-labelledby="nt-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="nt-h">How Claire <em class="ul">works</em></h2>
</div>
<div class="rv focus prose" style="--d: 100ms">
<p>"Most people come to me worried they've left it too late or don't have enough saved. My first job is to give you a straight answer on where you stand, even if it's 'not yet'.</p>
<p>If we go ahead, I'll show you the shortlist, explain the trade-offs and tell you how I'm paid before you choose. Then I'll chase the paperwork so you don't have to."</p>
<p class="cap" style="margin-top: 16px">Illustrative profile for this demo. <span class="ph">[PLACEHOLDER: replace with the broker's own words]</span></p>
</div>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What clients say about ","hBrush":"Claire","hTail":"","filterKey":"broker","filterVal":"claire"})}
</div>
</section>

${ctaBand(C, {"hLead":"Book a chat with ","hBrush":"Claire","hTail":"","sub":"Phone, video or at our office.","prefill":{"broker":"claire","source":"Claire Harlow profile"}})}`,
});
