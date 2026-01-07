# Das Ratendarlehen

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] Unterschied zwischen Tilgung und Zinsen verstehen
- [ ] Ratendarlehen (Annuitätendarlehen) kennen und berechnen
- [ ] Tilgungsplan erstellen können
- [ ] Anwendungsfälle in der IT-Finanzierung kennen

## Grundlagen

Ein **Ratendarlehen** (auch: **Annuitätendarlehen**) ist ein Kredit, bei dem die Rückzahlung in **gleichbleibenden Raten** (Annuitäten) über einen festen Zeitraum erfolgt.

**Merkmale:**
- Konstante Ratenhöhe über die gesamte Laufzeit
- Rate besteht aus Tilgung + Zinsen
- Zinsanteil sinkt, Tilgungsanteil steigt
- Häufigste Form der Unternehmensfinanzierung

## Grundbegriffe

| Begriff | Definition | Beispiel |
|---------|------------|----------|
| **Darlehenssumme** | Kreditbetrag (Nominalwert) | 100.000 € |
| **Zinssatz** | Jährlicher Zinssatz (nominal) | 5% p.a. |
| **Laufzeit** | Dauer der Rückzahlung | 5 Jahre |
| **Annuität** | Gleichbleibende Rate (Tilgung + Zinsen) | 23.097,48 €/Jahr |
| **Tilgung** | Rückzahlung des Darlehens | Steigt jährlich |
| **Zinsen** | Kosten für das Darlehen | Sinken jährlich |
| **Restschuld** | Noch offener Darlehensbetrag | Sinkt jährlich |

## Zusammensetzung der Rate (Annuität)

```
Annuität = Tilgung + Zinsen

Zinsen = Restschuld × Zinssatz
Tilgung = Annuität - Zinsen
Neue Restschuld = Alte Restschuld - Tilgung
```

**Wichtig:** Die Zinsen werden immer auf die **aktuelle Restschuld** berechnet!

## Berechnung der Annuität

### Formel (Annuitätenfaktor-Methode)

```
Annuität = Darlehenssumme × Annuitätenfaktor

Annuitätenfaktor = (q^n × (q - 1)) / (q^n - 1)

Dabei:
q = 1 + Zinssatz (z.B. 1,05 bei 5%)
n = Anzahl der Jahre
```

**Alternative einfachere Formel:**
```
Annuität = Darlehenssumme × (i × (1+i)^n) / ((1+i)^n - 1)

i = Zinssatz als Dezimalzahl (z.B. 0,05 für 5%)
n = Laufzeit in Jahren
```

## Tilgungsplan erstellen

### Beispiel: Darlehen über 100.000 €, 5% Zinsen, 5 Jahre

**Schritt 1: Annuität berechnen**

```
q = 1,05
n = 5

Annuitätenfaktor = (1,05^5 × (1,05 - 1)) / (1,05^5 - 1)
                 = (1,2763 × 0,05) / (1,2763 - 1)
                 = 0,0638 / 0,2763
                 = 0,2310

Annuität = 100.000 € × 0,2310 = 23.097,48 €
```

**Schritt 2: Tilgungsplan Jahr für Jahr**

| Jahr | Restschuld Anfang | Zinsen (5%) | Tilgung | Annuität | Restschuld Ende |
|------|-------------------|-------------|---------|----------|-----------------|
| 1 | 100.000,00 € | 5.000,00 € | 18.097,48 € | 23.097,48 € | 81.902,52 € |
| 2 | 81.902,52 € | 4.095,13 € | 19.002,35 € | 23.097,48 € | 62.900,17 € |
| 3 | 62.900,17 € | 3.145,01 € | 19.952,47 € | 23.097,48 € | 42.947,70 € |
| 4 | 42.947,70 € | 2.147,39 € | 20.950,09 € | 23.097,48 € | 21.997,61 € |
| 5 | 21.997,61 € | 1.099,88 € | 21.997,60 € | 23.097,48 € | 0,00 € |

**Berechnungsschritte für Jahr 1:**
- Zinsen Jahr 1: 100.000 € × 0,05 = 5.000 €
- Tilgung Jahr 1: 23.097,48 € - 5.000 € = 18.097,48 €
- Restschuld nach Jahr 1: 100.000 € - 18.097,48 € = 81.902,52 €

**Beobachtung:**
- Annuität bleibt konstant (23.097,48 €)
- Zinsanteil sinkt (5.000 € → 1.099,88 €)
- Tilgungsanteil steigt (18.097,48 € → 21.997,60 €)

## Unterschied: Ratendarlehen vs. Abzahlungsdarlehen

| Kriterium | Ratendarlehen (Annuität) | Abzahlungsdarlehen |
|-----------|--------------------------|---------------------|
| **Rate** | Konstant | Sinkend |
| **Tilgung** | Steigend | Konstant |
| **Zinsen** | Sinkend | Sinkend |
| **Planbarkeit** | Hoch (gleiche Rate) | Mittel (sinkende Rate) |
| **Gesamtkosten** | Etwas höher | Etwas niedriger |
| **Verwendung** | Häufiger | Seltener |

## Prüfungsrelevante Inhalte

**Wichtige Prüfungsfragen:**
1. Was ist ein Ratendarlehen (Annuitätendarlehen)?
2. Wie setzt sich die Annuität zusammen?
3. Warum sinken die Zinsen und steigt die Tilgung?
4. Berechnung der Annuität
5. Erstellung eines Tilgungsplans

**Typische Aufgaben:**
- Annuität für gegebenes Darlehen berechnen
- Tilgungsplan für erste Jahre erstellen
- Zinsen und Tilgung für ein bestimmtes Jahr berechnen
- Vergleich verschiedener Finanzierungsformen

## Beispiele / Praxisbezug

### Beispiel 1: IT-Infrastruktur-Finanzierung

**Szenario:** Ein Unternehmen finanziert eine neue IT-Infrastruktur über ein Darlehen.

**Daten:**
- Darlehenssumme: 200.000 €
- Zinssatz: 4% p.a.
- Laufzeit: 4 Jahre

**Annuität berechnen:**
```
i = 0,04
n = 4

Annuität = 200.000 × (0,04 × 1,04^4) / (1,04^4 - 1)
         = 200.000 × (0,04 × 1,1699) / (1,1699 - 1)
         = 200.000 × 0,0468 / 0,1699
         = 200.000 × 0,2755
         = 55.095,21 €
```

**Tilgungsplan (Auszug):**

| Jahr | Restschuld Anfang | Zinsen (4%) | Tilgung | Annuität | Restschuld Ende |
|------|-------------------|-------------|---------|----------|-----------------|
| 1 | 200.000,00 € | 8.000,00 € | 47.095,21 € | 55.095,21 € | 152.904,79 € |
| 2 | 152.904,79 € | 6.116,19 € | 48.979,02 € | 55.095,21 € | 103.925,77 € |
| 3 | 103.925,77 € | 4.157,03 € | 50.938,18 € | 55.095,21 € | 52.987,59 € |
| 4 | 52.987,59 € | 2.119,50 € | 52.975,71 € | 55.095,21 € | 0,00 € |

### Beispiel 2: Leasing vs. Darlehen

**Variante A - Ratendarlehen:**
- Darlehen: 50.000 €
- Zinssatz: 3%
- Laufzeit: 3 Jahre
- Annuität: ca. 18.263 €/Jahr
- **Gesamtkosten:** 54.789 €

**Variante B - Leasing:**
- Leasingrate: 1.600 €/Monat = 19.200 €/Jahr
- Laufzeit: 3 Jahre
- **Gesamtkosten:** 57.600 €

**Vergleich:**
- Darlehen ist günstiger (54.789 € vs. 57.600 €)
- Aber: Bei Leasing keine Kapitalbindung, steuerliche Vorteile möglich

### Beispiel 3: Sondertilgung

**Ausgangssituation:**
- Darlehen: 100.000 €, 5% Zinsen, 5 Jahre
- Annuität: 23.097,48 €

**Nach 2 Jahren Sondertilgung von 20.000 €:**
- Restschuld nach Jahr 2: 62.900,17 €
- Nach Sondertilgung: 42.900,17 €
- **Neue Annuität** für restliche 3 Jahre berechnen oder **Laufzeit verkürzen**

**Vorteil:** Weniger Zinsen, frühere Schuldenfreiheit

## Zinsberechnung bei monatlichen Raten

Viele Darlehen haben **monatliche Raten** statt jährlicher Annuitäten.

**Umrechnung:**
```
Monatlicher Zinssatz = Jährlicher Zinssatz / 12
Anzahl Raten = Laufzeit in Jahren × 12
```

**Beispiel:**
- Darlehen: 60.000 €
- Zinssatz: 6% p.a. → 0,5% pro Monat
- Laufzeit: 5 Jahre → 60 Monate

**Monatliche Rate:**
```
i = 0,005
n = 60

Rate = 60.000 × (0,005 × 1,005^60) / (1,005^60 - 1)
     = 60.000 × 0,0067 / 0,3489
     = 1.159,87 €/Monat
```

## Zusammenfassung

**Kernpunkte:**
- **Ratendarlehen:** Gleichbleibende Rate (Annuität) über gesamte Laufzeit
- **Annuität:** Tilgung + Zinsen
- **Zinsen:** Berechnung auf aktuelle Restschuld → sinken im Zeitverlauf
- **Tilgung:** Steigt im Zeitverlauf (Annuität - Zinsen)
- **Tilgungsplan:** Übersicht über Zinsen, Tilgung, Restschuld pro Jahr
- **Formel:** Annuität = Darlehen × Annuitätenfaktor
- **Anwendung:** IT-Investitionen, Unternehmensfinanzierung

## Prüfungsfragen zum Üben

- [ ] Was ist ein Ratendarlehen (Annuitätendarlehen)?
- [ ] Wie setzt sich die Annuität zusammen?
- [ ] Warum sinkt der Zinsanteil und steigt der Tilgungsanteil bei gleicher Rate?
- [ ] Berechnen Sie die Annuität für: 80.000 € Darlehen, 4% Zinsen, 5 Jahre Laufzeit.
- [ ] Erstellen Sie einen Tilgungsplan für die ersten 2 Jahre eines Darlehens über 50.000 € bei 3% Zinsen und einer Laufzeit von 3 Jahren.
- [ ] Was ist der Unterschied zwischen Ratendarlehen und Abzahlungsdarlehen?
- [ ] Ein Darlehen über 120.000 € soll in 6 Jahren zu 5% Zinsen zurückgezahlt werden. Wie hoch ist die jährliche Rate?
- [ ] Welche Vorteile hat eine Sondertilgung?

## Quellen

- [ ] IHK-Prüfungskatalog Fachinformatiker
- [ ] Finanzmathematik - Grundlagen
- [ ] Wöhe, Günter: Einführung in die BWL

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](06_Bezugskalkulation.md) | [Nächstes Thema](08_Harvard_Konzept.md)
