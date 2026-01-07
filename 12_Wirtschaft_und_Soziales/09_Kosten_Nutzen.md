# Kosten-Nutzen-Analyse

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] Kosten-Nutzen-Analyse verstehen und durchführen können
- [ ] Kostenarten (fix, variabel, Einzel-, Gemeinkosten) unterscheiden
- [ ] Nutzen quantifizieren und bewerten können
- [ ] Wirtschaftlichkeit von IT-Investitionen beurteilen

## Grundlagen

Die **Kosten-Nutzen-Analyse** (KNA, engl. Cost-Benefit-Analysis, CBA) ist ein Verfahren zur **systematischen Bewertung** einer Investition oder Maßnahme durch Gegenüberstellung aller **Kosten** und **Nutzen**.

**Ziel:** 
- Ermittlung der Wirtschaftlichkeit
- Entscheidungshilfe für Investitionen
- Vergleich von Alternativen

**Formel:**
```
Nutzen-Kosten-Verhältnis (NKV) = Gesamtnutzen / Gesamtkosten

NKV > 1: Nutzen überwiegt → Investition lohnt sich
NKV = 1: Nutzen = Kosten → Break-even
NKV < 1: Kosten überwiegen → Investition unwirtschaftlich
```

## Kostenarten

### 1. Nach Verhalten bei Beschäftigungsänderung

| Kostenart | Definition | Beispiel IT |
|-----------|------------|-------------|
| **Fixkosten** | Unabhängig von Auslastung/Menge | Miete Rechenzentrum, Lizenzen (Flatrate), Gehälter |
| **Variable Kosten** | Abhängig von Auslastung/Menge | Cloud-Nutzung (pay-per-use), Stromkosten, Datenverkehr |
| **Mischkosten** | Teils fix, teils variabel | Mobilfunkverträge (Grundgebühr + Mehrverbrauch) |

### 2. Nach Zurechenbarkeit

| Kostenart | Definition | Beispiel IT |
|-----------|------------|-------------|
| **Einzelkosten** | Direkt einem Kostenträger zurechenbar | Hardware für spezifisches Projekt, Lizenzen für eine Abteilung |
| **Gemeinkosten** | Nicht direkt zurechenbar, werden umgelegt | IT-Administration, Netzwerkinfrastruktur, allgemeine Bürosoftware |

### 3. Nach Erfassungszeitpunkt

| Kostenart | Definition |
|-----------|------------|
| **Ist-Kosten** | Tatsächlich angefallene Kosten |
| **Plan-Kosten** | Geplante/erwartete Kosten |
| **Soll-Kosten** | Kosten bei Normalbeschäftigung |

## Nutzenarten

### Quantifizierbare Nutzen (monetär)

**Direkte Nutzen:**
- Kosteneinsparungen (Personal, Material, Zeit)
- Umsatzsteigerungen
- Effizienzgewinne (weniger Zeitaufwand)
- Reduzierte Fehlerquote (weniger Nacharbeit)

**Indirekte Nutzen:**
- Zeitersparnis bei Prozessen (Zeit × Stundensatz)
- Geringere Ausfallzeiten (Produktivität × Zeit)
- Energieeinsparungen

### Nicht-quantifizierbare Nutzen (qualitativ)

- Verbesserte Kundenzufriedenheit
- Höhere Mitarbeitermotivation
- Besseres Unternehmensimage
- Flexibilität und Skalierbarkeit
- Wettbewerbsvorteile
- Sicherheit und Datenschutz

**Herausforderung:** Qualitative Nutzen in Geldwerte umrechnen (Monetarisierung)

## Durchführung einer Kosten-Nutzen-Analyse

### Schritt 1: Ziel definieren
- Was soll erreicht werden?
- Welche Alternativen gibt es?

### Schritt 2: Kosten erfassen

**Anschaffungskosten:**
- Hardware, Software, Lizenzen
- Installation, Einrichtung
- Schulungen

**Betriebskosten (laufend):**
- Wartung, Support
- Updates, Upgrades
- Energiekosten
- Personalkosten

**Einmalige Kosten:**
- Migration, Datentransfer
- Umstellung, Anpassungen
- Projektmanagement

### Schritt 3: Nutzen erfassen

**Quantifizierbare Nutzen:**
- Zeitersparnis: X Stunden/Monat × Stundensatz
- Kostenreduktion: Einsparung bei Papier, Druck, Lager
- Produktivitätssteigerung: Mehr Output in gleicher Zeit

**Qualitative Nutzen:**
- Bewertung mit Punkten oder monetärer Schätzung

### Schritt 4: Zeitraum festlegen
- Betrachtungszeitraum (z.B. 3-5 Jahre)
- Berücksichtigung von Abschreibungen

### Schritt 5: Berechnung und Bewertung
- Gesamtkosten aufsummieren
- Gesamtnutzen aufsummieren
- Nutzen-Kosten-Verhältnis berechnen
- Amortisationsdauer ermitteln

## Beispiel: Einführung eines Dokumentenmanagementsystems (DMS)

### Kosten (über 5 Jahre)

**Einmalige Kosten:**
- Software-Lizenzen: 50.000 €
- Hardware (Server): 20.000 €
- Implementierung: 30.000 €
- Schulung: 10.000 €
- **Summe einmalig:** 110.000 €

**Laufende Kosten (pro Jahr):**
- Wartung & Support: 8.000 €
- Updates: 2.000 €
- Administration (20% Stelle): 12.000 €
- **Summe jährlich:** 22.000 €
- **Summe 5 Jahre:** 110.000 €

**Gesamtkosten (5 Jahre):** 220.000 €

### Nutzen (über 5 Jahre)

**Quantifizierbare Einsparungen (pro Jahr):**
- Papier & Druck: 5.000 €
- Archivfläche (Lagermiete): 8.000 €
- Zeitersparnis Dokumentensuche: 200 Std. × 40 €/Std. = 8.000 €
- Zeitersparnis Archivierung: 100 Std. × 40 €/Std. = 4.000 €
- Weniger Verluste durch verlorene Dokumente: 3.000 €
- **Summe jährlich:** 28.000 €
- **Summe 5 Jahre:** 140.000 €

**Qualitative Nutzen:**
- Schnellerer Zugriff auf Informationen
- Bessere Zusammenarbeit
- Compliance (DSGVO, GoBD)
- Homeoffice-Fähigkeit
- **Geschätzt:** 10.000 €/Jahr = 50.000 € (5 Jahre)

**Gesamtnutzen (5 Jahre):** 190.000 €

### Bewertung

```
Nutzen-Kosten-Verhältnis = 190.000 € / 220.000 € = 0,86

NKV < 1 → Rein monetär nicht wirtschaftlich
```

**Aber:** Wenn qualitative Nutzen berücksichtigt werden (z.B. mit 60.000 € statt 50.000 €):
```
Gesamtnutzen = 200.000 €
NKV = 200.000 € / 220.000 € = 0,91
```

**Entscheidung:** Bei starker Gewichtung qualitativer Nutzen (Compliance, Zukunftssicherheit) kann Investition trotzdem sinnvoll sein.

## Kosten- vs. Nutzenrechnung: Kritische Betrachtung

**Vorteile:**
- ✅ Systematische Entscheidungsgrundlage
- ✅ Vergleich verschiedener Alternativen
- ✅ Transparenz über Wirtschaftlichkeit
- ✅ Risikominimierung

**Nachteile:**
- ❌ Schwierige Quantifizierung qualitativer Nutzen
- ❌ Schätzungen oft ungenau
- ❌ Keine Berücksichtigung strategischer Aspekte
- ❌ Vernachlässigung langfristiger Effekte

## Prüfungsrelevante Inhalte

**Wichtige Prüfungsfragen:**
1. Was ist eine Kosten-Nutzen-Analyse?
2. Unterschied zwischen Fix- und variablen Kosten
3. Unterschied zwischen Einzel- und Gemeinkosten
4. Nutzen-Kosten-Verhältnis berechnen
5. Quantifizierbare vs. qualitative Nutzen

**Typische Aufgaben:**
- Kosten einer IT-Investition berechnen
- Nutzen quantifizieren
- Nutzen-Kosten-Verhältnis ermitteln
- Investitionsentscheidung treffen
- Amortisationsdauer berechnen

## Beispiele / Praxisbezug

### Beispiel 1: Cloud-Migration

**Kosten (3 Jahre):**
- Migration: 50.000 €
- Cloud-Kosten: 30.000 €/Jahr = 90.000 €
- **Gesamt:** 140.000 €

**Nutzen (3 Jahre):**
- Wegfall Server-Hardware: 60.000 €
- Reduzierte Administration: 40.000 €
- Weniger Energiekosten: 15.000 €
- Höhere Verfügbarkeit (weniger Ausfälle): 20.000 €
- **Gesamt:** 135.000 €

**NKV = 135.000 € / 140.000 € = 0,96**

**Bewertung:** Knapp unwirtschaftlich rein monetär, aber strategisch sinnvoll (Skalierbarkeit, Flexibilität).

### Beispiel 2: Server-Virtualisierung

**Kosten:** 80.000 € (einmalig + 3 Jahre Betrieb)
**Nutzen:** 120.000 € (Stromersparnis, Platzbedarf, weniger Hardware)
**NKV = 1,5 → Investition lohnt sich**

### Beispiel 3: Helpdesk-Software

**Kosten (5 Jahre):** 100.000 €
**Nutzen (5 Jahre):**
- Zeitersparnis Support: 80.000 €
- Bessere Kundenzufriedenheit: 30.000 € (geschätzt)
- Weniger Eskalationen: 10.000 €
**Gesamt:** 120.000 €

**NKV = 1,2 → Investition wirtschaftlich**

## Zusammenfassung

**Kernpunkte:**
- **Kosten-Nutzen-Analyse:** Systematischer Vergleich von Kosten und Nutzen
- **Kostenarten:** Fix/variabel, Einzel-/Gemeinkosten
- **Nutzen:** Quantifizierbar (monetär) und qualitativ
- **NKV:** Nutzen-Kosten-Verhältnis > 1 → wirtschaftlich
- **Anwendung:** IT-Investitionen, Projektbewertung, Angebotsvergleich
- **Herausforderung:** Monetarisierung qualitativer Nutzen

## Prüfungsfragen zum Üben

- [ ] Was ist eine Kosten-Nutzen-Analyse?
- [ ] Unterscheiden Sie Fixkosten und variable Kosten mit je einem IT-Beispiel.
- [ ] Was sind Gemeinkosten? Nennen Sie ein Beispiel.
- [ ] Berechnen Sie das Nutzen-Kosten-Verhältnis: Kosten 150.000 €, Nutzen 180.000 €.
- [ ] Ein NKV von 0,8 bedeutet was? Sollte die Investition durchgeführt werden?
- [ ] Nennen Sie 3 quantifizierbare und 3 qualitative Nutzen einer IT-Investition.
- [ ] Warum ist die Monetarisierung qualitativer Nutzen schwierig?
- [ ] Eine Cloud-Migration kostet 200.000 €. Jährliche Einsparung: 60.000 €. Nach wie vielen Jahren amortisiert sich die Investition? Ist sie nach 5 Jahren wirtschaftlich (NKV)?

## Quellen

- [ ] IHK-Prüfungskatalog Fachinformatiker
- [ ] Controlling - Kosten- und Leistungsrechnung
- [ ] IT-Investitionsrechnung

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](08_Harvard_Konzept.md) | [Nächstes Thema](10_Make_or_Buy.md)
