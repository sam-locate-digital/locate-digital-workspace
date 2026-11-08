// Home loan guides (canvas/Guides.dc.html)
const { ctaBand } = require('../partials');

module.exports = (C, R) => ({
  title: "Home loan guides | Harlow Home Loans",
  description: "Plain-English guides: a first home buyer checklist, what happens when your fixed rate ends, and how lenders look at self-employed income.",
  active: "",
  drawerDefaults: {"source":"Guides page"},
  body: `
<section class="phero" id="hero" aria-labelledby="ph-h" style="padding-bottom: 40px">
<div class="wrap">
<h1 class="h1 hero-in" id="ph-h" style="max-width: 18ch">Guides, in plain English</h1>
<p class="lead hero-in" style="--d: 80ms; max-width: 680px">Short reads on the questions we hear most. General information only, so talk to us about your own situation.</p>
<nav class="hero-in" style="--d: 160ms; margin-top: 28px" aria-label="Guides on this page">
<ol class="olist" style="max-width: 760px">
<li><span class="n">01</span><b><a href="#first-home-checklist" style="color: #14204A">First home buyer checklist</a></b><p>What to sort out before you start looking.</p></li>
<li><span class="n">02</span><b><a href="#fixed-rate-ending" style="color: #14204A">What happens when your fixed rate ends</a></b><p>And what to do in the months before.</p></li>
<li><span class="n">03</span><b><a href="#self-employed-income" style="color: #14204A">How lenders look at self-employed income</a></b><p>Why two lenders can read the same tax return differently.</p></li>
</ol>
</nav>
</div>
</section>

<section class="band band-card" aria-label="Guides">
<div class="wrap">
<article class="guide rv rise" id="first-home-checklist" aria-labelledby="g1">
<div><p class="cap">Guide 01 · First home</p><h2 class="h3" id="g1" style="margin-top: 8px">First home buyer checklist</h2><p class="cap" style="margin-top: 10px">5 minute read <span class="ph">[PLACEHOLDER]</span></p></div>
<div class="prose">
<p>Buying your first home is mostly about getting a few things ready in the right order. Here's the short version.</p>
<ul>
<li>Know your savings, including any family help you might receive.</li>
<li>Pay down or close credit cards you don't use. Lenders count the limit, not just the balance.</li>
<li>Gather your last two payslips, three months of bank statements and photo ID.</li>
<li>Get pre-approval before you start bidding, so you know your limit.</li>
<li>Ask us to check which first home schemes, grants or stamp duty concessions you may be eligible for.</li>
<li>Budget for the extras: conveyancing, inspections, lender fees and moving costs.</li>
</ul>
<p class="note" style="margin-top: 16px">[PLACEHOLDER] Full article to be written and checked by the broker before going live.</p>
</div>
</article>

<article class="guide rv rise" id="fixed-rate-ending" aria-labelledby="g2">
<div><p class="cap">Guide 02 · Refinancing</p><h2 class="h3" id="g2" style="margin-top: 8px">What happens when your fixed rate ends</h2><p class="cap" style="margin-top: 10px">4 minute read <span class="ph">[PLACEHOLDER]</span></p></div>
<div class="prose">
<p>When a fixed term finishes, most loans move onto the lender's standard variable rate automatically. You don't have to do anything for that to happen, which is exactly why it's easy to miss.</p>
<p>That standard rate can be higher than the rates the same lender offers new customers. So the few months before your fixed rate ends are a good time to review: you might fix again, move to variable, split the loan, or switch lenders.</p>
<p>Start the conversation early. Switching takes time, and you'll want to compare options without a deadline breathing down your neck. If your rate is still fixed, breaking it early can cost money, so we'll check that first.</p>
<p><a href="health-check.html">Take the 2-minute health check</a> or <a href="refinancing.html">see how we help with refinancing</a>.</p>
<p class="note" style="margin-top: 16px">[PLACEHOLDER] Full article to be written and checked by the broker before going live.</p>
</div>
</article>

<article class="guide rv rise" id="self-employed-income" aria-labelledby="g3">
<div><p class="cap">Guide 03 · Self-employed</p><h2 class="h3" id="g3" style="margin-top: 8px">How lenders look at self-employed income</h2><p class="cap" style="margin-top: 10px">5 minute read <span class="ph">[PLACEHOLDER]</span></p></div>
<div class="prose">
<p>When you work for yourself, lenders can't just look at a payslip. They look at your tax returns and financial statements instead, and each lender has its own way of reading them.</p>
<p>Some use your most recent year, others average the last two. Some add back costs that don't really reduce your income, like depreciation or one-off expenses. That's why one lender might say no while another says yes to the same person.</p>
<p>If you've been trading for less than two years, or your latest return isn't done, there may still be options, including low-doc loans. They can cost more, so it's worth comparing them with standard loans first.</p>
<p><a href="self-employed.html">How we help self-employed borrowers</a>.</p>
<p class="note" style="margin-top: 16px">[PLACEHOLDER] Full article to be written and checked by the broker before going live.</p>
</div>
</article>
</div>
</section>

${ctaBand(C, {"hLead":"Got a question we haven't ","hBrush":"covered","hTail":"?","sub":"Ask us on a free 20-minute chat.","prefill":{"source":"Guides page"}})}`,
});
