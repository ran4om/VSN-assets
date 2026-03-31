**Navigation:**
- ← Previous: Open file `08_Umsatzsteuer.md`
- → Next: Continue to file `10_Bruttogewinn.md`
- ↑ Back to Master Guide: Open file `00_MASTER_Study_Guide.md`

---

# Spezifische Geschäftsfälle | Specific Business Transactions

This section covers common business transactions and their journal entries.

---

## Waren-Einkauf | Purchase of Goods

### English

**Example: Purchase €3,136.80 including 20% VAT (on credit)**

```
Calculation:
Netto = 3,136.80 ÷ 1.20 = €2,614.00
VAT = 3,136.80 - 2,614.00 = €522.80

Journal Entry:
5000 Handelswareneinsatz  2,614.00  /
    33039 Lieferanten            3,136.80
    2500 Vorsteuer                522.80
```

**Profit Impact:** G↓ (Cost of goods sold is an expense)

### Deutsch

**Beispiel: Einkauf €3.136,80 inkl. 20% USt (auf Ziel)**

```
Berechnung:
Netto = 3.136,80 ÷ 1,20 = €2.614,00
USt = 3.136,80 - 2.614,00 = €522,80

Buchungssatz:
5000 Handelswareneinsatz  2.614,00  /
    33039 Lieferanten            3.136,80
    2500 Vorsteuer                522,80
```

---

## Waren-Verkauf | Sale of Goods

### English

**Example: Sale €586.80 including 20% VAT**

```
Calculation:
Netto = 586.80 ÷ 1.20 = €489.00
VAT = 586.80 - 489.00 = €97.80

Journal Entry:
20004 Kunde  586.80  /
    4000 Handelswarenerlöse      489.00
    3500 Umsatzsteuer             97.80
```

**Profit Impact:** G↑ (Sales revenue increases profit)

### Deutsch

**Beispiel: Verkauf €586,80 inkl. 20% USt**

```
Berechnung:
Netto = 586,80 ÷ 1,20 = €489,00
USt = 586,80 - 489,00 = €97,80

Buchungssatz:
20004 Kunde  586,80  /
    4000 Handelswarenerlöse      489,00
    3500 Umsatzsteuer             97,80
```

---

## Forderungen und Verbindlichkeiten | Receivables and Payables

### Ausgleich AR (Settlement of Receivables)

**Example: Customer pays invoice**

```
Journal Entry:
2800 Bank  586.80  /  20004 Kunde  586.80
```

**Profit Impact:** GØ (neutral) - Asset exchange

### Ausgleich ER (Settlement of Payables)

**Example: Pay supplier invoice**

```
Journal Entry:
33039 Lieferanten  3,136.80  /  2800 Bank  3,136.80
```

**Profit Impact:** GØ (neutral) - Asset exchange

---

## Private Entnahmen | Private Withdrawals

### Private Geldentnahme (Cash Withdrawal)

```
Journal Entry:
9600 Privat  1,500.00  /  2700 Kassa  1,500.00
```

**Profit Impact:** GØ (neutral) - Directly affects equity

### Private Geldeinlage (Cash Deposit)

```
Journal Entry:
2700 Kassa  5,000.00  /  9600 Privat  5,000.00
```

**Profit Impact:** GØ (neutral) - Directly affects equity

---

## 💡 KEY POINT: Profit Impact Summary

| Transaction Type | Booking | Profit Effect |
|------------------|---------|---------------|
| Expense in Soll | Aufwand ↑ | G↓ |
| Revenue in Haben | Ertrag ↑ | G↑ |
| Only Balance Sheet | Bestandskonten | GØ (neutral) |

---

## ⚡ EXAM TIP

When forming journal entries:

1. **Identify accounts** - Which accounts are affected?
2. **Determine account types** - Bestandskonten or Erfolgskonten?
3. **Apply booking rules** - Is it an increase or decrease?
4. **Check for VAT** - Is there 20%, 10%, or 13%?
5. **Determine profit impact** - G↑, G↓, or GØ?

---

**Navigation:**
- ← Previous: Open file `08_Umsatzsteuer.md`
- → Next: Continue to file `10_Bruttogewinn.md`
- ↑ Back to Master Guide: Open file `00_MASTER_Study_Guide.md`
