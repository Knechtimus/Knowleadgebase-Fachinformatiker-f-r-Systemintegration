# Nutzwertanalyse

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] Nutzwertanalyse als Bewertungsverfahren verstehen
- [ ] Systematische Durchführung einer Nutzwertanalyse
- [ ] Gewichtung und Punktevergabe anwenden können
- [ ] Praktische Anwendung in IT-Entscheidungen

## Grundlagen

Die **Nutzwertanalyse** (NWA, auch: Scoring-Modell, Punktbewertungsverfahren) ist ein **multikriterielles Bewertungsverfahren** zur systematischen Entscheidungsfindung bei mehreren Alternativen und Kriterien.

**Besonderheit:** Ermöglicht die Bewertung von **nicht-monetären (qualitativen) Kriterien** neben monetären Kriterien.

**Ziel:**
- Objektive Entscheidungsgrundlage
- Transparente Bewertung
- Vergleich von Alternativen
- Berücksichtigung mehrerer Faktoren gleichzeitig

**Anwendungsbereiche:**
- Produktauswahl (Hardware, Software)
- Lieferantenauswahl
- Standortentscheidungen
- Projektpriorisierung
- Make-or-Buy-Entscheidungen

## Vorteile und Nachteile

### Vorteile
- ✅ Systematische, strukturierte Entscheidungsfindung
- ✅ Berücksichtigung qualitativer Kriterien
- ✅ Transparenz und Nachvollziehbarkeit
- ✅ Vergleichbarkeit mehrerer Alternativen
- ✅ Einbindung verschiedener Perspektiven möglich

### Nachteile
- ❌ Subjektivität bei Gewichtung und Punktevergabe
- ❌ Gefahr der Scheingenauigkeit
- ❌ Zeitaufwand
- ❌ Keine Berücksichtigung von Wechselwirkungen zwischen Kriterien
- ❌ Ergebnis hängt stark von gewählten Kriterien ab

## Durchführung in 6 Schritten

### Schritt 1: Ziel und Alternativen festlegen

**Ziel definieren:**
- Was soll erreicht werden?
- Welches Problem soll gelöst werden?

**Alternativen sammeln:**
- Mindestens 2 Alternativen
- Realistisch und umsetzbar
- Vergleichbar

**Beispiel:** Auswahl eines Projektmanagement-Tools
- Alternative A: Jira
- Alternative B: Asana
- Alternative C: Monday.com

### Schritt 2: Bewertungskriterien festlegen

**Kriterien auswählen:**
- Relevant für die Entscheidung
- Messbar oder bewertbar
- Unabhängig voneinander (keine Überschneidungen)

**Kategorien:**
- **Technische Kriterien:** Funktionalität, Performance, Kompatibilität
- **Wirtschaftliche Kriterien:** Preis, Betriebskosten, ROI
- **Organisatorische Kriterien:** Benutzerfreundlichkeit, Schulungsaufwand
- **Strategische Kriterien:** Zukunftssicherheit, Anbieterreputation

**Beispiel Projektmanagement-Tool:**
1. Funktionsumfang
2. Benutzerfreundlichkeit
3. Preis
4. Integration mit bestehenden Systemen
5. Support & Dokumentation
6. Skalierbarkeit

### Schritt 3: Gewichtung der Kriterien

**Gewichtung in Prozent:**
- Summe aller Gewichtungen = 100%
- Wichtigere Kriterien erhalten höhere Gewichtung
- Oft durch Team-Diskussion oder Management-Vorgabe

**Beispiel:**

| Kriterium | Gewichtung |
|-----------|------------|
| Funktionsumfang | 25% |
| Benutzerfreundlichkeit | 20% |
| Preis | 20% |
| Integration | 15% |
| Support | 10% |
| Skalierbarkeit | 10% |
| **Summe** | **100%** |

### Schritt 4: Punktevergabe für jede Alternative

**Bewertungsskala:**
- Meist 1-10 Punkte (oder 1-5, 1-100)
- 10 = Besterfüllung, 1 = Schlechterfüllung
- Einheitliche Skala für alle Kriterien

**Tipp:** Klare Kriterien für Punktevergabe definieren
- 10 Punkte: Alle Anforderungen übertroffen
- 7-9 Punkte: Anforderungen erfüllt
- 4-6 Punkte: Teilweise erfüllt
- 1-3 Punkte: Nicht erfüllt

**Beispiel:**

| Kriterium | Jira | Asana | Monday.com |
|-----------|------|-------|------------|
| Funktionsumfang | 9 | 7 | 8 |
| Benutzerfreundlichkeit | 6 | 9 | 8 |
| Preis | 5 | 8 | 6 |
| Integration | 9 | 6 | 7 |
| Support | 8 | 7 | 7 |
| Skalierbarkeit | 9 | 7 | 8 |

### Schritt 5: Berechnung der gewichteten Punkte

**Formel:**
```
Gewichtete Punkte = Punkte × Gewichtung

Nutzwert (Alternative) = Summe aller gewichteten Punkte
```

**Beispiel:**

| Kriterium | Gewichtung | Jira | Gewichtet | Asana | Gewichtet | Monday | Gewichtet |
|-----------|------------|------|-----------|-------|-----------|--------|-----------|
| Funktionsumfang | 25% | 9 | 2,25 | 7 | 1,75 | 8 | 2,00 |
| Benutzerfreundlichkeit | 20% | 6 | 1,20 | 9 | 1,80 | 8 | 1,60 |
| Preis | 20% | 5 | 1,00 | 8 | 1,60 | 6 | 1,20 |
| Integration | 15% | 9 | 1,35 | 6 | 0,90 | 7 | 1,05 |
| Support | 10% | 8 | 0,80 | 7 | 0,70 | 7 | 0,70 |
| Skalierbarkeit | 10% | 9 | 0,90 | 7 | 0,70 | 8 | 0,80 |
| **Nutzwert** | **100%** | - | **7,50** | - | **7,45** | - | **7,35** |

### Schritt 6: Entscheidung treffen

**Auswertung:**
- Alternative mit **höchstem Nutzwert** wird empfohlen
- Bei knappem Ergebnis: Sensitivitätsanalyse durchführen

**Beispiel-Ergebnis:**
- **Jira: 7,50** (Sieger)
- Asana: 7,45
- Monday.com: 7,35

**Empfehlung:** Jira, da höchster Nutzwert

**Hinweis:** Wenn Ergebnisse sehr nah beieinander liegen (z.B. 7,50 vs. 7,45), sollten zusätzliche Faktoren oder eine Sensitivitätsanalyse berücksichtigt werden.

## Sensitivitätsanalyse

**Ziel:** Prüfen, wie robust die Entscheidung ist

**Fragen:**
- Was passiert, wenn Gewichtungen geändert werden?
- Wie stark beeinflusst ein einzelnes Kriterium das Ergebnis?
- Ist die Entscheidung stabil?

**Beispiel:**
- Wenn "Preis" auf 30% erhöht wird: Asana könnte gewinnen
- Wenn "Integration" wichtiger wird: Jira bleibt vorn

## Prüfungsrelevante Inhalte

**Wichtige Prüfungsfragen:**
1. Was ist die Nutzwertanalyse?
2. Schritte der Nutzwertanalyse
3. Gewichtung von Kriterien
4. Berechnung gewichteter Punkte
5. Vor- und Nachteile der Nutzwertanalyse
6. Praktische Anwendung in IT-Entscheidungen

**Typische Aufgaben:**
- Nutzwertanalyse für gegebene Alternativen durchführen
- Gewichtete Punkte berechnen
- Entscheidung treffen und begründen
- Kritische Reflexion der Methode

## Beispiele / Praxisbezug

### Beispiel 1: Server-Auswahl

**Ziel:** Auswahl eines neuen Servers für Rechenzentrum

**Alternativen:**
- Dell PowerEdge
- HP ProLiant
- Lenovo ThinkSystem

**Kriterien und Gewichtung:**
- Performance (30%)
- Preis (25%)
- Energieeffizienz (20%)
- Support (15%)
- Lieferzeit (10%)

**Bewertung:**

| Kriterium | Gewichtung | Dell | Gewichtet | HP | Gewichtet | Lenovo | Gewichtet |
|-----------|------------|------|-----------|-----|-----------|--------|-----------|
| Performance | 30% | 9 | 2,70 | 8 | 2,40 | 7 | 2,10 |
| Preis | 25% | 6 | 1,50 | 8 | 2,00 | 9 | 2,25 |
| Energieeffizienz | 20% | 8 | 1,60 | 7 | 1,40 | 8 | 1,60 |
| Support | 15% | 9 | 1,35 | 8 | 1,20 | 7 | 1,05 |
| Lieferzeit | 10% | 7 | 0,70 | 6 | 0,60 | 9 | 0,90 |
| **Nutzwert** | **100%** | - | **7,85** | - | **7,60** | - | **7,90** |

**Ergebnis:** Lenovo ThinkSystem (7,90) - beste Balance aus allen Kriterien

### Beispiel 2: Cloud-Anbieter-Auswahl

**Alternativen:** AWS, Azure, Google Cloud

**Kriterien:**
- Funktionsumfang (20%)
- Preis (25%)
- Performance (20%)
- Verfügbarkeit (15%)
- Compliance (10%)
- Support (10%)

**Ergebnis (verkürzt):**
- AWS: 7,8
- Azure: 8,1 ← **Empfehlung**
- Google Cloud: 7,4

### Beispiel 3: Dienstleister-Auswahl

**Ziel:** Auswahl IT-Dienstleister für Softwareentwicklung

**Kriterien:**
- Preis (30%)
- Referenzen/Erfahrung (25%)
- Technische Kompetenz (20%)
- Kommunikation (15%)
- Projektmanagement (10%)

**Nutzwertanalyse hilft bei objektiver, transparenter Entscheidung trotz weicher Faktoren.**

## Tipps für die Praxis

1. **Kriterien klar definieren:** Vermeiden Sie Überschneidungen
2. **Gewichtung im Team:** Holen Sie verschiedene Perspektiven ein
3. **Punktevergabe dokumentieren:** Begründen Sie Bewertungen
4. **Skala einheitlich nutzen:** Konsistenz bei allen Alternativen
5. **Sensitivität prüfen:** Testen Sie verschiedene Gewichtungen
6. **Nicht überbewerten:** NWA ist Hilfsmittel, nicht absolute Wahrheit

## Zusammenfassung

**Kernpunkte:**
- **Nutzwertanalyse:** Systematisches Bewertungsverfahren für mehrere Alternativen
- **6 Schritte:** Ziel/Alternativen → Kriterien → Gewichtung → Punktevergabe → Berechnung → Entscheidung
- **Formel:** Nutzwert = Σ (Punkte × Gewichtung)
- **Vorteil:** Berücksichtigung qualitativer Kriterien, Transparenz
- **Nachteil:** Subjektivität, Scheingenauigkeit
- **Anwendung:** Produktauswahl, Lieferantenauswahl, Make-or-Buy
- **Empfehlung:** Alternative mit höchstem Nutzwert

## Prüfungsfragen zum Üben

- [ ] Was ist die Nutzwertanalyse und wofür wird sie eingesetzt?
- [ ] Nennen Sie die 6 Schritte der Nutzwertanalyse.
- [ ] Wie berechnet man den Nutzwert einer Alternative?
- [ ] Drei Alternativen werden bewertet: Kriterium "Preis" (Gewichtung 40%), Punkte: A=8, B=6, C=9. Berechnen Sie die gewichteten Punkte.
- [ ] Welche Vor- und Nachteile hat die Nutzwertanalyse?
- [ ] Was ist eine Sensitivitätsanalyse und wann ist sie sinnvoll?
- [ ] Erstellen Sie eine Nutzwertanalyse für die Auswahl zwischen 3 Laptop-Modellen mit den Kriterien: Preis (30%), Performance (30%), Gewicht (20%), Akkulaufzeit (20%).
- [ ] Warum sollte die Summe der Gewichtungen immer 100% ergeben?

## Quellen

- [ ] IHK-Prüfungskatalog Fachinformatiker
- [ ] Entscheidungstheorie - Nutzwertanalyse
- [ ] VDI-Richtlinie 2225 (Technisch-wirtschaftliches Konstruieren)

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](10_Make_or_Buy.md) | [Nächstes Thema](12_Rentabilitaetsrechnung.md)
