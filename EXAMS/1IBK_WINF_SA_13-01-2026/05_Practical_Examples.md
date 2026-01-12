# 05 - Practical Examples | Praktische Beispiele

**Navigation:**
- ← Previous: Open file **04_Excel_Functions.md**
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**

---

## 📑 In This File

1. [Sales Analysis (Hausverkauf, Outletcenter)](#sales-analysis)
2. [Employee Management (H2O Trink. Wasser)](#employee-management)
3. [Stock & Order Management](#stock-and-order-management)
4. [Salary Calculations](#salary-calculations)
5. [Interest Calculations](#interest-calculations)
6. [Exam Practice Checklist](#exam-practice-checklist)

---

## Sales Analysis

### Hausverkauf / Outletcenter Tasks

| Task | Function/Approach |
|------|-------------------|
| Total sum of offers | `=SUMME(Angebote)` |
| Highest offer | `=MAX(Angebote)` |
| Lowest offer | `=MIN(Angebote)` |
| Average offer | `=MITTELWERT(Angebote)` |
| Number of offers | `=ANZAHL(Angebote)` |

⚡ **EXAM TIP:** Format amounts as currency without decimals using: `#.##0 €`

---

## Employee Management

### H2O Trink. Wasser Tasks

**Sorting Tasks:**
- Sort alphabetically by last name
- Sort by age (youngest first)
- Sort by highest annual salary

**Filtering Tasks:**
- Filter male employees in "Sekretariat" → then count with `ANZAHL2`
- Count apprentices ("Lehrlinge") per department
- Filter employees in "Logistik, Marketing, Vertrieb" earning > €40,000
- Filter salary > €40,000 OR < €30,000

**Bonus Calculations:**

1.5% bonus for "Vertrieb" department:
```
=WENN(Abteilung="Vertrieb"; Gehalt*1,015; Gehalt)
```

💡 **KEY POINT:** Always use absolute reference for bonus percentage if it's in a fixed cell:
```
=WENN(Abteilung="Vertrieb"; Gehalt*(1+$B$20); Gehalt)
```

---

## Stock and Order Management

### Fressnapf - Stock Level Formatting

| Condition | Conditional Format |
|-----------|-------------------|
| Stock < 100 kg | Light red fill (reorder needed) |
| Initial stock > 200 kg | Blue font |

### H2O Bestellungen - Order Classification

| Order Quantity | Status | Format |
|----------------|--------|--------|
| < 35,000 bottles | Unprofitable | Light red fill |
| 35,000 – 60,000 | Critical | Yellow fill |
| > 60,000 | Optimal | Green checkmark ✓ |

### Gasthof Bieriger Bär - Inventory Alerts

| Item | Condition | Format |
|------|-----------|--------|
| Beer barrels | ≤ 5 | Red font |
| Wine bottles | < 20 | Red font |
| Wine bottles | = 20 | Violet font |
| Cola bottles | ≤ 10 | Red font |

### Stock Calculation Formula

```
Current Stock = Initial Stock - Sales + Additions
Aktueller Bestand = Anfangsbestand - Verkauf + Zugang
```

---

## Salary Calculations

### Formulas Summary

| Calculation | Formula |
|-------------|---------|
| Individual wage | `=Stunden * Stundenlohn` |
| Sum of all wages | `=SUMME(Lohnzahlungen)` |
| Average wage | `=MITTELWERT(Lohnzahlungen)` |
| Number of employees | `=ANZAHL2(Mitarbeiterliste)` |
| Highest wage | `=MAX(Lohnzahlungen)` |
| Lowest wage | `=MIN(Lohnzahlungen)` |
| % share of total | `=Einzellohn/SUMME($C$2:$C$20)` |

⚡ **EXAM TIP:** Use absolute reference for the total sum when calculating percentages so it doesn't change when copying!

---

## Interest Calculations

### Tiered Interest Rate Problem

**Scenario:**
- If balance > €10,000 → apply 3% interest
- Otherwise → apply 2.25% interest

**Solution:**
```
=WENN(Guthaben>10000; Guthaben*0,03; Guthaben*0,0225)
```

**Calculate new balance:**
```
=Guthaben + Zinsbetrag
```

💡 **KEY POINT:** Format interest rates as percentages and amounts as currency for clarity.

---

## Exam Practice Checklist

### ⚡ Quick Review: Must-Know Formulas

**Aggregation:**
- [ ] `=SUMME(range)` - adds all values
- [ ] `=MITTELWERT(range)` - calculates average
- [ ] `=MAX(range)` / `=MIN(range)` - finds extremes

**Counting:**
- [ ] `=ANZAHL(range)` - counts numbers only
- [ ] `=ANZAHL2(range)` - counts all non-empty

**Conditional:**
- [ ] `=WENN(test; true_value; false_value)`

**Subtotals:**
- [ ] `=TEILERGEBNIS(9; range)` - SUM ignoring hidden rows

**Dates:**
- [ ] `=HEUTE()` - today's date
- [ ] `=DATEDIF(start; end; "y")` - years between dates

### ⚡ Quick Review: Formatting

**Custom Number Formats:**
- `0" m²"` - adds unit text
- `#.##0,00 €` - currency with decimals
- `00000000` - leading zeros (8 digits)
- `[Blue]#;[Red]-#` - colors by value

**Conditional Formatting:**
- Formula for entire row: `=$B2>value`
- Always test conditions before the exam!

### ⚡ Quick Review: Cell References

| Type | Example | F4 Toggles To |
|------|---------|---------------|
| Relative | A1 | $A$1 |
| Absolute | $A$1 | A$1 |
| Mixed | A$1 | $A1 |
| Mixed | $A1 | A1 |

---

## 🎯 Final Exam Preparation

1. ✅ Review all definitions in files 01-04
2. ✅ Practice each function type with sample data
3. ✅ Test conditional formatting on real spreadsheets
4. ✅ Write out WENN formulas by hand
5. ✅ Memorize the TEILERGEBNIS function numbers (9=SUM, 2=COUNT)
6. ✅ Practice with files on Teams as mentioned in class materials

---

**Good luck on your exam! | Viel Erfolg bei der Prüfung! 🍀**

---

**Navigation:**
- ← Previous: Open file **04_Excel_Functions.md**
- → Finished! Return to file **00_MASTER_Study_Guide.md** for review
- ↑ Back to Master Guide: Open file **00_MASTER_Study_Guide.md**
