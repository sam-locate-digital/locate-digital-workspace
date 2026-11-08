# Prompt for Claude Code

Open Claude Code in this folder, then paste:

```
This folder has a working website prototype in design/Main.dc.html (a canvas component file, not plain HTML), the photos in images/, and HANDOFF.md. HANDOFF.md is the source of truth; BRIEF.md is the original brief for background only, and HANDOFF.md overrides it where they differ.

Rebuild it as a static site in plain HTML, CSS and vanilla JavaScript, with no framework:
- One HTML file per page (index, plumbing, electrical, the 4 service pages, suburb pages, landlords, reviews, about, emergency, book, thanks, privacy, terms), sharing one styles.css and one main.js.
- Keep every colour, font, spacing value, piece of copy and interaction exactly as in the prototype: the booking drawer, form validation, reviews carousel, how-it-works stepper, FAQ, suburb checker, mobile call bar and scroll reveals.
- Move the CONFIG object into config.js and the reviews into reviews.json, so a new tradie's version only means editing those two files plus the images.
- Point images at images/*.webp.
- Start with the homepage. Show it to me in a local preview before building the other pages.
```
