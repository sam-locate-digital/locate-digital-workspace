// Website terms (canvas/Terms.dc.html)
const { esc } = require('../partials');

module.exports = (C, R) => ({
  title: "Website terms | Harlow Home Loans",
  description: "Harlow Home Loans website terms of use (placeholder for the demo site).",
  active: "",
  drawerDefaults: {"source":"Terms page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap">
<div class="prose">
<h1 class="h1 hero-in" id="ph-h" style="max-width: none">Website terms</h1>
<p class="legal-note hero-in" style="--d: 80ms; margin-top: 20px">Placeholder. Replace this page with terms supplied or approved by <span class="ph">[Aggregator PLACEHOLDER] Pty Ltd</span> before the site goes live.</p>
<h2>General information only</h2>
<p>${esc(C.compliance.generalInfo)}</p>
<h2>Reviews</h2>
<p>Reviews on this demo site are illustrative. A live site should only show genuine reviews, used with the client's permission.</p>
<h2>Links</h2>
<p>We aren't responsible for the content of other websites we link to, such as government or lender sites.</p>
</div>
</div>
</section>`,
});
