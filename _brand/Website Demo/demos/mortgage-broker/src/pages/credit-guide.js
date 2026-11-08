// Credit Guide (canvas/CreditGuide.dc.html)
const { esc } = require('../partials');

module.exports = (C, R) => ({
  title: "Credit Guide | Harlow Home Loans",
  description: "Harlow Home Loans Credit Guide (placeholder for the demo site).",
  active: "",
  drawerDefaults: {"source":"Credit Guide page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap">
<div class="prose">
<h1 class="h1 hero-in" id="ph-h" style="max-width: none">Credit Guide</h1>
<p class="legal-note hero-in" style="--d: 80ms; margin-top: 20px">Placeholder. Replace this page with the Credit Guide supplied by <span class="ph">[Aggregator PLACEHOLDER] Pty Ltd</span> before the site goes live.</p>
<h2>About us</h2>
<p>${esc(C.compliance.entity)} (Credit Representative <span class="ph">[PLACEHOLDER]</span>) is authorised under Australian Credit Licence <span class="ph">[PLACEHOLDER]</span> held by <span class="ph">[Aggregator PLACEHOLDER] Pty Ltd</span>.</p>
<h2>Lenders we use</h2>
<p>We have access to <span class="ph">[PLACEHOLDER 30+]</span> lenders. The licensee's Credit Guide lists the lenders used most often.</p>
<h2>How we're paid</h2>
<p>${esc(C.compliance.feePolicy)} Any commission, fees and referral payments are disclosed in writing before you proceed.</p>
<h2>Our obligations to you</h2>
<p>We must act in your best interests and make reasonable inquiries about your situation before recommending a loan.</p>
<h2>Complaints</h2>
<p>See our <a href="complaints.html">Complaints page</a> for how to raise a concern and how we handle it.</p>
</div>
</div>
</section>`,
});
