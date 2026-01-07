# ROI - Return of Investment

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] ROI-Begriff verstehen und von Rentabilität abgrenzen
- [ ] ROI berechnen und interpretieren können
- [ ] ROI für IT-Investitionen anwenden
- [ ] Zusammenhang zwischen ROI, Amortisation und Rentabilität verstehen

## Grundlagen

Der **ROI (Return on Investment)** ist eine Kennzahl zur Messung der **Rendite einer Investition**. Er gibt an, wie viel Gewinn im Verhältnis zum eingesetzten Kapital erzielt wurde.

**Grundformel:**
```
ROI = ((Gewinn - Investition) / Investition) × 100%
```

**Alternative Formel:**
```
ROI = (Gewinn / Investition) × 100%

Oder:

ROI = ((Ertrag - Aufwand) / Aufwand) × 100%
```

**Bedeutung:**
- Universelle Kennzahl für Investitionsbewertung
- Ermöglicht Vergleich verschiedener Investitionen
- Zeitunabhängige Betrachtung (kann für Jahr, Monat, Gesamtlaufzeit berechnet werden)
- Je höher der ROI, desto rentabler die Investition

**Ziel:** ROI sollte positiv sein (ROI > 0%) und idealerweise alternative Anlagen übertreffen

## ROI-Formel im Detail

### Variante 1: Gewinnbezogen
```
ROI = ((Ertrag - Kosten) / Kosten) × 100%
```

**Beispiel:**
- Investition: 100.000 €
- Gesamtertrag (über Laufzeit): 150.000 €
- ROI = ((150.000 € - 100.000 €) / 100.000 €) × 100% = **50%**

**Interpretation:** Die Investition hat 50% Rendite gebracht.

### Variante 2: DuPont-Schema (erweitert)
```
ROI = Umsatzrentabilität × Kapitalumschlag

ROI = (Gewinn / Umsatz) × (Umsatz / Kapital)
```

**Beispiel:**
- Umsatzrentabilität: 10%
- Kapitalumschlag: 2 (Umsatz ist doppelt so hoch wie Kapital)
- ROI = 10% × 2 = **20%**

## ROI vs. Rentabilität

| Kriterium | ROI | Rentabilität |
|-----------|-----|--------------|
| **Fokus** | Spezifische Investition | Laufendes Geschäft |
| **Zeitbezug** | Punktuell (Projekt-Laufzeit) | Periodisch (meist jährlich) |
| **Berechnung** | (Gewinn - Investition) / Investition | Gewinn / Kapital |
| **Anwendung** | Projektbewertung | Unternehmensperformance |
| **Vergleich** | Verschiedene Projekte | Verschiedene Perioden/Unternehmen |

**Zusammenhang:** ROI ist eine Form der Rentabilitätsberechnung für einzelne Investitionen.

## ROI-Berechnung Schritt für Schritt

### Schritt 1: Investitionskosten ermitteln

**Einmalige Kosten:**
- Anschaffungskosten (Hardware, Software, Lizenzen)
- Implementierungskosten
- Schulungskosten
- Projektmanagementkosten

**Laufende Kosten (über Nutzungsdauer):**
- Betriebskosten
- Wartung und Support
- Personalkosten

**Gesamtinvestition = Einmalige Kosten + Summe laufende Kosten**

### Schritt 2: Erträge/Nutzen ermitteln

**Direkte Erträge:**
- Umsatzsteigerungen
- Kosteneinsparungen
- Effizienzgewinne (monetarisiert)

**Indirekte Erträge:**
- Zeitersparnis (× Stundensatz)
- Qualitätsverbesserungen (weniger Fehler/Nacharbeit)
- Produktivitätssteigerung

**Gesamtertrag = Summe aller Erträge über Nutzungsdauer**

### Schritt 3: ROI berechnen
```
ROI = ((Gesamtertrag - Gesamtinvestition) / Gesamtinvestition) × 100%
```

### Schritt 4: Interpretation
- **ROI > 0%:** Investition ist profitabel
- **ROI = 0%:** Break-even (Kosten = Erträge)
- **ROI < 0%:** Investition macht Verlust

## Beispiel 1: Server-Virtualisierung

### Investitionskosten (einmalig + 5 Jahre)

**Einmalig:**
- Virtualisierungs-Software: 30.000 €
- Hardware (Host-Server): 50.000 €
- Migration und Setup: 20.000 €
- Schulung: 5.000 €
- **Summe einmalig:** 105.000 €

**Laufend (5 Jahre):**
- Wartung: 5.000 €/Jahr × 5 = 25.000 €
- Support: 3.000 €/Jahr × 5 = 15.000 €
- **Summe laufend:** 40.000 €

**Gesamtinvestition:** 145.000 €

### Erträge (über 5 Jahre)

**Einsparungen:**
- Wegfall von 20 physischen Servern: 10.000 €/Jahr × 5 = 50.000 €
- Stromkosten: 15.000 €/Jahr × 5 = 75.000 €
- Kühlungskosten: 5.000 €/Jahr × 5 = 25.000 €
- Platzeinsparung (Raumkosten): 8.000 €/Jahr × 5 = 40.000 €
- Reduzierte Administrationszeit: 10.000 €/Jahr × 5 = 50.000 €
- **Gesamtertrag:** 240.000 €

### ROI-Berechnung
```
ROI = ((240.000 € - 145.000 €) / 145.000 €) × 100%
ROI = (95.000 € / 145.000 €) × 100%
ROI = 65,5%
```

**Interpretation:** Die Investition bringt über 5 Jahre eine Rendite von 65,5%. Pro investiertem Euro werden 0,66 € Gewinn erzielt.

**Jährlicher ROI:**
```
Jährlicher ROI = 65,5% / 5 Jahre = 13,1% pro Jahr
```

## Beispiel 2: Cloud-Migration

### Investition (3 Jahre)
- Migration: 80.000 €
- Schulung: 10.000 €
- Cloud-Kosten: 40.000 €/Jahr × 3 = 120.000 €
- **Gesamtinvestition:** 210.000 €

### Erträge (3 Jahre)
- Wegfall eigener Server: 100.000 €
- Reduzierte Stromkosten: 30.000 €
- Weniger IT-Personal: 60.000 €
- Höhere Verfügbarkeit (weniger Ausfälle): 40.000 €
- **Gesamtertrag:** 230.000 €

### ROI-Berechnung
```
ROI = ((230.000 € - 210.000 €) / 210.000 €) × 100% = 9,5%
```

**Interpretation:** Leicht positiver ROI (9,5%), zusätzlich qualitative Vorteile (Skalierbarkeit, Flexibilität).

## Beispiel 3: Helpdesk-Software

### Investition (5 Jahre)
- Software-Lizenzen: 50.000 €
- Implementierung: 15.000 €
- Schulung: 5.000 €
- Betrieb: 8.000 €/Jahr × 5 = 40.000 €
- **Gesamtinvestition:** 110.000 €

### Erträge (5 Jahre)
- Zeitersparnis Support: 100 Std./Monat × 40 €/Std. × 12 Monate × 5 Jahre = 240.000 €
- Bessere Kundenzufriedenheit (weniger Churn): 30.000 €
- Weniger Eskalationen: 20.000 €
- **Gesamtertrag:** 290.000 €

### ROI-Berechnung
```
ROI = ((290.000 € - 110.000 €) / 110.000 €) × 100% = 163,6%
```

**Interpretation:** Sehr hoher ROI von 163,6% - die Investition ist hochprofitabel.

## ROI-Optimierung

### Faktoren zur ROI-Steigerung

**1. Kosten senken:**
- Effiziente Implementierung
- Open-Source-Alternativen prüfen
- Verhandlung mit Anbietern
- Cloud statt On-Premise (niedrigere Initialkosten)

**2. Erträge steigern:**
- Vollständige Nutzung aller Features
- Schulungen für maximale Effizienz
- Schnelle Umsetzung (frühere Erträge)
- Skalierung

**3. Zeitraum optimieren:**
- Längere Nutzungsdauer → höhere Gesamterträge
- Schnellere Amortisation → besserer Cash-Flow

## ROI-Grenzen und Kritik

### Vorteile
- ✅ Einfache Berechnung und Verständlichkeit
- ✅ Vergleichbarkeit verschiedener Investitionen
- ✅ Universell einsetzbar
- ✅ Fokus auf Rentabilität

### Nachteile
- ❌ Ignoriert den Zeitwert des Geldes (keine Diskontierung)
- ❌ Schwierige Quantifizierung qualitativer Nutzen
- ❌ Keine Berücksichtigung von Risiken
- ❌ Keine Aussage über absolute Gewinngröße
- ❌ Kurzfristige vs. langfristige Betrachtung

**Beispiel Problem:**
- Projekt A: Investition 10.000 €, Gewinn 5.000 €, ROI 50%
- Projekt B: Investition 100.000 €, Gewinn 40.000 €, ROI 40%

**Nur ROI:** Projekt A ist besser (50% vs. 40%)
**Aber:** Projekt B bringt absolut mehr Gewinn (40.000 € vs. 5.000 €)

## Prüfungsrelevante Inhalte

**Wichtige Prüfungsfragen:**
1. Was ist der ROI?
2. ROI-Formel
3. Berechnung des ROI für IT-Investitionen
4. Unterschied zwischen ROI und Rentabilität
5. Interpretation von ROI-Werten
6. Vor- und Nachteile des ROI

**Typische Aufgaben:**
- ROI für gegebene Investition berechnen
- Vergleich mehrerer Investitionen anhand ROI
- Kostenermittlung und Ertragskalkulation
- Entscheidung treffen basierend auf ROI

## Zusammenfassung

**Kernpunkte:**
- **ROI:** Rendite einer Investition im Verhältnis zu den Kosten
- **Formel:** ((Ertrag - Investition) / Investition) × 100%
- **ROI > 0%:** Profitabel
- **ROI = 0%:** Break-even
- **ROI < 0%:** Verlust
- **Anwendung:** Bewertung von IT-Projekten, Investitionsentscheidungen
- **Vorteil:** Einfach, vergleichbar, universell
- **Nachteil:** Ignoriert Zeitwert des Geldes, qualitative Faktoren schwer zu quantifizieren
- **Zusammenhang:** ROI ist eine Form der Rentabilität für Einzelinvestitionen

## Prüfungsfragen zum Üben

- [ ] Was bedeutet ROI und wie wird er berechnet?
- [ ] Eine Investition von 80.000 € bringt über 4 Jahre Erträge von 120.000 €. Wie hoch ist der ROI?
- [ ] Was ist der Unterschied zwischen ROI und Rentabilität?
- [ ] Ein ROI von 75% bedeutet was genau?
- [ ] Projekt A: Investition 50.000 €, Ertrag 80.000 €. Projekt B: Investition 100.000 €, Ertrag 140.000 €. Welches hat den höheren ROI?
- [ ] Nennen Sie 3 Vorteile und 3 Nachteile des ROI.
- [ ] Warum ist ein hoher ROI allein nicht immer aussagekräftig?
- [ ] Eine Cloud-Migration kostet 200.000 € und spart über 5 Jahre 300.000 €. Berechnen Sie den ROI.

## Quellen

- [ ] IHK-Prüfungskatalog Fachinformatiker
- [ ] ROI-Analyse und Investitionsrechnung
- [ ] IT-Controlling und Kennzahlen

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](12_Rentabilitaetsrechnung.md)
