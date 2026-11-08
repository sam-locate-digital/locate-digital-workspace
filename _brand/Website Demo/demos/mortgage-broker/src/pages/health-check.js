// Refinance health check (canvas/HealthCheck.dc.html). The quiz itself is rendered by js/health-check.js.
const { photo, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: 'Refinance health check | Harlow Home Loans',
  description: 'Five quick questions to see whether your home loan is worth a review. Free, no credit check.',
  active: 'refinancing',
  drawerDefaults: { situation: 'refinance', source: 'Health check' },
  scripts: ['js/health-check.js'],
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap">
<div class="hc">
${photo({ cls: 'ph-ic ill hero-in', src: 'icons/compare.webp', alt: '', width: 240, height: 240, loading: 'eager' })}
<h1 class="h1 hero-in" id="ph-h" style="max-width: none">Refinance health check</h1>
<p class="lead hero-in" style="--d: 80ms">Five quick questions to see whether your loan is worth a closer look. No credit check, and nothing is sent unless you ask us to call.</p>

<div class="enq hero-in" style="--d: 160ms; margin-top: 28px" data-healthcheck>
<p class="sr" aria-live="polite" role="status" data-live></p>
<div data-hc-body><noscript><p>Turn on JavaScript to use the health check, or call us on ${C.contact.phone}.</p></noscript></div>
</div>
</div>
</div>
</section>

<section class="band band-card" aria-label="Reviews" style="overflow: hidden">
<div class="wrap">
${reviewRail(R, { hLead: 'Clients who ', hBrush: 'checked', hTail: '', filterKey: 'situation', filterVal: 'refinance' })}
</div>
</section>`,
});
