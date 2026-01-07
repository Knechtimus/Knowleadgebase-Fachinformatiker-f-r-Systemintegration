# Bezugskalkulation

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] Schema der Bezugskalkulation kennen und anwenden
- [ ] Bezugspreis berechnen können
- [ ] Unterschied zwischen Listeneinkaufspreis und Bezugspreis verstehen
- [ ] Praktische Anwendung in IT-Beschaffungsprozessen

## Grundlagen

Die **Bezugskalkulation** (auch: Beschaffungskalkulation) ist ein Verfahren zur Ermittlung des **tatsächlichen Einstandspreises** einer Ware oder Dienstleistung.

**Ziel:** Berechnung des **Bezugspreises** - der Preis, den das Unternehmen real bezahlt (inkl. aller Kosten und abzgl. aller Rabatte).

Der **Bezugspreis** ist die Grundlage für:
- Angebotsvergleich
- Verkaufskalkulation
- Lagerbewertung
- Kostenrechnung

## Schema der Bezugskalkulation

```
  Listeneinkaufspreis (Brutto)
- Lieferantenrabatt
= Zieleinkaufspreis
- Lieferantenskonto
= Bareinkaufspreis
+ Bezugskosten
= BEZUGSPREIS
```

## Begriffe und Definitionen

| Begriff | Definition | Beispiel |
|---------|------------|----------|
| **Listeneinkaufspreis** | Katalogpreis des Lieferanten (Bruttopreis) | 10.000 € |
| **Lieferantenrabatt** | Preisnachlass des Lieferanten (in %) | 15% = 1.500 € |
| **Zieleinkaufspreis** | Preis nach Abzug des Rabatts | 8.500 € |
| **Lieferantenskonto** | Nachlass bei schneller Zahlung (in %) | 2% = 170 € |
| **Bareinkaufspreis** | Preis nach Abzug von Rabatt und Skonto | 8.330 € |
| **Bezugskosten** | Transport, Versicherung, Verpackung, Zoll | 400 € |
| **Bezugspreis** | Tatsächlicher Einkaufspreis (Einstandspreis) | 8.730 € |

### Wichtige Hinweise

**Rabatt:**
- Mengenrabatt (bei größeren Bestellmengen)
- Treuerabatt (bei regelmäßigen Bestellungen)
- Sonderrabatt (z.B. Saisonrabatt)
- Wird immer auf den **Listeneinkaufspreis** berechnet

**Skonto:**
- Zeitlich begrenzt (z.B. "2% Skonto bei Zahlung innerhalb 10 Tagen")
- Wird auf den **Zieleinkaufspreis** berechnet (nach Rabattabzug!)
- Zahlungsbedingung, kein Preisnachlass

**Bezugskosten:**
- Frachtkosten (Transport)
- Verpackungskosten
- Versicherungskosten
- Zollgebühren (bei Import)
- Installationskosten

## Formeln

### Rabatt berechnen
```
Rabattbetrag = Listeneinkaufspreis × (Rabatt% / 100)
Zieleinkaufspreis = Listeneinkaufspreis - Rabattbetrag
```

### Skonto berechnen
```
Skontobetrag = Zieleinkaufspreis × (Skonto% / 100)
Bareinkaufspreis = Zieleinkaufspreis - Skontobetrag
```

### Bezugspreis berechnen
```
Bezugspreis = Bareinkaufspreis + Bezugskosten
```

## Schritt-für-Schritt Berechnung

### Beispiel 1: Standard-Bezugskalkulation

**Ausgangsdaten:**
- Listeneinkaufspreis: 12.000 €
- Lieferantenrabatt: 20%
- Lieferantenskonto: 3% bei Zahlung in 14 Tagen
- Bezugskosten: 600 €

**Berechnung:**

| Position | Berechnung | Betrag |
|----------|------------|--------|
| Listeneinkaufspreis | Gegeben | 12.000,00 € |
| - Lieferantenrabatt (20%) | 12.000 × 0,20 | 2.400,00 € |
| = Zieleinkaufspreis | 12.000 - 2.400 | 9.600,00 € |
| - Lieferantenskonto (3%) | 9.600 × 0,03 | 288,00 € |
| = Bareinkaufspreis | 9.600 - 288 | 9.312,00 € |
| + Bezugskosten | Gegeben | 600,00 € |
| = **Bezugspreis** | 9.312 + 600 | **9.912,00 €** |

**Ergebnis:** Der Bezugspreis beträgt **9.912,00 €**.

### Beispiel 2: Server-Beschaffung

**Ausgangsdaten:**
- 10 Server à 2.500 € (Listenpreis) = 25.000 €
- Mengenrabatt: 12%
- Skonto: 2% bei Zahlung in 10 Tagen
- Lieferkosten: 450 €
- Installation: 800 €

**Berechnung:**

| Position | Berechnung | Betrag |
|----------|------------|--------|
| Listeneinkaufspreis | 10 × 2.500 | 25.000,00 € |
| - Mengenrabatt (12%) | 25.000 × 0,12 | 3.000,00 € |
| = Zieleinkaufspreis | 25.000 - 3.000 | 22.000,00 € |
| - Skonto (2%) | 22.000 × 0,02 | 440,00 € |
| = Bareinkaufspreis | 22.000 - 440 | 21.560,00 € |
| + Lieferkosten | Gegeben | 450,00 € |
| + Installation | Gegeben | 800,00 € |
| = **Bezugspreis** | 21.560 + 1.250 | **22.810,00 €** |

**Bezugspreis pro Server:** 22.810 € / 10 = **2.281,00 €**

### Beispiel 3: Software-Lizenzierung

**Ausgangsdaten:**
- Software-Lizenzen: 50 User à 200 € = 10.000 €
- Volumenrabatt: 25%
- Skonto: Keine Skonto-Option
- Schulungskosten: 1.500 €
- Implementierung: 2.000 €

**Berechnung:**

| Position | Berechnung | Betrag |
|----------|------------|--------|
| Listeneinkaufspreis | 50 × 200 | 10.000,00 € |
| - Volumenrabatt (25%) | 10.000 × 0,25 | 2.500,00 € |
| = Zieleinkaufspreis | 10.000 - 2.500 | 7.500,00 € |
| - Skonto (0%) | - | 0,00 € |
| = Bareinkaufspreis | 7.500 - 0 | 7.500,00 € |
| + Schulung | Gegeben | 1.500,00 € |
| + Implementierung | Gegeben | 2.000,00 € |
| = **Bezugspreis** | 7.500 + 3.500 | **11.000,00 €** |

**Bezugspreis pro User:** 11.000 € / 50 = **220,00 €**

## Bezugskalkulation bei mehreren Lieferungen

Wenn mehrere Artikel mit unterschiedlichen Konditionen bestellt werden:

**Beispiel:**
- Artikel A: 5.000 €, Rabatt 10%, Skonto 2%
- Artikel B: 3.000 €, Rabatt 15%, Skonto 3%
- Gemeinsame Lieferkosten: 500 €

**Berechnung:**
1. Bezugskalkulation für jeden Artikel einzeln (ohne Lieferkosten)
2. Lieferkosten anteilig aufteilen (z.B. nach Wert oder Gewicht)

## Prüfungsrelevante Inhalte

**Wichtige Prüfungsfragen:**
1. Schema der Bezugskalkulation
2. Berechnung von Rabatt, Skonto, Bezugspreis
3. Unterschied zwischen Rabatt und Skonto
4. Wofür wird der Bezugspreis benötigt?
5. Bezugskosten: Was gehört dazu?

**Typische Aufgaben:**
- Bezugspreis berechnen mit gegebenem Listeneinkaufspreis, Rabatt, Skonto, Bezugskosten
- Angebotsvergleich: Mehrere Angebote kalkulieren und vergleichen
- Rückrechnung: Bezugspreis gegeben, Listeneinkaufspreis berechnen

## Beispiele / Praxisbezug

### Beispiel 1: Hardware-Beschaffung mit Vergleich

**Angebot A:**
- Listeneinkaufspreis: 8.000 €
- Rabatt: 15%
- Skonto: 2%
- Lieferkosten: 300 €

**Bezugspreis A:**
```
8.000 - 1.200 (15%) = 6.800
6.800 - 136 (2%) = 6.664
6.664 + 300 = 6.964 €
```

**Angebot B:**
- Listeneinkaufspreis: 7.500 €
- Rabatt: 10%
- Skonto: 3%
- Lieferkosten: 500 €

**Bezugspreis B:**
```
7.500 - 750 (10%) = 6.750
6.750 - 202,50 (3%) = 6.547,50
6.547,50 + 500 = 7.047,50 €
```

**Entscheidung:** Angebot A ist günstiger (6.964 € < 7.047,50 €)

### Beispiel 2: Cloud-Services (wiederkehrende Kosten)

Bei SaaS/Cloud-Abos gibt es oft keine klassische Bezugskalkulation, aber:
- Grundpreis pro User/Monat
- Rabatt bei Jahresvertrag (z.B. 20%)
- Zusatzkosten: Setup, Migration, Schulung

**Beispiel:**
- 100 User à 10 €/Monat = 1.000 €/Monat
- Jahresvertrag: 12.000 € - 20% Rabatt = 9.600 €
- Setup: 2.000 €
- **Gesamtkosten Jahr 1:** 11.600 €

## Zusammenfassung

**Kernpunkte:**
- **Bezugskalkulation:** Ermittlung des tatsächlichen Einkaufspreises
- **Schema:** Listeneinkaufspreis - Rabatt - Skonto + Bezugskosten = Bezugspreis
- **Rabatt:** Preisnachlass auf Listenpreis (in %)
- **Skonto:** Nachlass bei schneller Zahlung auf Zieleinkaufspreis (in %)
- **Bezugskosten:** Alle zusätzlichen Kosten (Transport, Installation, etc.)
- **Anwendung:** Angebotsvergleich, Kostenrechnung, Lagerbewertung

## Prüfungsfragen zum Üben

- [ ] Was ist der Bezugspreis und wozu wird er benötigt?
- [ ] Nennen Sie das Schema der Bezugskalkulation.
- [ ] Was ist der Unterschied zwischen Rabatt und Skonto?
- [ ] Berechnen Sie: Listeneinkaufspreis 6.000 €, Rabatt 18%, Skonto 2,5%, Bezugskosten 350 €.
- [ ] Welche Kosten gehören zu den Bezugskosten?
- [ ] Warum wird Skonto auf den Zieleinkaufspreis berechnet und nicht auf den Listeneinkaufspreis?
- [ ] Ein Unternehmen kauft 20 Notebooks à 800 €. Rabatt: 12%, Skonto: 3%, Lieferung: 200 €. Wie hoch ist der Bezugspreis pro Notebook?
- [ ] Wann ist es sinnvoll, Skonto zu nutzen?

## Quellen

- [ ] IHK-Prüfungskatalog Fachinformatiker
- [ ] Kaufmännisches Rechnen - Grundlagen
- [ ] Schmolke/Deitermann: Industrielles Rechnungswesen

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](05_Angebotsvergleich.md) | [Nächstes Thema](07_Das_Ratendarlehen.md)
