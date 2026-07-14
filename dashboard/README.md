# /dashboard

Single-page static dashboard (plain HTML/CSS/JS, no build step). Open `index.html` locally or serve via GitHub Pages.

It reads from JSON files in `data/`. Those JSON files are the interface: whenever the underlying repo files change (positioning, test log, compliance checks, research dates, pain-point map), the matching JSON in `data/` gets updated in the same commit.

Panels: positioning now, ad test log, open risks, research freshness (flags anything older than 45 days), pain points vs features matrix.
