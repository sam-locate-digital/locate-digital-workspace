# Testing in the browser

Lessons from verifying motion and layout changes in the Claude desktop browser pane.

## A hidden pane pauses the page

When the session window isn't open, or the browser pane is hidden, the page runs as a background page:

- no `requestAnimationFrame` callbacks
- no IntersectionObserver callbacks
- no native scroll events
- WAAPI animations don't progress and `finish` events don't fire
- screenshots can be stale frames (blank sections, old scroll positions)

So scroll reveals look "stuck" and loops never advance, even when the code is fine. Before treating that as a bug:

- Check `document.hidden` / `document.visibilityState`.
- Verify by **state**, not by watching: read computed styles, `getAnimations()` play states, class names and text content.
- Drive the logic by hand: `dispatchEvent(new Event('scroll'))`, call an animation's `onfinish` handler directly, or temporarily stub `requestAnimationFrame` with `setTimeout`.
- If a screenshot disagrees with computed styles, trust the styles and retake the screenshot.
- Use timers (`setTimeout`) rather than animation `finish` events for logic that must always run, such as swapping content after a fade.

Tell the user honestly what could not be watched live.

## Caching

The local preview server and the live CDN both cache. After editing a file, refresh it with `fetch(url, {cache: 'reload'})` before reloading the page, or the old version keeps showing. If the user reports seeing old content, suggest a hard refresh (Ctrl+F5).

## Client-side rendered pages

Pages rendered by a runtime (such as Claude Design `.dc.html` pages):

- The runtime can replace `<body>` after load, so MutationObservers must watch `document.documentElement`.
- Content appears after the first scan, so scan again on DOM mutations (throttled, not debounced: background canvases restyle every frame and would starve a debounce).
- The runtime can rewrite inline styles on re-render, so anything restyled from script must be re-applied when it is lost.
- Text can be wrapped in extra inner elements, so style the outer element when its background or shape matters.

## After a site-wide change

- Load every page and confirm all sections render and the console shows no new errors.
- Scan rendered text for leftovers of the removed pattern (for example, words still in capitals after a sentence-case conversion). Template strings that mix live values with fixed text are the usual misses.
- Check phone width (375px) for layout and horizontal overflow.
