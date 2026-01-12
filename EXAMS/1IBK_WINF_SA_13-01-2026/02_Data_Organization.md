# 02 - Data Organization & Analysis | Datenorganisation & -analyse

**Navigation:**
- ← Previous: Open file **01_Excel_Basics.md**
- → Next: Continue to file **03_Data_Formatting.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**

---

## 📑 In This File

1. [Filtering Data](#filtering-data)
2. [Sorting Data](#sorting-data)
3. [Subtotals (TEILERGEBNIS)](#subtotals)

---

## Filtering Data

### English
> **DEFINITION:** Filtering allows you to display only the rows that meet specific criteria, temporarily hiding the other rows.

### Deutsch
> **DEFINITION:** Filtern ermöglicht es Ihnen, nur die Zeilen anzuzeigen, die bestimmte Kriterien erfüllen, während die anderen Zeilen vorübergehend ausgeblendet werden.

### How to Activate Filters

1. Select your data range (including headers)
2. Go to **Data** tab (Daten)
3. Click **Filter** button
4. Dropdown arrows appear in each column header

### Filter Types

| Filter Type | Description EN | Beschreibung DE |
|-------------|---------------|-----------------|
| **Table Filters** | Basic dropdown selection | Einfache Dropdown-Auswahl |
| **Number Filters** | Greater than, Less than, Between | Größer als, Kleiner als, Zwischen |
| **Text Filters** | Contains, Begins with, Ends with | Enthält, Beginnt mit, Endet mit |

### Practical Filter Examples

⚡ **EXAM TIP:** Common exam tasks include:

- Filter female employees earning > €40,000
- Show only "AHS" branch data
- Filter numbers less than 20,000
- Find items matching criteria in multiple columns (AND logic)

⚡ **PRÜFUNGSTIPP:** Häufige Prüfungsaufgaben:

- Weibliche Mitarbeiter filtern, die > 40.000 € verdienen
- Nur Daten der Filiale "AHS" anzeigen
- Zahlen filtern, die kleiner als 20.000 sind
- Elemente finden, die Kriterien in mehreren Spalten erfüllen (UND-Logik)

---

## Sorting Data

### English
> **DEFINITION:** Sorting arranges data in a specified order (e.g., alphabetical, numerical, chronological).

### Deutsch
> **DEFINITION:** Sortieren ordnet Daten in einer bestimmten Reihenfolge an (z.B. alphabetisch, numerisch, chronologisch).

### Sort Types

| Type | Description EN | Beschreibung DE |
|------|---------------|-----------------|
| **Single-level** | Sorts by one column | Sortiert nach einer Spalte |
| **Multi-level** | Primary, secondary, tertiary keys | Primäre, sekundäre, tertiäre Schlüssel |

### Practical Sorting Examples

- Sort employees alphabetically by last name
- Sort by age (youngest first)
- Sort by salary (highest first)
- Sort cars by "previous owner" then by "list price"

💡 **KEY POINT:** Multi-level sorting is accessed via **Data → Sort** (not the quick A-Z button).

---

## Subtotals

### TEILERGEBNIS Function

### English
> **DEFINITION:** The `TEILERGEBNIS` (SUBTOTAL) function returns a subtotal in a list or database. It can perform different calculations and **ignores rows hidden by a filter**.

### Deutsch
> **DEFINITION:** Die Funktion `TEILERGEBNIS` liefert ein Teilergebnis in einer Liste oder Datenbank. Sie kann verschiedene Berechnungen durchführen und **ignoriert Zeilen, die durch einen Filter ausgeblendet wurden**.

### Syntax

```
=TEILERGEBNIS(function_number; range)
```

### Function Numbers

| Number | Function | Funktion |
|--------|----------|----------|
| 1 | AVERAGE | MITTELWERT |
| 2 | COUNT | ANZAHL |
| 9 | SUM | SUMME |
| 4 | MAX | MAX |
| 5 | MIN | MIN |

### Example

```
=TEILERGEBNIS(9; B2:B100)
```
This returns the SUM of visible (filtered) values only.

⚡ **EXAM TIP:** Use `TEILERGEBNIS` instead of `SUMME` when you need totals that respect active filters!

---

## ✅ Section Checklist

- [ ] I can activate and use table filters
- [ ] I understand number and text filter options
- [ ] I can perform single-level and multi-level sorting
- [ ] I know how TEILERGEBNIS differs from regular functions
- [ ] I can write TEILERGEBNIS formulas with correct function numbers

---

**Navigation:**
- ← Previous: Open file **01_Excel_Basics.md**
- → Next: Continue to file **03_Data_Formatting.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**
