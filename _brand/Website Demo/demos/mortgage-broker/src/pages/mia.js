// Mia Chen, client support (canvas/Mia.dc.html)
const { photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Mia Chen, client support | Harlow Home Loans",
  description: "Meet Mia Chen, client support at Harlow Home Loans. Updates in English and Mandarin.",
  active: "about",
  drawerDefaults: {"source":"Mia Chen profile"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap profile">
<div class="portrait phero-photo" style="max-width: 420px; aspect-ratio: 4 / 5">${photo({"src":"images/mia.jpg","alt":"Mia Chen, client support","width":236,"height":295,"loading":"eager"})}</div>
<div>
<a class="backlink hero-in" href="team.html"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>All of the team</a>
<h1 class="h1 hero-in" id="ph-h" style="margin-top: 8px">Mia Chen</h1>
<p class="lead hero-in" style="--d: 60ms; margin-top: 8px; color: #14204A; font-weight: 600">Client support</p>
<p class="lead hero-in" style="--d: 120ms">Mia keeps every application moving. She chases documents, books valuations and sends you an update at each step, so you always know what's happening. She works in English and Mandarin.</p>
<div class="hero-in" style="--d: 180ms; margin-top: 24px; display: grid; gap: 18px">
<div><p class="cap" style="margin-bottom: 8px">Looks after</p><div class="tags"><span class="tag">Application updates</span><span class="tag">Document checklists</span><span class="tag">Settlement bookings</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Languages</p><div class="tags"><span class="tag">English</span><span class="tag">Mandarin</span></div></div>
</div>
<div class="ctas hero-in" style="--d: 240ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book a free chat</button>
<a class="btn btn-secondary btn-lg" href="mailto:${C.contact.email}">Email the team</a>
</div>
<p class="cap hero-in" style="--d: 280ms; margin-top: 12px">Mia doesn't give credit advice. She'll pair you with Claire, Tom or Priya for that.</p>
</div>
</div>
</section>

<section class="band band-card" aria-labelledby="nt-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="nt-h">What Mia <em class="ul">handles</em></h2>
</div>
<div class="rv focus prose" style="--d: 100ms">
<p>"Once your broker has found the right loan, I make sure nothing stalls. You'll hear from me when the lender has your application, when the valuation is booked and when approval comes through.</p>
<p>If you'd rather get updates in Mandarin, or by text instead of email, just tell me."</p>
<p class="cap" style="margin-top: 16px">Illustrative profile for this demo. <span class="ph">[PLACEHOLDER: replace with the team member's own words]</span></p>
</div>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What clients say about ","hBrush":"Mia","hTail":"","filterKey":"broker","filterVal":"mia"})}
</div>
</section>

${ctaBand(C, {"hLead":"Start with a free ","hBrush":"chat","hTail":"","sub":"Mia will match you with the right broker.","prefill":{"source":"Mia Chen profile"}})}`,
});
