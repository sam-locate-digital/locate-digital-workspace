# Harlow Home Loans – mortgage broker demo site (Claude Design pack)

Everything Claude Design needs to build the demo website for a fictional Melbourne eastern-suburbs mortgage broker.

## What's in this folder

| File | What it is |
| --- | --- |
| 00-README.md | This file |
| 01-opening-prompt.md | The prompt to paste into Claude Design first |
| 02-brief.md | The full design brief: business, design decisions, visual system, motion, imagery, homepage copy, other pages, interactions, reusability, QA checklist |
| 03-design-reference-opendoor.md | The original Opendoor-style design.md the look is based on (the brief overrides it where they disagree) |
| config.js | Placeholder business details, team, suburbs, stats and calculator assumptions in one object |
| reviews.json | Six illustrative reviews for the carousel and filtered pages |
| image-manifest.csv | Each Higgsfield photo, its file name, where it goes, and alt text |
| download-images.ps1 | Downloads all 12 photos into an `images` folder next to it |

## How to use it

1. Right-click `download-images.ps1` and choose **Run with PowerShell** (or run `powershell -ExecutionPolicy Bypass -File .\download-images.ps1` from this folder). It creates `images\` with all 12 photos named to match the brief.
2. In Claude Design, paste `01-opening-prompt.md`, then attach or paste `02-brief.md`.
3. Attach `config.js`, `reviews.json` and the `images` folder.
4. Optionally attach `03-design-reference-opendoor.md` for the original look and feel.
5. Before showing a real broker, swap every [PLACEHOLDER] and have their aggregator check the compliance wording.

Live, editable version of the brief: https://claude.ai/artifact/Gj7WZDusmSYyCtx2KgZbjo
