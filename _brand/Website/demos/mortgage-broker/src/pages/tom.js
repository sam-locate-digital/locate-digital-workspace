// Tom Nguyen, broker (canvas/Tom.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Tom Nguyen, broker | Harlow Home Loans",
  description: "Meet Tom Nguyen, mortgage broker at Harlow Home Loans. Appointments in English and Vietnamese.",
  active: "about",
  drawerDefaults: {"broker":"tom","source":"Tom Nguyen profile"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap profile">
<div class="portrait phero-photo" style="max-width: 420px; aspect-ratio: 4 / 5">${photo({"src":"images/tom.jpg","alt":"Tom Nguyen, broker","width":236,"height":295,"loading":"eager"})}</div>
<div>
<a class="backlink hero-in" href="team.html"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>All of the team</a>
<h1 class="h1 hero-in" id="ph-h" style="margin-top: 8px">Tom Nguyen</h1>
<p class="lead hero-in" style="--d: 60ms; margin-top: 8px; color: #14204A; font-weight: 600">Broker</p>
<p class="lead hero-in" style="--d: 120ms">Tom joined Harlow in <span class="ph">[PLACEHOLDER year]</span>. He looks after a lot of our refinancing and investment clients, and likes nothing more than finding a fee or a feature someone has been paying for without using. He works in English and Vietnamese.</p>
<div class="hero-in" style="--d: 180ms; margin-top: 24px; display: grid; gap: 18px">
<div><p class="cap" style="margin-bottom: 8px">Specialities</p><div class="tags"><span class="tag">Refinancing</span><span class="tag">Investment loans</span><span class="tag">Fixed rate expiries</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Languages</p><div class="tags"><span class="tag">English</span><span class="tag">Vietnamese</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Credentials</p><p class="small">Member of <span class="ph">[PLACEHOLDER MFAA or FBAA]</span> · <span class="ph">[PLACEHOLDER qualifications]</span> · Credit Representative <span class="ph">[PLACEHOLDER]</span></p></div>
</div>
<div class="ctas hero-in" style="--d: 240ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book with Tom</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
</div>
</div>
</section>

<section class="band band-card" aria-labelledby="nt-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="nt-h">How Tom <em class="ul">works</em></h2>
</div>
<div class="rv focus prose" style="--d: 100ms">
<p>"A lot of people stay with the same loan for years because switching sounds like a hassle. I do the comparing and the forms, and I'll tell you honestly if staying put is the better call.</p>
<p>For investors, I spend time on the structure up front, with your accountant if you like, so the loan still works when you're ready for the next one."</p>
<p class="cap" style="margin-top: 16px">Illustrative profile for this demo. <span class="ph">[PLACEHOLDER: replace with the broker's own words]</span></p>
</div>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What clients say about ","hBrush":"Tom","hTail":"","filterKey":"broker","filterVal":"tom"})}
</div>
</section>

${ctaBand(C, {"hLead":"Book a chat with ","hBrush":"Tom","hTail":"","sub":"Phone, video or at our office, in English or Vietnamese.","prefill":{"broker":"tom","language":"English","source":"Tom Nguyen profile"}})}`,
});
