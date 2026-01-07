# Amortisationsrechnung

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] Begriff und Bedeutung der Amortisation verstehen
- [ ] Amortisationsdauer berechnen können
- [ ] Unterschied zwischen statischer und dynamischer Amortisation kennen
- [ ] Investitionsentscheidungen mit der Amortisationsrechnung treffen können

## Grundlagen

Die **Amortisationsrechnung** (auch: Pay-off-Methode, Kapitalrückfluss-Rechnung) ist ein **statisches Investitionsrechenverfahren**, das ermittelt, nach welcher Zeit sich eine Investition durch die erwirtschafteten Rückflüsse selbst finanziert hat.

**Amortisation** = Zeitraum bis zur vollständigen Deckung der Anschaffungskosten durch Rückflüsse

**Ziel:** Ermittlung der **Amortisationsdauer** (Payback-Period)

## Warum ist die Amortisationsrechnung wichtig?

**Vorteile:**
- ✅ Einfache Berechnung und Verständlichkeit
- ✅ Risikobeurteilung (kurze Amortisation = geringes Risiko)
- ✅ Liquiditätsbetrachtung (wann ist Geld zurück?)
- ✅ Schnelle Entscheidungshilfe bei Investitionen

**Nachteile:**
- ❌ Rückflüsse nach der Amortisation werden ignoriert
- ❌ Keine Berücksichtigung der Rentabilität
- ❌ Zeitwert des Geldes wird nicht beachtet (statisch)
- ❌ Keine absolute Vorteilhaftigkeitsaussage

## Formel zur Berechnung

### Variante 1: Bei gleichbleibenden jährlichen Rückflüssen

```
Amortisationsdauer = Anschaffungskosten / Jährlicher Rückfluss
```

**Formel:**
```
t = I₀ / R̄

t  = Amortisationsdauer in Jahren
I₀ = Anschaffungskosten (Investition)
R̄  = Durchschnittlicher jährlicher Rückfluss
```

### Variante 2: Bei unterschiedlichen jährlichen Rückflüssen

Die Amortisationsdauer wird durch **Kumulation der Rückflüsse** ermittelt:

```
Jahr für Jahr werden die Rückflüsse addiert,
bis die Summe ≥ Anschaffungskosten ist.
```

## Begriffe

| Begriff | Definition |
|---------|------------|
| **Anschaffungskosten (I₀)** | Initialer Kapitaleinsatz für die Investition |
| **Rückfluss (Cash-Flow)** | Einzahlungen - Auszahlungen pro Periode (meist pro Jahr) |
| **Amortisationsdauer (t)** | Zeitraum bis zur vollständigen Deckung der Investition |
| **Kumulierter Rückfluss** | Summe aller Rückflüsse bis zu einem Zeitpunkt |
| **Restwert** | Wert der Investition am Ende der Nutzungsdauer |

## Berechnung Schritt für Schritt

### Methode 1: Gleichbleibende Rückflüsse

**Beispiel:**
- Anschaffungskosten neuer Server: 50.000 €
- Jährliche Kosteneinsparung: 12.500 €

**Berechnung:**
```
t = 50.000 € / 12.500 € = 4 Jahre
```

**Ergebnis:** Die Investition amortisiert sich nach **4 Jahren**.

### Methode 2: Unterschiedliche Rückflüsse

**Beispiel:**
- Anschaffungskosten Software: 100.000 €
- Rückflüsse:
  - Jahr 1: 20.000 €
  - Jahr 2: 30.000 €
  - Jahr 3: 35.000 €
  - Jahr 4: 40.000 €
  - Jahr 5: 25.000 €

**Berechnung:**

| Jahr | Rückfluss | Kumulierter Rückfluss | Status |
|------|-----------|-----------------------|--------|
| 1 | 20.000 € | 20.000 € | Noch nicht amortisiert |
| 2 | 30.000 € | 50.000 € | Noch nicht amortisiert |
| 3 | 35.000 € | 85.000 € | Noch nicht amortisiert |
| 4 | 40.000 € | **125.000 €** | ✅ **Amortisiert!** |

**Ergebnis:** Die Investition amortisiert sich **im 4. Jahr**.

**Genaue Berechnung (mit Monaten):**
- Nach 3 Jahren fehlen noch: 100.000 € - 85.000 € = 15.000 €
- Im 4. Jahr Rückfluss: 40.000 €
- Benötigte Zeit im 4. Jahr: 15.000 € / 40.000 € = 0,375 Jahre = 4,5 Monate

**Exakte Amortisationsdauer:** 3 Jahre und 4,5 Monate

## Entscheidungsregel

**Bei einer Investition:**
- ✅ Investition durchführen, wenn **Amortisationsdauer < vorgegebene Maximalzeit**
- ❌ Investition ablehnen, wenn **Amortisationsdauer > vorgegebene Maximalzeit**

**Bei mehreren Investitionsalternativen:**
- Wähle die Investition mit der **kürzesten Amortisationsdauer**

**Beispiel:**
- Maximale akzeptable Amortisationsdauer: 5 Jahre
- Investition A: Amortisationsdauer 4 Jahre → ✅ Annehmen
- Investition B: Amortisationsdauer 6 Jahre → ❌ Ablehnen

## Prüfungsrelevante Inhalte

**Wichtige Prüfungsfragen:**
1. Was versteht man unter Amortisation?
2. Formel für die Amortisationsrechnung
3. Berechnung der Amortisationsdauer (gleichbleibend/unterschiedlich)
4. Vor- und Nachteile der Amortisationsrechnung
5. Investitionsentscheidung anhand der Amortisation

**Typische Aufgaben:**
- Amortisationsdauer berechnen (mit Formel)
- Kumulative Rückflüsse tabellarisch darstellen
- Investitionsentscheidung treffen
- Vergleich mehrerer Investitionsalternativen

## Beispiele / Praxisbezug

### Beispiel 1: Server-Virtualisierung

**Ausgangssituation:**
- Anschaffungskosten für Virtualisierungslösung: 80.000 €
- Jährliche Einsparungen:
  - Stromkosten: 15.000 €
  - Wartungskosten: 10.000 €
  - Lizenzkosten: 5.000 €
  - **Gesamt:** 30.000 € pro Jahr

**Berechnung:**
```
t = 80.000 € / 30.000 € = 2,67 Jahre ≈ 2 Jahre und 8 Monate
```

**Entscheidung:** Wenn das Management eine maximale Amortisationsdauer von 3 Jahren vorgibt, ist die Investition **vorteilhaft**.

### Beispiel 2: Cloud-Migration

**Ausgangssituation:**
- Migrationskosten: 200.000 €
- Rückflüsse durch reduzierte Betriebskosten:

| Jahr | Kosteneinsparung | Kumuliert |
|------|------------------|-----------|
| 1 | 40.000 € | 40.000 € |
| 2 | 50.000 € | 90.000 € |
| 3 | 60.000 € | 150.000 € |
| 4 | 70.000 € | 220.000 € ✅ |

**Amortisationsdauer:** 3 Jahre + (50.000 € / 70.000 €) = **3,71 Jahre** (≈ 3 Jahre 8,5 Monate)

### Beispiel 3: Neue Hardware vs. Leasing

**Variante A - Kauf:**
- Anschaffung: 60.000 €
- Jährliche Betriebskosten: 5.000 €

**Variante B - Leasing:**
- Jährliche Leasingrate: 18.000 €

**Einsparung durch Kauf:**
- Einsparung pro Jahr: 18.000 € - 5.000 € = 13.000 €

**Amortisation:**
```
t = 60.000 € / 13.000 € = 4,62 Jahre ≈ 4 Jahre und 7,5 Monate
```

**Entscheidung:** Bei Nutzungsdauer > 5 Jahre ist Kauf vorteilhaft.

## Dynamische Amortisationsrechnung (Erweiterung)

Die **dynamische Amortisationsrechnung** berücksichtigt den **Zeitwert des Geldes** durch Diskontierung (Abzinsung).

**Formel:**
```
Barwert = Rückfluss / (1 + i)^t

i = Kalkulationszinssatz
t = Jahr
```

**Vorteil:** Realistischere Bewertung, da spätere Rückflüsse weniger wert sind.

**Prüfungshinweis:** Meist wird nur die **statische Amortisation** geprüft.

## Zusammenfassung

**Kernpunkte:**
- **Amortisation:** Zeitraum bis zur Deckung der Anschaffungskosten
- **Formel:** t = Anschaffungskosten / Jährlicher Rückfluss (bei konstanten Rückflüssen)
- **Kumulation:** Bei unterschiedlichen Rückflüssen Jahr für Jahr addieren
- **Vorteil:** Einfach, risikobeurteilend, liquiditätsorientiert
- **Nachteil:** Ignoriert Rückflüsse nach Amortisation, keine Rentabilitätsaussage
- **Entscheidung:** Kürzere Amortisation = bevorzugte Investition

## Prüfungsfragen zum Üben

- [ ] Was versteht man unter Amortisation?
- [ ] Berechnen Sie die Amortisationsdauer: Investition 75.000 €, jährlicher Rückfluss 15.000 €.
- [ ] Welche Vor- und Nachteile hat die Amortisationsrechnung?
- [ ] Ein Unternehmen investiert 120.000 € in neue IT. Rückflüsse: Jahr 1: 30.000 €, Jahr 2: 40.000 €, Jahr 3: 50.000 €, Jahr 4: 60.000 €. Wann amortisiert sich die Investition?
- [ ] Warum ist eine kurze Amortisationsdauer ein Indikator für geringes Risiko?
- [ ] Was ist der Unterschied zwischen statischer und dynamischer Amortisation?
- [ ] Sollte ein Unternehmen nur aufgrund der Amortisationsdauer entscheiden? Warum (nicht)?

## Quellen

- [ ] IHK-Prüfungskatalog Fachinformatiker
- [ ] Wöhe, Günter: Einführung in die Allgemeine Betriebswirtschaftslehre
- [ ] Investitionsrechnung - Grundlagen und Methoden

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](03_Wirtschaftssektoren.md) | [Nächstes Thema](05_Angebotsvergleich.md)
