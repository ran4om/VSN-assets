# Agent Notes — 1IBK DEUTSCH LZK 15-04-2026

## Project Overview
This folder holds VSN-branded learning materials for the **1IBK German LZK exam on April 15, 2026**.

---

## File Structure
```
1IBK_DEUTSCH_LZK_15-04-2026/
├── RAW/                          # Raw source files
│   ├── Deutsch_Grammatik_Komplett.md   # Combined full raw Markdown (106 KB!)
│   └── combine.py                      # Script that merges RAW markdown files
├── MADE/                         # Output: finished learning materials
│   ├── assets/
│   │   └── VSN_new.png           # VSN logo (use with: filter: brightness(0) invert(1) for white)
│   ├── deutsch_grammatik_satzgefuege.html  # Satzgefüge & Nebensätze learning material
│   └── agent.md                  # This file
└── RAW.md                        # Another raw source (20 KB)
```

---

## VSN Design System (for all HTML outputs)

### Colors
- Primary: `#1e2e48` — headers, table headers, main brand identity
- Secondary: `#fbc92d` — accents, borders, section dividers
- Accent/Complementary: `#dc4ebf` — Definition callout boxes, subtitle highlights
- Info Blue: `#2980b9` — Info callout boxes
- Background: `#f7f8fb` — light section backgrounds

### Fonts
- Body: `Open Sans` (Google Fonts)
- Specialized (code/formulas): `Roboto Mono` (Google Fonts)
- Display (cover title): `Playfair Display` (for premium feel)

### Callout Boxes (3 types)
| Type | Border Color | Background | Label Color | Usage |
|------|-------------|-----------|-------------|-------|
| Definition | `#dc4ebf` | `rgba(220,78,191,0.12)` | `#c0359e` | Definitions, key concepts |
| Info | `#2980b9` | `rgba(41,128,185,0.10)` | `#1a6a9a` | Facts, exceptions, notes |
| Tip | `#d4a800` | `rgba(251,201,45,0.15)` | `#8a6b00` | Exam tips, shortcuts |

### CRITICAL: Print Color Fix
Always include this in every HTML for print:
```css
* {
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```
Without this, browsers strip all background colors in print/PDF mode → callout boxes become invisible white boxes.

### Page Setup
```css
@page { size: A4; margin: 15mm 18mm 18mm 18mm; }
```

---

## Document Architecture Pattern

### For bilingual EN/DE documents:
```html
<div class="bilingual-grid">
  <div class="col-en"> <!-- border-right: 3px solid #fbc92d --> </div>
  <div class="col-de"> <!-- padding-left: 22px --> </div>
</div>
```

### For major sections:
- Wrap each section in `<div class="section page-break">` for proper PDF pagination
- Section header uses: number badge (primary bg, secondary text) + title block

### Logo usage:
```html
<img src="assets/VSN_new.png" alt="VSN Logo" style="filter: brightness(0) invert(1);">
```
Use `filter: brightness(0) invert(1)` on dark backgrounds for white logo.
Use `filter: none` on light backgrounds (original color).

---

## Source Content Notes

### Deutsch_Grammatik_Komplett.md (106 KB)
This is the main combined German grammar source file. It contains ALL topics for the exam combined by `combine.py`. Future materials for this exam should be extracted from this file.

### Markers in RAW content:
- `[DEFINITION]` → Magenta callout box
- `[INFO]` → Blue callout box  
- `[TIP]` → Yellow callout box
- `[CLARIFICATION NEEDED]` → Treat as Blue Info box (exception/important note)
- `[DIAGRAM SUGGESTION]` → Build an inline SVG diagram

---

## Lessons Learned

1. **SVG diagrams**: Build directly inline as `<svg>` in the HTML. Use `viewBox` for scalability. Keep font sizes at 8–11pt for legibility when printed on A4. Always set `width: 100%` and `height: auto` on the SVG element.

2. **Tables**: Always use `border-radius` on the first `th:first-child` and `th:last-child` for rounded table headers. Use `page-break-inside: avoid` on `.table-wrap`.

3. **Bilingual layout**: Two-column grid with `gap: 0` and individual column padding works better for print than `gap: X` (avoids orphan lines at column edges).

4. **Conjunction pills**: `<span class="conj-pill">` with Roboto Mono and pill shape styling makes conjunctions very scannable.

5. **NS labels**: Use `<span class="ns-label">NS 1</span>` pattern for labeling clause degrees inline in example sentences.

6. **Cover page**: Use `min-height: 100vh` for the cover but also wrap it in `page-break` class so it always ends on its own page.

---

## Git Workflow
- Always push to GitHub after generating materials.
- This project lives under the VSN organization workspace.
- Branch: use descriptive feature branches per user's global rules.
