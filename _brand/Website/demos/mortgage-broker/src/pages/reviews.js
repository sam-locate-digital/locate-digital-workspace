// Client reviews (canvas/Reviews.dc.html)
const { ctaBand, reviewRail } = require('../partials');

module.exports = (C, R) => ({
  title: "Client reviews | Harlow Home Loans",
  description: "What first home buyers, refinancers, investors and self-employed clients say about Harlow Home Loans.",
  active: "",
  drawerDefaults: {"source":"Reviews page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h" style="padding-bottom: 32px">
<div class="wrap">
<h1 class="h1 hero-in" id="ph-h" style="max-width: 18ch">What our clients say</h1>
<p class="lead hero-in" style="--d: 80ms; max-width: 680px">Reviews from first home buyers, families moving on, refinancers, investors and business owners across Melbourne. Filter by what you're planning.</p>
</div>
</section>

<section class="band" aria-label="All reviews" style="padding-top: 0">
<div class="wrap rv rise">
${reviewRail(R, {"mode":"grid","hLead":"Every review, in one ","hBrush":"place","hTail":""})}
</div>
</section>

${ctaBand(C, {"hLead":"Ready to make your ","hBrush":"move","hTail":"?","sub":"Book a free 20-minute chat.","prefill":{"source":"Reviews page"}})}`,
});
