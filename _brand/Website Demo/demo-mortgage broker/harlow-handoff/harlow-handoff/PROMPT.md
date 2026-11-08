# Prompts to paste into Claude Code

Paste these one at a time. Wait for each to finish and check the result before sending the next.

## 1. Plan

Read CLAUDE.md, then look through canvas/, assets/ and photos/PHOTO-LIST.md. Don't write code yet. Give me a short plan to rebuild this design canvas as an Astro static site: the folder structure, how each .dc.html page and component maps to Astro pages and components, how you'll handle the interactive parts (header, enquiry drawer and form, review carousel, steps, odometer, reveals), and anything in the canvas files you're unsure about.

## 2. Set up and build the shell

Go ahead with the plan. Create the Astro project in this folder, keep canvas/ untouched as the reference, move site.css, the icons and the underline into the project, and use assets/asset-map.json to replace every /_blob/ URL with a local file. Build the shared layout plus the Header, Footer, Enquiry drawer and EnquiryForm components first, then the homepage. Start the dev server and tell me the local address.

## 3. Build the rest

Now build the remaining pages from canvas/ in this order: FirstHome, NextHome, Refinancing, Investing, SelfEmployed, Building, HealthCheck, Team, the four broker profiles, Reviews, Guides, Book, Thanks, then the four legal pages. Reuse ReviewRail and CtaBand as components. Keep every [PLACEHOLDER] exactly as it is. When you're done, list anything you couldn't match to the canvas.

## 4. Check

Run the checks in CLAUDE.md. Also open every page at 390px and 1440px wide with Playwright, screenshot them into a checks/ folder, and fix anything that overflows, overlaps or looks different from the canvas. Test with reduced motion turned on. Then give me a short report.
