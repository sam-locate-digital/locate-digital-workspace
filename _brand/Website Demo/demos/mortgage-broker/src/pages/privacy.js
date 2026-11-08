// Privacy Policy (canvas/Privacy.dc.html)
const { esc } = require('../partials');

module.exports = (C, R) => ({
  title: "Privacy Policy | Harlow Home Loans",
  description: "Harlow Home Loans Privacy Policy (placeholder for the demo site).",
  active: "",
  drawerDefaults: {"source":"Privacy page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap">
<div class="prose">
<h1 class="h1 hero-in" id="ph-h" style="max-width: none">Privacy Policy</h1>
<p class="legal-note hero-in" style="--d: 80ms; margin-top: 20px">Placeholder. Replace this page with the Privacy Policy supplied by <span class="ph">[Aggregator PLACEHOLDER] Pty Ltd</span> before the site goes live.</p>
<h2>What we collect</h2>
<p>The details you give us in an enquiry or booking: your name, contact details, the situation you're asking about and any figures you choose to share.</p>
<h2>How we use it</h2>
<p>To contact you about your enquiry and, if you go ahead, to arrange a loan. We don't sell your information.</p>
<h2>Credit checks</h2>
<p>We don't run a credit check for a first chat or an estimate. If you apply for a loan, the lender will, with your consent.</p>
<h2>Access and correction</h2>
<p>You can ask to see or correct the information we hold about you by emailing <a href="mailto:${C.contact.email}">${esc(C.contact.email)}</a>.</p>
</div>
</div>
</section>`,
});
