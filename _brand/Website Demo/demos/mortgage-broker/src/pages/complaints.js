// Complaints (canvas/Complaints.dc.html)
const { esc } = require('../partials');

module.exports = (C, R) => ({
  title: "Complaints | Harlow Home Loans",
  description: "How to make a complaint to Harlow Home Loans (placeholder for the demo site).",
  active: "",
  drawerDefaults: {"source":"Complaints page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap">
<div class="prose">
<h1 class="h1 hero-in" id="ph-h" style="max-width: none">Complaints</h1>
<p class="legal-note hero-in" style="--d: 80ms; margin-top: 20px">Placeholder. Replace this page with the complaints process supplied by <span class="ph">[Aggregator PLACEHOLDER] Pty Ltd</span> before the site goes live.</p>
<h2>Tell us first</h2>
<p>If something hasn't gone the way it should, please tell us. Call <a href="${C.contact.phoneHref}">${esc(C.contact.phone)}</a> or email <a href="mailto:${C.contact.email}">${esc(C.contact.email)}</a> and we'll try to fix it straight away.</p>
<h2>If it isn't resolved</h2>
<p>You can contact our licensee, <span class="ph">[Aggregator PLACEHOLDER] Pty Ltd</span>, on <span class="ph">[PLACEHOLDER contact details]</span>. We aim to respond within <span class="ph">[PLACEHOLDER timeframe]</span>.</p>
<h2>External dispute resolution</h2>
<p>If you're still not satisfied, you can contact the Australian Financial Complaints Authority (AFCA), a free and independent service, at <a href="https://www.afca.org.au">afca.org.au</a>. <span class="ph">[PLACEHOLDER: confirm AFCA membership number and contact details]</span></p>
</div>
</div>
</section>`,
});
