# 04 - Excel Functions | Excel-Funktionen

**Navigation:**
- ← Previous: Open file **03_Data_Formatting.md**
- → Next: Continue to file **05_Practical_Examples.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**

---

## 📑 In This File

1. [Aggregation Functions](#aggregation-functions)
2. [Counting Functions](#counting-functions)
3. [The IF (WENN) Function](#the-if-function)
4. [Date and Time Functions](#date-and-time-functions)
5. [Financial Calculations](#financial-calculations)

---

## Aggregation Functions

### English
> **DEFINITION:** Aggregation functions perform common statistical calculations on a range of numbers.

### Deutsch
> **DEFINITION:** Aggregationsfunktionen führen gängige statistische Berechnungen für einen Zahlenbereich durch.

### Function Reference

| Function | Purpose EN | Zweck DE | Syntax |
|----------|-----------|----------|--------|
| `SUMME` | Sum of all values | Summe aller Werte | `=SUMME(A1:A10)` |
| `MITTELWERT` | Average (mean) | Durchschnitt | `=MITTELWERT(A1:A10)` |
| `MAX` | Largest value | Größter Wert | `=MAX(A1:A10)` |
| `MIN` | Smallest value | Kleinster Wert | `=MIN(A1:A10)` |

### Common Tasks

- Calculate total sum of house offers
- Find highest and lowest salary
- Calculate average customer payment
- Determine max/min sales figures

---

## Counting Functions

### English
> **DEFINITION:** Counting functions count the number of cells in a range that meet specific criteria.

### Deutsch
> **DEFINITION:** Zählfunktionen zählen die Anzahl der Zellen in einem Bereich, die bestimmte Kriterien erfüllen.

### Function Comparison

| Function | Counts | Zählt |
|----------|--------|-------|
| `ANZAHL` | Cells containing **numbers only** | Nur Zellen mit **Zahlen** |
| `ANZAHL2` | **All non-empty** cells (numbers, text, errors) | **Alle nicht-leeren** Zellen |

### When to Use Each

- `ANZAHL`: Count numeric entries (e.g., how many prices are listed)
- `ANZAHL2`: Count items with any content (e.g., how many employees in a list)

⚡ **EXAM TIP:** After filtering data, use `ANZAHL2` to count visible results. Example: Count male employees in "Sekretariat" department after filtering.

---

## The IF Function

### English
> **DEFINITION:** The `WENN` (IF) function checks whether a condition is met and returns one value if TRUE, and another value if FALSE.

### Deutsch
> **DEFINITION:** Die `WENN`-Funktion prüft, ob eine Bedingung erfüllt ist, und gibt einen Wert zurück, wenn WAHR, und einen anderen Wert, wenn FALSCH.

### Syntax

```
=WENN(condition; value_if_true; value_if_false)
=WENN(Prüfung; Dann_Wert; Sonst_Wert)
```

### Components

| Part | Description EN | Beschreibung DE |
|------|---------------|-----------------|
| `condition` | The test to evaluate | Die zu prüfende Bedingung |
| `value_if_true` | Result when TRUE | Ergebnis wenn WAHR |
| `value_if_false` | Result when FALSE | Ergebnis wenn FALSCH |

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `=` | Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `<>` | Not equal to |

### Practical Examples

| Scenario | Formula |
|----------|---------|
| Bonus if sales ≥ €50,000 | `=WENN(Umsatz>=50000;"Bonus";"-")` |
| Salutation by gender | `=WENN(Geschlecht="m";"Herr";"Frau")` |
| Pass/Fail (27+ points needed) | `=WENN(Punkte>=27;"bestanden";"nicht bestanden")` |
| Discount if total > €500 | `=WENN(Rechnungssumme>500;"ja";"nein")` |
| Tiered interest rate | `=WENN(Guthaben>10000;Guthaben*0,03;Guthaben*0,0225)` |
| Commission check | `=WENN(Umsatz>50000;"Ja";"Nein")` |

💡 **KEY POINT:** Text values in the result must be enclosed in double quotes: `"bestanden"`

⚡ **EXAM TIP:** Use absolute references (`$B$16`) for threshold values that shouldn't change when copying formulas!

---

## Date and Time Functions

### English
> **DEFINITION:** Excel provides functions to work with dates and times, allowing calculations based on these values.

### Deutsch
> **DEFINITION:** Excel bietet Funktionen zur Arbeit mit Daten und Zeiten, die Berechnungen auf der Grundlage dieser Werte ermöglichen.

### Function Reference

| Function | Purpose EN | Zweck DE | Example |
|----------|-----------|----------|---------|
| `HEUTE()` | Current date | Heutiges Datum | `=HEUTE()` |
| `DATUM` | Create date from parts | Datum erstellen | `=DATUM(2026;1;12)` |
| `JAHR` | Extract year | Jahr extrahieren | `=JAHR(A1)` |
| `MONAT` | Extract month | Monat extrahieren | `=MONAT(A1)` |
| `TAG` | Extract day | Tag extrahieren | `=TAG(A1)` |
| `DATEDIF` | Difference between dates | Differenz zwischen Daten | `=DATEDIF(A1;B1;"d")` |

### DATEDIF Units

| Unit | Returns | Gibt zurück |
|------|---------|------------|
| `"d"` | Days | Tage |
| `"m"` | Months | Monate |
| `"y"` | Years | Jahre |

### Age Calculation Example

```
=DATEDIF(Geburtsdatum; HEUTE(); "y")
```
This returns the person's age in years.

⚡ **EXAM TIP:** Combine with WENN for age-based conditions:
```
=WENN(DATEDIF(Geburt;HEUTE();"d")<10000;"sehr JUNG";"nicht so jung")
```

---

## Financial Calculations

### Interest Calculation

> **DEFINITION:** Interest calculation determines the amount earned on a principal sum.

**Formulas:**
- Interest Amount: `=Kapital * Zinssatz`
- New Balance: `=Kapital + Zinsbetrag`

### Tiered Interest Example

If balance > €10,000 → 3% interest  
Otherwise → 2.25% interest

```
=WENN(Guthaben>10000; Guthaben*0,03; Guthaben*0,0225)
```

### Salary Calculations

| Calculation | Formula |
|-------------|---------|
| Individual wage | `=Stunden * Stundenlohn` |
| Total wages | `=SUMME(Lohnzahlungen)` |
| Average wage | `=MITTELWERT(Lohnzahlungen)` |
| % of total | `=Einzellohn / SUMME(Alle_Löhne)` |

---

## ✅ Section Checklist

- [ ] I can use SUMME, MITTELWERT, MAX, MIN correctly
- [ ] I understand the difference between ANZAHL and ANZAHL2
- [ ] I can write WENN formulas with proper syntax
- [ ] I know when to use absolute references in WENN
- [ ] I can calculate age using DATEDIF and HEUTE
- [ ] I can implement tiered interest calculations

---

**Navigation:**
- ← Previous: Open file **03_Data_Formatting.md**
- → Next: Continue to file **05_Practical_Examples.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**
