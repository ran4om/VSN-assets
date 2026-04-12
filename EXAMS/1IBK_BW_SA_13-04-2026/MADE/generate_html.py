import re

markdown_content = """
# Sales Contracts: Initiation, Conclusion, Fulfillment, and Components

## 1. Initiation of Sales Contracts (Anbahnung)

### [English]
The initiation phase is the first step in creating a sales contract. During this phase, the essential information about the product, price, and conditions is exchanged between the potential buyer and seller. 

### [German]
Die Anbahnungsphase ist der erste Schritt bei der Entstehung eines Kaufvertrags. In dieser Phase werden die wesentlichsten Informationen über Produkt, Preis und Konditionen zwischen dem potenziellen Käufer und Verkäufer ausgetauscht.

---

### 1.1 Promotion (Anpreisung)

### [English]
[DEFINITION] A promotion (Anpreisung) is a non-binding declaration of a seller's willingness to sell goods. 

[INFO] Promotions are directed at the general public rather than a specific individual. Because they lack a definitive intention to be legally bound (Bindungswille), the seller is not obligated to sell the items. Examples include catalogs, flyers, shop window displays, print advertisements, and online shop listings.

[TIP] You can often recognize a promotion by explicit disclaimers such as "while stocks last" (solange der Vorrat reicht).

### [German]
[DEFINITION] Eine Anpreisung ist eine rechtlich unverbindliche Erklärung der Verkaufsbereitschaft eines Verkäufers.

[INFO] Anpreisungen richten sich an die Allgemeinheit und nicht an eine bestimmte Person. Da ihnen der Bindungswille fehlt, ist der Verkäufer nicht verpflichtet, die Ware zu verkaufen. Beispiele sind Kataloge, Flugblätter, Schaufensterauslagen, Zeitungsanzeigen und Onlineshops.

[TIP] Eine Anpreisung erkennt man oft an Freizeichnungsklauseln wie „solange der Vorrat reicht“.

---

### 1.2 Inquiry (Anfrage)

### [English]
[DEFINITION] An inquiry (Anfrage) is a request for information made by a prospective buyer to a seller. It is legally non-binding and establishes no obligation to purchase.

[INFO] Inquiries can be made verbally or in writing. There are two main types:
*   **General Inquiry (Allgemeine Anfrage):** The buyer requests general information, such as catalogs, price lists, or general brochures (e.g., "Please send us your latest catalog").
*   **Specific Inquiry (Spezielle Anfrage):** The buyer asks for detailed information regarding a specific product, its price, delivery times, or payment conditions (e.g., "What is the price for 50 laptops of model X?").

### [German]
[DEFINITION] Eine Anfrage ist die rechtlich unverbindliche Informationsbeschaffung eines potenziellen Käufers an einen Verkäufer. Sie verpflichtet nicht zum Kauf.

[INFO] Anfragen können mündlich oder schriftlich erfolgen. Es gibt zwei Hauptarten:
*   **Allgemeine Anfrage:** Der Käufer bittet um allgemeine Informationen wie Kataloge, Preislisten oder Prospekte (z. B. „Bitte senden Sie uns Ihren aktuellen Katalog“).
*   **Spezielle Anfrage:** Der Käufer bittet um detaillierte Informationen zu einem bestimmten Produkt, dessen Preis, Lieferzeiten oder Zahlungsbedingungen (z. B. „Was kosten 50 Laptops des Modells X?“).

---

### 1.3 Offer (Angebot)

### [English]
[DEFINITION] An offer (Angebot) is a declaration by the seller expressing their willingness to sell specific goods under specific conditions. If legally binding, it can lead directly to a contract if accepted by the buyer.

[DIAGRAM SUGGESTION: A flowchart showing the types of offers: Requested vs. Unsolicited, and Binding vs. Non-binding.]

**Requested vs. Unsolicited Offers:**
*   **Requested Offer (Verlangtes Angebot):** The offer is made in response to a specific inquiry from the buyer.
*   **Unsolicited Offer (Unverlangtes Angebot):** The seller takes the initiative and sends an offer without a prior inquiry from the buyer.

**Binding vs. Non-binding Offers:**
*   **Binding Offer (Verbindliches Angebot):** The seller is legally bound to the offer for a certain period. For an offer to be binding, it must contain a clear intention to be bound (Bindungswille), be addressed to a specific person, and include the 5 mandatory contract components (Seller, Buyer, Quality, Quantity, Price).
*   **Non-binding / Provisional Offer (Freibleibendes Angebot):** The seller limits their legal obligation by using exemption clauses (Freizeichnungsklauseln).
    *   *Examples of clauses:* "prices subject to change without notice" (Preisänderungen vorbehalten), "only while stocks last" (solange der Vorrat reicht), "this offer is not binding" / "without obligation" (freibleibend / ohne Obligo).

**Binding Duration (Bindungsdauer):**
If an offer is binding, how long does the commitment last?
1.  **Specified in the offer:** E.g., "This offer is valid until May 15th" or "Valid for 14 days."
2.  **Statutory binding period (Gesetzliche Bindungsdauer):**
    *   *Among present parties (Mündlich/Telefonisch):* Valid only for the duration of the conversation. There is no consideration period.
    *   *Among absent parties (Schriftlich - Mail/Brief):* The duration consists of double the transport time (Hin- und Rückweg) plus an appropriate consideration period (angemessene Überlegungsfrist). For emails, the transport time is negligible, so only the consideration period applies. For letters, expect 4-6 days total.

### [German]
[DEFINITION] Ein Angebot ist die Erklärung des Verkäufers, bestimmte Waren zu bestimmten Bedingungen verkaufen zu wollen. Ist es rechtlich bindend, führt die Annahme durch den Käufer direkt zum Vertrag.

[DIAGRAM SUGGESTION: Ein Flussdiagramm, das die Arten von Angeboten zeigt: Verlangt vs. Unverlangt und Verbindlich vs. Unverbindlich.]

**Verlangtes vs. Unverlangtes Angebot:**
*   **Verlangtes Angebot:** Das Angebot erfolgt als Antwort auf eine konkrete Anfrage des Käufers.
*   **Unverlangtes Angebot:** Der Verkäufer ergreift die Initiative und sendet ein Angebot ohne vorherige Anfrage.

**Verbindliches vs. Unverbindliches Angebot:**
*   **Verbindliches Angebot:** Der Verkäufer ist für eine bestimmte Zeit rechtlich an das Angebot gebunden. Voraussetzung: Es muss ein erkennbarer Bindungswille vorliegen, sich an eine bestimmte Person richten und die 5 gesetzlichen Bestandteile (Verkäufer, Käufer, Qualität, Quantität, Preis) enthalten.
*   **Unverbindliches / Freibleibendes Angebot:** Der Verkäufer schränkt seine rechtliche Bindung durch Freizeichnungsklauseln ein.
    *   *Klauselbeispiele:* „Preisänderungen vorbehalten“, „solange der Vorrat reicht“, „freibleibend / ohne Obligo“.

**Bindungsdauer:**
Wenn ein Angebot verbindlich ist, wie lange gilt die Bindung?
1.  **Im Angebot angegeben:** Z. B. „Dieses Angebot gilt bis 15. Mai“ oder „14 Tage gültig“.
2.  **Gesetzliche Bindungsdauer (falls nicht angegeben):**
    *   *Unter Anwesenden (mündlich/telefonisch):* Gültig nur für die Dauer des Gesprächs. Es gibt keine Überlegungsfrist.
    *   *Unter Abwesenden (schriftlich - Mail/Brief):* Setzt sich zusammen aus dem doppelten Transportweg plus einer angemessenen Überlegungsfrist. Bei E-Mails entfällt der Transportweg weitgehend. Bei Briefen rechnet man mit 4-6 Tagen.

---

## 2. Conclusion of Sales Contracts (Abschluss)

### [English]
[INFO] The conclusion of the contract is the second phase. It occurs when two parties reach a mutual agreement (meeting of minds / übereinstimmende Willenserklärung).

**The Order (Bestellung):**
*   An order is the buyer's declaration to accept the seller's offer.
*   If the buyer orders exactly according to a *binding offer* within the binding period, the sales contract is concluded immediately.
*   If the order deviates from the offer, or if it is based on a *non-binding offer* (or just a promotion), the order legally acts as a new offer from the buyer. In this case, the seller must confirm it to close the contract.

**The Order Confirmation (Auftragsbestätigung):**
*   This is the seller's declaration that the order has been received and accepted.
*   It is mandatory if:
    1. The order deviates from the original offer.
    2. The order is based on a non-binding offer.
    3. The buyer placed an order without a prior offer.
*   In B2C e-commerce (online shopping), an electronic order confirmation is always legally required immediately after purchase.

### [German]
[INFO] Der Vertragsabschluss ist die zweite Phase. Er kommt durch eine übereinstimmende Willenserklärung beider Parteien zustande (meeting of minds).

**Die Bestellung:**
*   Die Bestellung ist die Erklärung des Käufers, das Angebot des Verkäufers anzunehmen.
*   Bestellt der Käufer rechtzeitig und unverändert auf Basis eines *verbindlichen Angebots*, ist der Kaufvertrag sofort abgeschlossen.
*   Weicht die Bestellung vom Angebot ab oder basiert sie auf einem *unverbindlichen Angebot* (bzw. einer Anpreisung), gilt die Bestellung rechtlich als neues Angebot des Käufers. Der Verkäufer muss dann bestätigen.

**Die Auftragsbestätigung:**
*   Dies ist die Erklärung des Verkäufers, dass die Bestellung eingegangen ist und angenommen wird.
*   Sie ist verpflichtend, wenn:
    1. Die Bestellung vom Angebot abweicht.
    2. Die Bestellung auf einem freibleibenden Angebot basiert.
    3. Der Käufer ohne vorheriges Angebot bestellt hat.
*   Beim Online-Shopping (B2C) ist nach erfolgter Bestellung gesetzlich immer eine elektronische Auftragsbestätigung zwingend erforderlich.

---

## 3. Fulfillment of Sales Contracts (Erfüllung)

### [English]
[INFO] Fulfillment represents the final stage where both parties meet their contractual obligations: The seller delivers the goods, and the buyer accepts and pays for them.

**1. Delivery (Lieferung):**
The seller must deliver the goods as agreed. If delivered via a freight carrier, accompanying documents (Begleitpapiere) are issued:
*   **Delivery Note (Lieferschein):** Goes to the buyer detailing the shipment.
*   **Counter-slip (Gegenschein):** The buyer signs this to confirm receipt for the seller.
*   **Freight Documents (Frachtdokumente):** Used when external carriers (post, rail, logistics) transport the goods.

**2. Invoicing (Rechnungslegung):**
The seller issues an invoice (Rechnung/Faktura). According to tax laws (UStG), an invoice must contain specific elements, including the names/addresses of both parties, date of issue, date of delivery, quantity, commercial description, net amount, tax rate, gross amount, and, for larger amounts, the VAT identification numbers (UID-Nummern).

**3. Acceptance of Goods (Annahme):**
The buyer must inspect the goods upon receipt. This includes checking the delivery note against the order and checking for obvious defects. Acceptance is confirmed by signing the counter-slip.

**4. Payment (Zahlung):**
The buyer must pay the invoice according to the agreed payment terms (e.g., prompt payment, advance, or within a credit period).

### [German]
[INFO] Die Erfüllung ist die letzte Phase, in der beide Parteien ihren vertraglichen Pflichten nachkommen: Der Verkäufer liefert die Ware, der Käufer nimmt sie an und bezahlt.

**1. Lieferung:**
Der Verkäufer übergibt die Ware wie vereinbart. Bei Lieferung durch einen Frachtführer werden Begleitpapiere ausgestellt:
*   **Lieferschein:** Geht an den Käufer und listet die gelieferten Waren auf.
*   **Gegenschein:** Wird vom Käufer als Empfangsbestätigung unterschrieben und geht an den Verkäufer zurück.
*   **Frachtdokumente:** Werden verwendet, wenn externe Transportunternehmen (Post, Bahn, Spedition) beauftragt werden.

**2. Rechnungslegung:**
Der Verkäufer stellt eine Rechnung (Faktura) aus. Laut UStG muss eine Rechnung bestimmte Mindestbestandteile aufweisen, darunter Name/Anschrift von Käufer und Verkäufer, Ausstellungsdatum, Lieferdatum, Menge, handelsübliche Bezeichnung, Nettoentgelt, Umsatzsteuersatz, Bruttobetrag und bei höheren Beträgen die UID-Nummern.

**3. Annahme der Ware:**
Der Käufer muss die Ware bei Erhalt prüfen. Dazu gehört der Abgleich von Lieferschein und Bestellung sowie die Prüfung auf offensichtliche Mängel. Die Annahme wird mit der Unterschrift auf dem Gegenschein bestätigt.

**4. Zahlung:**
Der Käufer muss die Rechnung entsprechend den vereinbarten Zahlungsbedingungen begleichen (z. B. prompt, im Voraus oder mit Zahlungsziel).

---

## 4. Components of a Sales Contract (Bestandteile)

### [English]
A sales contract consists of legally required mandatory components and additional commercial components. (Note: Price calculations are excluded here).

### [German]
Ein Kaufvertrag besteht aus gesetzlich verpflichtenden Mindestbestandteilen und zusätzlichen kaufmännischen Bestandteilen. (Hinweis: Preiskalkulationen sind hier ausgenommen).

---

### 4.1 Mandatory Components (Verpflichtende Bestandteile)

### [English]
To form a valid sales contract, five elements MUST be present:
1.  **Seller (Bestimmter Verkäufer)**
2.  **Buyer (Bestimmter Käufer)**
3.  **Quality / Product Type (Qualität / Produktart)**
4.  **Quantity (Quantität / Menge)**
5.  **Price (Preis)**

**A. Quality Specification (Qualitätsfestlegung):**
How quality is defined depends on whether the goods are fungible or non-fungible.
*   *Fungible goods (Vertretbare Waren):* Standardized, interchangeable items (e.g., a specific smartphone model, A4 paper). Quality is defined by standards, norms, brands, or samples.
*   *Non-fungible goods (Nicht vertretbare Waren):* Unique items (e.g., original artwork, real estate, used cars). Quality is defined by detailed description or physical inspection.

*Methods of defining quality:*
*   **Inspection (Besichtigung):** Typical for used goods or real estate.
*   **Description and Illustration (Beschreibung und Abbildung):** Crucial for online shopping.
*   **Samples (Muster und Proben):** E.g., paint swatches or fabric. Includes "Sale by sample" (Kauf nach Muster), "Sale on approval" (Kauf auf Probe - conditional), and "Sale for testing" (Kauf zur Probe - unconditional small purchase).
*   **Brands and Types (Marken und Typen):** Trademarks (Word, Image, Combined) ensure consistent quality (e.g., Apple, Coca-Cola).
*   **Standards and Grades (Normen, Qualitätsklassen, Gütezeichen):** General guidelines (like DIN A4), classes (Class 1 apples), or quality seals (AMA, Fairtrade).
*   **Special Regulations:** "Sale by specification" (Spezifikationskauf - buying a total quantity but specifying sizes/colors later) and "Sale in bulk" (Kauf in Bausch und Bogen - buying the whole lot without guaranteeing specific individual quality, e.g., a whole harvest).

**B. Quantity Specification (Quantitätsfestlegung):**
*   **Precise statement:** E.g., 50 kg cement.
*   **Approximate statement:** "Circa" contracts (e.g., 3000 kg +/- 5%).
*   **No statement:** Sale in bulk (Bausch und Bogen).
*   *Packaging weights:* Gross weight (Product + Packaging), Net weight (Product only), Tare (Weight of packaging).

**C. Price Specification (Preisfestsetzung):**
Prices can be fixed or subject to change.
*   *Cost Fluctuation Clause (Kostenschwankungsklausel):* Allows the seller to adjust the price if production or transport costs rise (common in construction).
*   *Index Clause (Wertsicherungsklausel):* Links the price to an economic index like inflation.

### [German]
Damit ein Kaufvertrag zustande kommt, müssen zwingend fünf Elemente vorhanden sein:
1.  **Bestimmter Verkäufer**
2.  **Bestimmter Käufer**
3.  **Qualität / Produktart**
4.  **Quantität / Menge**
5.  **Preis**

**A. Qualitätsfestlegung:**
Wie die Qualität festgelegt wird, hängt davon ab, ob die Waren vertretbar (fungibel) oder nicht vertretbar sind.
*   *Vertretbare Waren (Fungible goods):* Standardisierte, austauschbare Güter (z. B. Serien-Smartphones, A4-Papier). Festlegung durch Normen, Marken oder Muster.
*   *Nicht vertretbare Waren (Non-fungible goods):* Einzigartige Güter (z. B. Kunstwerke, Grundstücke, Gebrauchtwagen). Festlegung durch genaue Beschreibung oder Besichtigung.

*Formen der Qualitätsfestlegung:*
*   **Besichtigung:** Typisch bei Gebrauchtwaren oder Immobilien.
*   **Beschreibung und Abbildung:** Unerlässlich beim Online-Shopping.
*   **Muster und Proben:** Z. B. Farbmuster oder Stoffproben. Unterscheidung in "Kauf nach Probe/Muster", "Kauf auf Probe" (bedingt, mit Rückgaberecht) und "Kauf zur Probe" (unbedingt, kleine Menge zum Testen).
*   **Marken und Typen:** Wort-, Bild- oder kombinierte Marken (z. B. Apple, Coca-Cola) garantieren gleichbleibende Qualität.
*   **Normen, Qualitätsklassen, Gütezeichen:** Richtlinien (wie DIN A4), Handelsklassen (Äpfel Klasse 1) oder Siegel (AMA, Fairtrade).
*   **Sonderregelungen:** "Spezifikationskauf" (Gesamtmenge wird gekauft, Details wie Farben/Größen werden später bestimmt) und "Kauf in Bausch und Bogen" (Kauf der Gesamtware ohne Rücksicht auf die Qualität einzelner Stücke, z. B. eine Ernte).

**B. Quantitätsfestlegung (Menge):**
*   **Genaue Angabe:** Z. B. 50 kg Zement.
*   **Ungefähre Angabe:** Zirka-Verträge (z. B. 3000 kg +/- 5%).
*   **Ohne Angabe:** Kauf in Bausch und Bogen.
*   *Gewichtsabzüge:* Bruttogewicht (Produkt + Verpackung), Nettogewicht (nur Produkt), Tara (Gewicht der Verpackung).

**C. Preisfestsetzung:**
Preise können fest oder freibleibend sein.
*   *Kostenschwankungsklausel:* Erlaubt dem Verkäufer, den Preis anzupassen, wenn z.B. Produktions- oder Transportkosten steigen (häufig im Bauwesen).
*   *Wertsicherungsklausel:* Bindet den Preis an einen Index (z.B. Verbraucherpreisindex/Inflation).

---

### 4.2 Additional Components (Zusätzliche Bestandteile)

### [English]
If not explicitly negotiated, default legal provisions (Usancen or ABGB) apply. Parties usually define these in the contract or via General Terms & Conditions (AGB).

**A. Terms of Delivery (Lieferbedingungen):**
Determine Time, Place, and the Transfer of Risk/Costs.
*   **Time of Delivery (Erfüllungszeit):** 
    *   *Prompt delivery (Promptgeschäft):* Immediately after ordering.
    *   *Fixed date (Fixgeschäft):* Exact date ("Delivery on May 4th fixed"). If missed, the contract is automatically broken.
    *   *Scheduled (Termingeschäft):* Within a specific period ("Delivery within 2 weeks").
*   **Place of Delivery & Risk Transfer (Erfüllungsort & Risiko-/Kostenübergang):** 
    Determines where risk (loss/damage) and freight costs shift from seller to buyer.
    *   *Ex works (ab Werk):* Buyer bears all costs and risks from the seller's factory. (One-point clause / Einpunktklausel).
    *   *Free house / Free domicile (frei Haus):* Seller bears all costs and risks up to the buyer's address. (One-point clause).
    *   *Carriage paid to... / Freight free (frachtfrei...):* Seller pays transport costs up to a named destination (e.g., a train station), but the risk transfers to the buyer as soon as the goods are handed to the first carrier. (Two-point clause / Zweipunktklausel).

**B. Terms of Payment (Zahlungsbedingungen):**
Determine when, where, and how payment is made.
*   **Time of Payment (Erfüllungszeit der Zahlung):**
    *   *Payment in advance (Vorauszahlung):* Before delivery (e.g., online shopping).
    *   *Prompt payment (Kassakauf):* Upon delivery or receipt of invoice.
    *   *Deferred payment / Credit (Spätere Zahlung / Zielkauf):* E.g., "30 days net".
*   **Discounts:**
    *   *Cash Discount (Skonto):* A percentage reduction (usually 2-3%) for paying earlier than the final deadline (e.g., "Payable within 10 days at 2% skonto, or 30 days net").
    *   *Quantity Discount (Mengenrabatt):* For buying in bulk.
    *   *Trade/Annual Discount (Händlerrabatt / Umsatzbonus).*

**C. Other Contract Components (Sonstige Vertragsbestandteile):**
*   **Reservation of Ownership (Eigentumsvorbehalt):** "The goods remain the property of the seller until full payment is received." Secures the seller in case of credit sales.
*   **Penalty (Pönale):** A pre-agreed financial penalty for late delivery. The seller must pay it and still deliver.
*   **Cancellation Fee (Stornogebühr / Reuegeld):** A fee paid by the buyer to withdraw from a valid contract.
*   **Warranty & Guarantee (Gewährleistung & Garantie):** Warranty is statutory (legal obligation for defects present at delivery). Guarantee is a voluntary service provided by the seller/manufacturer.
*   **Right to Exchange (Umtauschrecht):** Legally, there is NO automatic right to exchange non-defective goods bought in a physical store. It is purely voluntary (Kulanz) unless explicitly agreed.
*   **Packaging (Verpackung):** Protects goods, enables transport, advertises, and informs. Costs are usually borne by the buyer unless otherwise agreed.

**D. General Terms & Conditions (AGB):**
[DEFINITION] Pre-formulated standard contract terms created by the company to simplify mass contracts.
[INFO] AGBs must be brought to the buyer's attention *before* the contract is signed. The law protects consumers from highly disadvantageous or completely incomprehensible clauses hidden in the fine print.

### [German]
Wenn nicht ausdrücklich verhandelt, gelten die gesetzlichen Bestimmungen (Usancen oder ABGB). Meistens definieren Parteien dies im Vertrag oder in den Allgemeinen Geschäftsbedingungen (AGB).

**A. Lieferbedingungen:**
Bestimmen Zeit, Ort und den Risiko-/Kostenübergang.
*   **Erfüllungszeit der Lieferung:**
    *   *Sofortige Lieferung (Promptgeschäft):* Unmittelbar nach der Bestellung.
    *   *Fixgeschäft:* Genauer Termin ("Lieferung am 4. Mai fix"). Bei Verzug platzt der Vertrag sofort.
    *   *Gewöhnliches Termingeschäft:* Innerhalb eines bestimmten Zeitraums ("Lieferung innerhalb von 2 Wochen").
*   **Erfüllungsort & Risiko-/Kostenübergang:**
    Bestimmt, wo das Risiko (Verlust/Beschädigung) und die Transportkosten vom Verkäufer auf den Käufer übergehen.
    *   *Ab Werk (ex works):* Käufer trägt Risiko und Kosten ab dem Werk des Verkäufers. (Einpunktklausel).
    *   *Frei Haus (free domicile):* Verkäufer trägt Risiko und Kosten bis zur Adresse des Käufers. (Einpunktklausel).
    *   *Frachtfrei... (carriage paid to...):* Verkäufer zahlt die Kosten bis zu einem bestimmten Ort (z. B. Bahnhof), aber das Risiko geht bereits bei Übergabe an den ersten Frachtführer auf den Käufer über. (Zweipunktklausel).

**B. Zahlungsbedingungen:**
Bestimmen wann, wo und wie bezahlt wird.
*   **Erfüllungszeit der Zahlung:**
    *   *Vorauszahlung:* Vor der Lieferung (z. B. im Online-Handel).
    *   *Prompte Zahlung (Kassakauf):* Bei Übergabe oder Rechnungserhalt.
    *   *Spätere Zahlung (Zielkauf):* Z. B. "30 Tage netto".
*   **Preisabzüge:**
    *   *Skonto:* Ein prozentualer Abzug (meist 2-3%) als Belohnung für eine vorzeitige Zahlung vor dem eigentlichen Fälligkeitsdatum (z. B. "Zahlbar innerhalb von 10 Tagen mit 2 % Skonto, oder 30 Tage netto").
    *   *Mengenrabatt:* Preisnachlass für den Kauf großer Mengen.
    *   *Händlerrabatt / Umsatzbonus:* Nachlass für Wiederverkäufer oder am Jahresende bei Erreichen einer Umsatzgrenze.

**C. Sonstige kaufmännische Bestandteile:**
*   **Eigentumsvorbehalt:** "Bis zur vollständigen Bezahlung bleibt die Ware Eigentum des Verkäufers." Dient der Absicherung des Verkäufers bei Zielkäufen.
*   **Pönale (Vertragsstrafe):** Eine vorab vereinbarte Geldstrafe für verspätete Lieferung. Der Verkäufer muss zahlen und trotzdem erfüllen.
*   **Stornogebühr (Reuegeld):** Eine Gebühr, die der Käufer zahlt, um straffrei von einem gültigen Vertrag zurückzutreten.
*   **Gewährleistung & Garantie:** Gewährleistung ist die gesetzliche Haftung für Mängel zum Zeitpunkt der Übergabe. Garantie ist eine freiwillige Zusatzleistung des Verkäufers oder Herstellers.
*   **Umtauschrecht:** Gesetzlich gibt es KEIN automatisches Recht auf Umtausch mangelfreier Ware im stationären Handel. Dies geschieht rein freiwillig (Kulanz), sofern nicht vertraglich vereinbart.
*   **Verpackung:** Dient dem Schutz, dem Transport, der Werbung und der Information. Die Kosten trägt in der Regel der Käufer, sofern nicht anders vereinbart.

**D. Allgemeine Geschäftsbedingungen (AGB):**
[DEFINITION] Vorformulierte Standardvertragsbedingungen, die von Unternehmen erstellt werden, um Massenverträge zu vereinfachen.
[INFO] Der Konsument muss *vor* Vertragsabschluss auf die AGB hingewiesen werden und die Möglichkeit haben, sie einzusehen. Das Gesetz schützt Konsumenten vor grob benachteiligenden oder unverständlichen Klauseln im Kleingedruckten.

---

### 4.3 E-Commerce and Special Withdrawal Rights (E-Commerce & Rücktrittsrechte)

### [English]
[INFO] Special rules apply when consumers (B2C) buy goods outside of traditional retail stores. 
*   **FAGG (Fern- und Auswärtsgeschäfte-Gesetz):** Governs distance selling (Fernabsatzgeschäfte like online shopping, catalogs) and off-premises contracts (Auswärtsgeschäfte like door-to-door sales or street peddling).
*   **Right of Withdrawal (Rücktrittsrecht):** Consumers generally have the right to withdraw from a distance or off-premises contract within **14 days** of receiving the goods, **without giving any reason**.
*   If the seller fails to properly inform the buyer about this withdrawal right, the period extends to 12 months and 14 days.

[TIP] Always favor online shops within the EU, as they are subject to strict EU directives (e.g., the "Button-Lösung" where the final order button must clearly indicate a payment obligation, and mandatory legal information obligations via the ECG).

### [German]
[INFO] Besondere Regeln gelten, wenn Konsumenten (B2C) Waren außerhalb klassischer Geschäftsräume kaufen.
*   **FAGG (Fern- und Auswärtsgeschäfte-Gesetz):** Regelt Fernabsatzgeschäfte (Onlineshops, Kataloge) und Auswärtsgeschäfte (Haustürgeschäfte, Werbefahrten).
*   **Rücktrittsrecht:** Konsumenten haben grundsätzlich das Recht, innerhalb von **14 Tagen** ab Erhalt der Ware **ohne Angabe von Gründen** vom Vertrag zurückzutreten.
*   Wurde der Käufer nicht ordnungsgemäß über sein Rücktrittsrecht belehrt, verlängert sich diese Frist auf 12 Monate und 14 Tage.

[TIP] Bevorzuge Onlineshops innerhalb der EU, da diese strengen EU-Richtlinien unterliegen (z.B. die "Button-Lösung", bei der der Bestell-Button eindeutig auf eine Zahlungsverpflichtung hinweisen muss, sowie die gesetzliche Informationspflicht laut ECG/E-Commerce-Gesetz).

# Sales Contract Preparation: Inquiry, Offer, and Order / Anbahnung des Kaufvertrags: Anfrage, Angebot und Bestellung

## 1. The Inquiry / Die Anfrage

### [English]
[DEFINITION] An **inquiry** (or enquiry) is a request from a potential buyer to a seller. The buyer asks for information about goods or services. An inquiry is always legally non-binding. It can be made verbally (in person, by phone) or in writing (email, letter).

### [German]
[DEFINITION] Eine **Anfrage** ist die rechtlich unverbindliche Aufforderung eines potenziellen Käufers an einen Verkäufer, Informationen über Waren oder Dienstleistungen zu übermitteln. Sie ist an keine Form gebunden und kann mündlich (persönlich, telefonisch) oder schriftlich (E-Mail, Brief) erfolgen.

## 1.1 Types of Inquiries / Arten der Anfrage

### [English]
[INFO] There are four main types of inquiries, depending on the buyer's intention:
1. **General Inquiry (Allgemeine Anfrage):** The buyer only wants general information, such as brochures, catalogs, or general price lists.
2. **Special Inquiry (Spezielle Anfrage):** The buyer requests precise information about specific product characteristics, exact prices, delivery terms, and payment conditions.
3. **Follow-up Inquiry (Rückfrage):** The buyer refers to information already received and requests additional details.
4. **Counter-offer (Gegenangebot):** The buyer wishes to modify specific conditions of an existing offer (e.g., requesting a lower price or faster delivery time).

### [German]
[INFO] Je nach Absicht des Käufers unterscheidet man vier Arten der Anfrage:
1. **Allgemeine Anfrage:** Der Käufer möchte nur allgemeine Informationen, z. B. Prospekte, Kataloge oder Preislisten.
2. **Spezielle Anfrage:** Der Käufer benötigt genaue Informationen über bestimmte Eigenschaften, Preise, Liefer- und Zahlungsbedingungen.
3. **Rückfrage:** Der Käufer bezieht sich auf bereits erhaltene Informationen und wünscht Zusatzinformationen.
4. **Gegenangebot:** Der Käufer möchte bestimmte Bedingungen eines vorliegenden Angebots abändern (z. B. niedrigere Preise oder schnellere Lieferzeit verlangen).

## 1.2 How to Structure and Write an Inquiry / Struktur und Formulierung einer Anfrage

### [English]
[TIP] A well-structured written inquiry should include the following elements:
* **Subject Line:** Clear statement of intent (e.g., "Inquiry regarding [Product]").
* **Salutation:** Formal greeting (e.g., "Dear Sir or Madam," or "Dear Mr./Ms. [Name]").
* **Introduction:** State the reason for the inquiry (e.g., "We are looking for...", "We saw your advertisement...").
* **Main Body:** Detail the exact requirements (quantity, specific product features, quality). 
* **Questions/Conditions:** Ask for prices, terms of delivery (Lieferbedingungen), and terms of payment (Zahlungsbedingungen).
* **Call to Action:** Request an offer (e.g., "Please send us a binding offer...").
* **Closing & Signature:** Formal sign-off (e.g., "Yours sincerely,") followed by the sender's details.

### [German]
[TIP] Eine gut strukturierte schriftliche Anfrage sollte folgende Elemente enthalten:
* **Betreff:** Klare Nennung des Anliegens (z. B. "Anfrage bezüglich [Produkt]").
* **Anrede:** Formelle Begrüßung (z. B. "Sehr geehrte Damen und Herren," oder "Sehr geehrte/r Herr/Frau [Name]").
* **Einleitung:** Grund der Anfrage nennen (z. B. "Wir sind auf der Suche nach...", "Wir haben Ihre Anzeige gesehen...").
* **Hauptteil:** Genaue Anforderungen auflisten (Menge, spezifische Eigenschaften, Qualität).
* **Fragen/Bedingungen:** Nach Preisen, Lieferbedingungen und Zahlungsbedingungen fragen.
* **Aufforderung:** Um ein Angebot bitten (z. B. "Bitte senden Sie uns ein verbindliches Angebot...").
* **Schluss & Unterschrift:** Formelle Grußformel (z. B. "Mit freundlichen Grüßen") und Kontaktdaten des Absenders.

---

## 2. The Offer / Das Angebot

### [English]
[DEFINITION] With an **offer**, the seller declares their willingness to sell goods to a customer under specific conditions. 
[INFO] Note the difference from **Advertising (Anpreisung)**: General advertisements (like a shop window display, a flyer, or a website) are addressed to the general public and are *not* legally binding offers. A valid offer must address a specific recipient.

### [German]
[DEFINITION] Mit dem **Angebot** erklärt sich der Verkäufer bereit, dem Kunden Waren zu bestimmten Bedingungen zu verkaufen.
[INFO] Wichtiger Unterschied zur **Werbung/Anpreisung**: Allgemeine Werbung (wie Schaufenster, Flugblätter oder Webseiten) richtet sich an die Allgemeinheit und stellt *kein* rechtlich bindendes Angebot dar. Ein gültiges Angebot muss an einen bestimmten Empfänger gerichtet sein.

## 2.1 Statutory Components of an Offer / Gesetzliche Bestandteile eines Angebots

### [English]
[INFO] For an offer to be legally valid and binding, it must contain five statutory components (Kaufvertragsbestandteile):
1. **Specific Seller** (Bestimmter Verkäufer)
2. **Specific Buyer** (Bestimmter Käufer)
3. **Quantity** (Menge)
4. **Quality** (Qualität/Güte)
5. **Price** (Preis)

Furthermore, the offer must show the **intent to bind** (Bindungswille) of both parties and must be **received** personally by the recipient (Zugang).

### [German]
[INFO] Damit ein Angebot rechtlich gültig und verbindlich ist, muss es fünf gesetzliche Bestandteile enthalten:
1. **Bestimmter Verkäufer**
2. **Bestimmter Käufer**
3. **Menge**
4. **Qualität**
5. **Preis**

Außerdem muss das Angebot den **Bindungswillen** von Verkäufer und Käufer erkennen lassen und es muss dem Empfänger persönlich **zugehen** (Zugang).

## 2.2 Types of Offers / Angebotsarten

### [English]
[DIAGRAM SUGGESTION: A flowchart showing the types of offers split by "Initiative" (Demanded vs. Undemanded) and by "Binding nature" (Binding vs. Non-binding).]

**Based on Initiative:**
* **Demanded Offer (Verlangtes Angebot):** The initiative comes from the buyer (an inquiry preceded it).
* **Unsolicited Offer (Unverlangtes Angebot):** The initiative comes from the seller (sent without a prior inquiry).

**Based on Binding Nature:**
* **Binding Offer (Verbindliches Angebot):** Contains all statutory components, shows clear intent to bind, and has no exclusion clauses. If the buyer accepts it on time and without changes, a sales contract is immediately formed.
* **Provisional/Non-binding Offer (Freibleibendes/Unverbindliches Angebot):** The seller restricts their binding commitment by using an exclusion clause.

### [German]
[DIAGRAM SUGGESTION: Ein Flussdiagramm, das die Angebotsarten nach "Initiative" (Verlangt vs. Unverlangt) und nach "Bindung" (Verbindlich vs. Unverbindlich) aufteilt.]

**Nach der Initiative:**
* **Verlangtes Angebot:** Die Initiative geht vom Käufer aus (eine Anfrage ging voraus).
* **Unverlangtes Angebot:** Die Initiative geht vom Verkäufer aus (wird ohne vorherige Anfrage gesendet).

**Nach der Bindung:**
* **Verbindliches Angebot:** Enthält alle gesetzlichen Bestandteile, zeigt erkennbaren Bindungswillen und hat keine Freizeichnungsklausel. Wird es rechtzeitig und unverändert angenommen, entsteht ein Kaufvertrag.
* **Freibleibendes/Unverbindliches Angebot:** Der Verkäufer schränkt seine Bindung durch eine Freizeichnungsklausel ein.

## 2.3 Exclusion Clauses / Freizeichnungsklauseln

### [English]
[DEFINITION] **Exclusion clauses** are phrases used by the seller to make an offer legally non-binding. This is advantageous for the seller because it allows them to react flexibly to market changes or find better buyers.
Common clauses include:
* "Without obligation" (Unverbindlich / Ohne Obligo)
* "Only while stocks last" (Solange der Vorrat reicht)
* "Subject to change" (Freibleibend)
* "Prices are subject to change without notice" (Preisänderungen vorbehalten)

### [German]
[DEFINITION] **Freizeichnungsklauseln** sind Formulierungen, die der Verkäufer nutzt, um ein Angebot rechtlich unverbindlich zu machen. Dies ist für den Verkäufer günstiger, da er so flexibel auf Marktsituationen reagieren oder bessere Käufer finden kann.
Häufige Klauseln sind:
* "Unverbindlich" / "Ohne Obligo"
* "Solange der Vorrat reicht"
* "Freibleibend"
* "Preisänderungen vorbehalten"

## 2.4 Validity Period of Binding Offers / Bindungsdauer von verbindlichen Angeboten

### [English]
How long is a binding offer valid? There are two main scenarios:
**1. Validity specified in the offer:**
The specified time applies (e.g., "This offer is valid for 14 days," or "Valid until April 15").

**2. No validity specified (Statutory binding period):**
* **Among present parties (Oral, Telephone):** Valid only for the duration of the conversation. There is no consideration period.
* **Among absent parties (Email, Fax, Letter):** Valid for: *Double the transport time + an appropriate consideration period.*
  * Email/Fax transport time is immediate. Consideration period is a few days.
  * Letter transport time is 4-6 days (round trip) plus consideration period (often resulting in approx. 7-14 days total).
  * [INFO] A consideration period is given because purchasing goods is not an everyday activity and requires time to think.

### [German]
Wie lange ist ein verbindliches Angebot bindend? Es gibt zwei Fälle:
**1. Im Angebot angegebene Bindungsdauer:**
Es gilt die angegebene Frist (z. B. "Dieses Angebot ist 14 Tage gültig" oder "Gültig bis 15. April").

**2. Keine Angabe (Gesetzliche Bindungsdauer lt. ABGB):**
* **Unter Anwesenden (Mündlich, Telefonisch):** Nur für die Dauer des Gesprächs gültig. Es gibt keine Überlegungsfrist.
* **Unter Abwesenden (E-Mail, Fax, Brief):** Gültig für: *Doppelter Transportweg + angemessene Überlegungsfrist.*
  * E-Mail/Fax: Transportweg ist sofort. Überlegungsfrist beträgt wenige Tage.
  * Brief: Transportweg ca. 4-6 Tage (hin und zurück) + Überlegungsfrist (ergibt oft ca. 7-14 Tage gesamt).
  * [INFO] Eine angemessene Überlegungsfrist wird gewährt, da ein Kauf im B2B-Bereich keine alltägliche Handlung ist und Bedenkzeit erfordert.

## 2.5 How to Structure and Write an Offer / Struktur und Formulierung eines Angebots

### [English]
[TIP] A complete and legally sound offer should be structured as follows:
* **Subject Line:** Reference the inquiry (e.g., "Your inquiry regarding [Product]").
* **Salutation:** Formal greeting.
* **Introduction:** Thank the customer for their inquiry (e.g., "Thank you for your inquiry. We are pleased to offer you...").
* **Detailed Specifications (The 5 statutory components):**
  * Exact description of the product (Quality).
  * Quantity offered.
  * Price (per unit and total), clearly stating if VAT is included or excluded.
* **Terms of Delivery & Payment:** E.g., "Delivery within 7 working days," "14 days net without deduction."
* **Validity Period / Exclusion Clauses:** State explicitly how long the offer is valid, or insert an exclusion clause if non-binding.
* **Closing & Signature:** Polite sign-off (e.g., "We look forward to receiving your order").

### [German]
[TIP] Ein vollständiges und rechtssicheres Angebot sollte wie folgt strukturiert sein:
* **Betreff:** Bezug auf die Anfrage (z. B. "Angebot auf Ihre Anfrage bezüglich [Produkt]").
* **Anrede:** Formelle Begrüßung.
* **Einleitung:** Bedanken für die Anfrage (z. B. "Vielen Dank für Ihre Anfrage. Gerne bieten wir Ihnen... an.").
* **Detailangaben (Die 5 gesetzlichen Bestandteile):**
  * Genaue Beschreibung der Ware (Qualität).
  * Angebotene Menge.
  * Preis (Stück- und Gesamtpreis), klare Angabe ob inkl. oder exkl. USt.
* **Liefer- und Zahlungsbedingungen:** Z. B. "Lieferzeit: innerhalb von 7 Werktagen", "Zahlung: 14 Tage netto ohne Abzug".
* **Bindungsfrist / Freizeichnungsklausel:** Konkret angeben, bis wann das Angebot gültig ist, oder eine Klausel einbauen, falls es unverbindlich sein soll.
* **Schluss & Unterschrift:** Höfliche Grußformel (z. B. "Wir freuen uns auf Ihre Bestellung").

---

## 3. Comparing Offers / Angebote vergleichen

### [English]
[CLARIFICATION NEEDED: The user requested "comparing offers in detail", but the provided source materials do not contain deep instructions on this topic. The following information has been researched to fulfill the curriculum requirements for business administration at the requested level.]

When a buyer receives multiple offers, they must compare them systematically. This is divided into **quantitative** (calculable) and **qualitative** (non-calculable) criteria.

**1. Quantitative Comparison (Costing / Bezugskalkulation):**
The goal is to find the true cost of the goods (Einstandspreis/Bezugspreis) by neutralizing different discounts and shipping costs.
`List Price (Listeneinkaufspreis)`
`- Supplier Discount (Lieferantenrabatt)`
`= Target Price (Zieleinkaufspreis)`
`- Cash Discount (Lieferskonto)`
`= Cash Price (Bareinkaufspreis)`
`+ Delivery Costs / Freight (Bezugskosten)`
`= Cost Price (Einstandspreis)`

**2. Qualitative Comparison:**
The cheapest offer is not always the best. Other crucial factors include:
* Quality of the goods
* Delivery time and reliability
* Payment terms (flexibility)
* Warranty and customer service
* Sustainability and environmental standards of the supplier

### [German]
[CLARIFICATION NEEDED: Der Benutzer hat "Angebote vergleichen im Detail" angefordert, die bereitgestellten Materialien enthalten jedoch keine tiefgehenden Informationen dazu. Die folgenden Informationen wurden ergänzt, um die Standardanforderungen im Bereich Betriebswirtschaft (BW) zu erfüllen.]

Wenn ein Käufer mehrere Angebote erhält, muss er diese systematisch vergleichen. Man unterscheidet **quantitative** (rechnerische) und **qualitative** (nicht rechnerische) Kriterien.

**1. Quantitativer Angebotsvergleich (Bezugskalkulation):**
Ziel ist es, den tatsächlichen Preis der Ware (Einstandspreis/Bezugspreis) zu ermitteln, indem unterschiedliche Rabatte, Skonti und Lieferkosten vergleichbar gemacht werden.
`Listeneinkaufspreis`
`- Lieferantenrabatt`
`= Zieleinkaufspreis`
`- Lieferskonto`
`= Bareinkaufspreis`
`+ Bezugskosten (Transport, Versicherung)`
`= Einstandspreis (Bezugspreis)`

**2. Qualitativer Angebotsvergleich:**
Das billigste Angebot ist nicht zwingend das beste. Weitere entscheidende Faktoren sind:
* Qualität der Ware
* Lieferzeit und Zuverlässigkeit
* Zahlungsbedingungen (Flexibilität)
* Garantieleistungen und Kundenservice
* Nachhaltigkeit und Umweltstandards des Lieferanten

---

## 4. The Order and Order Confirmation / Bestellung und Auftragsbestätigung

## 4.1 How to Write an Order / Eine Bestellung schreiben

### [English]
[DEFINITION] An order is a binding declaration by the buyer to purchase goods. If it is based on a valid, unchanged offer, the sales contract is concluded upon dispatch/receipt of the order.
[TIP] Structure of an Order:
* **Subject Line:** State "Order" and reference the offer date/number.
* **Salutation:** Formal greeting.
* **Introduction:** Refer to the previous offer (e.g., "Thank you for your offer dated...").
* **Order Details:** Explicitly list the items (Quantity, Exact model name/description, Specifications like storage, display, color).
* **Pricing & Terms:** Confirm the individual prices, total prices, discounts, and VAT. Explicitly repeat the agreed terms of delivery and payment (e.g., "Delivery: free of charge within 14 days", "Payment: 10 days 2% cash discount, 30 days net").
* **Legal clause:** "Your terms and conditions of offer apply, there are no deviations."
* **Closing:** Request an order confirmation and sign off.

### [German]
[DEFINITION] Eine Bestellung ist die verbindliche Erklärung des Käufers, Waren kaufen zu wollen. Basiert sie auf einem gültigen, unveränderten Angebot, kommt mit der Bestellung der Kaufvertrag zustande.
[TIP] Struktur einer Bestellung:
* **Betreff:** "Bestellung" und Bezug auf das Angebotsdatum/die Angebotsnummer.
* **Anrede:** Formelle Begrüßung.
* **Einleitung:** Bezugnahme auf das vorherige Angebot (z. B. "Vielen Dank für Ihr Angebot vom... auf das wir uns hiermit beziehen.").
* **Bestelldetails:** Genaue Auflistung der Artikel (Menge, genaue Modellbezeichnung, Spezifikationen wie Speicher, Display, Farbe).
* **Preise & Konditionen:** Bestätigung der Einzel- und Gesamtpreise, Rabatte und USt. Ausdrückliche Wiederholung der Liefer- und Zahlungsbedingungen (z. B. "Lieferung: frei Haus innerhalb von 14 Tagen", "Zahlung: 10 Tage 2 % Skonto, 30 Tage netto").
* **Klausel:** "Es gelten Ihre Angebotsbedingungen, Abweichungen bestehen keine."
* **Schluss:** Bitte um eine schriftliche Auftragsbestätigung und formelle Grußformel.

## 4.2 How to Write an Order Confirmation / Eine Auftragsbestätigung schreiben

### [English]
[DEFINITION] The order confirmation (Auftragsbestätigung) is sent by the seller to confirm receipt and acceptance of the order. It is especially necessary if the order deviates from the original offer, or if the offer was non-binding (unsolicited/provisional).
[TIP] Structure of an Order Confirmation:
* **Subject Line:** "Order Confirmation" and date of the customer's order.
* **Salutation:** Formal greeting.
* **Introduction:** Thank the customer and confirm receipt (e.g., "Thank you for your order dated..., which we hereby confirm. The order has been received and will be processed as agreed.").
* **Delivery Assurance:** "We guarantee proper and timely delivery."
* **Itemized List:** Detail exactly what will be delivered (Quantity, product name, weight/size).
* **Financial Summary:** Confirm total price (gross/net) and note that conditions from the prior offer apply (including discounts).
* **Terms:** Reiterate payment and delivery terms (e.g., "Payment within 10 days with 2% discount", "Delivery within two weeks free of charge").
* **Closing:** Thank them for their trust and sign off.

### [German]
[DEFINITION] Die Auftragsbestätigung wird vom Verkäufer gesendet, um den Eingang und die Annahme der Bestellung zu bestätigen. Sie ist besonders wichtig, wenn die Bestellung vom ursprünglichen Angebot abweicht oder wenn das Angebot freibleibend (unverbindlich) war.
[TIP] Struktur einer Auftragsbestätigung:
* **Betreff:** "Auftragsbestätigung Ihrer Bestellung vom [Datum]".
* **Anrede:** Formelle Begrüßung.
* **Einleitung:** Dank und Bestätigung (z. B. "Vielen Dank für Ihre Bestellung vom..., die wir hiermit bestätigen. Der Auftrag ist bei uns eingegangen und wird wie vereinbart bearbeitet.").
* **Lieferzusage:** "Eine ordnungsgemäße und termingerechte Lieferung sichern wir Ihnen zu."
* **Artikelliste:** Genaue Auflistung der zu liefernden Artikel (Menge, Produktbezeichnung, Gewicht/Größe).
* **Finanzielle Zusammenfassung:** Gesamtpreis (brutto/netto) bestätigen und auf Angebotsbedingungen (inkl. Rabatte) hinweisen.
* **Konditionen:** Wiederholung der Zahlungs- und Lieferbedingungen (z. B. "Zahlung innerhalb von 10 Tagen mit 2 % Skonto", "Lieferung innerhalb von zwei Wochen frei Haus").
* **Schluss:** Dank für das Vertrauen und formelle Grußformel.

---

## 5. English: Worksheet "Enquiry and Offer" / Englisch: Arbeitsblatt "Anfrage und Angebot"

## 5.1 Business Vocabulary / Fachwortschatz

### [English]
[INFO] Essential English vocabulary for international trade based on the provided worksheets:

**1. Parties to the Contract:**
* **buyer:** The person/company purchasing goods.
* **seller:** The person/company offering and selling goods.

**2. Enquiry and Offer:**
* **enquiry:** A request for information (Anfrage).
* **offer:** A proposal to sell goods under specific terms (Angebot).
* **unsolicited offer:** An offer made without a prior inquiry.
* **demanded offer:** An offer made in response to an inquiry.
* **counteroffer:** A response proposing changes to the original offer.
* **unaddressed mailing:** Mass mailings not targeting a specific person (not legally binding).

**3. Terms and Conditions:**
* **terms of delivery:** Conditions detailing how goods are shipped.
* **terms of payment:** Conditions detailing how and when to pay.

**4. Conclusion of Contract and Legal Effect:**
* **conclusion of a sales contract:** When buyer and seller agree to terms.
* **binding / not binding:** Whether an offer carries a legal obligation.
* **legal binding period:** The time frame during which an offer is valid.
* **provisional offer:** A non-binding offer.

**5. Other Important Terms:**
* **stocks:** Inventory available (Vorräte).
* **Only while stocks last:** Clause limiting availability.
* **Prices are subject to change without notice:** Clause protecting seller from price fluctuations.
* **delivery time:** Time taken to ship goods.
* **consideration period:** Time given to the buyer to think about the offer.

### [German]
[INFO] Wichtiger englischer Fachwortschatz für den internationalen Handel basierend auf den bereitgestellten Arbeitsblättern:

**1. Beteiligte am Kaufvertrag:**
* **buyer:** Käufer, Abnehmer.
* **seller:** Verkäufer, Anbieter.

**2. Anfrage und Angebot:**
* **enquiry:** Anfrage.
* **offer:** Angebot.
* **unsolicited offer:** unverlangtes Angebot.
* **demanded offer:** verlangtes Angebot.
* **counteroffer:** Gegenangebot.
* **unaddressed mailing:** Postwurfsendung (nicht rechtlich bindend).

**3. Bedingungen und Inhalte:**
* **terms of delivery:** Lieferbedingungen.
* **terms of payment:** Zahlungsbedingungen.

**4. Vertragsabschluss und Rechtswirkung:**
* **conclusion of a sales contract:** Abschluss eines Kaufvertrags.
* **binding / not binding:** Verbindlich / unverbindlich.
* **legal binding period:** gesetzliche Bindungsfrist.
* **provisional offer:** freibleibendes Angebot.

**5. Sonstige wichtige Begriffe:**
* **stocks:** Vorräte, Lagerbestand.
* **Only while stocks last:** Nur solange der Vorrat reicht.
* **Prices are subject to change without notice:** Preisänderungen vorbehalten.
* **delivery time:** Lieferzeit.
* **consideration period:** Überlegungsfrist.

## 5.2 Key Concepts from the Worksheet / Schlüsselkonzepte aus dem Arbeitsblatt

### [English]
[TIP] Summary of the grammatical and logical structures used in English business correspondence (from the "Fill in the gaps" exercises):

* **The Enquiry Process:** The **buyer** asks the **seller** to make an offer. If the buyer wants to change conditions, they write a **counteroffer**. An enquiry generally concerns prices, **terms of delivery or payment**, or technical descriptions.
* **The Offer Process:** An offer is made by the **seller** and should lead to the **conclusion of a sales contract**. 
* **Binding Rules:** A **provisional offer** is not **legal/binding** to the seller. Clauses like "Only while **stocks** last" are used. Unaddressed mailings are never binding.
* **Time limits:** Under people present, there is no **consideration period**. For absent people, **double** delivery time and an appropriate consideration period are applied.

### [German]
[TIP] Zusammenfassung der logischen Strukturen, die in der englischen Handelskorrespondenz verwendet werden (aus den Lückentext-Übungen):

* **Der Anfrageprozess:** Der Käufer (**buyer**) bittet den Verkäufer (**seller**), ein Angebot zu legen. Will der Käufer Bedingungen ändern, schreibt er ein Gegenangebot (**counteroffer**). Eine Anfrage betrifft meist Preise, Liefer-/Zahlungsbedingungen (**terms of delivery or payment**) oder technische Details.
* **Der Angebotsprozess:** Ein Angebot wird vom Verkäufer (**seller**) erstellt und soll zum Abschluss eines Kaufvertrags (**conclusion of a sales contract**) führen.
* **Bindungsregeln:** Ein freibleibendes Angebot (**provisional offer**) ist für den Verkäufer nicht bindend (**legal/binding**). Hierfür werden Klauseln wie "Nur solange der Vorrat reicht" (**Only while stocks last**) genutzt. Postwurfsendungen sind nie bindend.
* **Fristen:** Unter Anwesenden gibt es keine Überlegungsfrist (**consideration period**). Unter Abwesenden gilt die doppelte (**double**) Transportzeit plus eine angemessene Überlegungsfrist.
"""

from bs4 import BeautifulSoup
import mistune

def parse_callouts(html_str):
    icons = {
        'DEFINITION': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"></path></svg>',
        'INFO': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
        'TIP': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18h6m-3 3v-3m4.3-11.4a5 5 0 1 0-8.6 0 3.8 3.8 0 0 1-1.3 4.8 2 2 0 0 0-1 1.7v1.8a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-1.8a2 2 0 0 0-1-1.7 3.8 3.8 0 0 1-1.3-4.8z"></path></svg>',
        'CLARIFICATION NEEDED': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>'
    }
    
    classes = {
        'DEFINITION': 'definition',
        'INFO': 'info',
        'TIP': 'tip',
        'CLARIFICATION NEEDED': 'info'
    }

    def replace_func(match):
        type_str = match.group(1)
        content = match.group(2)
        css_class = classes.get(type_str, 'info')
        icon = icons.get(type_str, '')
        return f'<div class="callout {css_class}">{icon}<div class="callout-content"><strong>{type_str}</strong>: {content}</div></div>'

    html_str = re.sub(r'\[(DEFINITION|INFO|TIP|CLARIFICATION NEEDED)\]\s*(.*?)(?=\n<p>|\n\[|<\/p>|$)', replace_func, html_str, flags=re.DOTALL)
    
    # Diagrams
    diagram_svg = '''
    <div class="diagram-container">
        <svg viewBox="0 0 600 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="#1e2e48" />
                </marker>
            </defs>
            <rect x="200" y="20" width="200" height="40" rx="8" fill="#1e2e48" />
            <text x="300" y="45" font-family="Open Sans" font-size="14" font-weight="bold" fill="white" text-anchor="middle">OFFER (Angebot)</text>

            <path d="M 300 60 L 300 90" stroke="#1e2e48" stroke-width="2" marker-end="url(#arrow)" />
            <path d="M 300 90 L 150 90 L 150 110" stroke="#1e2e48" stroke-width="2" marker-end="url(#arrow)" fill="none" />
            <path d="M 300 90 L 450 90 L 450 110" stroke="#1e2e48" stroke-width="2" marker-end="url(#arrow)" fill="none" />

            <rect x="50" y="110" width="200" height="40" rx="8" fill="#2980b9" />
            <text x="150" y="135" font-family="Open Sans" font-size="14" fill="white" text-anchor="middle">Initiative</text>

            <rect x="350" y="110" width="200" height="40" rx="8" fill="#fbc92d" />
            <text x="450" y="135" font-family="Open Sans" font-size="14" fill="#1e2e48" text-anchor="middle">Binding Nature</text>

            <path d="M 150 150 L 150 160 L 90 160 L 90 180" stroke="#2980b9" stroke-width="2" marker-end="url(#arrow)" fill="none" />
            <path d="M 150 150 L 150 160 L 210 160 L 210 180" stroke="#2980b9" stroke-width="2" marker-end="url(#arrow)" fill="none" />

            <rect x="30" y="180" width="120" height="40" rx="8" fill="rgba(41, 128, 185, 0.2)" stroke="#2980b9" />
            <text x="90" y="200" font-family="Open Sans" font-size="12" fill="#1e2e48" text-anchor="middle">Requested</text>
            <text x="90" y="215" font-family="Open Sans" font-size="10" fill="#1e2e48" text-anchor="middle">(Verlangt)</text>

            <rect x="150" y="180" width="120" height="40" rx="8" fill="rgba(41, 128, 185, 0.2)" stroke="#2980b9" />
            <text x="210" y="200" font-family="Open Sans" font-size="12" fill="#1e2e48" text-anchor="middle">Unsolicited</text>
            <text x="210" y="215" font-family="Open Sans" font-size="10" fill="#1e2e48" text-anchor="middle">(Unverlangt)</text>

            <path d="M 450 150 L 450 160 L 390 160 L 390 180" stroke="#fbc92d" stroke-width="2" marker-end="url(#arrow)" fill="none" />
            <path d="M 450 150 L 450 160 L 510 160 L 510 180" stroke="#fbc92d" stroke-width="2" marker-end="url(#arrow)" fill="none" />

            <rect x="330" y="180" width="120" height="40" rx="8" fill="rgba(251, 201, 45, 0.2)" stroke="#fbc92d" />
            <text x="390" y="200" font-family="Open Sans" font-size="12" fill="#1e2e48" text-anchor="middle">Binding</text>
            <text x="390" y="215" font-family="Open Sans" font-size="10" fill="#1e2e48" text-anchor="middle">(Verbindlich)</text>

            <rect x="450" y="180" width="120" height="40" rx="8" fill="rgba(251, 201, 45, 0.2)" stroke="#fbc92d" />
            <text x="510" y="200" font-family="Open Sans" font-size="12" fill="#1e2e48" text-anchor="middle">Non-binding</text>
            <text x="510" y="215" font-family="Open Sans" font-size="10" fill="#1e2e48" text-anchor="middle">(Freibleibend)</text>
        </svg>
    </div>
    '''

    html_str = re.sub(r'\[DIAGRAM SUGGESTION.*?\]', diagram_svg, html_str)
    
    return html_str

def generate():
    sections = re.split(r'\n(?=## |\n# )', markdown_content)
    
    html_output = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sales Contracts & Preparation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #1e2e48;
            --secondary: #fbc92d;
            --complementary: #dc4ebf;
            --text: #333;
            --bg: #fff;
        }
        
        body {
            font-family: 'Open Sans', sans-serif;
            color: var(--text);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: #f0f2f5;
        }

        .page {
            max-width: 1000px;
            margin: 40px auto;
            padding: 50px 60px;
            background: white;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        @media print {
            @page { size: A4; margin: 15mm; }
            body { background: white; }
            .page { margin: 0; padding: 0; width: 100%; box-shadow: none; }
            .page-break { page-break-after: always; }
            .avoid-break { page-break-inside: avoid; }
            .callout { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            
            /* Ensures no widows or orphans */
            h2, h3, h4 { page-break-after: avoid; }
            p { orphans: 3; widows: 3; }
        }

        header.brand-header {
            border-bottom: 4px solid var(--primary);
            padding-bottom: 20px;
            margin-bottom: 40px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }
        .brand-header img {
            height: 60px;
            object-fit: contain;
        }
        .brand-header .meta {
            text-align: right;
        }
        .brand-header .meta h1 {
            margin: 0 0 5px 0;
            font-size: 24px;
            color: var(--primary);
            border: none;
            padding: 0;
        }
        .brand-header .meta p {
            margin: 0;
            color: #666;
            font-size: 14px;
        }

        h1, h2, h3, h4 { 
            color: var(--primary); 
            margin-top: 1.5em; 
            margin-bottom: 0.5em;
        }
        h1 { font-size: 2.2rem; border-bottom: 3px solid var(--primary); padding-bottom: 10px; }
        h2 { font-size: 1.8rem; border-bottom: 2px solid var(--secondary); padding-bottom: 8px; }
        h3 { font-size: 1.3rem; color: var(--primary); }

        .bilingual-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-bottom: 2rem;
        }
        .bilingual-grid > div {
            min-width: 0;
        }

        /* Subsections container to avoid awkward breaks entirely */
        .subsection {
            margin-bottom: 2rem;
        }

        .callout {
            border-radius: 8px;
            padding: 16px 20px;
            margin: 16px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 12px;
            page-break-inside: avoid;
            font-size: 0.95em;
        }
        .callout svg {
            flex-shrink: 0;
            width: 24px;
            height: 24px;
        }
        .callout-content { flex-grow: 1; }
        .callout-content p { margin-top: 0; }
        .callout-content p:last-child { margin-bottom: 0; }

        .callout.definition { background-color: rgba(220, 78, 191, 0.7); color: white; }
        .callout.info { background-color: rgba(41, 128, 185, 0.7); color: white; }
        .callout.tip { background-color: rgba(251, 201, 45, 0.7); color: var(--primary); }

        ul, ol { padding-left: 20px; }
        li { margin-bottom: 8px; }
        
        .mono {
            font-family: 'Roboto Mono', monospace;
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
            color: var(--complementary);
        }
        code {
            font-family: 'Roboto Mono', monospace;
            background: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
            color: var(--complementary);
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            page-break-inside: avoid;
            font-size: 0.9em;
        }
        table th {
            background-color: var(--primary);
            color: white;
            padding: 12px;
            text-align: left;
        }
        table td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        table tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        .diagram-container {
            margin: 20px 0;
            text-align: center;
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            page-break-inside: avoid;
        }
        
        .toc {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--secondary);
            margin-bottom: 30px;
        }
        .toc ul { list-style-type: none; padding-left: 0; }
        .toc li { margin-bottom: 10px; }
        .toc a { color: var(--primary); text-decoration: none; font-weight: 600; }
        .toc a:hover { text-decoration: underline; color: var(--complementary); }
    </style>
</head>
<body>
    <div class="page">
        <header class="brand-header">
            <img src="assets/VSN_new.png" alt="VSN Logo">
            <div class="meta">
                <h1>Sales Contracts & Preparation</h1>
                <p>Curriculum Learning Material</p>
                <p>Date: 2026-04-12</p>
            </div>
        </header>

        <div class="toc">
            <h2>Table of Contents</h2>
            <ul>
                <li><a href="#sec1">1. Initiation of Sales Contracts / Anbahnung</a></li>
                <li><a href="#sec2">2. Conclusion of Sales Contracts / Abschluss</a></li>
                <li><a href="#sec3">3. Fulfillment of Sales Contracts / Erfüllung</a></li>
                <li><a href="#sec4">4. Components of a Sales Contract / Bestandteile</a></li>
                <li><a href="#sec5">5. The Inquiry / Die Anfrage</a></li>
                <li><a href="#sec6">6. The Offer / Das Angebot</a></li>
                <li><a href="#sec7">7. Comparing Offers / Angebote vergleichen</a></li>
                <li><a href="#sec8">8. The Order and Order Confirmation</a></li>
                <li><a href="#sec9">9. English Worksheet: Vocabulary & Concepts</a></li>
            </ul>
        </div>
"""
    
    current_sec_id = 0
    md = mistune.create_markdown()

    for sec in sections:
        if not sec.strip():
            continue
            
        if sec.startswith('# '):
            # Ignore main titles as we have header
            continue
            
        if sec.startswith('## '):
            current_sec_id += 1
            
            # Find the title
            title_match = re.search(r'## (.*?)\n', sec)
            if not title_match:
                continue
            title = title_match.group(1)
            
            html_output += f'\n        <div class="page-break"></div>\n'
            html_output += f'        <h2 id="sec{current_sec_id}">{title}</h2>\n'
            
            # Subsections separated by ---
            subsections = sec.split('---')
            
            for index, sub in enumerate(subsections):
                if index == 0:
                    # Remove the h2 from the first subsection
                    sub = re.sub(r'## .*?\n', '', sub, 1)
                
                # Check for bilingual translation
                if '### [English]' in sub and '### [German]' in sub:
                    # Parse out english and german blocks
                    # Often there is a pre-text, like a sub-header
                    
                    header = ""
                    header_match = re.search(r'(### \d\.\d.*?)\n', sub)
                    if header_match:
                        header = md(header_match.group(1))
                        sub = sub.replace(header_match.group(1), '')

                    eng_match = re.search(r'### \[English\]\n(.*?)(?=### \[German\])', sub, re.DOTALL)
                    ger_match = re.search(r'### \[German\]\n(.*)', sub, re.DOTALL)
                    
                    html_output += '        <div class="subsection avoid-break">\n'
                    if header:
                        html_output += f'            {header}\n'
                    
                    eng_text = eng_match.group(1).strip() if eng_match else ""
                    ger_text = ger_match.group(1).strip() if ger_match else ""
                    
                    eng_html = md(eng_text)
                    ger_html = md(ger_text)
                    
                    eng_html = parse_callouts(eng_html)
                    ger_html = parse_callouts(ger_html)
                    
                    html_output += '            <div class="bilingual-grid">\n'
                    html_output += f'                <div class="lang-col">\n{eng_html}\n                </div>\n'
                    html_output += f'                <div class="lang-col">\n{ger_html}\n                </div>\n'
                    html_output += '            </div>\n'
                    html_output += '        </div>\n'
                else:
                    # Normal block (maybe no translation)
                    html_content = md(sub.strip())
                    html_content = parse_callouts(html_content)
                    html_output += f'        <div class="subsection avoid-break">\n{html_content}\n        </div>\n'

    html_output += """
    </div>
    <script>
        // Apply monospace font to code blocks
        document.querySelectorAll('code').forEach(el => {
            el.classList.add('mono');
        });
    </script>
</body>
</html>
"""
    
    with open('sales_contracts.html', 'w', encoding='utf-8') as f:
        f.write(html_output)

if __name__ == '__main__':
    generate()
