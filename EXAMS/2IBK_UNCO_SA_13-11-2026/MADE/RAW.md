# Unternehmensrechnung: Beschaffung, Absatz und Anlagen

## [English]

### 1. Posting documents in procurement and sales

#### Documents, VAT and entries

[DEFINITION] A **journal entry (Buchungssatz)** records equal amounts on the debit side, Soll, and the credit side, Haben. `Debit / Credit` below means the account before `/` is debited and the account after it is credited. E = incoming invoice, A = outgoing invoice, K = cash voucher, B = bank statement, S = other voucher, U = adjustment voucher. Amounts are euros.

[DEFINITION] **Input VAT (Vorsteuer, 2500)** is deductible VAT on qualifying purchases. **Output VAT (Umsatzsteuer, 3500)** is VAT charged on sales. At 20%, gross = net × 1,20; net = gross / 1,20; VAT = gross / 6. Use the rate on the document.

For goods bought on credit, debit 5000 HW-Einsatz and 2500 Vorsteuer, credit the supplier account 33…. For a sale on credit, debit customer account 20…, credit 4000 HW-Erlöse and 3500 Umsatzsteuer. Cash uses 2700 Kassa. A later bank payment uses 2800 Bank and clears the supplier or customer account. Source: book pp. 4–6, 36–38.

#### Fixed assets, low-value assets and vehicles

[DEFINITION] A **fixed asset (Anlagegut)** is held for lasting business use, not for resale. **Capitalisation (Aktivierung)** records acquisition cost on an asset account. The cost includes purchase price after reductions and directly attributable delivery and installation costs. Deductible input VAT is not part of cost. Ordinary repairs and fuel are expenses, not asset acquisition costs. Book pp. 7–13; Stoff.

[DEFINITION] A **low-value asset (geringwertiges Wirtschaftsgut, GWG)** is a depreciable asset with acquisition cost up to € 1.000 excluding deductible VAT, under the book's § 13 EStG rule. It must be independently usable. Items forming a functional unit are assessed together. The book treats a camera and its necessary memory card as a unit, but permits separately usable computer peripherals to be considered separately. The business may elect immediate full depreciation or capitalise and depreciate over useful life. Book pp. 8–10.

Immediate write-off: `7060 Abschreibungen GWG + 2500 Vorsteuer / 33…`, 2700 or 3180/3190. Alternatively, use the suitable asset account such as 0672 on purchase and `7060 / 0672` for full write-off at year end. Do not post both alternatives. The expense reduces profit; capitalisation alone does not.

For a normal business car, use `0630 Pkw und Kombis / supplier` for the gross price because input VAT is generally not deductible. For fuel and ordinary running costs, use `7320 Pkw-Betriebsaufwand / payment account` for gross. For a qualifying business truck use 0640 for acquisition and 7330 for running costs, with 2500 where input VAT is deductible. The book states that a zero-emission electric car costing up to € 40.000 gross qualifies for full input VAT deduction; electric vehicle rules can have further limits, so do not generalise this threshold to all cars. Book pp. 7, 13, 81–83.

**Example / Übung: printer, book pp. 7–8.** E 514, € 1.320 net + € 264 input VAT = € 1.584: `0620 1.320 + 2500 264 / 33401 1.584`. Profit € 0, cash € 0. Bank settlement: `33401 1.584 / 2800 1.584`. Profit € 0, cash −€ 1.584. Depreciation is a separate later entry.

**Example / Übung: vehicles, Ü 1.7, book p. 13.** Assume the truck and electric car meet the conditions for the book's input VAT deduction. Truck E 138: € 75.000 / 1,20 = € 62.500 net and € 12.500 VAT: `0640 62.500 + 2500 12.500 / 33159 75.000`. Later `33159 75.000 / 2800 75.000`. Diesel car E 256: no input VAT deduction, so `0630 33.000 / 33160 33.000`; the gross price includes NoVA. Electric car E 279: € 37.200 / 1,20 = € 31.000 and VAT € 6.200: `0630 31.000 + 2500 6.200 / 33161 37.200`. Each purchase has profit 0 and cash 0; only the stated truck settlement reduces cash, by € 75.000.

#### Returns, discounts and transport

[DEFINITION] A **return (Warenrücksendung)** or subsequent **discount (nachträglicher Rabatt)** changes an already recorded invoice. A supplier credit note S reduces the supplier liability and reverses the appropriate net purchase and input VAT: `33… / 5000 + 2500`. For a customer return the book reverses the sale with `4000 + 3500 / 20…`; for a later customer discount it uses `4400 Erlösberichtigungen + 3500 / 20…`. An immediate discount is deducted before the invoice is posted; only the reduced net price and its VAT are recorded. Book pp. 4, 24–35.

**Example / Übung: discounts.** Book Ü 1.13, p. 28: € 2.000 net list price less 30% = € 1.400 net, plus € 280 VAT = € 1.680. Post `20093 1.680 / 4000 1.400 + 3500 280`; profit +€ 1.400, cash 0. Book L 1.7, pp. 31–32: a later customer discount of € 456 net plus € 91,20 VAT reduces the claim by € 547,20: `4400 456 + 3500 91,20 / 20890 547,20`; profit −€ 456, cash 0.

[DEFINITION] **Inward transport (Bezugskosten)** relates to goods purchased; **outward transport (Versandkosten)** relates to goods sold. Check the loading place, destination and who bears the cost on the forwarding invoice. Post goods-related inward freight to 5000 and deductible VAT to 2500. Net landed cost = net goods after returns and discounts + net inward costs. For outward freight use 7300; taxable parcel charges 7310; the book uses 7311 for the Austrian Post exempt parcel example. Exemption depends on the service, not weight alone. Delivery costs directly attributable to a fixed asset are capitalised on its asset account, not 5000. Book pp. 14–21; Stoff.

**Example / Übung: L 1.3, book p. 16.** Goods € 9.875 net, freight € 137,80 + fuel surcharge € 10,40 + toll € 4,89 = € 153,09 net. Landed cost = € 10.028,09. Freight input VAT € 30,62 and gross € 183,71 are not added to net landed cost.

#### Reminder fees and default interest

[DEFINITION] **Reminder fees (Mahnspesen)** and **default interest (Verzugszinsen)** compensate for late payment; the book posts them without VAT. Charged by supplier: `8321 Mahnspesen + 8320 Verzugszinsenaufwand / 33…`. Charged to customer: `20… / 4890 Mahnspesenvergütungen + 8055 Verzugszinsenerträge`. Settlement later clears the full claim or liability through bank. Source: book p. 39.

**Example / Übung: Ü 1.18, book p. 39.** Supplier reminder S 319 adds € 10 fees and € 15 interest to the existing € 540 liability: `8321 10 + 8320 15 / 33077 25`. Profit −€ 25, cash 0. Then `33077 565 / 2800 565` clears the debt: profit 0, cash −€ 565. Customer reminder S 321: `20421 20 / 8055 20`, profit +€ 20, cash 0. The existing € 1.420 claim plus interest is collected as `2800 1.440 / 20421 1.440`, profit 0, cash +€ 1.440.

[TIP] First decide whether the document concerns the company's own purchase or sale. A credit note reverses the original VAT direction. Distinguish a later bank settlement, which normally has no new profit effect, from the expense or revenue entry.

#### Assigned Ü 1.11, book pp. 20–21

The amounts and transaction numbers come from the book. Effect columns use the convention in section 8. All entries are debit / credit. Rounding on K 16 is to cents.

| No. and voucher | Entry | Profit | Cash |
|---|---|---:|---:|
| 1 E 4 | 5000 10.000 + 2500 2.000 / 33030 12.000 | −10.000 | 0 |
| 2 E 7 | 5000 753 + 2500 150,60 / 33115 903,60 | −753 | 0 |
| 3 K 11 | 5000 111 + 2500 22,20 / 2700 133,20 | −111 | −133,20 |
| 4 S 10 | 33030 216 / 5000 180 + 2500 36 | +180 | 0 |
| 5 A 17 | 20013 204 / 4000 170 + 3500 34 | +170 | 0 |
| 6 B 6 | 33030 11.784 / 2800 11.784 | 0 | −11.784 |
| 7 K 16 | 7310 11,58 + 2500 2,32 / 2700 13,90 | −11,58 | −13,90 |
| 8 B 8 | 33115 903,60 / 2800 903,60 | 0 | −903,60 |
| 9 A 21 | 20022 2.568 / 4000 2.140 + 3500 428 | +2.140 | 0 |
| 10 K 20 | 7300 128 + 2500 25,60 / 2700 153,60 | −128 | −153,60 |
| 11 S 14 | 4000 600 + 3500 120 / 20022 720 | −600 | 0 |
| 12 B 13 | 2800 204 / 20013 204 | 0 | +204 |

6: € 12.000 − € 216 = € 11.784. Payment order: Michael Schober OG, IBAN AT17 1200 0519 6810 1201, BIC BKAUATWW; payer Anneliese Müller e. U., IBAN AT94 1700 0006 1060 0800, BIC BFKKAT2K; purpose invoice 0034 less credit S 10, signed Anneliese Müller. The freight is a separate debt to Schenker. Landed cost = € 10.000 − € 180 + € 753 = € 10.573. The indicated delivery clause is `ab Werk Bregenz, Belrupstraße 20`.

### 2. Fixed asset register and depreciation

#### Register and calculation

[DEFINITION] The **fixed asset register (Anlagenverzeichnis, AVZ)** records each capitalised asset, its inventory number, description, document and supplier, purchase and commissioning dates, acquisition cost, useful life, depreciation rate, annual depreciation and carrying amount. It supports the closing entries and tracking of the asset. Source: book pp. 12–13; RAW/AVZ.pdf; homework sheet p. 1.

[DEFINITION] **Useful life (Nutzungsdauer)** is the expected period of business use. **Straight-line depreciation (lineare Abschreibung, AfA)** allocates cost evenly: annual rate = 100% / years; full annual depreciation = acquisition cost / years. **Book value (Buchwert)** = opening book value + capitalised additions − depreciation. Depreciation is an expense, not a fresh cash payment. In the Austrian tax half-year convention, use a full year for commissioning in the first half and half a year in the second half. Keep a € 1 memory value while an asset remains in use, where the exercise uses that convention. Book pp. 12–13; AVZ sheet.

Posting: `7010 Abschreibungen auf Sachanlagen / relevant asset account`, e.g. 0620. Profit falls by depreciation; cash does not change. Ordinary land is not depreciated merely because time passes.

[INFO] The supplied AVZ sheet gives the € 1.160 dishwasher commissioned on 18 May 2023 a 2023 depreciation of € 96,67, which is eight months of its € 145 annual amount. This differs from the tax half-year convention above, under which the full € 145 would apply. Use the method specified in the particular exercise; do not mix those two schedules.

**Example / Übung: McSHARK homework, RAW/AVZ_GWG_Hausuebung.pdf p. 1.** iPad purchased and commissioned on 2 October 2026, € 1.200 net + € 240 VAT = € 1.440. Ten-year life, immediate commissioning per instruction. Assuming full input VAT deduction and capitalisation, `0620 1.200 + 2500 240 / payment clearing account 1.440`. Receipt confirms payment but does not resolve cash versus debit/credit card; select 2700, 3190 or 3180 only from the actual payment evidence. It exceeds the book's GWG limit. AVZ: cost € 1.200, rate 10%, full-year AfA € 120, 2026 half-year AfA € 60, book value 31 December € 1.140. No opening book value on 1 January because the asset was not yet owned. Closing: `7010 60 / 0620 60`. Profit −€ 60, cash 0.

**Example / Übung: Saturn homework, p. 2.** The invoice states one combined € 629 gross, € 524,17 net and € 104,83 VAT for computer, monitor and printer, without separate prices. Under the stated assumption that the set is assessed as one eligible unit and input VAT is deductible, its € 524,17 cost is below the book's limit: `7060 524,17 + 2500 104,83 / 2700 629` if the documented cash sale was paid in cash. Profit −€ 524,17, cash −€ 629. If the payment method was different, use the corresponding clearing account. Immediate write-off means no ordinary depreciating AVZ entry. Without individual prices and facts about independent use, separate GWG decisions cannot be calculated from this invoice.

[DIAGRAM SUGGESTION: Acquisition cost → asset register → annual depreciation → remaining book value; show immediate GWG write-off as a separate choice.]

[TIP] In English questions distinguish acquisition date from commissioning date, and book value from market value. Calculate the 2026 depreciation only after deciding whether the item was capitalised and when it was put into use.

### 3. Bank closing items

[DEFINITION] **Bank closing items (Abschlussposten)** include credit interest, debit interest, bank charges and capital income tax. For an individual business or partnership in the book examples: `2800 / 8050` credit interest, `8310 / 2800` debit interest, `7790 / 2800` charges, `9600 / 2800` KESt. Credit interest raises profit; interest expense and charges reduce it; private KESt is not an expense. Use the actual bank account, including 3120 for the stated overdrawn account. Book pp. 67–69.

**Example / Übung: Ü 2.3, book p. 69.** Volksbank V 179: `2804 12,32 / 8050 12,32`, profit +12,32, cash +12,32; `9600 3,08 / 2804 3,08`, profit 0, cash −3,08; `7790 238,12 / 2804 238,12`, profit −238,12, cash −238,12. Fees = 64,62 + 173,50. UniCredit B 151: `8310 1.516,93 / 3120 1.516,93`, profit −1.516,93, cash −1.516,93; `7790 260,30 / 3120 260,30`, profit −260,30, cash −260,30. Fees = 185,50 + 50 + 24,80. For 3120 the negative cash effect means the bank debt increases; see section 8.

[TIP] Do not net KESt against interest revenue. Show the gross interest, private tax and charges separately. The original PDF supplies 2804 and 3120 in the exercise account list, which the OCR omitted.

### 4. Cash transfers with banks

[DEFINITION] **Cash in transit with banks (Barverkehr mit Banken, 2870)** bridges the cash voucher and bank statement. Withdrawal: `2700 / 2870`, then `2870 / 2800`. Deposit: `2870 / 2700`, then `2800 / 2870`. Once both documents are posted, 2870 clears. Neither transfer is income or expense. Book pp. 64–67.

**Example / Übung: Ü 2.4, book pp. 69–70.** 1 December K 656 `2700 1.500 / 2870 1.500`; B 184 `2870 1.500 / 2800 1.500`. 9 December K 679 `2870 2.300 / 2700 2.300`; 10 December B 188 `2800 2.300 / 2870 2.300`. Each has profit 0. At cash-plus-bank level each complete transfer has cash effect 0; individual voucher movements are +1.500, −1.500, −2.300 and +2.300 respectively.

31 December B 198: `8310 21,78 / 2800 21,78`, profit −21,78, cash −21,78; `2800 54,80 / 8050 54,80`, profit +54,80, cash +54,80; `9600 13,70 / 2800 13,70`, profit 0, cash −13,70; `7790 40,58 / 2800 40,58`, profit −40,58, cash −40,58. Charges = 36,22 + 4,36.

[TIP] Do not post both the direct `2700 / 2800` shortcut and the two 2870 entries for the same withdrawal.

### 5. Debit and credit card settlements

[DEFINITION] A card sale creates a claim against the card processor: `2880` for credit cards or `2885` for debit cards. Debit the claim for gross sales and credit net revenue and VAT. When money arrives, clear the claim against bank; credit-card commission, fixed fees and deductible VAT may be withheld. Use 7792 for fees and 2500 for deductible VAT. The purchaser uses 3180 for credit-card and 3190 for debit-card liabilities, clearing these against bank later. Book pp. 40–45.

**Example / Übung: Ü 1.20, book pp. 44–45.**

| Voucher | Entry | Profit | Cash |
|---|---|---:|---:|
| 2 Feb B 14 | 7792 140,16 + 2500 28,03 / 2800 168,19 | −140,16 | −168,19 |
| 18 Feb K 102 | 2700 3.816 / 4000 3.180 + 3500 636 | +3.180 | +3.816 |
| 18 Feb S 80 | 2885 2.382 / 4000 1.985 + 3500 397 | +1.985 | 0 |
| 23 Feb B 24 | 2800 2.382 / 2885 2.382 | 0 | +2.382 |
| 1 Mar B 28 | 2800 8.065,72 + 7792 211,90 + 2500 42,38 / 2880 8.320 | −211,90 | +8.065,72 |

The settlement fee is 2,5% × 8.320 = 208 plus 3,90 = 211,90; VAT 42,38; total withheld 254,28. The € 8.320 claim is assumed already recorded. Its sale date and VAT split are not given; do not invent them or book revenue again.

[DIAGRAM SUGGESTION: Card sale → gross claim → bank settlement; fee and VAT leave the claim before the net transfer.]

[TIP] The card claim is not bank cash yet. Book the fee expense, not the entire deduction including deductible VAT, as the profit effect.

### 6. Taxes and chamber levy KU1

[DEFINITION] Classify the payment before posting. Business property tax is an expense `7100 / 2800`; the owner's income tax and private property tax use `9600 / 2800`, with no profit effect; VAT liability uses `3520 / 2800`, also no new profit effect. Acquisition taxes such as land transfer tax on undeveloped land increase `0200` rather than immediate expense. Source: book pp. 71–76.

[DEFINITION] **Chamber levy 1 (Kammerumlage 1, KU1)** finances the chamber. The book's teaching model uses 3‰ of its defined input-VAT-based assessment base, with an annual turnover exemption threshold of € 150.000, quarterly calculation and payment by the 15th of the second following month. The base includes specified input VAT and import/acquisition VAT, less the specified own-consumption adjustment. The book simplifies the rule; use the applicable current law for real filings, including exclusions and graduated rates. `7780 / 2800` records a direct payment. For quarter 4 use `7780 / 3540` at year end and `3540 / 2800` on payment. Book pp. 74–75.

**Example / Übung: Ü 2.6, book p. 76.** 31 Dec U 54 `7780 420 / 3540 420`, profit −420, cash 0. 15 Feb next year B 25 `3540 420 / 2800 420`, profit 0, cash −420. 15 May next year B 69 `7780 312 / 2800 312`, profit −312, cash −312.

**Example / Übung: Ü 2.7, book p. 76.** 15 May B 45 `9600 8.130 + 7780 64,20 + 3520 3.142 / 2800 11.336,20`: profit −64,20, cash −11.336,20. 2 July B 61 `0200 7.000 / 2800 7.000`: profit 0, cash −7.000. 16 August B 78 `9600 180 + 7100 220 / 2800 400`: profit −220, cash −400.

The private withdrawals also reduce equity: in Ü 2.3 the KESt reduces it by € 3,08, in Ü 2.4 by € 13,70. In Ü 2.7 B 45 total equity falls by € 8.194,20, including € 8.130 private tax and € 64,20 expense. B 78 reduces equity by € 400, including € 180 private tax and € 220 expense. These equity changes are not all profit effects.

[TIP] An expense and a liability payment can occur in different years. Do not deduct the fourth-quarter KU1 expense twice.

### 7. Settlement with cash discount

[DEFINITION] A **cash discount (Skonto)** is a reduction for payment within the agreed short period. For a 20% gross invoice, gross discount = invoice gross × discount rate; net discount = gross discount / 1,20; VAT correction = gross discount / 6. The account is fully cleared by the payment plus gross discount. Source: book pp. 45–51.

**Example / Übung: supplier, L 1.10 p. 47.** Invoice E 7: `5000 7.000 + 2500 1.400 / 33008 8.400`. Payment within 3% discount: 8.400 × 3% = 252 gross, 210 net and 42 VAT; bank payment 8.148. Two entries: `33008 8.148 / 2800 8.148` has profit 0 and cash −8.148; `33008 252 / 5880 210 + 2500 42` has profit +210 and cash 0.

**Example / Übung: customer, L 1.11 p. 51.** Invoice A 2437: `20048 4.680 / 4000 3.900 + 3500 780`. At 2%, discount 93,60 gross = 78 net + 15,60 VAT; bank receipt 4.586,40. Two entries: `2800 4.586,40 / 20048 4.586,40`, profit 0, cash +4.586,40; `4410 78 + 3500 15,60 / 20048 93,60`, profit −78, cash 0.

[TIP] In both cases the cash discount is calculated on the eligible gross invoice; correct VAT separately. The book examples concern goods, not asset purchases.

### 8. Effect on profit and liquidity

[DEFINITION] **Profit effect (Erfolgswirkung)** is the change in revenue less expense, before tax, in the book's simplified direct-expense approach to merchandise. **Cash effect (Liquiditätswirkung)** here means the change in cash plus bank, including a change in bank overdraft as negative bank cash. A supplier liability or a card-processor claim alone is not cash. Owner withdrawals reduce equity but are not business expenses; profit 0 does not mean equity is unchanged. For 2870 transfers, individual legs temporarily change cash plus bank, but the completed transfer does not.

| Event | Profit | Cash |
|---|---:|---:|
| Credit goods purchase / later payment | net expense / 0 | 0 / gross outflow |
| Capitalised asset / later depreciation | 0 / depreciation expense | payment outflow / 0 |
| Credit sale / collection | net revenue / 0 | 0 / gross inflow |
| Private tax paid | 0 | payment outflow |

[TIP] VAT is normally not profit when fully deductible or payable. Compare debits and credits, and do not count a card settlement as a second sale. If VAT is not deductible, it is included in the relevant cost or expense.

## [Deutsch]

### 1. Belegverbuchung im Beschaffungs- und Absatzprozess

#### Belege, Umsatzsteuer und Buchungssätze

[DEFINITION] Ein **Buchungssatz** erfasst im Soll und Haben gleich hohe Beträge. `Soll / Haben` bedeutet hier: Konten vor `/` im Soll, Konten danach im Haben. E = Eingangsrechnung, A = Ausgangsrechnung, K = Kassabeleg, B = Bankbeleg, S = sonstiger Beleg, U = Umbuchungsbeleg. Beträge sind in Euro.

[DEFINITION] **Vorsteuer (2500)** ist die bei berechtigten Einkäufen abzugsfähige Umsatzsteuer. **Umsatzsteuer (3500)** wird beim Verkauf verrechnet. Bei 20 % gilt: Brutto = Netto × 1,20; Netto = Brutto / 1,20; Steuer = Brutto / 6. Der Steuersatz steht auf dem Beleg.

Wareneinkauf auf Ziel: 5000 HW-Einsatz und 2500 Vorsteuer an Lieferantenkonto 33…. Warenverkauf auf Ziel: Kundenkonto 20… an 4000 HW-Erlöse und 3500 Umsatzsteuer. Bei Barzahlung 2700 Kassa verwenden. Ein späterer Bankausgleich über 2800 Bank schließt das Kunden- oder Lieferantenkonto. Quelle: Buch S. 4–6, 36–38.

#### Anlagegüter, GWG und Fahrzeuge

[DEFINITION] Ein **Anlagegut** dient dem Betrieb dauerhaft und ist nicht zum Weiterverkauf bestimmt. **Aktivieren** bedeutet, Anschaffungskosten auf einem aktiven Bestandskonto zu erfassen. Dazu gehören der um Preisnachlässe verminderte Kaufpreis und direkt zurechenbare Transport- und Montagekosten. Abzugsfähige Vorsteuer gehört nicht dazu. Laufende Reparaturen und Treibstoff sind Aufwand. Buch S. 7–13; Stoff.

[DEFINITION] Ein **geringwertiges Wirtschaftsgut (GWG)** ist ein abnutzbares Anlagegut mit Anschaffungswert bis € 1.000 ohne abzugsfähige USt nach der im Buch behandelten Regel des § 13 EStG. Es muss selbstständig nutzbar sein. Eine funktionelle Einheit wird gemeinsam beurteilt. Das Buch nennt Kamera und erforderliche Speicherkarte als Einheit, lässt aber eine getrennte Beurteilung selbstständig nutzbarer PC-Zubehörteile zu. Das Unternehmen kann die Sofortabschreibung wählen oder aktivieren und über die Nutzungsdauer abschreiben. Buch S. 8–10.

Sofort: `7060 Abschreibungen GWG + 2500 Vorsteuer / 33…`, 2700 oder 3180/3190. Alternativ zunächst z. B. 0672 statt 7060 verwenden und am Jahresende `7060 / 0672` vollständig abschreiben. Die Varianten nicht doppelt buchen. Der Aufwand vermindert den Erfolg; die Aktivierung allein nicht.

Beim üblichen Firmen-Pkw `0630 Pkw und Kombis / Lieferant` mit dem Bruttobetrag buchen, weil grundsätzlich kein Vorsteuerabzug besteht. Tank- und laufende Betriebskosten brutto auf `7320 Pkw-Betriebsaufwand / Zahlungskonto`. Beim vorsteuerabzugsberechtigten Lkw 0640 für die Anschaffung und 7330 für Betriebskosten sowie gegebenenfalls 2500 verwenden. Das Buch nennt für ein betriebliches Elektroauto mit 0 g CO₂ bis € 40.000 Anschaffungswert inklusive USt den vollen Vorsteuerabzug. Darüber und bei Sonderfällen gelten weitere Regeln. Buch S. 7, 13, 81–83.

**Beispiel / Übung: Drucker, Buch S. 7–8.** E 514, € 1.320 netto + € 264 Vorsteuer = € 1.584: `0620 1.320 + 2500 264 / 33401 1.584`. Erfolg € 0, Liquidität € 0. Bankausgleich: `33401 1.584 / 2800 1.584`. Erfolg € 0, Liquidität −€ 1.584. Die Abschreibung ist eine spätere Buchung.

**Beispiel / Übung: Fahrzeuge, Ü 1.7, Buch S. 13.** Für Lkw und Elektroauto wird angenommen, dass die Voraussetzungen des Vorsteuerabzugs laut Buch erfüllt sind. Lkw E 138: € 75.000 / 1,20 = € 62.500 netto und € 12.500 Vorsteuer: `0640 62.500 + 2500 12.500 / 33159 75.000`. Später `33159 75.000 / 2800 75.000`. Diesel-Pkw E 256: kein Vorsteuerabzug, daher `0630 33.000 / 33160 33.000`; der Bruttobetrag enthält NoVA. Elektroauto E 279: € 37.200 / 1,20 = € 31.000 und € 6.200 Vorsteuer: `0630 31.000 + 2500 6.200 / 33161 37.200`. Jeder Kauf hat Erfolg 0 und Liquidität 0. Erst der angegebene Bankausgleich des Lkw vermindert die Liquidität um € 75.000.

#### Rücksendungen, Rabatte und Transport

[DEFINITION] Eine **Warenrücksendung** oder ein **nachträglicher Rabatt** verändert eine bereits gebuchte Rechnung. Die Gutschrift S des Lieferanten vermindert die Schuld und korrigiert Einkauf und Vorsteuer: `33… / 5000 + 2500`. Bei einer Kundenrücksendung kehrt das Buch den Verkauf mit `4000 + 3500 / 20…` um; für einen nachträglichen Kundenrabatt verwendet es `4400 Erlösberichtigungen + 3500 / 20…`. Ein sofort gewährter Rabatt wird vor der Buchung abgezogen. Gebucht werden nur der verminderte Nettopreis und dessen USt. Buch S. 4, 24–35.

**Beispiel / Übung: Rabatte.** Buch Ü 1.13, S. 28: € 2.000 Nettolistenpreis minus 30 % = € 1.400 netto, plus € 280 USt = € 1.680. Buchung `20093 1.680 / 4000 1.400 + 3500 280`; Erfolg +€ 1.400, Liquidität 0. Buch L 1.7, S. 31–32: Ein nachträglicher Kundenrabatt von € 456 netto plus € 91,20 USt vermindert die Forderung um € 547,20: `4400 456 + 3500 91,20 / 20890 547,20`; Erfolg −€ 456, Liquidität 0.

[DEFINITION] **Bezugskosten** entstehen beim Wareneinkauf, **Versandkosten** beim Warenverkauf. Auf der Speditionsrechnung Ladeort, Zielort und Kostentragung prüfen. Warenbezogene Bezugskosten auf 5000, abzugsfähige Vorsteuer auf 2500 buchen. Nettoeinstandspreis = Nettowarenpreis nach Rücksendungen und Rabatten + Nettobezugskosten. Für Ausgangsfrachten 7300, für steuerpflichtige Paketgebühren 7310 verwenden. Das Buch verwendet für sein steuerfreies Postpaket 7311. Ob eine Befreiung vorliegt, hängt von der Leistung ab, nicht allein vom Gewicht. Direkt zurechenbare Transportkosten eines Anlageguts gehören auf das Anlagenkonto, nicht auf 5000. Buch S. 14–21; Stoff.

**Beispiel / Übung: L 1.3, Buch S. 16.** Waren € 9.875 netto, Fracht € 137,80 + Treibstoffzuschlag € 10,40 + Maut € 4,89 = € 153,09 netto. Einstandspreis = € 10.028,09. Die Vorsteuer € 30,62 und der Bruttobetrag € 183,71 erhöhen den Nettoeinstandspreis nicht.

#### Mahnspesen und Verzugszinsen

[DEFINITION] **Mahnspesen** und **Verzugszinsen** entstehen bei verspäteter Zahlung. Das Buch verbucht sie ohne USt. Belastung durch Lieferanten: `8321 Mahnspesen + 8320 Verzugszinsenaufwand / 33…`. Belastung eines Kunden: `20… / 4890 Mahnspesenvergütungen + 8055 Verzugszinsenerträge`. Der spätere Ausgleich tilgt die gesamte Forderung oder Schuld über Bank. Quelle: Buch S. 39.

**Beispiel / Übung: Ü 1.18, Buch S. 39.** Die Lieferantenmahnung S 319 erhöht die bestehende Schuld von € 540 um € 10 Spesen und € 15 Zinsen: `8321 10 + 8320 15 / 33077 25`. Erfolg −€ 25, Liquidität 0. Danach gleicht `33077 565 / 2800 565` die Schuld aus: Erfolg 0, Liquidität −€ 565. Kundenmahnung S 321: `20421 20 / 8055 20`, Erfolg +€ 20, Liquidität 0. Die bestehende Forderung von € 1.420 wird samt Zinsen bezahlt: `2800 1.440 / 20421 1.440`, Erfolg 0, Liquidität +€ 1.440.

[TIP] Zuerst klären, ob der Beleg den Einkauf oder Verkauf betrifft. Bei einer Gutschrift läuft die Steuerkorrektur entgegengesetzt zur ursprünglichen Buchung. Der spätere Zahlungsausgleich verändert den Erfolg normalerweise nicht nochmals.

#### Zugewiesene Ü 1.11, Buch S. 20–21

Die Geschäftsfälle und Beträge stammen aus dem Buch. Die Wirkungsspalten folgen der Definition in Abschnitt 8. Alle Buchungen stehen im Format Soll / Haben. K 16 ist auf Cent gerundet.

| Nr. und Beleg | Buchungssatz | Erfolg | Liquidität |
|---|---|---:|---:|
| 1 E 4 | 5000 10.000 + 2500 2.000 / 33030 12.000 | −10.000 | 0 |
| 2 E 7 | 5000 753 + 2500 150,60 / 33115 903,60 | −753 | 0 |
| 3 K 11 | 5000 111 + 2500 22,20 / 2700 133,20 | −111 | −133,20 |
| 4 S 10 | 33030 216 / 5000 180 + 2500 36 | +180 | 0 |
| 5 A 17 | 20013 204 / 4000 170 + 3500 34 | +170 | 0 |
| 6 B 6 | 33030 11.784 / 2800 11.784 | 0 | −11.784 |
| 7 K 16 | 7310 11,58 + 2500 2,32 / 2700 13,90 | −11,58 | −13,90 |
| 8 B 8 | 33115 903,60 / 2800 903,60 | 0 | −903,60 |
| 9 A 21 | 20022 2.568 / 4000 2.140 + 3500 428 | +2.140 | 0 |
| 10 K 20 | 7300 128 + 2500 25,60 / 2700 153,60 | −128 | −153,60 |
| 11 S 14 | 4000 600 + 3500 120 / 20022 720 | −600 | 0 |
| 12 B 13 | 2800 204 / 20013 204 | 0 | +204 |

Zu 6: € 12.000 − € 216 = € 11.784. Zahlungsanweisung: Michael Schober OG, IBAN AT17 1200 0519 6810 1201, BIC BKAUATWW; Auftraggeberin Anneliese Müller e. U., IBAN AT94 1700 0006 1060 0800, BIC BFKKAT2K; Zweck Rechnung 0034 abzüglich Gutschrift S 10, Unterschrift Anneliese Müller. Die Fracht ist eine eigene Schuld an Schenker. Einstandspreis = € 10.000 − € 180 + € 753 = € 10.573. Die passende Lieferklausel lautet `ab Werk Bregenz, Belrupstraße 20`.

### 2. Anlagenverzeichnis und Abschreibung

#### Verzeichnis und Berechnung

[DEFINITION] Das **Anlagenverzeichnis (AVZ)** enthält pro aktivierter Anlage unter anderem Inventarnummer, Bezeichnung, Beleg und Lieferant, Anschaffungs- und Inbetriebnahmedatum, Anschaffungswert, Nutzungsdauer, Abschreibungssatz, jährliche AfA und Buchwert. Es dient der laufenden Erfassung und dem Jahresabschluss. Quelle: Buch S. 12–13; RAW/AVZ.pdf; Hausübung S. 1.

[DEFINITION] Die **Nutzungsdauer** ist die erwartete betriebliche Einsatzdauer. Die **lineare Abschreibung (AfA)** verteilt die Kosten gleichmäßig: jährlicher Satz = 100 % / Jahre; volle Jahres-AfA = Anschaffungswert / Jahre. **Buchwert** = Anfangsbuchwert + aktivierte Zugänge − Abschreibung. AfA ist Aufwand, aber keine neuerliche Zahlung. Nach der steuerlichen Halbjahresregel gilt bei Inbetriebnahme im ersten Halbjahr die volle, im zweiten die halbe Jahres-AfA. Solange eine Anlage noch genutzt wird, bleibt in Aufgaben mit dieser Konvention ein Erinnerungswert von € 1. Buch S. 12–13; AVZ-Blatt.

Buchung: `7010 Abschreibungen auf Sachanlagen / Anlagenkonto`, z. B. 0620. Der Erfolg sinkt um die AfA, die Liquidität bleibt unverändert. Ein unbebautes Grundstück wird nicht allein wegen Zeitablaufs abgeschrieben.

[INFO] Das mitgelieferte AVZ-Blatt weist für den am 18. Mai 2023 in Betrieb genommenen Geschirrspüler mit € 1.160 Anschaffungswert im Jahr 2023 eine AfA von € 96,67 aus. Das sind acht Monate der Jahres-AfA von € 145. Die oben beschriebene steuerliche Halbjahresregel ergäbe dagegen die volle Jahres-AfA von € 145. In der jeweiligen Aufgabe die vorgegebene Methode verwenden und die beiden Zeitpläne nicht vermischen.

**Beispiel / Übung: McSHARK-Hausübung, RAW/AVZ_GWG_Hausuebung.pdf S. 1.** iPad am 2. Oktober 2026 angeschafft und laut Aufgabenstellung sofort in Betrieb genommen, € 1.200 netto + € 240 USt = € 1.440. Nutzungsdauer zehn Jahre. Bei unterstelltem vollem Vorsteuerabzug und Aktivierung: `0620 1.200 + 2500 240 / Zahlungs-Verrechnungskonto 1.440`. Der Beleg bestätigt die Zahlung, unterscheidet aber nicht sicher zwischen bar, Debit- und Kreditkarte. Erst mit Zahlungsnachweis 2700, 3190 oder 3180 wählen. Der Wert liegt über der GWG-Grenze des Buches. AVZ: Anschaffungswert € 1.200, Satz 10 %, volle Jahres-AfA € 120, Halbjahres-AfA 2026 € 60, Buchwert 31. Dezember € 1.140. Am 1. Jänner noch kein Anfangsbuchwert, da noch nicht angeschafft. Abschluss: `7010 60 / 0620 60`. Erfolg −€ 60, Liquidität 0.

**Beispiel / Übung: Saturn-Hausübung, S. 2.** Die Rechnung nennt für Computer, Monitor und Drucker gemeinsam € 629 brutto, € 524,17 netto und € 104,83 USt, aber keine Einzelpreise. Unter der Annahme einer gemeinsam beurteilten GWG-fähigen Einheit und eines Vorsteuerabzugs liegt der Wert unter der Buchgrenze: `7060 524,17 + 2500 104,83 / 2700 629`, falls der als Barverkauf bezeichnete Beleg tatsächlich bar bezahlt wurde. Erfolg −€ 524,17, Liquidität −€ 629. Bei anderer Zahlungsart das passende Verrechnungskonto verwenden. Bei Sofortabschreibung gibt es keinen regulären AfA-Eintrag im AVZ. Ohne Einzelpreise und Angaben zur selbstständigen Nutzbarkeit lässt sich eine getrennte GWG-Beurteilung aus dieser Rechnung nicht berechnen.

[DIAGRAM SUGGESTION: Anschaffungswert → Anlagenverzeichnis → jährliche AfA → verbleibender Buchwert; GWG-Sofortabschreibung als eigenen Wahlweg zeigen.]

[TIP] In englischen Fragen Anschaffungsdatum und Inbetriebnahme sowie Buchwert und Marktwert unterscheiden. Erst prüfen, ob aktiviert wurde und wann die Anlage in Betrieb ging, dann die AfA 2026 berechnen.

### 3. Abschlussposten am Bankkonto

[DEFINITION] Zu den **Abschlussposten** zählen Habenzinsen, Sollzinsen, Bankspesen und Kapitalertragsteuer. Bei Einzelunternehmen und Personengesellschaften in den Buchbeispielen: `2800 / 8050` Habenzinsen, `8310 / 2800` Sollzinsen, `7790 / 2800` Spesen, `9600 / 2800` KESt. Habenzinsen erhöhen den Erfolg; Zinsenaufwand und Spesen vermindern ihn; die private KESt ist kein Aufwand. Das tatsächliche Bankkonto verwenden, bei der angegebenen Überziehung 3120. Buch S. 67–69.

**Beispiel / Übung: Ü 2.3, Buch S. 69.** Volksbank V 179: `2804 12,32 / 8050 12,32`, Erfolg +12,32, Liquidität +12,32; `9600 3,08 / 2804 3,08`, Erfolg 0, Liquidität −3,08; `7790 238,12 / 2804 238,12`, Erfolg −238,12, Liquidität −238,12. Spesen = 64,62 + 173,50. UniCredit B 151: `8310 1.516,93 / 3120 1.516,93`, Erfolg −1.516,93, Liquidität −1.516,93; `7790 260,30 / 3120 260,30`, Erfolg −260,30, Liquidität −260,30. Spesen = 185,50 + 50 + 24,80. Bei 3120 bedeutet die negative Liquiditätswirkung eine höhere Bankschuld; siehe Abschnitt 8.

[TIP] KESt nicht vom Zinsertrag abziehen. Bruttozinsen, private Steuer und Spesen getrennt buchen. Das Original-PDF nennt 2804 und 3120 im Kontenplan; die OCR hat diese Angabe ausgelassen.

### 4. Bankkonto und Barverkehr mit Banken

[DEFINITION] **2870 Barverkehr mit Banken** überbrückt die Zeit zwischen Kassenbeleg und Kontoauszug. Abhebung: `2700 / 2870`, dann `2870 / 2800`. Einzahlung: `2870 / 2700`, dann `2800 / 2870`. Nach beiden Belegen ist 2870 ausgeglichen. Die Umbuchung ist weder Ertrag noch Aufwand. Buch S. 64–67.

**Beispiel / Übung: Ü 2.4, Buch S. 69–70.** 1. Dezember K 656 `2700 1.500 / 2870 1.500`; B 184 `2870 1.500 / 2800 1.500`. 9. Dezember K 679 `2870 2.300 / 2700 2.300`; 10. Dezember B 188 `2800 2.300 / 2870 2.300`. Jeder Satz hat Erfolgswirkung 0. Die vollständige Umbuchung verändert Kassa plus Bank insgesamt nicht; die einzelnen Belegbuchungen wirken dort mit +1.500, −1.500, −2.300 und +2.300.

31. Dezember B 198: `8310 21,78 / 2800 21,78`, Erfolg −21,78, Liquidität −21,78; `2800 54,80 / 8050 54,80`, Erfolg +54,80, Liquidität +54,80; `9600 13,70 / 2800 13,70`, Erfolg 0, Liquidität −13,70; `7790 40,58 / 2800 40,58`, Erfolg −40,58, Liquidität −40,58. Spesen = 36,22 + 4,36.

[TIP] Für dieselbe Abhebung nicht gleichzeitig die direkte Kurzbuchung `2700 / 2800` und die beiden Buchungen über 2870 erfassen.

### 5. Debit- und Kreditkartenabrechnung

[DEFINITION] Ein Kartenverkauf erzeugt eine Forderung gegenüber dem Kartenunternehmen: `2880` für Kreditkarten oder `2885` für Debitkarten. Die Bruttoforderung steht im Soll, Nettoerlös und USt im Haben. Beim Geldeingang wird die Forderung gegen Bank ausgeglichen. Bei Kreditkarten können Provision, Fixentgelt und abzugsfähige Vorsteuer einbehalten werden. Gebühren auf 7792, abzugsfähige Vorsteuer auf 2500 buchen. Beim Einkauf verwendet der Käufer 3180 für Kreditkarten- und 3190 für Debitkartenverbindlichkeiten und gleicht sie später über Bank aus. Buch S. 40–45.

**Beispiel / Übung: Ü 1.20, Buch S. 44–45.**

| Beleg | Buchungssatz | Erfolg | Liquidität |
|---|---|---:|---:|
| 2. Feb. B 14 | 7792 140,16 + 2500 28,03 / 2800 168,19 | −140,16 | −168,19 |
| 18. Feb. K 102 | 2700 3.816 / 4000 3.180 + 3500 636 | +3.180 | +3.816 |
| 18. Feb. S 80 | 2885 2.382 / 4000 1.985 + 3500 397 | +1.985 | 0 |
| 23. Feb. B 24 | 2800 2.382 / 2885 2.382 | 0 | +2.382 |
| 1. März B 28 | 2800 8.065,72 + 7792 211,90 + 2500 42,38 / 2880 8.320 | −211,90 | +8.065,72 |

Gebührenrechnung: 2,5 % × 8.320 = 208 plus 3,90 = 211,90; USt 42,38; Einbehalt insgesamt 254,28. Die Forderung über € 8.320 wird als bereits verbucht vorausgesetzt. Das Datum und die Umsatzsteueraufteilung des ursprünglichen Verkaufs sind nicht angegeben. Keinen zusätzlichen Verkauf erfinden.

[DIAGRAM SUGGESTION: Kartenverkauf → Bruttoforderung → Bankabrechnung; Gebühr und Vorsteuer vermindern den überwiesenen Betrag.]

[TIP] Die Kartenforderung ist noch kein Bankguthaben. Erfolgswirksam ist der Nettoaufwand für die Gebühr, nicht der gesamte Einbehalt einschließlich abzugsfähiger Vorsteuer.

### 6. Steuern und Kammerumlage KU1

[DEFINITION] Vor der Buchung die Art der Abgabe bestimmen. Grundsteuer für ein Betriebsgrundstück ist Aufwand: `7100 / 2800`. Einkommensteuer des Inhabers und Grundsteuer für ein Privatgrundstück: `9600 / 2800`, ohne Erfolgswirkung. Die USt-Zahllast wird `3520 / 2800` ohne neue Erfolgswirkung bezahlt. Anschaffungsnebenkosten wie Grunderwerbsteuer für ein unbebautes Grundstück erhöhen `0200` und sind nicht sofortiger Aufwand. Quelle: Buch S. 71–76.

[DEFINITION] Die **Kammerumlage 1 (KU1)** finanziert die Wirtschaftskammer. Das Lehrbuchmodell rechnet mit 3 ‰ der definierten vorsteuerbezogenen Bemessungsgrundlage, einer jährlichen Umsatzfreigrenze von € 150.000, vierteljährlicher Berechnung und Zahlung bis zum 15. des zweitfolgenden Monats. Zur Grundlage zählen unter anderem bestimmte Vorsteuern, Einfuhrumsatzsteuer und Erwerbsteuer, abzüglich der angegebenen Eigenverbrauchskorrektur. Das Buch vereinfacht die Regel. Für echte Abrechnungen gelten die jeweils aktuellen gesetzlichen Ausnahmen und Tarifstufen. Direkte Zahlung: `7780 / 2800`. Für das vierte Quartal am Jahresende `7780 / 3540`, bei späterer Zahlung `3540 / 2800`. Buch S. 74–75.

**Beispiel / Übung: Ü 2.6, Buch S. 76.** 31. Dez. U 54 `7780 420 / 3540 420`, Erfolg −420, Liquidität 0. 15. Feb. Folgejahr B 25 `3540 420 / 2800 420`, Erfolg 0, Liquidität −420. 15. Mai Folgejahr B 69 `7780 312 / 2800 312`, Erfolg −312, Liquidität −312.

**Beispiel / Übung: Ü 2.7, Buch S. 76.** 15. Mai B 45 `9600 8.130 + 7780 64,20 + 3520 3.142 / 2800 11.336,20`: Erfolg −64,20, Liquidität −11.336,20. 2. Juli B 61 `0200 7.000 / 2800 7.000`: Erfolg 0, Liquidität −7.000. 16. August B 78 `9600 180 + 7100 220 / 2800 400`: Erfolg −220, Liquidität −400.

Die Privatentnahmen vermindern zusätzlich das Eigenkapital: in Ü 2.3 durch KESt um € 3,08, in Ü 2.4 um € 13,70. In Ü 2.7 sinkt das Eigenkapital bei B 45 insgesamt um € 8.194,20, davon € 8.130 Privatsteuer und € 64,20 Aufwand. Bei B 78 sinkt es um € 400, davon € 180 Privatsteuer und € 220 Aufwand. Nicht die gesamte Eigenkapitalminderung ist erfolgswirksam.

[TIP] Aufwand und Zahlung einer Verbindlichkeit können in verschiedenen Jahren liegen. Die KU1 des vierten Quartals nicht zweimal als Aufwand erfassen.

### 7. Zahlung mit Skontoabzug

[DEFINITION] **Skonto** ist ein Preisnachlass bei Zahlung innerhalb der vereinbarten kurzen Frist. Bei einer Bruttorechnung mit 20 % USt gilt: Bruttoskonto = Rechnungsbrutto × Skontosatz; Nettoskonto = Bruttoskonto / 1,20; Steuerkorrektur = Bruttoskonto / 6. Zahlung und Bruttoskonto gleichen das Personenkonto vollständig aus. Quelle: Buch S. 45–51.

**Beispiel / Übung: Lieferant, L 1.10 S. 47.** Rechnung E 7: `5000 7.000 + 2500 1.400 / 33008 8.400`. Zahlung mit 3 % Skonto: 8.400 × 3 % = 252 brutto, davon 210 netto und 42 Vorsteuer; Bankzahlung 8.148. Zwei Buchungen: `33008 8.148 / 2800 8.148`, Erfolg 0 und Liquidität −8.148; `33008 252 / 5880 210 + 2500 42`, Erfolg +210 und Liquidität 0.

**Beispiel / Übung: Kunde, L 1.11 S. 51.** Rechnung A 2437: `20048 4.680 / 4000 3.900 + 3500 780`. Bei 2 % beträgt das Skonto 93,60 brutto = 78 netto + 15,60 USt; Bankeingang 4.586,40. Zwei Buchungen: `2800 4.586,40 / 20048 4.586,40`, Erfolg 0, Liquidität +4.586,40; `4410 78 + 3500 15,60 / 20048 93,60`, Erfolg −78, Liquidität 0.

[TIP] In beiden Fällen wird das Skonto vom skontofähigen Bruttobetrag berechnet und die Steuer gesondert korrigiert. Die Buchbeispiele betreffen Waren, nicht Anlagenkäufe.

### 8. Auswirkung auf Unternehmenserfolg und Liquidität

[DEFINITION] **Erfolgswirkung** ist die Veränderung von Ertrag minus Aufwand vor Steuern, bei Waren nach dem vereinfachten direkten Aufwandsansatz des Buches. **Liquiditätswirkung** bedeutet hier die Veränderung von Kassa plus Bank. Eine höhere Kontoüberziehung zählt als negative Bankliquidität. Eine Lieferverbindlichkeit oder Kartenforderung allein ist kein Zahlungsmittel. Privatentnahmen vermindern das Eigenkapital, sind aber kein betrieblicher Aufwand; Erfolg 0 bedeutet daher nicht immer unverändertes Eigenkapital. Bei 2870 ändern die einzelnen Teilbuchungen Kassa plus Bank vorübergehend, die vollständige Umbuchung aber nicht.

| Geschäftsfall | Erfolg | Liquidität |
|---|---:|---:|
| Wareneinkauf auf Ziel / spätere Zahlung | Nettoaufwand / 0 | 0 / Bruttoabfluss |
| Aktivierte Anlage / spätere AfA | 0 / Abschreibungsaufwand | Zahlungsabfluss / 0 |
| Verkauf auf Ziel / Zahlungseingang | Nettoertrag / 0 | 0 / Bruttozufluss |
| Zahlung einer Privatsteuer | 0 | Zahlungsabfluss |

[TIP] Abzugsfähige Vorsteuer und abzuführende USt sind grundsätzlich nicht erfolgswirksam. Bei einer Kartenabrechnung keinen zweiten Verkauf buchen. Nicht abzugsfähige Vorsteuer gehört hingegen zum jeweiligen Aufwand oder Anschaffungswert.
