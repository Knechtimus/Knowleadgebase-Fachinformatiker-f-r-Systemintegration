# Merkmale und Methoden des Projektmanagements

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Lernziele
- [ ] Merkmale eines Projekts nach DIN 69901-5 verstehen
- [ ] Projektstrukturplan erstellen können
- [ ] Unterschiede zwischen Lasten- und Pflichtenheft kennen
- [ ] Netzplantechnik anwenden können
- [ ] SMART-Prinzip anwenden
- [ ] Wasserfallmodell und Scrum verstehen
- [ ] Gantt-Diagramme lesen und erstellen
- [ ] Teamphasen kennen

## Grundlagen

Projektmanagement ist die Gesamtheit von Führungsaufgaben, -organisation, -techniken und -mitteln zur Abwicklung eines Projekts. In der IT-Systemintegration ist professionelles Projektmanagement essentiell für:

- **Strukturierte Planung** von IT-Projekten (Installation, Migration, Implementierung)
- **Termingerechte Umsetzung** unter Einhaltung von Zeitvorgaben und Meilensteinen
- **Budgetkontrolle** und Einhaltung der Kostenplanung
- **Qualitätssicherung** der zu liefernden IT-Lösungen
- **Risikomanagement** zur frühzeitigen Erkennung und Vermeidung von Problemen
- **Koordination** verschiedener Stakeholder (Kunde, Team, Management)

Ein Projekt durchläuft typischerweise folgende **Phasen**:
1. **Initialisierung** - Projektauftrag, Zieldefinition
2. **Planung** - Ressourcen, Zeit, Kosten, Risiken
3. **Durchführung** - Umsetzung der geplanten Aufgaben
4. **Controlling** - Überwachung und Steuerung (parallel zur Durchführung)
5. **Abschluss** - Abnahme, Dokumentation, Lessons Learned

**Magisches Dreieck des Projektmanagements:**
Die drei Hauptfaktoren stehen in gegenseitiger Abhängigkeit:
- **Zeit** (Termine, Dauer)
- **Kosten** (Budget, Ressourcen)
- **Qualität** (Leistungsumfang, Anforderungen)

Änderungen an einem Faktor beeinflussen automatisch die anderen beiden Faktoren.

## Wichtige Begriffe

| Begriff | Definition |
|---------|------------|
| Projekt | |
| Projektmanagement | |
| Meilenstein | |
| Sprint | |
| Gantt-Diagramm | |

## Merkmale eines Projekts (DIN 69901-5)
Projekte lassen sich durch spezifische Merkmale definieren:
Jedes Projekt hat ein Vorgegebenes Ziel, meist basierend auf eine Problemstellung.
Projekte kann man auch als Problemlösung für neuartige Aufgaben mit großem Spektrum sehen.
Solche Projekte werden auch meist nur einmal durchgeführt, oder können bspw. Bei mehreren 
Standorten auch als Blueprint dienen.
Aus der DIN 69901-5 lässt sich auch folgende Definiton zu einem Projekt finden:
Ein Projekt ist ein Vorhaben, das im Wesentlichen durch Einmaligkeit der Bedinugngen in ihrer 
Gesamtheit gekennzeichnet ist.
Es kennzeichnet sich aus durch:
- Eine Zielvorgabe
- Zeitliche, finanzielle, personelle oder andere Begrenzugen
- Eine projektspezifische Organisation


## Projektstrukturplan

Ein Strukturplan ist im Großen und Ganzen die Gliederung eines Projektes in einzelne 
Elemente.
Das Primäre Ziel ist hier, alle Elemente in planbare und kontrollierbare Teilaufgaben und 
Arbeitspakete zu zerlegen. So erhält man ein ordentlichen Gesamtüberblick des gesamten 
Projektes

### Methoden
- **Top-Down**: 
Das Projekt wird zuerst als ganzes betrachtet, dann werden einzelne 
Teilaufgaben/Teilprojekte identifiziert und definiert, woraus sich dann die Arbeitspakete 
und einzelnen Teilaufgaben festlegen.
- **Bottom-Up**: 
Der Bottom-Up Ansatz ist entgegengesetzt dem Top-Down Ansatz. Welche 
Arbeitspakete sind Nötig, in welche Teilprojekte lassen sich diese dann definieren, um 
das Ziel des Gesamtprojektes zu erreichen bzw. dieses zu definieren?
- **Yo-Yo**: 
Beim Yo-Yo Ansatz wird von beiden Richtungen gleichzeitig geplant

## Lasten- und Pflichtenheft

**Lastenheft:**
Das Lastenheft beschreibt die Anforderungen und Erwartungen des Auftraggebers an das 
Projekt. Es legt fest, was das zu entwickelndes System oder Produkt leisten soll, ohne jedoch 
technische Details zu definieren.

**Pflichtenheft:**
Das Pflichtenheft wird vom Auftragnehmer erstellt und beschreibt, wie die im Lastenheft 
definierten Anforderungen umgesetzt werden. Es enthält konkrete technische Lösungen, 
Verfahren und Vorgehensweisen, um die Anforderungen zu erfüllen.


## Netzplantechnik

Nach DIN 69 900 ist ein Netzplan wie folgt definiert:
Ein Netzplan ist eine grafische oder tabellarische Darstellung einer Ablaufstruktur, die aus 
Vorgängen bzw. Ereignissen und Anordnungsbeziehungen besteht.

Ein solcher Netzplan hilft, eine Terminplanung zu bilden.
Es hilft, eine Gesamtdauer des Projektes festzulegen und eine zeitliche und logische Abfolge 
der Vorgänge im Projekt zu definieren.
Hierraus können sich dann kritische Pfade und Vorgänge identifizieren, die essenziell wichtig 
für das geplante Projektende sind und hilft, Puffer und Zeitreserven herauszufinden.

### Netzplan-Begriffe

| Abkürzung | Bedeutung |
|-----------|-----------|
| FAZ | Frühester Anfangszeitpunkt |
| FEZ | Frühester Endzeitpunkt |
| SAZ | Spätester Anfangszeitpunkt |
| SEZ | Spätester Endzeitpunkt |
| GP | Gesamtpuffer (GP = SAZ - FAZ oder GP = SEZ - FEZ) |
| FP | Freier Puffer (FP = FAZ des Nachfolgers - FEZ des Vorgängers) |

**Vorwärtsrechnung:** Prozess beginnt mit dem Startpunkt des Projekts, nach vorne Arbeiten

**Beispiel:** 

Aufgabe A hat eine Dauer von 3 Tagen und keine Vorgänger, also ist der FAZ der 1. Tag und 
FEZ der 3. Tag.
Aufgabe B hat eine Dauer von 5 Tagen und ist von Aufgabe A abhängig. Der FAZ von B ist der 
4. Tag (EF von A + 1), der FEZ von B ist der 8. Tag (ES von B + Dauer).

**Rückwärtsrechnung:** Spätester Start- und Endzeitpunkt

Man beginnt bei der Letzten Aufgabe.
Angenommen, das Projekt hat eine Gesamtdauer von 10 Tagen. Aufgabe C dauert 5 Tage
Aufgabe C ist der letzte Vorgang und hat keine Nachfolger, also ist der SEZ der 10. Tag und 
der SAZ der 6. Tag (LF - Dauer).

## SMART-Prinzip

| Buchstabe | Bedeutung | Beschreibung |
|-----------|-----------|--------------|
| S | Spezifisch | Ziele müssen eindeutig definiert sein |
| M | Messbar | Ziele müssen messbar sein |
| A | Attraktiv | Ziele sind Ansprechend bzw. Erstrebenswert |
| R | Realistisch | Das gestreckte Ziele muss möglich realisierbar sein |
| T | Terminiert | Das Ziel muss mit einem fixen Datum festgelegt werden |

## Meilensteine
Meilensteine sind Bestandteil desd klassischen Projektmanagements, an einem Meilenstein wird ein bestimmtes Ziel erreicht oder ein definiertes Ergebnis erarbeitet.
Das Erarbeiten / Erreichen aller Ziele ist wichtig für das gelingen des Projektes.

![Meilensteinbild](https://projekte-leicht-gemacht.de/wp-content/uploads/2015/07/phasenplanung3.jpg)

## Wasserfallmodell

![Wasserfallmodell](https://blog.assets.studyflix.de/wp-content/uploads/2023/06/Wasserfallmodell-Projektmanagement-1-1024x576.jpg)

Im Wasserfallmodell "fließt" eine Projektphase in die Nächste - immer in eine Richtung, ohne die Reihenfolge zu verändern, wie ein Wasserfall.

-> die Phasen sind dadurch klar abgegrenzt.

## Scrum

Scrum ist ein Agiles Modell im Projektmanagement, was darauf basiert, flexibel und iterative (wiederholende) Prozesse zu verwenden, um das Projekt effizient steuern und entwickeln zukönnen

Ein Sprint int eine festgelegte Entwicklungsphase, in der Regel 1-4 Wochen lang, in der es eine Sprintplanung und ein Sprint-Review gibt. Dieser darf nicht unterbrochen werden.

In einem Daily Scrum bspw. wird in 15 Minuten der aktuelle Stand geteilt, oft auch "Standup" genannt. Hier wird versucht Hindernisse frühzeitig zu erkennen und zu beheben.


### Scrum-Rollen

| Rolle | Beschreibung |
|-------|--------------|
| Scrum Master | Sorgt für Einhaltung der Regeln. beteiligt sich nicht an der Entwicklung |
| Entwicklerteam | 3 bis max 9 Personen. Entwickler, tester und Architekten |
| Product Owner | kümmert sich um das Produkt Backlog und die Schnittstelle zwischen Kunden und Projektbeteiligten |
| Stakeholder | Alle Personen, die Interesse an einem Projekt haben und beinflusst werden können z.B. Kunden, Investoren aber auch Führungskräfte |

### Scrum-Artefakte
- Product Backlog - Priorisierte Liste aller Anforderungen/Features für da Produkt. Wird vom Product owner Verwaltet
- Sprint Backlog - Ausgewählte Items aus dem Product Backlog für den aktuellen Sprint + Plan zur Umsetzung
- Increment - Die Summe aller fertigen Product Backlog Items am Ende eines Sprints. Muss der "Definition of Done" entsprechen.

### Scrum-Events 

| Event | Beschreibung | Timebox |
|-------|--------------|---------|
| Sprint Planning | Planung der Arbeit für den kommenden Sprint. Was wird erledigt? Wie wird es umgesetzt? | Max. 8h (bei 4-Wochen-Sprint) |
| Daily Scrum | Tägliches Stand-up-Meeting zur Synchronisation des Teams. Was habe ich getan? Was werde ich tun? Gibt es Hindernisse? | Max. 15 Min. |
| Sprint Review | Präsentation des Increments vor Stakeholdern. Feedback einholen. | Max. 4h |
| Sprint Retrospective | Team reflektiert den vergangenen Sprint: Was lief gut? Was kann verbessert werden? | Max. 3h |

## Gantt-Diagramm

Zeitliche Abfolge von Aktivitäten grafisch in Form von Balken auf einer Zeitachse. Dies hilft eine realistische Terminierung zu erhalten, wie die Aufgaben miteinander verknüpft sind und welche evt. sich überschneiden und Parallel laufen.

Hier sind auch wichtige Bestandteile der Projektphasen ersichtlich. Sinnvoll ist es z.B. Meilensteine mit dem Gantt-Diagramm zu verknüfen
<!-- TODO: Gantt-Diagramm Beispiel und Erklärung ergänzen -->

![Gantt-Diagramm](image.png)

## Teamphasen nach Tuckman

| Phase | Beschreibung |
|-------|--------------|
| Forming | Formieren, kennenlernen, klarstellung der Rollen & auflösen von anfänglicher Unsicherheit |
| Storming | zubeginn kommt es häufig zu Diskussionen mit Interessengegensätzen und Meinungsverschiedenheiten |
| Norming | Team findet seinen Rhythmus. Individuelle Rollenverteilung und Arbeitsweisen sind bekannt |
| Performing | ab hier ist das Team vollständig eingespielt und verfolgt gemeinsam ein Ziel und können Potenzial voll ausschöpfen |
| Adjourning | das Team wird aufgelöst und Erfolg wird besprochen. Das Projekt ist hier abgeschlossen |

## Reflektionsmethoden

Eine Feedback-Kultur ist wichtig, um im Projektablauf reflektieren zu können. Regelmäßig sollte hier kontstruktive und offene Rückmeldungen passieren

### Lessons Learned

Hier werden nach Abschluss eines Projektes oder einer Phase die wichtigsten Erkenntnisse und Erfarungen zusammengetragen. Hauptsächlich, um aus Erfolgen und Misserfolgen zu lernen, diese dann dokumentiert in zukünftige Projekte einfließen zulassen und eine kontinuierliche Verbesserung zu gewährleisten

## Prüfungsrelevante Inhalte

- **DIN 69901-5:** Merkmale eines Projekts (Einmaligkeit, Zielvorgabe, Begrenzungen, projektspezifische Organisation)
- **Magisches Dreieck:** Zeit, Kosten, Qualität und deren Abhängigkeiten
- **Projektstrukturplan:** Top-Down, Bottom-Up, Yo-Yo Methoden
- **Lasten- vs. Pflichtenheft:** Wer erstellt was? (Auftraggeber vs. Auftragnehmer)
- **Netzplantechnik:** FAZ, FEZ, SAZ, SEZ, GP, FP berechnen können
- **Kritischer Pfad:** Vorgänge ohne Puffer identifizieren
- **SMART-Prinzip:** Alle 5 Buchstaben mit Bedeutung
- **Scrum:** Rollen (Scrum Master, Product Owner, Entwicklerteam), Artefakte, Events
- **Wasserfallmodell vs. Agile:** Vor- und Nachteile beider Ansätze
- **Teamphasen nach Tuckman:** Reihenfolge und Merkmale jeder Phase

## Beispiele / Praxisbezug

**Beispiel IT-Projekt:** Migration eines Unternehmens auf Microsoft 365
- **Lastenheft:** "E-Mail-System soll in die Cloud migriert werden, 500 Postfächer, max. 2h Downtime"
- **Pflichtenheft:** "Migration erfolgt mittels Exchange Hybrid, Cutover am Wochenende, Testphase 2 Wochen"

**Netzplan-Beispiel:**
| Vorgang | Dauer | Vorgänger | FAZ | FEZ | SAZ | SEZ | GP |
|---------|-------|-----------|-----|-----|-----|-----|-----|
| A - Planung | 3 | - | 1 | 3 | 1 | 3 | 0 |
| B - Beschaffung | 5 | A | 4 | 8 | 4 | 8 | 0 |
| C - Dokumentation | 2 | A | 4 | 5 | 7 | 8 | 3 |
| D - Installation | 4 | B,C | 9 | 12 | 9 | 12 | 0 |

→ Kritischer Pfad: A → B → D (kein Puffer)

## Zusammenfassung

Projektmanagement umfasst die strukturierte Planung, Durchführung und Kontrolle von Projekten. Kernelemente sind:

1. **Projektdefinition** nach DIN 69901-5 mit klaren Merkmalen
2. **Planungsinstrumente:** Projektstrukturplan, Netzplantechnik, Gantt-Diagramme
3. **Dokumentation:** Lastenheft (WAS) → Pflichtenheft (WIE)
4. **Vorgehensmodelle:** Klassisch (Wasserfall) vs. Agil (Scrum)
5. **Teamführung:** Teamphasen nach Tuckman beachten
6. **Zieldefinition:** SMART-Prinzip anwenden
7. **Reflexion:** Lessons Learned für kontinuierliche Verbesserung

## Prüfungsfragen zum Üben

- [ ] Was sind die Merkmale eines Projekts nach DIN 69901-5?
- [ ] Welche Methoden gibt es zur Erstellung eines Projektstrukturplans?
- [ ] Was ist der Unterschied zwischen Lasten- und Pflichtenheft?
- [ ] Welche Rollen gibt es in Scrum?
- [ ] Was bedeutet SMART in Bezug auf Projektziele?

## Quellen

- [ ] Noch keine Quellen

---
[↩ Zurück zur Übersicht](../README.md) | [Nächstes Thema](02_Machbarkeit_Wirtschaftlichkeit.md)
