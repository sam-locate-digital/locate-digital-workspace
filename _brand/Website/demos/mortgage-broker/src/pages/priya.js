// Priya Shah, broker (canvas/Priya.dc.html)
const { esc, photo, ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Priya Shah, broker | Harlow Home Loans",
  description: "Meet Priya Shah, mortgage broker at Harlow Home Loans. Appointments in English, Hindi and Gujarati.",
  active: "about",
  drawerDefaults: {"broker":"priya","source":"Priya Shah profile"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap profile">
<div class="portrait phero-photo" style="max-width: 420px; aspect-ratio: 4 / 5">${photo({"src":"images/priya.jpg","alt":"Priya Shah, broker","width":236,"height":295,"loading":"eager"})}</div>
<div>
<a class="backlink hero-in" href="team.html"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5"></path><path d="m11 18-6-6 6-6"></path></svg>All of the team</a>
<h1 class="h1 hero-in" id="ph-h" style="margin-top: 8px">Priya Shah</h1>
<p class="lead hero-in" style="--d: 60ms; margin-top: 8px; color: #14204A; font-weight: 600">Broker</p>
<p class="lead hero-in" style="--d: 120ms">Priya joined Harlow in <span class="ph">[PLACEHOLDER year]</span> and helps a lot of families who are upsizing or buying before they sell. She's good at making bridging finance make sense, and often explains it twice: once in English and once in Hindi or Gujarati for the parents.</p>
<div class="hero-in" style="--d: 180ms; margin-top: 24px; display: grid; gap: 18px">
<div><p class="cap" style="margin-bottom: 8px">Specialities</p><div class="tags"><span class="tag">Next home buyers</span><span class="tag">Bridging finance</span><span class="tag">Construction loans</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Languages</p><div class="tags"><span class="tag">English</span><span class="tag">Hindi</span><span class="tag">Gujarati</span></div></div>
<div><p class="cap" style="margin-bottom: 8px">Credentials</p><p class="small">Member of <span class="ph">[PLACEHOLDER MFAA or FBAA]</span> · <span class="ph">[PLACEHOLDER qualifications]</span> · Credit Representative <span class="ph">[PLACEHOLDER]</span></p></div>
</div>
<div class="ctas hero-in" style="--d: 240ms">
<button type="button" class="btn btn-primary btn-lg" data-enquire="{}">Book with Priya</button>
<a class="btn btn-secondary btn-lg" href="${C.contact.phoneHref}">Call ${esc(C.contact.phone)}</a>
</div>
</div>
</div>
</section>

<section class="band band-card" aria-labelledby="nt-h">
<div class="wrap two-col">
<div class="rv focus">
<h2 class="h2" id="nt-h">How Priya <em class="ul">works</em></h2>
</div>
<div class="rv focus prose" style="--d: 100ms">
<p>"Moving house is stressful enough without wondering how two settlements will line up. I map out the dates and the money with you before you sign anything.</p>
<p>Families often make these decisions together, so I'm happy to sit down with everyone, in whichever language works best around the table."</p>
<p class="cap" style="margin-top: 16px">Illustrative profile for this demo. <span class="ph">[PLACEHOLDER: replace with the broker's own words]</span></p>
</div>
</div>
</section>

<section class="band" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, {"hLead":"What clients say about ","hBrush":"Priya","hTail":"","filterKey":"broker","filterVal":"priya"})}
</div>
</section>

${ctaBand(C, {"hLead":"Book a chat with ","hBrush":"Priya","hTail":"","sub":"Phone, video or at our office, in English, Hindi or Gujarati.","prefill":{"broker":"priya","source":"Priya Shah profile"}})}`,
});
