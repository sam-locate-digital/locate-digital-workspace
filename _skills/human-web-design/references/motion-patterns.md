# Motion patterns

Working patterns from locatedigital.io (`_brand/site/motion.js` and the AI page workflow loop in `_brand/site/ai.html` in the Locate workspace). Vanilla JS, no libraries. Adapt the selectors to the page.

## Ground rules

- Animate with the individual `translate` / `scale` / `rotate` properties, not `transform`. That leaves a page's own `transform` (hover lifts) untouched.
- Every effect checks `prefers-reduced-motion` and shows the end state instead.
- Skip anything the page already animates itself (inline `opacity: 0`, its own reveal attributes) so effects never stack.

## 1. Scroll reveals that rotate per section

Pre-hide with a paused WAAPI animation (no CSS flash), play it on entry, then cancel it so inline styles take over again. The style rotates section by section, so neighbours never animate the same way.

```js
const EASE = 'cubic-bezier(.2,.7,.2,1)';
const STYLES = [ // [heading frames, block frames]
  [[{opacity:0, clipPath:'inset(0 0 100% 0)', translate:'0 24px'}, {opacity:1, clipPath:'inset(0 0 0% 0)', translate:'0 0'}],
   [{opacity:0, translate:'0 16px'}, {opacity:1, translate:'0 0'}]],               // rise
  [[{opacity:0, filter:'blur(8px)'}, {opacity:1, filter:'blur(0)'}],
   [{opacity:0, filter:'blur(6px)'}, {opacity:1, filter:'blur(0)'}]],              // focus
  [[{opacity:0, translate:'-28px 0'}, {opacity:1, translate:'0 0'}],
   [{opacity:0, translate:'-18px 0'}, {opacity:1, translate:'0 0'}]],              // slide
  [[{opacity:0, scale:'0.96'}, {opacity:1, scale:'1'}],
   [{opacity:0, scale:'0.965', translate:'0 8px'}, {opacity:1, scale:'1', translate:'0 0'}]] // scale
];
function hold(el, frames, ms) { const a = el.animate(frames, {duration: ms, easing: EASE, fill: 'both'}); a.pause(); return a; }
// For section n: style = n % STYLES.length. Queue blocks below the fold only.
// On entry: a.effect.updateTiming({delay: k * 80}); a.onfinish = () => a.cancel(); a.play();
```

Gotchas:
- A heading pre-clipped to zero height (`inset(0 0 100% 0)`) is invisible to IntersectionObserver. Observe its parent instead.
- Add a scroll-position fallback: on scroll, reveal anything pending whose top is above about 92% of the viewport.
- On `beforeprint`, cancel all pending reveals.

## 2. Brush underline on accent words

Drawn as a background image so a phrase that wraps is underlined on both lines (`box-decoration-break: clone`). It paints in by animating `background-size`.

```js
const brush = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 28' preserveAspectRatio='none'%3E%3Cpath d='M3 19 C 28 11, 96 5, 190 2 C 196 1, 200 4, 197 8 C 186 10, 120 13, 60 17 C 38 19, 18 21, 9 25 C 3 27, 0 22, 3 19 Z' fill='%23007ae8'/%3E%3C/svg%3E\")";
const css = `.ld-ul{background-image:${brush};background-repeat:no-repeat;background-position:0 100%;
  background-size:0% .44em;padding:0 .06em .14em;margin:0 -.06em;
  -webkit-box-decoration-break:clone;box-decoration-break:clone}
 .ld-ul.ld-ul-on{background-size:100% .44em}
 .ld-ul{transition:background-size .75s cubic-bezier(.7,0,.2,1)}`; // omit the transition for reduced motion
// Find spans inside h1/h2 (and display-size <p>, >= 36px) whose colour is the accent colour,
// add .ld-ul, and add .ld-ul-on 350ms after it enters view.
```

Gotchas:
- If a headline's lines are clipped (`overflow: hidden` for an entrance mask), give those wrappers extra bottom padding with matching negative margin, or the stroke gets cut. Don't raise the stroke into the letters instead; it blurs the word.
- Change the `fill` to the brand accent (URL-encoded `#` as `%23`).
- For a single hand-placed instance, an absolutely positioned inline SVG with the same path works, revealed with `clip-path: inset(...)` animated from `100%` to `0` on the right side.

## 3. Pause-aware autoplay loop

The active tab's progress line is the timer: its animation's `onfinish` advances to the next item. Every animation in the run sits in one list, so pausing and resuming is one call.

```js
// hold reasons: hover, focus, off (IntersectionObserver), hidden (visibilitychange)
wfSync() {
  const h = this.hold, stop = Object.values(h).some(Boolean), reading = h.hover || h.focus;
  this.anims.forEach(a => {
    if (a.playState === 'finished') return;
    if (reading && a.reveal) { a.finish(); return; } // someone is reading: show everything in full
    stop ? a.pause() : a.play();
  });
}
play() {
  this.anims.forEach(a => a.cancel());
  const bar = tabs[active].querySelector('[data-bar]');
  const timer = bar.animate([{transform:'scaleX(0)'}, {transform:'scaleX(1)'}], {duration: 7000, easing:'linear', fill:'forwards'});
  timer.onfinish = () => this.go((active + 1) % count);
  // Per step i at start + i * gap: brighten text (.35 -> 1), colour the numeral, slide the tag in.
  // Mark those animations a.reveal = true. All use fill:'both'.
}
go(i) {
  // Cancel any fade still running first, so rapid clicks can't leave the panel hidden.
  // Fade the panel out, swap content after a setTimeout (not an onfinish event), stagger the new rows in, then play().
}
```

- No autoplay at all under reduced motion; tabs still work by click.
- A thin vertical timeline line (`scaleY` 0 to 1 across the step numbers, numbers on a white disc to mask it) reads as "the workflow is running" without cards or badges.

## 4. Small touches

- **Section label rule draw-in:** the short rule before a label animates `scale: '0 1'` to `'1 1'` from the left over 800ms.
- **Card glow:** a soft radial highlight that follows the cursor. Use a registered `--spot` custom property animated with WAAPI, and `!important` on the background-image so a page's inline `background` shorthand doesn't wipe it. Skip panels nested inside another card.
- **Button pull:** pill buttons lean a few pixels towards the cursor via `style.translate` with an rAF lerp, easing back on leave.
- **Background graphics:** if a section's background engine already does scroll parallax, don't add more on top.
