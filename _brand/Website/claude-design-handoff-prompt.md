# Claude Design → Claude Code handoff prompt

Paste this into the Claude Design session once a website design is finished. Download the zip it makes, unzip it into `_brand/Website/<name>/`, then run `/design-to-site` in Claude Code and point it at that folder.

If Claude Design can't include the photos, save each one from the canvas (right-click → Save image as) into the same folder. `/design-to-site` can match loose photos to their canvas ids.

---

```text
Package this design as a handoff for Claude Code, as a zip I can download. Claude Code will rebuild it as a plain HTML/CSS/JS static site (no npm, no framework).

Include:
1. canvas/ – every page and component file exactly as they are, plus canvas.json. These are the spec; don't simplify them.
2. assets/ – the shared stylesheet, every icon and SVG, and asset-map.json mapping every /_blob/<id> URL in the canvas files to a file path in the zip.
3. photos/ – every photo used on the canvas, saved under a descriptive file name (e.g. hero-family.jpg). If you can't include a photo, list it in photos/PHOTO-LIST.md with its blob id, the file name to use, where it's used, its alt text and its aspect ratio.
4. CLAUDE.md – for Claude Code:
   - what the site is (business name, industry, location, that it's a demo for prospects)
   - how to read the canvas files (template syntax, conditionals, loops, imports, props, what's canvas-only)
   - every page with its route (kebab-case) and every shared component
   - the brand rules: fonts, colours, layout rules, things never to use
   - content rules: which values are [PLACEHOLDER], that they must be kept exactly, that reviews are illustrative, and the compliance or legal text that stays as placeholders
   - interactive behaviour to keep (header, menus, forms, carousels, quizzes, animations) and how each should behave with prefers-reduced-motion
   - checks that must pass before a page is done
5. A list of anything you're unsure about or that isn't finished in the design.

Don't include a PROMPT.md of build steps. I have my own Claude Code skill for the build.
```
