// Book a free chat (canvas/Book.dc.html)
const { esc, inlineForm } = require('../partials');

module.exports = (C, R) => ({
  title: "Book a free chat | Harlow Home Loans",
  description: "Book a free 20-minute chat with a Harlow Home Loans broker. Phone, video or at our office. No credit check.",
  active: "",
  drawerDefaults: {"source":"Book page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h">
<div class="wrap cta-grid" style="align-items: start">
<div class="hero-in" style="--d: 120ms; order: 2">
${inlineForm({"source":"Book page"})}
</div>
<div style="order: 1">
<h1 class="h1 hero-in" id="ph-h">Book a free 20-minute chat</h1>
<p class="lead hero-in" style="--d: 60ms">Tell us a little about your plans, pick a time and a broker, and we'll call you. It ends with a clear answer on roughly what you could borrow and your best next step.</p>
<ul class="hl-list hero-in" style="--d: 120ms; margin-top: 28px">
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>No obligation, no credit check</b><p>A first chat and estimate don't touch your credit file.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Phone, video or our office</b><p>Evening video calls and Saturday appointments too.</p></li>
<li><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"></path></svg><b>Usually free to you</b><p>${esc(C.compliance.feePolicy)}</p></li>
</ul>
<p class="cap hero-in" style="--d: 180ms; margin-top: 24px">Rather talk now? Call <a href="${C.contact.phoneHref}">${esc(C.contact.phone)}</a>. ${esc(C.hours)}.</p>
</div>
</div>
</section>`,
});
