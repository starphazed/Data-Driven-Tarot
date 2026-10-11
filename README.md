# Data-Driven Tarot

A static companion site for a twelve-card handmade tarot deck.

## Preview

Run `python -m http.server 8766` and open http://localhost:8766.
No build step, JavaScript, external fonts, or package installation is required.

## Editing

- `index.html`: introduction and card gallery
- `card1.html` through `card12.html`: original card introductions and meanings
- `process.html`: illustrated project case study and credits
- `style.css`: shared responsive layout and typography
- `assets/`: optimized WebP versions of the original photographs

Keep all existing HTML filenames and the repository's GitHub Pages address unchanged: the physical QR codes point to these URLs. Original card PNGs and source photographs are retained.

Run `python verify.py` to check internal links, anchors, image attributes, heading structure, and preservation of the original card text. This verifies website structure and content, not physical QR scanning.

## Refresh verification

All 14 pages passed structural checks. Homepage, card reading, and case-study layouts were visually inspected at desktop/phone sizes during development. Existing artwork is reused, with no generated replacement photos. Four optimized photographs total approximately 900 KB versus 4.7 MB for the original JPEGs.
