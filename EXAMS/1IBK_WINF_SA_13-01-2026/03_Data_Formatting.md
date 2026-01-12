# 03 - Data Formatting | Datenformatierung

**Navigation:**
- ← Previous: Open file **02_Data_Organization.md**
- → Next: Continue to file **04_Excel_Functions.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**

---

## 📑 In This File

1. [Custom Number Formats](#custom-number-formats)
2. [Conditional Formatting](#conditional-formatting)
3. [Text Alignment](#text-alignment)

---

## Custom Number Formats

### English
> **DEFINITION:** Custom number formats allow you to display numbers in a specific way without changing their underlying value. They are defined by up to four sections, separated by semicolons.

### Deutsch
> **DEFINITION:** Benutzerdefinierte Zahlenformate ermöglichen es Ihnen, Zahlen auf eine bestimmte Weise anzuzeigen, ohne deren zugrunde liegenden Wert zu ändern. Sie werden durch bis zu vier Abschnitte definiert, die durch Semikolons getrennt sind.

### The Four-Section Syntax

```
[Positive];[Negative];[Zero];[Text]
```

| Section | Purpose | Zweck |
|---------|---------|-------|
| 1st | Positive numbers | Positive Zahlen |
| 2nd | Negative numbers | Negative Zahlen |
| 3rd | Zero values | Nullwerte |
| 4th | Text values | Textwerte |

### Placeholder Symbols

| Symbol | Meaning EN | Bedeutung DE |
|--------|-----------|--------------|
| `#` | Optional digit (no leading zeros) | Optionale Ziffer (keine führenden Nullen) |
| `0` | Required digit (shows zeros) | Erforderliche Ziffer (zeigt Nullen) |
| `@` | Text placeholder | Textplatzhalter |
| `[Color]` | Font color (e.g., [Red], [Blue]) | Schriftfarbe (z.B. [Rot], [Blau]) |

### Common Format Examples

| Desired Output | Format Code |
|----------------|-------------|
| 80 m² | `0" m²"` |
| 27881 EUR | `0" EUR"` |
| 1,75% p.a. | `0,00"% p.a."` |
| 1.250 Liter | `#.##0" Liter"` |
| 1,1 Mio. | `0,0" Mio."` |
| 00012369 (8 digits) | `00000000` |
| Currency € | `#.##0,00 €` |
| Negative in red | `[Blue]#.##0;[Red]-#.##0` |

💡 **KEY POINT:** Text appended to numbers must be enclosed in double quotes: `" Stück"`

⚡ **EXAM TIP:** Custom formats only change the DISPLAY, not the VALUE. Calculations still work on the original number!

---

## Conditional Formatting

### English
> **DEFINITION:** Conditional formatting automatically applies formatting (like colors, icon sets, data bars) to cells based on their values.

### Deutsch
> **DEFINITION:** Die bedingte Formatierung wendet automatisch Formatierungen (wie Farben, Symbolsätze, Datenbalken) auf Zellen basierend auf deren Werten an.

### How to Create Rules

1. Select your data range
2. Go to **Home → Conditional Formatting → New Rule**
3. Choose rule type
4. Set conditions and format
5. Click OK

### Rule Types

| Type | Description |
|------|-------------|
| **Highlight Cells Rules** | Greater Than, Less Than, Between, Text Contains |
| **Top/Bottom Rules** | Top 10 Items, Bottom 10% |
| **Data Bars** | Visual bar based on value |
| **Color Scales** | Gradient colors (low to high) |
| **Icon Sets** | Symbols (✓, ⚠, ✗) based on thresholds |
| **Formula-based** | Most flexible - use custom formulas |

### Practical Examples

| Scenario | Condition | Format |
|----------|-----------|--------|
| Stock < 100 kg | Less than 100 | Light red fill |
| Initial stock > 200 kg | Greater than 200 | Blue font |
| Orders < 35,000 | Unprofitable | Red fill |
| Orders 35,000–60,000 | Critical | Yellow fill |
| Orders > 60,000 | Optimal | Green checkmark ✓ |
| Beer barrels ≤ 5 | Low stock | Red font |
| Phone call after 18:00 | Time condition | Highlight entire row |

### Formula-Based Conditional Formatting

⚡ **EXAM TIP:** When using a formula for an entire row, make the column reference absolute but the row relative:

```
=$B2>ZEIT(18;0;0)
```

This formats the entire row if the time in column B is after 18:00.

💡 **KEY POINT:** The `$` locks the column (B) while the row number (2) adjusts as the rule applies to each row.

---

## Text Alignment

### Alignment Options

| Option | Description EN | Beschreibung DE |
|--------|---------------|-----------------|
| **Text Wrap** | Wraps long text in cell | Umbricht langen Text in Zelle |
| **Horizontal** | Left, Center, Right | Links, Mitte, Rechts |
| **Vertical** | Top, Middle, Bottom | Oben, Mitte, Unten |
| **Indent** | Moves text from cell edge | Verschiebt Text vom Rand |
| **Rotate Text** | Angle or vertical orientation | Winkel oder vertikale Ausrichtung |

💡 **KEY POINT:** Use **Text Wrap** (`Textumbruch`) for long text in narrow columns to improve readability.

---

## ✅ Section Checklist

- [ ] I understand the four-section custom format syntax
- [ ] I can use # and 0 placeholders correctly
- [ ] I can add text to number formats with quotes
- [ ] I know how to create conditional formatting rules
- [ ] I can write formula-based conditions with proper cell references
- [ ] I understand when to use icon sets vs. color formatting

---

**Navigation:**
- ← Previous: Open file **02_Data_Organization.md**
- → Next: Continue to file **04_Excel_Functions.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**
