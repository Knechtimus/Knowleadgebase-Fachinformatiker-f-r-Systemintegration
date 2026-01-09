# OSI-Modell

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen
## Lernziele
- [x] 7 Schichten des OSI-Modells kennen
- [x] Protokolle den Schichten zuordnen
- [x] Geräte den Schichten zuordnen

## Grundlagen

Das OSI-Modell (Open Systems Interconnection Model) ist ein Referenzmodell zur Beschreibung der Kommunikation in Netzwerken. Es unterteilt die Netzwerkkommunikation in 7 aufeinander aufbauende Schichten. Jede Schicht erfüllt spezifische Aufgaben und stellt Dienste für die darüberliegende Schicht bereit.

## Wichtige Begriffe

| Begriff   | Definition                                 |
|-----------|--------------------------------------------|
| OSI       | Open Systems Interconnection               |
| Schicht   | Ebene im OSI-Modell mit spezifischer Funktion |
| Protokoll | Vereinbarung zur Kommunikation zwischen Systemen |
| PDU       | Protocol Data Unit, Datenpaket einer Schicht |

## OSI-Modell 7 Schichten

| Schicht | Name                        | Protokolle                        | Geräte                | PDU         |
|---------|-----------------------------|-----------------------------------|-----------------------|-------------|
| 7       | Anwendung (Application)     | HTTP, FTP, SMTP                   | Computer, Server      | Daten       |
| 6       | Darstellung (Presentation)  | SSL, TLS, JPEG, MPEG              | Computer, Server      | Daten       |
| 5       | Sitzung (Session)           | NetBIOS, RPC, SMB                 | Computer, Server      | Daten       |
| 4       | Transport                   | TCP, UDP                          | Gateway, Firewall     | Segment     |
| 3       | Vermittlung (Network)       | IP, ICMP, ARP                     | Router                | Paket       |
| 2       | Sicherung (Data Link)       | Ethernet, PPP, Switch-Protokolle  | Switch, Bridge        | Frame       |
| 1       | Bitübertragung (Physical)   | Ethernet, DSL, WLAN, Kabel        | Hub, Repeater, Kabel  | Bit         |

## Prüfungsrelevante Inhalte

- Die Aufgaben und Funktionen jeder Schicht kennen
- Typische Protokolle und Geräte den Schichten zuordnen können
- Unterschiede zwischen OSI-Modell und TCP/IP-Modell verstehen

## Beispiele / Praxisbezug

- Ein Switch arbeitet auf Schicht 2 (Sicherungsschicht)
- Ein Router arbeitet auf Schicht 3 (Vermittlungsschicht)
- HTTPS nutzt Protokolle der Schichten 7 (HTTP), 6 (TLS/SSL) und 4 (TCP)

## Zusammenfassung

Das OSI-Modell hilft, Netzwerkkommunikation zu strukturieren und zu verstehen. Es ist prüfungsrelevant, die Schichten, deren Aufgaben, typische Protokolle und Geräte zu kennen.

## Prüfungsfragen zum Üben

- [ ] Welche 7 Schichten hat das OSI-Modell?
- [ ] Auf welcher Schicht arbeitet ein Router?
- [ ] Auf welcher Schicht arbeitet ein Switch?

## Quellen

- [ ] Noch keine Quellen

---
[↩ Zurück zur Übersicht](../README.md) | [Nächstes Thema](02_TCP_IP_Protokollstack.md)
