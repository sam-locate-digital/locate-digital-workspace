// Site-wide motion. Scroll reveals: content fades in with a short stagger and images settle
// from a slight zoom. The reveal style rotates section by section (rise, focus, slide, scale)
// so no two neighbouring sections animate the same way. Pages that already have their own
// reveals load this with data-reveal="off". Details everywhere: blue highlighted words in
// headings get a brush underline, eyebrow rules draw in, step numbers rise, cards pick up a
// cursor glow, and pill buttons lean toward the cursor.
// Pages render client-side, so new content is picked up as it appears. Anything a page
// already animates itself (inline opacity 0, data-rv, data-fade) is left alone.
(function () {
  var REVEAL = !(document.currentScript && document.currentScript.dataset.reveal === 'off');

  // Blue highlighted words in headings get a tapered brush underline, matching the AI page hero,
  // that paints in left to right as the heading comes into view. It is drawn as a background so
  // a phrase that wraps onto two lines is underlined on both. This runs before the reduced-motion
  // exit below: those visitors still get the underline, just without the paint-in.
  (function () {
    var still = !window.matchMedia || matchMedia('(prefers-reduced-motion: reduce)').matches;
    var brush = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 28' preserveAspectRatio='none'%3E%3Cpath d='M3 19 C 28 11, 96 5, 190 2 C 196 1, 200 4, 197 8 C 186 10, 120 13, 60 17 C 38 19, 18 21, 9 25 C 3 27, 0 22, 3 19 Z' fill='%23007ae8'/%3E%3C/svg%3E\")";
    var tag = document.createElement('style');
    tag.textContent = '.ld-ul{background-image:' + brush + ';background-repeat:no-repeat;background-position:0 100%;background-size:0% .44em;padding:0 .06em .14em;margin:0 -.06em;-webkit-box-decoration-break:clone;box-decoration-break:clone}' +
      '.ld-ul.ld-ul-on{background-size:100% .44em}' + (still ? '' : '.ld-ul{transition:background-size .75s cubic-bezier(.7,0,.2,1)}');
    (document.head || document.documentElement).appendChild(tag);

    function blue(c) { var m = c.match(/\d+/g); return m && +m[2] > +m[0] + 80 && +m[2] >= +m[1]; }
    var io = !still && 'IntersectionObserver' in window && new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        var el = e.target; setTimeout(function () { el.classList.add('ld-ul-on'); }, 350);
      });
    }, { rootMargin: '0px 0px -12% 0px' });

    function scan() {
      // Headings, plus paragraphs set as display type (the homepage hero headline is a <p>).
      document.querySelectorAll('h1 span, h2 span, p span').forEach(function (el) {
        // Skip the hero's hand-placed stroke, spans inside one already underlined, and empty spans.
        if (el.__ldUl || el.querySelector('svg') || el.parentElement.closest('.ld-ul') || !el.textContent.trim()) return;
        var head = el.closest('h1, h2, p'), cs = getComputedStyle(el);
        if (head.tagName === 'P' && parseFloat(cs.fontSize) < 36) return;
        if (!blue(cs.color) || cs.color === getComputedStyle(head).color) return;
        el.__ldUl = true;
        el.classList.add('ld-ul');
        if (io) io.observe(el); else el.classList.add('ld-ul-on');
      });
    }
    var t;
    function queue() { if (!t) t = setTimeout(function () { t = 0; scan(); }, 150); }
    function start() { queue(); new MutationObserver(queue).observe(document.documentElement, { childList: true, subtree: true }); }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  })();
  if (!window.matchMedia || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!('IntersectionObserver' in window) || !Element.prototype.animate) return;

  var EASE = 'cubic-bezier(.2,.7,.2,1)';
  var BLOCKS = 'h2, h3, h4, p, ul, ol, blockquote, figure, img, picture, video, form, table, a[style*="padding"], button';
  var SKIP = 'nav, header, footer, [data-hero], [data-rv], [data-fade], [data-stagger], [aria-hidden="true"], canvas, svg, dc-import[name="Site Nav"], dc-import[name="Site Footer"]';
  var seen = new WeakSet();
  var pending = new Map();

  function css(el) { return getComputedStyle(el); }

  // ---- Scroll reveals --------------------------------------------------------------------

  function hiddenByPage(el) {
    for (var n = el; n && n !== document.body; n = n.parentElement) {
      if (parseFloat(css(n).opacity) < 0.05) return true;
    }
    var owned = el.querySelectorAll('[style*="opacity"]');
    for (var i = 0; i < owned.length; i++) if (owned[i].style.opacity === '0') return true;
    return false;
  }

  // Treat a grid/flex row of two or more blocks as cards, so each one reveals as a unit.
  function isCardRow(el) {
    if (el.children.length < 2) return false;
    var d = css(el).display;
    if (d !== 'grid' && d !== 'inline-grid' && d !== 'flex') return false;
    var sized = 0;
    for (var i = 0; i < el.children.length; i++) if (el.children[i].offsetHeight > 40) sized++;
    return sized >= 2;
  }

  function collect(section) {
    var out = [];
    (function walk(node) {
      for (var i = 0; i < node.children.length; i++) {
        var c = node.children[i];
        if (c.matches(SKIP) || c.offsetHeight === 0) continue;
        if (isCardRow(c)) { for (var j = 0; j < c.children.length; j++) if (c.children[j].offsetHeight > 0) out.push(c.children[j]); continue; }
        if (c.matches(BLOCKS)) { out.push(c); continue; }
        walk(c);
      }
    })(section);
    return out;
  }

  // Reveal styles, one per section in turn: [heading frames, block frames]. Individual
  // translate/scale properties leave the page's own inline transform (hover lifts) untouched.
  var STYLES = [
    [[{ opacity: 0, clipPath: 'inset(0 0 100% 0)', translate: '0 24px' }, { opacity: 1, clipPath: 'inset(0 0 0% 0)', translate: '0 0' }],
     [{ opacity: 0, translate: '0 16px' }, { opacity: 1, translate: '0 0' }]],
    [[{ opacity: 0, filter: 'blur(8px)' }, { opacity: 1, filter: 'blur(0)' }],
     [{ opacity: 0, filter: 'blur(6px)' }, { opacity: 1, filter: 'blur(0)' }]],
    [[{ opacity: 0, translate: '-28px 0' }, { opacity: 1, translate: '0 0' }],
     [{ opacity: 0, translate: '-18px 0' }, { opacity: 1, translate: '0 0' }]],
    [[{ opacity: 0, scale: '0.96' }, { opacity: 1, scale: '1' }],
     [{ opacity: 0, scale: '0.965', translate: '0 8px' }, { opacity: 1, scale: '1', translate: '0 0' }]]
  ];

  function animFor(el, style) {
    var img = /^(IMG|PICTURE|VIDEO|FIGURE)$/.test(el.tagName);
    var frames = img ? [{ opacity: 0, scale: '1.035' }, { opacity: 1, scale: '1' }] : STYLES[style][el.tagName === 'H2' ? 0 : 1];
    var a = el.animate(frames, { duration: el.tagName === 'H2' ? 950 : img ? 1100 : 700, easing: EASE, fill: 'both' });
    a.pause();
    return a;
  }

  // pending maps the element we watch to the animations it starts. A heading starts fully
  // clipped, which the observer reads as zero size, so its parent is watched instead.
  function reveal(triggers) {
    var k = 0;
    triggers.sort(function (a, b) { var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect(); return ra.top - rb.top || ra.left - rb.left; })
      .forEach(function (el) {
        var list = pending.get(el) || [];
        io.unobserve(el); pending.delete(el);
        list.forEach(function (a) {
          // Content already passed (an anchor jump) appears without a stagger.
          a.effect.updateTiming({ delay: el.getBoundingClientRect().bottom < 0 ? 0 : Math.min(k++, 6) * 80 });
          a.onfinish = function () { a.cancel(); };
          a.play();
        });
      });
  }

  var io = new IntersectionObserver(function (entries) {
    reveal(entries.filter(function (e) { return e.isIntersecting; }).map(function (e) { return e.target; }));
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.01 });

  // Backup for the observer: on scroll, reveal anything that has reached the fold.
  var st;
  window.addEventListener('scroll', function () {
    clearTimeout(st);
    st = setTimeout(function () {
      var fold = window.innerHeight * 0.92, due = [];
      pending.forEach(function (_, el) { if (el.getBoundingClientRect().top < fold) due.push(el); });
      if (due.length) reveal(due);
    }, 200);
  }, { passive: true });

  function scanReveal() {
    var fold = window.innerHeight * 0.92;
    var n = 0;
    document.querySelectorAll('section, main > div, [data-section]').forEach(function (section) {
      if (section.closest(SKIP)) return;
      var style = n++ % STYLES.length;
      collect(section).forEach(function (el) {
        if (seen.has(el)) return;
        seen.add(el);
        if (el.getBoundingClientRect().top < fold || hiddenByPage(el)) return;
        // The wipe-up heading starts fully clipped, so its parent is the one watched.
        var trigger = el.tagName === 'H2' && style === 0 ? el.parentElement : el;
        if (!pending.has(trigger)) { pending.set(trigger, []); io.observe(trigger); }
        pending.get(trigger).push(animFor(el, style));
      });
    });
  }

  // ---- Details ---------------------------------------------------------------------------

  var FINE = matchMedia('(hover: hover) and (pointer: fine)').matches;
  var done = new WeakSet();
  var entering = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      entering.unobserve(e.target);
      var fn = e.target.__ldIn; e.target.__ldIn = null;
      if (fn) fn();
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  function onEnter(el, fn) { el.__ldIn = fn; entering.observe(el); }

  function isLight(color) {
    var m = color.match(/[\d.]+/g); if (!m) return true;
    return (m[3] !== undefined && +m[3] < 0.3) || (0.299 * m[0] + 0.587 * m[1] + 0.114 * m[2]) > 160;
  }

  // Eyebrow labels: the short rule before the label draws in and the letters settle.
  function eyebrow(el) {
    var rule = el.previousElementSibling;
    var isRule = rule && rule.offsetHeight > 0 && rule.offsetHeight <= 3 && rule.offsetWidth >= 16 && rule.offsetWidth <= 96;
    var ls = parseFloat(css(el).letterSpacing) || 0;
    onEnter(el, function () {
      if (isRule) rule.animate([{ scale: '0 1', transformOrigin: 'left center' }, { scale: '1 1', transformOrigin: 'left center' }], { duration: 800, easing: EASE });
      el.animate([{ letterSpacing: (ls + 3) + 'px', opacity: 0.4 }, { letterSpacing: ls + 'px', opacity: 1 }], { duration: 900, delay: isRule ? 150 : 0, easing: EASE });
    });
  }

  // Large step numbers (1, 2 ...) rise and sharpen into place.
  var stepK = 0;
  function stepNumber(el) {
    var delay = 120 + (stepK++ % 3) * 90;
    onEnter(el, function () {
      el.animate([{ opacity: 0, translate: '0 0.45em', filter: 'blur(3px)' }, { opacity: 1, translate: '0 0', filter: 'blur(0)' }], { duration: 750, delay: delay, easing: EASE, fill: 'backwards' });
    });
  }

  // Cards: a soft glow follows the cursor across the surface. !important wins over a page's
  // inline background shorthand, and the glow layer sits under the card's content.
  var spotReady = false;
  function spotStyles() {
    if (spotReady) return; spotReady = true;
    try { CSS.registerProperty({ name: '--ld-spot', syntax: '<number>', inherits: false, initialValue: '0' }); } catch (e) {}
    var tag = document.createElement('style');
    tag.textContent = '[data-ld-spot]{background-image:radial-gradient(380px circle at var(--ld-x,50%) var(--ld-y,50%),rgb(var(--ld-rgb,0 122 232) / calc(var(--ld-spot) * var(--ld-a,.08))),transparent 70%)!important}';
    document.head.appendChild(tag);
  }
  // A panel inside another card (or a card that already has its own glow) is left alone.
  function insideCard(el) {
    for (var n = el.parentElement; n && n.tagName !== 'SECTION'; n = n.parentElement) {
      var cs = css(n);
      if (parseFloat(cs.borderRadius) >= 12 && (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none')) return true;
    }
    return false;
  }
  function card(el) {
    if (insideCard(el)) return;
    spotStyles();
    el.setAttribute('data-ld-spot', '');
    var fade = function (to) { el.animate([{ '--ld-spot': 1 - to }, { '--ld-spot': to }], { duration: 350, easing: 'ease-out', fill: 'forwards' }); };
    el.addEventListener('pointerenter', function () {
      var light = isLight(css(el).backgroundColor);
      el.style.setProperty('--ld-rgb', light ? '0 122 232' : '255 255 255');
      el.style.setProperty('--ld-a', light ? '0.08' : '0.18');
      fade(1);
    });
    el.addEventListener('pointerleave', function () { fade(0); });
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect();
      el.style.setProperty('--ld-x', (e.clientX - r.left) + 'px');
      el.style.setProperty('--ld-y', (e.clientY - r.top) + 'px');
    });
  }

  // Pill buttons lean a few pixels toward the cursor and ease back when it leaves.
  function magnet(el) {
    var x = 0, y = 0, tx = 0, ty = 0, raf = 0;
    var step = function () {
      x += (tx - x) * 0.18; y += (ty - y) * 0.18;
      el.style.translate = x.toFixed(2) + 'px ' + y.toFixed(2) + 'px';
      if (Math.abs(tx - x) > 0.05 || Math.abs(ty - y) > 0.05) raf = requestAnimationFrame(step);
      else { raf = 0; if (!tx && !ty) el.style.translate = ''; }
    };
    var go = function () { if (!raf) raf = requestAnimationFrame(step); };
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect();
      tx = ((e.clientX - r.left) / r.width - 0.5) * 8; ty = ((e.clientY - r.top) / r.height - 0.5) * 6; go();
    });
    el.addEventListener('pointerleave', function () { tx = 0; ty = 0; go(); });
  }

  function scanDetails() {
    var all = document.querySelectorAll('section *');
    for (var i = 0; i < all.length; i++) {
      var el = all[i];
      if (done.has(el)) continue;
      var w = el.offsetWidth, h = el.offsetHeight;
      if (!w || !h) continue;
      done.add(el);
      // Nothing inside a card that already has the glow, so effects never double up.
      if (el.closest('nav, header, footer, [aria-hidden="true"], [data-ld-spot]')) continue;
      var cs = css(el), text = el.textContent.trim(), leaf = el.children.length === 0, fs = parseFloat(cs.fontSize);
      var clear = cs.backgroundColor === 'rgba(0, 0, 0, 0)';
      if (leaf && cs.textTransform === 'uppercase' && fs < 15 && text.length > 2 && parseFloat(cs.letterSpacing) > 0.5 && !el.closest('h1, h2') && el.previousElementSibling) eyebrow(el);
      else if (leaf && /^[1-9]$/.test(text) && fs >= 28) stepNumber(el);
      else if (FINE && /^(A|BUTTON)$/.test(el.tagName) && parseFloat(cs.borderRadius) >= 20 && h <= 64 && w <= 360 && text.length > 3 && !clear) magnet(el);
      else if (FINE && !leaf && parseFloat(cs.borderRadius) >= 12 && h > 140 && w > 200 && w < 900 && !clear && cs.backgroundImage === 'none' && text.length > 20 && !el.querySelector('input, textarea')) card(el);
    }
  }

  // ---- Wiring ----------------------------------------------------------------------------

  function scan() {
    if (REVEAL) scanReveal();
    scanDetails();
  }

  // Never leave content hidden for printing or if something goes wrong mid-page.
  function revealAll() { pending.forEach(function (list) { list.forEach(function (a) { a.cancel(); }); }); pending.clear(); io.disconnect(); }
  window.addEventListener('beforeprint', revealAll);

  var t;
  function queue() { clearTimeout(t); t = setTimeout(scan, 120); }
  function start() {
    queue();
    // Watch the root: the page runtime can swap out <body> after load.
    new MutationObserver(queue).observe(document.documentElement, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
