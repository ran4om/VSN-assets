**Navigation:**
- ← Previous: Open file `07_Buchungsregeln.md`
- → Next: Continue to file `09_Geschaeftsfaelle.md`
- ↑ Back to Master Guide: Open file `00_MASTER_Study_Guide.md`

---

# Umsatzsteuer (VAT) | Value Added Tax

> **DEFINITION:** Value Added Tax (Umsatzsteuer) is a consumption tax placed on products and services at each stage of production.

---

## Key Terms | Wichtige Begriffe

### Vorsteuer (Input VAT)

> **DEFINITION:** The VAT paid to suppliers on purchases. It is a **claim against the tax authority**.

| | |
|---|---|
| Account | 2500 Vorsteuer |
| Type | Aktive Bestandskonto (Active Balance Sheet Account) |
| Treatment | Debit (Soll) when incurred |

### Umsatzsteuer (Output VAT)

> **DEFINITION:** The VAT charged to customers on sales. It is a **liability to the tax authority**.

| | |
|---|---|
| Account | 3500 Umsatzsteuer |
| Type | Passive Bestandskonto (Passive Balance Sheet Account) |
| Treatment | Credit (Haben) when incurred |

### USt-Zahllast (VAT Payable/Receivable)

> **DEFINITION:** Account 3520 used at month-end to rebook Vorsteuer and Umsatzsteuer balances.

| | |
|---|---|
| Account | 3520 USt-Zahllast |
| Type | Passive Bestandskonto |

---

## VAT Rates | Umsatzsteuersätze

| Rate | German | English | Application |
|------|--------|---------|-------------|
| **20%** | Normalsteuersatz | Standard rate | Most goods and services |
| **10%** | Ermäßigter Satz | Reduced rate | Certain food, books, etc. |
| **13%** | Sonstige Leistungen | Other services | Some specific services |

---

## Kleinbetragsrechnungen | Small Invoices

> **DEFINITION:** For invoices ≤ €400 (gross), VAT is not shown separately.

### English

Calculate VAT from gross amount:

| VAT Rate | Formula |
|----------|---------|
| 20% | `VAT = Gross ÷ 6` |
| 10% | `VAT = Gross ÷ 11` |
| 13% | `VAT = Gross ÷ 13 × 0.13` |

### Deutsch

Berechnung aus Bruttobetrag:

| USt-Satz | Formel |
|----------|--------|
| 20% | `USt = Brutto ÷ 6` |
| 10% | `USt = Brutto ÷ 11` |
| 13% | `USt = Brutto ÷ 13 × 0.13` |

---

## Example Calculation | Beispielrechnung

### English

**Invoice: €332 including 20% VAT**

```
Netto = 332 ÷ 1.20 = €276.67
VAT = 332 - 276.67 = €55.33
OR: VAT = 332 ÷ 6 = €55.33
```

### Deutsch

**Rechnung: €332 inkl. 20% USt**

```
Netto = 332 ÷ 1,20 = €276,67
USt = 332 - 276,67 = €55,33
ODER: USt = 332 ÷ 6 = €55,33
```

---

## USt-Zahllast Settlement | USt-Zahllast Ausgleich

### English

At the end of each month:

1. **Rebook Input VAT:** `3520 USt-Zahllast / 2500 Vorsteuer`
2. **Rebook Output VAT:** `3500 USt / 3520 USt-Zahllast`
3. **Settle:** `3520 USt-Zahllast / 2800 Bank`

**Result:**
- If USt > Vorsteuer → Payment to tax authority
- If Vorsteuer > USt → Refund from tax authority

### Deutsch

Am Monatsende:

1. **Vorsteuer umbuchen:** `3520 USt-Zahllast / 2500 Vorsteuer`
2. **Umsatzsteuer umbuchen:** `3500 USt / 3520 USt-Zahllast`
3. **Ausgleich:** `3520 USt-Zahllast / 2800 Bank`

---

## ⚡ EXAM TIP

Remember the VAT flow:

- **Kunde zahlt** → brutto price (Netto + USt)
- **Unternehmen berechnet** → USt on sales, pays Vorsteuer on purchases
- **Difference** → USt-Zahllast to be paid to Finanzamt

For small invoices (≤€400), always use the division method to calculate VAT!

---

**Navigation:**
- ← Previous: Open file `07_Buchungsregeln.md`
- → Next: Continue to file `09_Geschaeftsfaelle.md`
- ↑ Back to Master Guide: Open file `00_MASTER_Study_Guide.md`
