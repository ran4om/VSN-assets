```markdown
# Excel Skills for Business Informatics (Wirtschaftsinformatik)

### [English]
This material covers essential Excel skills relevant to business informatics, focusing on data manipulation, analysis, and presentation. It is designed for high school level (Gymnasium Oberstufe).

### [German]
Dieses Material behandelt grundlegende Excel-Fertigkeiten, die für die Wirtschaftsinformatik relevant sind, mit Schwerpunkt auf Datenbearbeitung, -analyse und -präsentation. Es ist für die Oberstufe des Gymnasiums konzipiert.

## 1. Excel Basics

### [English]
### 1.1. Basic Calculations
[INFO] Excel allows for various mathematical operations directly in cells using formulas.
*   **Addition:** `=` A1+B1
*   **Subtraction:** `=` A1-B1
*   **Multiplication:** `=` A1*B1
*   **Division:** `=` A1/B1

### [German]
### 1.1. Grundlegende Berechnungen
[INFO] Excel ermöglicht verschiedene mathematische Operationen direkt in Zellen mithilfe von Formeln.
*   **Addition:** `=` A1+B1
*   **Subtraktion:** `=` A1-B1
*   **Multiplikation:** `=` A1*B1
*   **Division:** `=` A1/B1

### [English]
### 1.2. Cell References
[DEFINITION] A cell reference indicates the location of a cell or a range of cells in a worksheet.
*   **Relative Reference:** Changes when a formula is copied to another cell (e.g., A1).
*   **Absolute Reference:** Stays constant when a formula is copied (e.g., $A$1).
    *   [TIP] To make a reference absolute, press `F4` after typing the cell reference.
*   **Mixed Reference:** Either the row or the column is absolute (e.g., $A1$ or $A$1).

### [German]
### 1.2. Zellbezüge
[DEFINITION] Ein Zellbezug gibt den Speicherort einer Zelle oder eines Zellbereichs in einem Arbeitsblatt an.
*   **Relativer Bezug:** Ändert sich, wenn eine Formel in eine andere Zelle kopiert wird (z.B. A1).
*   **Absoluter Bezug:** Bleibt konstant, wenn eine Formel kopiert wird (z.B. $A$1).
    *   [TIP] Um einen Bezug absolut zu machen, drücken Sie `F4` nach Eingabe des Zellbezugs.
*   **Gemischter Bezug:** Entweder die Zeile oder die Spalte ist absolut (z.B. $A1$ oder $A$1$).

### [English]
### 1.3. Working with Files
[INFO] The materials provided indicate that "all files are on Teams" and there is a "PowerPoint for Excel examples from the book." This implies that Excel is often used in conjunction with other Microsoft Office applications and cloud platforms for file management and sharing.

### [German]
### 1.3. Arbeiten mit Dateien
[INFO] Die bereitgestellten Materialien weisen darauf hin, dass "alle Dateien auf Teams" sind und es eine "PowerPoint zu Excel-Beispielen aus dem Buch" gibt. Dies impliziert, dass Excel oft in Verbindung mit anderen Microsoft Office-Anwendungen und Cloud-Plattformen für die Dateiverwaltung und -freigabe verwendet wird.

## 2. Data Organization and Analysis

### [English]
### 2.1. Filtering Data
[DEFINITION] Filtering allows you to display only the rows that meet specific criteria, temporarily hiding the other rows.
*   **Activating Filters:** Select your data range and go to `Data > Filter`.
*   **Table Filters:** Basic filters that appear as dropdown arrows in the header of each column.
*   **Number Filters:** Special filters for numerical data, allowing criteria like "greater than," "less than," "between," etc.
    *   **Example Tasks:**
        *   Display only female employees earning more than €40,000 annually.
        *   Filter vehicles by "previous owner" and then by "list price."
        *   Show "AHS" branch data.
        *   Show "Private" owner data.
        *   Filter numbers less than 20,000.
        *   Find models sold in Germany AND Italy (requires filtering multiple columns).
        *   Find employees in the "Sekretariat" department that are male (then use `COUNTA` to count them).
        *   Filter employees in "Logistik, Marketing, Vertrieb" earning >€40,000 per year.
        *   Filter employees with an annual salary >€40,000 OR <€30,000.

### [German]
### 2.1. Filtern von Daten
[DEFINITION] Filtern ermöglicht es Ihnen, nur die Zeilen anzuzeigen, die bestimmte Kriterien erfüllen, während die anderen Zeilen vorübergehend ausgeblendet werden.
*   **Filter aktivieren:** Wählen Sie Ihren Datenbereich aus und gehen Sie zu `Daten > Filter`.
*   **Tabellenfilter:** Grundlegende Filter, die als Dropdown-Pfeile in der Kopfzeile jeder Spalte erscheinen.
*   **Zahlenfilter:** Spezielle Filter für numerische Daten, die Kriterien wie "größer als", "kleiner als", "zwischen" usw. zulassen.
    *   **Beispielaufgaben:**
        *   Nur weibliche Mitarbeiter anzeigen, die jährlich mehr als 40.000 € verdienen.
        *   Autos nach "Vorbesitzer" und anschließend nach "Listenpreis" filtern.
        *   Daten der Filiale "AHS" anzeigen.
        *   Daten von "Privat"-Besitzern anzeigen.
        *   Zahlen filtern, die kleiner als 20.000 sind.
        *   Modelle finden, die in Deutschland UND Italien verkauft wurden (erfordert Filtern mehrerer Spalten).
        *   Männliche Mitarbeiter in der Abteilung "Sekretariat" finden (anschließend mit `ANZAHL2` zählen).
        *   Mitarbeiter der Abteilung "Logistik, Marketing, Vertrieb" filtern, die mehr als 40.000 € pro Jahr verdienen.
        *   Mitarbeiter mit einem Jahresgehalt >40.000 € ODER <30.000 € filtern.

### [English]
### 2.2. Sorting Data
[DEFINITION] Sorting arranges data in a specified order (e.g., alphabetical, numerical, chronological).
*   **Single-level Sort:** Sorts by one column.
*   **Multi-level Sort:** Sorts by multiple columns, defining primary, secondary, and tertiary sort keys.
    *   **Example Tasks:**
        *   Sort cars by "previous owner" and then by "list price."
        *   Sort employees alphabetically by last name.
        *   Sort employees by age (youngest first).
        *   Sort employees by highest annual salary.

### [German]
### 2.2. Sortieren von Daten
[DEFINITION] Sortieren ordnet Daten in einer bestimmten Reihenfolge an (z.B. alphabetisch, numerisch, chronologisch).
*   **Einfache Sortierung:** Sortiert nach einer Spalte.
*   **Mehrstufige Sortierung:** Sortiert nach mehreren Spalten, wobei primäre, sekundäre und tertiäre Sortierschlüssel definiert werden.
    *   **Beispielaufgaben:**
        *   Autos nach "Vorbesitzer" und anschließend nach "Listenpreis" sortieren.
        *   Mitarbeiter alphabetisch nach Nachnamen sortieren.
        *   Mitarbeiter nach dem Alter sortieren (jüngste zuerst).
        *   Mitarbeiter nach dem höchsten Jahresgehalt sortieren.

### [English]
### 2.3. Subtotals (`TEILERGEBNIS`)
[DEFINITION] The `TEILERGEBNIS` (SUBTOTAL) function returns a subtotal in a list or database. It can perform different types of calculations (e.g., SUM, COUNT, AVERAGE) and ignores rows hidden by a filter.
*   **Syntax:** `=TEILERGEBNIS(Funktionsnummer; Bereich)`
    *   `Funktionsnummer`: Specifies the type of aggregation (e.g., 9 for SUM, 2 for COUNT).
    *   `Bereich`: The range of cells to subtotal.
*   **Example Task:** Calculate a subtotal of sales or counts (`TEILERGEBNIS(SUMME; Umsatz)/TEILERGEBNIS(ANZAHL; Anzahl)`).

### [German]
### 2.3. Teilergebnisse (`TEILERGEBNIS`)
[DEFINITION] Die Funktion `TEILERGEBNIS` liefert ein Teilergebnis in einer Liste oder Datenbank. Sie kann verschiedene Arten von Berechnungen durchführen (z.B. SUMME, ANZAHL, MITTELWERT) und ignoriert Zeilen, die durch einen Filter ausgeblendet wurden.
*   **Syntax:** `=TEILERGEBNIS(Funktionsnummer; Bereich)`
    *   `Funktionsnummer`: Gibt die Art der Aggregation an (z.B. 9 für SUMME, 2 für ANZAHL).
    *   `Bereich`: Der Zellbereich, für den das Teilergebnis berechnet werden soll.
*   **Beispielaufgabe:** Ein Teilergebnis von Umsatz oder Anzahl berechnen (`TEILERGEBNIS(SUMME; Umsatz)/TEILERGEBNIS(ANZAHL; Anzahl)`).

## 3. Data Formatting

### [English]
### 3.1. Custom Number Formats
[DEFINITION] Custom number formats allow you to display numbers in a specific way without changing their underlying value. They are defined by up to four sections, separated by semicolons, for positive numbers, negative numbers, zero values, and text.
*   **Syntax Structure:** `[Positive];[Negative];[Zero];[Text]`
    *   `#`: Placeholder for significant digits, does not display insignificant zeros.
    *   `0`: Placeholder for digits, displays insignificant zeros if needed.
    *   `@`: Placeholder for text input.
    *   `[Color]`: Specifies font color (e.g., `[Red]`).
    *   `"Text"`: Displays custom text.
*   **Key Concepts:**
    *   Text appended to numbers should be enclosed in double quotes (e.g., `" Stück"`).
    *   Single characters or symbols (like `m²`) typically do not require quotes unless they contain spaces or are multi-character words.
    *   Custom formats only change display, not value, so calculations still work.
    *   [DIAGRAM SUGGESTION: A diagram illustrating the four sections of custom number formats with examples.]
*   **Example Applications:**
    *   `80 m²`: Format `0" m²"`
    *   `27881 EUR`: Format `"EUR "Standard` or `0,00" EUR"`
    *   `1,75% p.a.`: Format `0,00" % p.a."`
    *   `1.250 Liter`: Format `0" Liter"`
    *   `1,1 Mio.`: Format `0,0" Mio."`
    *   Numbers with 8 digits (leading zeros): Format `00000000` (e.g., `00012369` for `12369`)
    *   Currency with decimals: Format `#.##0,00 €`
    *   Negative numbers in red: `[Blue]#.##0,00;[Red]-#.##0,00;"" ;[Green]@` (as shown in material).

### [German]
### 3.1. Benutzerdefinierte Zahlenformate
[DEFINITION] Benutzerdefinierte Zahlenformate ermöglichen es Ihnen, Zahlen auf eine bestimmte Weise anzuzeigen, ohne deren zugrunde liegenden Wert zu ändern. Sie werden durch bis zu vier Abschnitte definiert, die durch Semikolons getrennt sind, für positive Zahlen, negative Zahlen, Nullwerte und Text.
*   **Syntax-Struktur:** `[Positiv];[Negativ];[Null];[Text]`
    *   `#`: Platzhalter für signifikante Ziffern, zeigt keine unwesentlichen Nullen an.
    *   `0`: Platzhalter für Ziffern, zeigt unwesentliche Nullen bei Bedarf an.
    *   `@`: Platzhalter für Texteingaben.
    *   `[Farbe]`: Gibt die Schriftfarbe an (z.B. `[Rot]`).
    *   `"Text"`: Zeigt benutzerdefinierten Text an.
*   **Schlüsselkonzepte:**
    *   Text, der an Zahlen angehängt wird, sollte in doppelten Anführungszeichen stehen (z.B. `" Stück"`).
    *   Einzelne Zeichen oder Symbole (wie `m²`) benötigen normalerweise keine Anführungszeichen, es sei denn, sie enthalten Leerzeichen oder sind mehrteilige Wörter.
    *   Benutzerdefinierte Formate ändern nur die Anzeige, nicht den Wert, sodass Berechnungen weiterhin funktionieren.
    *   [DIAGRAMM VORSCHLAG: Ein Diagramm, das die vier Abschnitte benutzerdefinierter Zahlenformate mit Beispielen illustriert.]
*   **Beispielanwendungen:**
    *   `80 m²`: Format `0" m²"`
    *   `27881 EUR`: Format `"EUR "Standard` oder `0,00" EUR"`
    *   `1,75% p.a.`: Format `0,00" % p.a."`
    *   `1.250 Liter`: Format `0" Liter"`
    *   `1,1 Mio.`: Format `0,0" Mio."`
    *   Zahlen mit 8 Stellen (führende Nullen): Format `00000000` (z.B. `00012369` für `12369`)
    *   Währung mit Dezimalstellen: Format `#.##0,00 €`
    *   Negative Zahlen in Rot: `[Blau]#.##0,00;[Rot]-#.##0,00;"" ;[Grün]@` (wie im Material gezeigt).

### [English]
### 3.2. Conditional Formatting
[DEFINITION] Conditional formatting automatically applies formatting (like colors, icon sets, data bars) to cells based on their values.
*   **Creating Rules:** Go to `Home > Conditional Formatting > New Rule`.
*   **Rule Types:**
    *   Highlight Cells Rules (e.g., Greater Than, Less Than, Text that Contains)
    *   Top/Bottom Rules (e.g., Top 10 Items, Bottom 10%)
    *   Data Bars, Color Scales, Icon Sets
    *   `Use a formula to determine which cells to format` (most flexible).
        *   [TIP] When using a formula for an entire row, ensure the column reference is absolute (e.g., `$B2`) while the row reference is relative.
*   **Example Applications:**
    *   **Stock Levels (Fressnapf):**
        *   If stock < 100 kg, highlight cell with light red fill (signals reorder need).
        *   If initial stock > 200 kg, display font in blue.
    *   **Order Quantities (H2O):**
        *   Unprofitable orders (< 35,000 bottles): Highlight with light red fill.
        *   Critical orders (between 35,000 and 60,000 bottles): Highlight with yellow fill.
        *   Optimal orders (> 60,000 bottles): Apply a green checkmark icon.
        *   Orders between 20,000 and 35,000 bottles (for specific analysis).
    *   **Inn Stock Management (Gasthof Bieriger Bär):**
        *   If Beer barrels <= 5, display font in red.
        *   If Wine bottles < 20, display font in red.
        *   If Wine bottles == 20, display font in violet.
        *   If Cola bottles <= 10, display font in red.
    *   **Conditional Time-based Formatting:** Format entire row if a phone call was made after 18:00 (e.g., `=$B2>ZEIT(18;0;0)`).

### [German]
### 3.2. Bedingte Formatierung
[DEFINITION] Die bedingte Formatierung wendet automatisch Formatierungen (wie Farben, Symbolsätze, Datenbalken) auf Zellen basierend auf deren Werten an.
*   **Regeln erstellen:** Gehen Sie zu `Start > Bedingte Formatierung > Neue Regel`.
*   **Regeltypen:**
    *   Regeln zum Hervorheben von Zellen (z.B. Größer als, Kleiner als, Text enthält)
    *   Regeln für obere/untere Werte (z.B. Obere 10 Elemente, Untere 10 %)
    *   Datenbalken, Farbskalen, Symbolsätze
    *   `Formel zur Ermittlung der zu formatierenden Zellen verwenden` (am flexibelsten).
        *   [TIP] Bei Verwendung einer Formel für eine ganze Zeile muss der Spaltenbezug absolut (z.B. `$B2`) sein, während der Zeilenbezug relativ bleibt.
*   **Beispielanwendungen:**
    *   **Lagerbestände (Fressnapf):**
        *   Wenn Lagerbestand < 100 kg, Zelle hellrot hervorheben (signalisiert Bestellbedarf).
        *   Wenn Anfangsbestand > 200 kg, Schrift blau darstellen.
    *   **Bestellmengen (H2O):**
        *   Unrentable Bestellungen (< 35.000 Flaschen): Hellrot hervorheben.
        *   Kritische Bestellungen (zwischen 35.000 und 60.000 Flaschen): Gelb hervorheben.
        *   Optimale Bestellungen (> 60.000 Flaschen): Grünes Häkchen-Symbol anwenden.
        *   Bestellungen zwischen 20.000 und 35.000 Flaschen (für spezifische Analyse).
    *   **Gasthof-Lagerverwaltung (Gasthof Bieriger Bär):**
        *   Wenn Bierfässer <= 5, Schrift rot darstellen.
        *   Wenn Weinflaschen < 20, Schrift rot darstellen.
        *   Wenn Weinflaschen == 20, Schrift violett darstellen.
        *   Wenn Cola-Flaschen <= 10, Schrift rot darstellen.
    *   **Bedingte zeitbasierte Formatierung:** Ganze Zeile formatieren, wenn ein Telefonat nach 18:00 Uhr geführt wurde (z.B. `=$B2>ZEIT(18;0;0)`).

### [English]
### 3.3. Text Alignment in Cells
[INFO] Proper text alignment and wrap settings improve readability and table aesthetics.
*   **Text Wrap (`Textumbruch`):** Automatically adjusts text within a cell to fit the column width by wrapping it onto multiple lines. This is useful for long texts in narrow columns.
*   **Alignment:**
    *   Horizontal: Left, Center, Right.
    *   Vertical: Top, Middle, Bottom.
*   **Indent (`Einzug`):** Moves text away from the cell border.
*   **Rotate Text:** Changes the orientation of text within a cell (e.g., vertical text for narrow headers).
    *   [DIAGRAM SUGGESTION: A diagram showing examples of text wrap, different alignments, and rotated text.]

### [German]
### 3.3. Textausrichtung in Zellen
[INFO] Die richtige Textausrichtung und Umbruchseinstellungen verbessern die Lesbarkeit und Ästhetik von Tabellen.
*   **Textumbruch:** Passt den Text innerhalb einer Zelle automatisch an die Spaltenbreite an, indem er ihn auf mehrere Zeilen umbricht. Dies ist nützlich für lange Texte in schmalen Spalten.
*   **Ausrichtung:**
    *   Horizontal: Links, Zentriert, Rechts.
    *   Vertikal: Oben, Mitte, Unten.
*   **Einzug:** Verschiebt den Text vom Zellrand weg.
*   **Text drehen:** Ändert die Ausrichtung des Textes innerhalb einer Zelle (z.B. vertikaler Text für schmale Überschriften).
    *   [DIAGRAMM VORSCHLAG: Ein Diagramm, das Beispiele für Textumbruch, verschiedene Ausrichtungen und gedrehten Text zeigt.]

## 4. Excel Functions

### [English]
### 4.1. Basic Functions

### [English]
#### 4.1.1. Aggregation Functions (`SUMME`, `MITTELWERT`, `MAX`, `MIN`)
[DEFINITION] These functions perform common statistical calculations on a range of numbers.
*   **`SUMME` (SUM):** Adds all the numbers in a range of cells.
    *   **Syntax:** `=SUMME(Zahl1; [Zahl2]; ...)`
*   **`MITTELWERT` (AVERAGE):** Returns the average (arithmetic mean) of the numbers in a range.
    *   **Syntax:** `=MITTELWERT(Zahl1; [Zahl2]; ...)`
*   **`MAX`:** Returns the largest value in a set of values.
    *   **Syntax:** `=MAX(Zahl1; [Zahl2]; ...)`
*   **`MIN`:** Returns the smallest value in a set of values.
    *   **Syntax:** `=MIN(Zahl1; [Zahl2]; ...)`
*   **Example Tasks:**
    *   Calculate the total sum, highest, lowest, and average of house offers.
    *   Calculate the total sum, highest, lowest, and average of customer payments over several years.
    *   Calculate the sum, average, maximum, and minimum for sales analysis data.
    *   Calculate the sum, average, maximum, and minimum of wages.

### [German]
### 4.1. Grundlegende Funktionen

### [German]
#### 4.1.1. Aggregationsfunktionen (`SUMME`, `MITTELWERT`, `MAX`, `MIN`)
[DEFINITION] Diese Funktionen führen gängige statistische Berechnungen für einen Zahlenbereich durch.
*   **`SUMME` (SUM):** Addiert alle Zahlen in einem Zellbereich.
    *   **Syntax:** `=SUMME(Zahl1; [Zahl2]; ...)`
*   **`MITTELWERT` (AVERAGE):** Gibt den Durchschnitt (arithmetisches Mittel) der Zahlen in einem Bereich zurück.
    *   **Syntax:** `=MITTELWERT(Zahl1; [Zahl2]; ...)`
*   **`MAX`:** Gibt den größten Wert in einem Wertebereich zurück.
    *   **Syntax:** `=MAX(Zahl1; [Zahl2]; ...)`
*   **`MIN`:** Gibt den kleinsten Wert in einem Wertebereich zurück.
    *   **Syntax:** `=MIN(Zahl1; [Zahl2]; ...)`
*   **Beispielaufgaben:**
    *   Die Gesamtsumme, den höchsten, niedrigsten und durchschnittlichen Wert von Hausangeboten berechnen.
    *   Die Gesamtsumme, den höchsten, niedrigsten und durchschnittlichen Wert von Kundenzahlungen über mehrere Jahre berechnen.
    *   Die Summe, den Mittelwert, das Maximum und das Minimum für Umsatzanalysedaten berechnen.
    *   Die Summe, den Mittelwert, das Maximum und das Minimum der Lohnzahlungen berechnen.

### [English]
#### 4.1.2. Counting Functions (`ANZAHL`, `ANZAHL2`)
[DEFINITION] These functions count the number of cells in a range that meet specific criteria.
*   **`ANZAHL` (COUNT):** Counts the number of cells that contain numbers.
    *   **Syntax:** `=ANZAHL(Wert1; [Wert2]; ...)`
*   **`ANZAHL2` (COUNTA):** Counts the number of non-empty cells in a range. This includes numbers, text, and errors.
    *   **Syntax:** `=ANZAHL2(Wert1; [Wert2]; ...)`
*   **Example Tasks:**
    *   Count the number of house offers (`ANZAHL`).
    *   Count all cells with content (e.g., for number of persons) (`ANZAHL2`).
    *   Count male employees in a specific department after filtering (`ANZAHL2`).
    *   Count apprentices per department after filtering (`ANZAHL2`).
    *   Count successful or failed participants in an exam (`ANZAHL` or `ANZAHL2` combined with filtering).

### [German]
#### 4.1.2. Zählfunktionen (`ANZAHL`, `ANZAHL2`)
[DEFINITION] Diese Funktionen zählen die Anzahl der Zellen in einem Bereich, die bestimmte Kriterien erfüllen.
*   **`ANZAHL` (COUNT):** Zählt die Anzahl der Zellen, die Zahlen enthalten.
    *   **Syntax:** `=ANZAHL(Wert1; [Wert2]; ...)`
*   **`ANZAHL2` (COUNTA):** Zählt die Anzahl der nicht leeren Zellen in einem Bereich. Dies umfasst Zahlen, Text und Fehler.
    *   **Syntax:** `=ANZAHL2(Wert1; [Wert2]; ...)`
*   **Beispielaufgaben:**
    *   Die Anzahl der Hausangebote zählen (`ANZAHL`).
    *   Alle Zellen mit Inhalt zählen (z.B. für die Anzahl der Personen) (`ANZAHL2`).
    *   Männliche Mitarbeiter in einer bestimmten Abteilung nach dem Filtern zählen (`ANZAHL2`).
    *   Lehrlinge pro Abteilung nach dem Filtern zählen (`ANZAHL2`).
    *   Erfolgreiche oder nicht bestandene Prüfungsteilnehmer zählen (`ANZAHL` oder `ANZAHL2` in Kombination mit Filtern).

### [English]
### 4.2. Logical Functions

### [English]
#### 4.2.1. `WENN` (IF) Function
[DEFINITION] The `WENN` (IF) function checks whether a condition is met and returns one value if TRUE, and another value if FALSE.
*   **Syntax:** `=WENN(Prüfung; Dann_Wert; Sonst_Wert)`
    *   `Prüfung`: The condition to test.
    *   `Dann_Wert`: The value to return if the condition is TRUE.
    *   `Sonst_Wert`: The value to return if the condition is FALSE.
*   **Key Concepts:**
    *   Often used with comparison operators (`=`, `>`, `<`, `>=`, `<=`, `<>`).
    *   Text values in `Dann_Wert` or `Sonst_Wert` must be enclosed in double quotes.
    *   [DIAGRAM SUGGESTION: A flowchart illustrating the IF function logic (Condition -> True/False branch -> Result).]
*   **Example Applications:**
    *   **Branch Manager Bonus:** `=WENN(Umsatz in € >= 10.000; "Ja"; "Nein")`
    *   **Bonus Calculation (Sales target):** `=WENN(Jahresumsatz >= 320.000; Betrag der Zahlung; "-")` where the "Betrag der Zahlung" might be `Jahresumsatz * 2%` (requires nested logic or separate calculation if not directly given as a fixed amount).
    *   **Employee Commission:** `=WENN(Umsatz > 50.000; "Ja"; "Nein")`
    *   **Discount:** `=WENN(Rechnungssumme > 500; "ja"; "xxx")`
    *   **Bonus Payment:** `=WENN(Umsatz >= 50.000; "Bonus"; "-")` using an absolute reference for the bonus threshold (e.g., `$B$21`).
    *   **Interest Calculation:** `=WENN(Guthaben > 10.000; Guthaben * 0,03; Guthaben * 0,0225)` (for 3% vs 2.25% interest).
    *   **Salutation:** `=WENN(Geschlecht = "m"; "Herr"; "Frau")`
    *   **Exam Results:** `=WENN(erreichte Punkte >= 27; "bestanden"; "nicht bestanden")` using an absolute reference for the passing score (e.g., `$B$16`).
    *   **Complex Scenarios (implied):** Combining conditions or calculations within IF statements. For example, `WENN(C9="Ja"; B9*($G$16,0))` or `WENN(Baltesal="Ja"; Umsatz*(2%;0))`.

### [German]
### 4.2. Logische Funktionen

### [German]
#### 4.2.1. `WENN` (IF) Funktion
[DEFINITION] Die `WENN`-Funktion prüft, ob eine Bedingung erfüllt ist, und gibt einen Wert zurück, wenn WAHR, und einen anderen Wert, wenn FALSCH.
*   **Syntax:** `=WENN(Prüfung; Dann_Wert; Sonst_Wert)`
    *   `Prüfung`: Die zu testende Bedingung.
    *   `Dann_Wert`: Der Wert, der zurückgegeben wird, wenn die Bedingung WAHR ist.
    *   `Sonst_Wert`: Der Wert, der zurückgegeben wird, wenn die Bedingung FALSCH ist.
*   **Schlüsselkonzepte:**
    *   Wird oft mit Vergleichsoperatoren verwendet (`=`, `>`, `<`, `>=`, `<=`, `<>`).
    *   Textwerte in `Dann_Wert` oder `Sonst_Wert` müssen in doppelten Anführungszeichen stehen.
    *   [DIAGRAMM VORSCHLAG: Ein Flussdiagramm, das die Logik der WENN-Funktion (Bedingung -> Wahr/Falsch-Zweig -> Ergebnis) illustriert.]
*   **Beispielanwendungen:**
    *   **Filialleiterbonus:** `=WENN(Umsatz in € >= 10.000; "Ja"; "Nein")`
    *   **Bonusberechnung (Umsatzziel):** `=WENN(Jahresumsatz >= 320.000; Betrag der Zahlung; "-")`, wobei der "Betrag der Zahlung" `Jahresumsatz * 2%` sein könnte (erfordert verschachtelte Logik oder separate Berechnung, wenn nicht direkt als fester Betrag angegeben).
    *   **Mitarbeiterprovision:** `=WENN(Umsatz > 50.000; "Ja"; "Nein")`
    *   **Rabatt:** `=WENN(Rechnungssumme > 500; "ja"; "xxx")`
    *   **Bonuszahlung:** `=WENN(Umsatz >= 50.000; "Bonus"; "-")` unter Verwendung eines absoluten Bezugs für die Bonusschwelle (z.B. `$B$21`).
    *   **Zinsberechnung:** `=WENN(Guthaben > 10.000; Guthaben * 0,03; Guthaben * 0,0225)` (für 3% vs. 2,25% Zinsen).
    *   **Anrede:** `=WENN(Geschlecht = "m"; "Herr"; "Frau")`
    *   **Prüfungsergebnisse:** `=WENN(erreichte Punkte >= 27; "bestanden"; "nicht bestanden")` unter Verwendung eines absoluten Bezugs für die Bestehensgrenze (z.B. `$B$16`).
    *   **Komplexe Szenarien (impliziert):** Kombinieren von Bedingungen oder Berechnungen innerhalb von WENN-Anweisungen. Zum Beispiel `WENN(C9="Ja"; B9*($G$16,0))` oder `WENN(Baltesal="Ja"; Umsatz*(2%;0))`.

### [English]
### 4.3. Date and Time Functions
[DEFINITION] Excel provides functions to work with dates and times, allowing calculations based on these values.
*   **`JAHR` (YEAR):** Extracts the year from a date.
*   **`MONAT` (MONTH):** Extracts the month from a date.
*   **`TAG` (DAY):** Extracts the day from a date.
*   **`DATUM` (DATE):** Creates a date from a given year, month, and day.
    *   **Syntax:** `=DATUM(Jahr; Monat; Tag)`
*   **`HEUTE` (TODAY):** Returns the current date.
    *   **Syntax:** `=HEUTE()`
*   **`DATEDIF`:** Calculates the number of days, months, or years between two dates.
    *   **Syntax:** `=DATEDIF(Startdatum; Enddatum; "Einheit")`
        *   `"d"` for days, `"m"` for months, `"y"` for years.
*   **Example Tasks:**
    *   Enter year, month, and day as numbers.
    *   Determine the birth date from these values using `DATUM`.
    *   Find the current date using `HEUTE`.
    *   Calculate the difference in days between birth date and today's date using `DATEDIF`.
    *   Determine "very young" if the difference in days is less than 10,000, otherwise "not so young."

### [German]
### 4.3. Datums- und Zeitfunktionen
[DEFINITION] Excel bietet Funktionen zur Arbeit mit Daten und Zeiten, die Berechnungen auf der Grundlage dieser Werte ermöglichen.
*   **`JAHR` (YEAR):** Extrahiert das Jahr aus einem Datum.
*   **`MONAT` (MONTH):** Extrahiert den Monat aus einem Datum.
*   **`TAG` (DAY):** Extrahiert den Tag aus einem Datum.
*   **`DATUM` (DATE):** Erstellt ein Datum aus einem gegebenen Jahr, Monat und Tag.
    *   **Syntax:** `=DATUM(Jahr; Monat; Tag)`
*   **`HEUTE` (TODAY):** Gibt das aktuelle Datum zurück.
    *   **Syntax:** `=HEUTE()`
*   **`DATEDIF`:** Berechnet die Anzahl der Tage, Monate oder Jahre zwischen zwei Daten.
    *   **Syntax:** `=DATEDIF(Startdatum; Enddatum; "Einheit")`
        *   `"d"` für Tage, `"m"` für Monate, `"y"` für Jahre.
*   **Beispielaufgaben:**
    *   Jahr, Monat und Tag als Zahlen eingeben.
    *   Das Geburtsdatum aus diesen Werten mit `DATUM` ermitteln.
    *   Das heutige Datum mit `HEUTE` ermitteln.
    *   Den Unterschied in Tagen zwischen Geburtsdatum und heutigem Datum mit `DATEDIF` berechnen.
    *   Ermitteln, ob "sehr JUNG" (weniger als 10.000 Tage Unterschied) oder "nicht so jung".

### [English]
### 4.4. Financial Calculations

### [English]
#### 4.4.1. Interest Calculation
[DEFINITION] Interest calculation determines the amount of interest earned or paid on a principal sum over a period.
*   **Formula for Interest Amount:** `Interest Amount = Principal * Interest Rate * Time` (where Time is typically 1 for one year in simple interest scenarios).
*   **New Balance:** `New Balance = Principal + Interest Amount`
*   **Example Task:**
    *   Calculate interest based on account balance:
        *   If balance > €10,000, apply 3% interest.
        *   Otherwise, apply 2.25% interest.
    *   Calculate the interest amount and the new balance after one year.
    *   Format percentage values as percentages.

### [German]
### 4.4. Finanzielle Berechnungen

### [German]
#### 4.4.1. Zinsberechnung
[DEFINITION] Die Zinsberechnung ermittelt die Höhe der Zinsen, die auf einen Kapitalbetrag über einen bestimmten Zeitraum verdient oder gezahlt werden.
*   **Formel für den Zinsbetrag:** `Zinsbetrag = Kapital * Zinssatz * Zeit` (wobei die Zeit in einfachen Zinsszenarien typischerweise 1 für ein Jahr ist).
*   **Neues Guthaben:** `Neues Guthaben = Kapital + Zinsbetrag`
*   **Beispielaufgabe:**
    *   Zinsen basierend auf dem Guthaben berechnen:
        *   Wenn Guthaben > 10.000 €, 3 % Zinsen anwenden.
        *   Andernfalls 2,25 % Zinsen anwenden.
    *   Den Zinsbetrag und das neue Guthaben nach einem Jahr berechnen.
    *   Prozentwerte als Prozent formatieren.

### [English]
### 4.5. Other Calculations

### [English]
#### 4.5.1. Salary Calculations
*   **Wage Calculation:** `Lohnzahlung = Stunden * Stundenlohn` (Wages = Hours * Hourly Rate).
*   **Percentage of Total Wage:** `Prozentueller Anteil am Gesamtlohn = Lohnzahlung / SUMME(Alle Lohnzahlungen)` (Percentage of Total Wage = Individual Wage / SUM(All Wages)).
*   **Example Tasks:**
    *   Calculate individual wages using the formula `Stunden * Stundenlohn`.
    *   Calculate the sum of all wages.
    *   Calculate the average wage.
    *   Determine the number of employees.
    *   Find the highest and lowest individual wages.
    *   Calculate each employee's percentage share of the total wage.

### [German]
### 4.5. Weitere Berechnungen

### [German]
#### 4.5.1. Gehaltsberechnungen
*   **Lohnzahlung:** `Lohnzahlung = Stunden * Stundenlohn`.
*   **Prozentualer Anteil am Gesamtlohn:** `Prozentueller Anteil am Gesamtlohn = Lohnzahlung / SUMME(Alle Lohnzahlungen)`.
*   **Beispielaufgaben:**
    *   Die Lohnzahlungen mit der Formel `Stunden * Stundenlohn` berechnen.
    *   Die Summe aller Lohnzahlungen berechnen.
    *   Den Durchschnittslohn berechnen.
    *   Die Anzahl der Mitarbeiter ermitteln.
    *   Den höchsten und niedrigsten Einzellohn finden.
    *   Den prozentualen Anteil jedes Mitarbeiters am Gesamtlohn berechnen.

## 5. Practical Examples and Exercises

### [English]
### 5.1. Sales Analysis (Hausverkauf, Outletcenter)
*   Calculate MAX, MIN, AVERAGE, and COUNT of offers or sales figures.
*   Format amounts as currency without decimal places.

### [German]
### 5.1. Umsatzanalyse (Hausverkauf, Outletcenter)
*   MAX, MIN, MITTELWERT und ANZAHL von Angeboten oder Umsatzzahlen berechnen.
*   Beträge als Währung ohne Dezimalstellen formatieren.

### [English]
### 5.2. Employee Management (H2O Trink. Wasser)
*   Sort employee data by various criteria (last name, age, salary).
*   Filter and count specific employee groups (e.g., male employees in "Sekretariat", apprentices per department).
*   Calculate salary increases or bonuses for specific departments (e.g., 1.5% bonus for "Vertrieb" employees).
*   Calculate highest, lowest, and average salaries overall and for specific departments.

### [German]
### 5.2. Mitarbeiterverwaltung (H2O Trink. Wasser)
*   Mitarbeiterdaten nach verschiedenen Kriterien sortieren (Nachname, Alter, Gehalt).
*   Spezifische Mitarbeitergruppen filtern und zählen (z.B. männliche Mitarbeiter im "Sekretariat", Lehrlinge pro Abteilung).
*   Gehaltserhöhungen oder Prämien für bestimmte Abteilungen berechnen (z.B. 1,5 % Prämie für Mitarbeiter im "Vertrieb").
*   Höchstes, niedrigstes und durchschnittliches Gehalt insgesamt und für bestimmte Abteilungen berechnen.

### [English]
### 5.3. Stock and Order Management (Fressnapf, H2O Bestellungen, Gasthof Bieriger Bär)
*   Calculate current stock levels.
*   Apply conditional formatting to highlight critical stock levels (e.g., red for low stock, blue for high initial stock).
*   Implement icon sets for order status (unprofitable, critical, optimal).
*   Calculate reorder quantities based on minimum stock levels.

### [German]
### 5.3. Lager- und Bestellverwaltung (Fressnapf, H2O Bestellungen, Gasthof Bieriger Bär)
*   Aktuelle Lagerbestände berechnen.
*   Bedingte Formatierung anwenden, um kritische Lagerbestände hervorzuheben (z.B. rot für niedrigen Bestand, blau für hohen Anfangsbestand).
*   Symbolsätze für den Bestellstatus implementieren (unrentabel, kritisch, optimal).
*   Nachzubestellende Mengen basierend auf Mindestbeständen berechnen.
```