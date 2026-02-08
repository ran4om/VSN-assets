# VSN Learning Material Generator - Agent Memory

## Project Purpose
This project contains a professional VSN-branded geography learning material (`geography_humans_nature.html`) created following VSN's unified design system specifications.

## Key Learning

### VSN Design System Implementation
- **Brand Colors**:
  - Primary (`#1e2e48`): Headers, table headers, main brand identity
  - Secondary (`#fbc92d`): Accents, borders, list bullets
  - Complementary (`#dc4ebf`): Navigation highlights, subtitle accents

- **Typography System**:
  - **Open Sans**: All body text, headings, tables, general content
  - **Roboto Mono**: Specialized text like chemical formulas (CO₂), scientific notation

- **Semantic Callout Box System** (70% opacity with rounded corners):
  - **Magenta (`#dc4ebf`)**: Key definitions (e.g., Arid, Humid, Desertification)
  - **Blue (`#2980b9`)**: Supplemental information (Geo-Facts, statistics)
  - **Yellow (`#fbc92d`)**: Practical tips (GEO-TRAINING exercises, exam tips)

### HTML/CSS Best Practices for Print Materials
1. **Bilingual Layout**: Use CSS Grid with `grid-template-columns: 1fr 1fr` for side-by-side English/German
2. **Print CSS**: Essential rules:
   ```css
   @media print {
     @page { size: A4; margin: 2cm; }
     section { page-break-before: always; }
     .callout-box, table { page-break-inside: avoid; }
   }
   ```
3. **SVG Diagrams**: Use inline SVG for resolution-independent graphics that print perfectly
4. **Self-contained HTML**: Embed all CSS, use Google Fonts CDN, minimal external dependencies

### Project Structure
```
MADE/
├── assets/
│   └── VSN_new.png (Yellow square VSN logo)
├── geography_humans_nature.html (Main deliverable)
└── agent.md (This file)
```

### How This Project Works
1. **Single HTML file** contains everything: structure, styling, content, diagrams
2. **Bilingual content** organized in two-column grid layout
3. **Three semantic callout types** guide students to definitions, facts, and tips
4. **Print-ready**: Browser print (Ctrl+P) → Save as PDF → Perfect A4/Letter output
5. **VSN branded**: Logo, colors, typography all follow brand guidelines

### Important Notes
- VSN logo must be in `assets/` folder relative to HTML file
- Google Fonts must be accessible (requires internet on first load, then cached)
- Print with "Background graphics" enabled to show callout box colors
- All content is bilingual (English/German) side-by-side

### Future VSN Projects
When creating new VSN learning materials:
1. Reuse the CSS styles from this HTML as a template
2. Follow the semantic callout box classification:
   - Magenta = Definitions
   - Blue = Supplemental Info  
   - Yellow = Tips/Exercises
3. Always use Open Sans + Roboto Mono typography
4. Always include VSN logo from `assets/` folder
5. Structure with: Header → TOC → Sections (with page breaks) → Callouts/Tables/Diagrams

### Known Best Practices
- **Bilingual**: Two-column grid with border between languages
- **Page breaks**: Each major section starts new page
- **Callout icons**: Book (definitions), Info-circle (facts), Lightbulb (tips)
- **Tables**: Dark blue headers (#1e2e48), striped rows for readability
- **SVG colors**: Use VSN brand palette within diagrams
