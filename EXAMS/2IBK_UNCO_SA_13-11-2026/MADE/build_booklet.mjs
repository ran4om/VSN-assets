import fs from 'node:fs';

// Compact, student-facing visual companion to MADE/RAW.md.
const topics = [
  {
    en:'Documents, purchases and sales', de:'Belegverbuchung: Einkauf und Verkauf', img:'trading.jpg',
    enText:'A journal entry balances debit and credit. An incoming invoice creates a supplier liability; an outgoing invoice creates a customer claim. Input VAT 2500 belongs to qualifying purchases; output VAT 3500 belongs to sales.',
    deText:'Ein Buchungssatz hat gleich hohe Soll- und Habenbeträge. Eine Eingangsrechnung erzeugt eine Lieferverbindlichkeit, eine Ausgangsrechnung eine Kundenforderung. Vorsteuer 2500 steht beim berechtigten Einkauf, Umsatzsteuer 3500 beim Verkauf.',
    enTip:'Returns reverse the original entry. Immediate discounts reduce the invoice before posting; later discounts need a separate credit note.',
    deTip:'Rücksendungen kehren die ursprüngliche Buchung um. Sofortrabatte stehen schon auf der Rechnung, spätere Rabatte brauchen eine eigene Gutschrift.',
    flow:['Purchase / Einkauf','Invoice / Rechnung','Liability / Schuld','Bank payment'],
    rows:[['Goods bought on credit','5000 + 2500 / 33…'],['Goods sold on credit','20… / 4000 + 3500'],['Supplier return','33… / 5000 + 2500'],['Customer return','4000 + 3500 / 20…'],['Reminder / Mahnung','8321 + 8320 / 33…; 20… / 4890 + 8055']],
    example:'At 20 % VAT: € 1.000 net + € 200 VAT = € 1.200 gross. Purchase: 5000 1.000 + 2500 200 / 33… 1.200. Profit −1.000; cash 0.',
    extra:'Capitalisation records a fixed asset and directly attributable transport and installation. A low-value asset (GWG) up to € 1.000 may be written off immediately. Ordinary cars normally have no input VAT deduction; qualifying trucks and zero-emission cars can differ. Incoming freight raises net landed cost; outward freight is an expense. Reminder fees and default interest are posted separately.',
    extraDe:'Anlagegüter samt direkt zurechenbarem Transport und Montage aktivieren. Ein GWG bis € 1.000 kann sofort abgeschrieben werden. Beim Pkw besteht grundsätzlich kein Vorsteuerabzug; beim berechtigten Lkw und E-Auto gelten andere Regeln. Bezugskosten erhöhen den Einstandspreis; Versandkosten sind Aufwand. Buchungen und Ausnahmen stehen im Lerntext.'
  },
  {
    en:'Fixed assets and depreciation',de:'Anlagenverzeichnis und Abschreibung',img:'register.jpg',
    enText:'The fixed asset register lists acquisition cost, commissioning date, useful life, depreciation and book value. Straight-line depreciation allocates cost evenly over useful life.',
    deText:'Das Anlagenverzeichnis enthält Anschaffungswert, Inbetriebnahme, Nutzungsdauer, Abschreibung und Buchwert. Die lineare AfA verteilt die Kosten gleichmäßig auf die Nutzungsdauer.',
    enTip:'The supplied worksheet also shows a monthly method. Follow the method specified in the exercise; do not mix schedules.',
    deTip:'Das AVZ-Blatt zeigt auch eine Monatsmethode. Verwende die in der Aufgabe verlangte Methode und vermische die Zeitpläne nicht.',
    flow:['Cost / Wert','Register / AVZ','AfA expense','Book value'],
    rows:[['Annual rate / Satz','100 % ÷ useful life / Nutzungsdauer'],['Annual AfA','acquisition cost ÷ useful life'],['Book value / Buchwert','opening value + additions − AfA'],['Closing entry','7010 / relevant asset account']],
    example:'€ 1.200 ÷ 10 years = € 120 annual AfA. Commissioned in October: tax half-year AfA € 60; closing book value € 1.140. 7010 60 / 0620 60. Profit −60; cash 0.',
    extra:'Tax half-year rule: full annual AfA for commissioning in the first half, half in the second. A € 1 memory value is used while the asset remains in use where the exercise specifies it.',
    extraDe:'Steuerliche Halbjahresregel: volle Jahres-AfA bei Inbetriebnahme im ersten Halbjahr, halbe im zweiten. Einen Erinnerungswert von € 1 belassen, wenn die Aufgabe diese Konvention vorgibt.'
  },
  {
    en:'Bank closing items',de:'Abschlussposten am Bankkonto',img:'interest.jpg',
    enText:'Credit interest is revenue. Debit interest and bank fees are expenses. In the textbook examples for sole proprietors, capital income tax is a private withdrawal, not an expense.',
    deText:'Habenzinsen sind Ertrag. Sollzinsen und Bankspesen sind Aufwand. Die KESt ist in den Buchbeispielen für Einzelunternehmen eine Privatentnahme und kein Aufwand.',
    enTip:'Post gross interest and tax separately. An overdraft becoming larger is a negative cash effect.',deTip:'Bruttozinsen und KESt getrennt buchen. Eine steigende Kontoüberziehung wirkt negativ auf die Liquidität.',
    flow:['Bank statement','Gross interest','Tax / KESt','Bank balance'],
    rows:[['Credit interest / Habenzinsen','2800 / 8050'],['Debit interest / Sollzinsen','8310 / 2800'],['Charges / Spesen','7790 / 2800'],['Private KESt','9600 / 2800']],
    example:'Ü 2.3: interest € 12,32; KESt € 3,08; fees € 238,12. 2804 / 8050 12,32; 9600 / 2804 3,08; 7790 / 2804 238,12.',
    extra:'Profit: +12,32 −238,12. Cash: +12,32 −3,08 −238,12. KESt also reduces equity as a private withdrawal.',
    extraDe:'Erfolg: +12,32 −238,12. Liquidität: +12,32 −3,08 −238,12. Die KESt vermindert als Privatentnahme auch das Eigenkapital.'
  },
  {
    en:'Cash transfers with banks',de:'Barverkehr mit Banken',img:'bank.jpg',
    enText:'Cash in transit with banks uses account 2870 to bridge the cash voucher and bank statement. The completed transfer changes the location of cash, not total cash plus bank or profit.',
    deText:'Das Konto 2870 überbrückt Kassenbeleg und Kontoauszug. Die vollständige Umbuchung ändert den Ort des Geldes, aber weder Kassa plus Bank noch den Erfolg.',
    enTip:'Use both legs exactly once. After both documents are recorded, account 2870 clears.',deTip:'Beide Belege genau einmal buchen. Danach ist das Konto 2870 ausgeglichen.',
    flow:['Cash / Kassa','Transit / 2870','Bank / 2800','2870 clears'],
    rows:[['Withdrawal: cash voucher','2700 / 2870'],['Withdrawal: bank statement','2870 / 2800'],['Deposit: cash voucher','2870 / 2700'],['Deposit: bank statement','2800 / 2870']],
    example:'Withdraw € 1.500: 2700 1.500 / 2870 1.500, then 2870 1.500 / 2800 1.500. Combined cash effect 0; profit 0.',
    extra:'Before the second leg arrives, the individual voucher temporarily changes cash plus bank; 2870 carries the amount in transit.',
    extraDe:'Vor der zweiten Buchung verändert der einzelne Beleg Kassa plus Bank vorübergehend. 2870 hält den Zwischenbetrag.'
  },
  {
    en:'Card sales and settlements',de:'Debit- und Kreditkartenabrechnung',img:'cards.jpg',
    enText:'A card sale first creates a gross claim against the processor. Account 2885 is used for debit-card claims and 2880 for credit-card claims. Bank settlement clears the claim.',
    deText:'Ein Kartenverkauf erzeugt zuerst eine Bruttoforderung gegenüber dem Kartenunternehmen. 2885 erfasst Debitkarten-, 2880 Kreditkartenforderungen. Die Bankabrechnung gleicht sie aus.',
    enTip:'A withheld fee is an expense; deductible VAT on that fee is not. Do not post the sale a second time.',deTip:'Eine einbehaltene Nettogebühr ist Aufwand; abzugsfähige Vorsteuer darauf nicht. Den Verkauf nicht ein zweites Mal buchen.',
    flow:['Sale / Verkauf','Claim / Forderung','Fee / Gebühr','Bank receipt'],
    rows:[['Sale / Verkauf','2880 or 2885 / 4000 + 3500'],['Debit-card settlement','2800 / 2885'],['Credit-card settlement','2800 + 7792 + 2500 / 2880'],['Buyer: card liability','3180 credit; 3190 debit']],
    example:'Ü 1.20: claim € 8.320; fee € 208 + € 3,90; VAT € 42,38. Bank receives € 8.065,72. 2800 8.065,72 + 7792 211,90 + 2500 42,38 / 2880 8.320.',
    extra:'The original credit-card sale date and its VAT split are not given in this exercise. The € 8.320 claim is assumed to have been recorded already.',
    extraDe:'Datum und USt-Aufteilung des ursprünglichen Kreditkartenverkaufs sind nicht angegeben. Die Forderung von € 8.320 ist bereits verbucht.'
  },
  {
    en:'Taxes and chamber levy',de:'Steuern und Kammerumlage KU1',img:'tax.jpg',
    enText:'Classify the tax first. Business property tax is an expense; an owner’s income tax is private. Paying an existing VAT liability has no new profit effect. Chamber levy 1 finances the chamber.',
    deText:'Bestimme zuerst die Abgabe. Betriebliche Grundsteuer ist Aufwand, Einkommensteuer des Inhabers privat. Die Zahlung einer bestehenden USt-Zahllast ändert den Erfolg nicht erneut.',
    enTip:'The book uses 3 ‰ and a € 150.000 turnover exemption in its KU1 teaching model. Real rules include exceptions and graduated rates.',deTip:'Das Buchmodell verwendet 3 ‰ und eine Umsatzfreigrenze von € 150.000. In der Praxis gelten Ausnahmen und Tarifstufen.',
    flow:['Tax / Abgabe','Classify / Art','Entry / Buchung','Payment'],
    rows:[['Business property tax','7100 / 2800'],['Owner income tax','9600 / 2800'],['VAT liability','3520 / 2800'],['KU1 quarter 4','7780 / 3540; then 3540 / 2800']],
    example:'Ü 2.6: year-end KU1 € 420: 7780 420 / 3540 420. Next February: 3540 420 / 2800 420. Profit −420, then 0; cash 0, then −420.',
    extra:'A tax directly attributable to acquiring undeveloped land increases its asset cost. KU1 is calculated quarterly on the defined assessment base.',
    extraDe:'Eine direkt zurechenbare Grunderwerbsteuer erhöht den Anschaffungswert des unbebauten Grundstücks. KU1 wird vierteljährlich auf die definierte Grundlage berechnet.'
  },
  {
    en:'Cash discount',de:'Zahlung mit Skontoabzug',img:'discount.jpg',
    enText:'Cash discount rewards payment within the agreed period. Calculate the discount from the eligible gross amount, split it into net discount and VAT correction, then clear the personal account.',
    deText:'Skonto ist ein Nachlass für rasche Zahlung. Berechne es vom skontofähigen Bruttobetrag, trenne Nettoskonto und Steuerkorrektur und gleiche das Personenkonto aus.',
    enTip:'The test requires two entries: payment and discount. The payment plus gross discount equals the original claim or liability.',deTip:'Für die Schularbeit zwei Buchungssätze bilden: Zahlung und Skonto. Zahlung plus Bruttoskonto ergibt den ursprünglichen offenen Betrag.',
    flow:['Gross invoice','Discount %','Net + VAT','Payment'],
    rows:[['Supplier payment','33… / 2800'],['Supplier discount','33… / 5880 + 2500'],['Customer payment','2800 / 20…'],['Customer discount','4410 + 3500 / 20…']],
    example:'Supplier: € 8.400 × 3 % = € 252 gross = € 210 net + € 42 VAT. Pay € 8.148. 33… 8.148 / 2800 8.148; 33… 252 / 5880 210 + 2500 42.',
    extra:'Customer example: € 4.680 × 2 % = € 93,60 gross = € 78 net + € 15,60 VAT. Bank receives € 4.586,40; the discount reduces profit by € 78.',
    extraDe:'Kundenbeispiel: € 4.680 × 2 % = € 93,60 brutto = € 78 netto + € 15,60 USt. Die Bank erhält € 4.586,40; das Skonto senkt den Erfolg um € 78.'
  },
  {
    en:'Profit and liquidity',de:'Erfolg und Liquidität',img:'profit.jpg',
    enText:'Profit changes through revenue and expense. Liquidity here tracks cash plus bank, including bank overdrafts. A claim or liability alone is not cash.',
    deText:'Der Erfolg ändert sich durch Ertrag und Aufwand. Liquidität meint hier Kassa plus Bank einschließlich Überziehung. Eine Forderung oder Schuld allein ist kein Zahlungsmittel.',
    enTip:'Ask two questions for every entry: is there revenue or expense? Does cash or the bank balance change?',deTip:'Stelle bei jedem Buchungssatz zwei Fragen: Entsteht Ertrag oder Aufwand? Ändert sich Kassa oder Bank?',
    flow:['Document','Revenue / expense','Cash / bank','Two effects'],
    rows:[['Credit purchase / Einkauf auf Ziel','profit −net; cash 0'],['Later supplier payment','profit 0; cash −gross'],['Depreciation / AfA','profit −AfA; cash 0'],['Customer payment','profit 0; cash +gross'],['Private tax / Privatsteuer','profit 0; cash decreases']],
    example:'Buy goods on credit for € 1.000 + € 200 VAT: profit −€ 1.000, cash 0. Pay later: profit 0, cash −€ 1.200.',
    extra:'Private withdrawals reduce equity even though they do not reduce profit. Deductible input VAT and output VAT normally have no profit effect.',
    extraDe:'Privatentnahmen senken das Eigenkapital, aber nicht den Erfolg. Abzugsfähige Vorsteuer und Umsatzsteuer wirken normalerweise nicht auf den Erfolg.'
  }
];

const examplesDe = [
 'Bei 20 % USt: € 1.000 netto + € 200 USt = € 1.200 brutto. Einkauf: 5000 1.000 + 2500 200 / 33… 1.200. Erfolg −1.000; Liquidität 0.',
 '€ 1.200 ÷ 10 Jahre = € 120 Jahres-AfA. Inbetriebnahme im Oktober: steuerliche Halbjahres-AfA € 60; Buchwert € 1.140. 7010 60 / 0620 60. Erfolg −60; Liquidität 0.',
 'Ü 2.3: Habenzinsen € 12,32; KESt € 3,08; Spesen € 238,12. Buchungen: 2804 / 8050 12,32; 9600 / 2804 3,08; 7790 / 2804 238,12.',
 'Abhebung € 1.500: 2700 1.500 / 2870 1.500, danach 2870 1.500 / 2800 1.500. Insgesamt Liquiditätswirkung 0 und Erfolgswirkung 0.',
 'Ü 1.20: Forderung € 8.320; Gebühr € 208 + € 3,90; USt € 42,38. Bankeingang € 8.065,72. Buchung: 2800 8.065,72 + 7792 211,90 + 2500 42,38 / 2880 8.320.',
 'Ü 2.6: KU1 € 420 am Jahresende: 7780 420 / 3540 420. Im Februar: 3540 420 / 2800 420. Erfolg −420, danach 0; Liquidität 0, danach −420.',
 'Lieferant: € 8.400 × 3 % = € 252 brutto = € 210 netto + € 42 Vorsteuer. Zahlung € 8.148. Buchungen: 33… 8.148 / 2800 8.148; 33… 252 / 5880 210 + 2500 42.',
 'Wareneinkauf auf Ziel um € 1.000 + € 200 USt: Erfolg −€ 1.000, Liquidität 0. Spätere Zahlung: Erfolg 0, Liquidität −€ 1.200.'
];

const esc = s => String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const template = fs.readFileSync('/home/kiarad/VSN-internal/skills/vsn-study-set/assets/template.html','utf8');
const head = template.slice(0, template.indexOf('<body>')).replaceAll('{{TITLE}}','Accounting').replaceAll('{{SUBJECT}}','UNCO').replaceAll('{{CLASS}}','2IBK').replaceAll('{{TYPE}}','SA').replaceAll('{{DATE}}','13.11.2026').replaceAll('{{SUBJECT_DE}}','UNCO').replaceAll('{{TITLE_DE}}','Beschaffung, Absatz und Anlagen');
const cover = `<div class="cover page-break"><div class="cover-bg-pattern"></div><div class="cover-content"><div class="cover-header"><img class="cover-logo" src="assets/VSN_new.png" alt="VSN"><span class="cover-badge">2IBK · SA · 13.11.2026</span></div><div class="cover-main"><div class="cover-label">UNCO · ACCOUNTING</div><div class="cover-title">Beschaffung,<br>Absatz und Anlagen</div><div class="cover-title-de">Purchases, sales and fixed assets</div><div class="cover-divider"></div><div class="cover-meta"><div class="cover-meta-item">8 Kapitel · 8 chapters</div><div class="cover-meta-item">Buchungen · AVZ · Bank · Skonto</div><div class="cover-meta-item">Deutsch / English</div></div></div><div class="cover-footer"><span class="cover-footer-text">VSN Lernunterlage © 2026</span><span class="cover-footer-text">2IBK · UNCO</span></div></div><div class="cover-accent-bar"></div></div>`;
const toc = `<div class="toc-page page-break"><div class="toc-header"><h2>Inhaltsverzeichnis · Table of contents</h2><h1>Übersicht der Kapitel</h1></div><ul class="toc-list">${topics.map((t,i)=>`<li class="toc-item no-break"><span class="toc-num">${i+1}</span><div class="toc-content"><div class="toc-title-en">${esc(t.en)}</div><div class="toc-title-de">${esc(t.de)}</div></div></li>`).join('')}</ul></div>`;
function flow(labels) { return `<div class="diagram-wrap" style="margin:2px 0"><svg viewBox="0 0 680 75" style="width:100%;max-width:680px;height:auto" role="img" aria-label="${esc(labels.join(' → '))}">${labels.map((x,i)=>`<rect x="${i*170+2}" y="12" width="145" height="42" rx="8" fill="${['#1e2e48','#2980b9','#dc4ebf','#1e2e48'][i]}"/><text x="${i*170+74}" y="38" text-anchor="middle" font-size="12" font-family="sans-serif" fill="white">${esc(x)}</text>${i<3?`<path d="M${i*170+150} 33 h14 m-5 -5 5 5 -5 5" stroke="#d4a800" stroke-width="3" fill="none"/>`:''}`).join('')}</svg></div>`; }
function col(lang, text, tip, extra) {return `<div class="col-${lang}"><div class="col-label" style="margin-bottom:2px"><span class="col-label-dot"></span>${lang==='en'?'English':'Deutsch'}</div><div class="callout-box callout-def" style="padding:7px 10px;margin:5px 0"><div class="callout-content"><div class="callout-label">${lang==='en'?'Key idea':'Grundidee'}</div><div class="callout-text">${esc(text)}</div></div></div>${extra.split(/(?<=[.!?])\s+/).map(s=>`<p style="font-size:.9em;line-height:1.4">${esc(s)}</p>`).join('')}<div class="callout-box callout-tip" style="padding:7px 10px;margin:5px 0"><div class="callout-content"><div class="callout-label">${lang==='en'?'Exam tip':'Prüfungstipp'}</div><div class="callout-text">${esc(tip)}</div></div></div></div>`;}
const exampleBlock = i => `<div class="example-block no-break" style="margin:4px 0;padding:6px 10px"><strong>Worked example · Beispiel</strong><br>${esc(topics[i].example)}<br>${esc(examplesDe[i])}</div>`;
const supplementary = `<div style="break-before:page;padding-top:4mm"><div class="section-header" style="margin-bottom:5px;padding-bottom:5px"><div class="section-num">1</div><div class="section-title-block"><div class="section-title-en">Assets, freight and corrections</div><div class="section-title-de">Anlagen, Fracht und Korrekturen</div></div></div><figure style="margin:2px 0"><img src="assets/assets.jpg" alt="Office assets and a calculator" style="max-height:40mm;box-shadow:none"></figure>${flow(['Purchase price','+ Freight','+ Installation','Asset cost'])}<div class="bilingual-grid">${col('en','Capitalise directly attributable acquisition costs on the asset account. Deductible VAT is separate; a normal car without input VAT deduction is recorded gross.','A return or later discount corrects the original entry and VAT.','A qualifying GWG may be expensed immediately. Inward freight on goods belongs in landed cost; outward freight is a selling expense.')}${col('de','Direkt zurechenbare Anschaffungsnebenkosten auf dem Anlagenkonto aktivieren. Abzugsfähige Vorsteuer wird gesondert gebucht; ein Pkw ohne Vorsteuerabzug wird brutto aktiviert.','Eine Rücksendung oder ein späterer Rabatt korrigiert ursprüngliche Buchung und Steuer.','Ein berechtigtes GWG kann sofort Aufwand sein. Warenbezugskosten gehören zum Einstandspreis; Versandkosten sind Vertriebsaufwand.')}</div><div class="table-wrap" style="margin:5px 0"><table class="vsn-table"><thead><tr><th>Situation · Geschäftsfall</th><th>Entry · Buchung</th></tr></thead><tbody>${[['GWG, immediate / sofort','7060 + 2500 / 33…'],['Car without input VAT / Pkw','0630 gross / 33…'],['Truck with input VAT / Lkw','0640 + 2500 / 33…'],['Goods freight / Bezugskosten','5000 + 2500 / 33…'],['Outward freight / Ausgangsfracht','7300 + 2500 / 33…'],['Customer reminder / Mahnung','20… / 4890 + 8055']].map(row=>`<tr><td style="padding:3px 8px">${esc(row[0])}</td><td style="padding:3px 8px"><code>${esc(row[1])}</code></td></tr>`).join('')}</tbody></table></div><div class="example-block"><strong>Landed cost · Einstandspreis</strong><br>Goods / Waren € 9.875 + freight / Bezugskosten € 153,09 = landed cost / Einstandspreis € 10.028,09 net. Deductible VAT is separate / Vorsteuer ist gesondert.</div>${exampleBlock(0)}</div>`;
const sections=topics.map((t,i)=>`<div class="section page-break" style="padding-top:4mm;padding-bottom:0" id="s${i+1}"><div class="section-header no-break" style="margin-bottom:5px;padding-bottom:5px"><div class="section-num">${i+1}</div><div class="section-title-block"><div class="section-title-en">${esc(t.en)}</div><div class="section-title-de">${esc(t.de)}</div></div></div><figure style="margin:2px 0"><img src="assets/${t.img}" alt="${esc(t.en)}" style="max-height:40mm;box-shadow:none"></figure>${flow(t.flow)}<div class="bilingual-grid">${col('en',t.enText,t.enTip,t.extra)}${col('de',t.deText,t.deTip,t.extraDe)}</div><div class="table-wrap no-break" style="margin:5px 0"><table class="vsn-table"><thead><tr><th style="padding:4px 8px">Event · Geschäftsfall</th><th style="padding:4px 8px">Entry · Buchung</th></tr></thead><tbody>${t.rows.map(row=>`<tr><td style="padding:3px 8px">${esc(row[0])}</td><td style="padding:3px 8px"><code>${esc(row[1])}</code></td></tr>`).join('')}</tbody></table></div>${i===0?supplementary:exampleBlock(i)}</div>`).join('');
fs.writeFileSync(new URL('./unco_accounting.html',import.meta.url),head+'<body>'+cover+toc+sections+'</body></html>');
