# Agent Notes — VSN 1IBK BW Schriftliche Arbeit 13-04-2026

## Project Purpose
Transform raw bilingual (EN/DE) sales contract study material into a professionally branded, print-ready HTML learning document.

## Directory Structure
```
/MADE/
  RAW.md            ← Source content (1063 lines, bilingual EN/DE)
  agent.md          ← This file
  kaufvertrag.html  ← OUTPUT (generated)
  assets/
    VSN_new.png     ← VSN logo (7604 bytes, PNG)
```

## VSN Brand Identity
- Primary: `#1e2e48` (Dark Blue) — headers, table headers
- Secondary: `#fbc92d` (Yellow) — accent borders, bullets
- Complementary: `#dc4ebf` (Magenta) — subtitles, nav highlights
- Body font: Open Sans (Google Fonts)
- Mono font: Roboto Mono (formulas, clauses, code)

## Callout Box System
| Tag | Color | Hex | Usage |
|---|---|---|---|
| [DEFINITION] | Magenta | rgba(220,78,191,0.7) | Definitions, key concepts |
| [INFO] | Blue | rgba(41,128,185,0.7) | Facts, exceptions, context |
| [TIP] | Yellow | rgba(251,201,45,0.7) | Exam tips, shortcuts |

## Content Structure (RAW.md)
The RAW.md contains TWO documents merged into one file:
- **Doc A (lines 1–691):** Sales Contracts: Initiation, Conclusion, Fulfillment, Components
  - NOTE: Lines 66-409 contain a duplicate of Doc A intro — this is a RAW source artifact, IGNORE the duplicate block.
- **Doc B (lines 694–1063):** Sales Contract Preparation: Inquiry, Offer, Order

Both documents overlap in topic (Anbahnung, Anfrage, Angebot) — Doc B expands with more detail on writing inquiries/offers and the Bezugskalkulation formula.

## Output File: kaufvertrag.html
- Self-contained HTML with embedded CSS + Google Fonts CDN links
- Logo: relative path `./assets/VSN_new.png`
- Bilingual layout: CSS Grid `1fr 1fr` side-by-side EN|DE
- A4 print-optimized with `@page` and `@media print` rules
- Page breaks between major sections

## Key Design Decisions
- Two-column bilingual grid for all content sections
- SVG diagrams inline for: Offer Types Flowchart, Binding Duration Timeline
- Bezugskalkulation formula displayed in Roboto Mono code-style block
- Tables: dark blue header `#1e2e48`, alternating rows `#f5f7fa`
- Callout boxes: 70% opacity bg, 8px border-radius, SVG icons, box-shadow

## GitHub
- Push all changes after generation is complete
- Branch: stay on current branch unless told otherwise
- Commit message: "feat: add kaufvertrag.html learning material"

## Lessons Learned
- RAW.md has content duplication — always deduplicate when generating
- The [DIAGRAM SUGGESTION] tags in source → replace with actual inline SVG
- Logo at `./assets/VSN_new.png` — verify relative path works from HTML file location
- Print color adjust: add `-webkit-print-color-adjust: exact; print-color-adjust: exact;` to preserve callout backgrounds when printing
