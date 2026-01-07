# Formelsammlung

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Elektrotechnik-Formeln

| Größe | Formel | Einheit | Beschreibung |
|-------|--------|---------|--------------|
| Spannung (U) | U = R × I | Volt (V) | Ohmsches Gesetz |
| Stromstärke (I) | I = U / R | Ampere (A) | Ohmsches Gesetz |
| Widerstand (R) | R = U / I | Ohm (Ω) | Ohmsches Gesetz |
| Leistung (P) | P = U × I | Watt (W) | Elektrische Leistung |
| Leistung (P) | P = R × I² | Watt (W) | Alternative Formel |
| Leistung (P) | P = U² / R | Watt (W) | Alternative Formel |
| Energie (E) | E = P × t | Wattstunde (Wh) | Elektrische Arbeit |
| Gesamtwiderstand (Reihe) | R_ges = R₁ + R₂ + ... + Rₙ | Ohm (Ω) | Reihenschaltung |
| Gesamtwiderstand (Parallel) | 1/R_ges = 1/R₁ + 1/R₂ + ... + 1/Rₙ | Ohm (Ω) | Parallelschaltung |

## Übertragungsraten-Formeln

### Binär vs. Dezimal

| Einheit (Binär) | Wert | Einheit (Dezimal) | Wert |
|-----------------|------|-------------------|------|
| 1 KiB (Kibibyte) | 1024 Byte | 1 KB (Kilobyte) | 1000 Byte |
| 1 MiB (Mebibyte) | 1024 KiB | 1 MB (Megabyte) | 1000 KB |
| 1 GiB (Gibibyte) | 1024 MiB | 1 GB (Gigabyte) | 1000 MB |
| 1 TiB (Tebibyte) | 1024 GiB | 1 TB (Terabyte) | 1000 GB |

### Datenübertragung

| Formel | Beschreibung |
|--------|--------------|
| Übertragungszeit = Datenmenge / Übertragungsrate | Zeit für Datenübertragung |
| Datenmenge = Übertragungsrate × Zeit | Übertragene Datenmenge |
| Übertragungsrate = Datenmenge / Zeit | Geschwindigkeit der Übertragung |

### Bit und Byte

- 1 Byte = 8 Bit
- 1 Kilobit (Kbit) = 1000 Bit
- 1 Megabit (Mbit) = 1000 Kbit = 1.000.000 Bit
- 1 Gigabit (Gbit) = 1000 Mbit = 1.000.000.000 Bit

**Umrechnung Bit/s in Byte/s:**
- Teile durch 8: z.B. 100 Mbit/s = 12,5 MB/s

## Subnetting-Formeln

### IPv4 Subnetting - Die wichtigsten Formeln! 🔴

```
Anzahl verfügbarer Hosts = 2^(32 - Präfixlänge) - 2
Anzahl Subnetze = 2^(geliehene Bits)

Netzadresse = Erste IP-Adresse im Subnetz
Broadcast-Adresse = Letzte IP-Adresse im Subnetz
Erste nutzbare IP = Netzadresse + 1
Letzte nutzbare IP = Broadcast-Adresse - 1
```

**Beispiel:**
- 192.168.1.0/26
- Hosts: 2^(32-26) - 2 = 2^6 - 2 = 64 - 2 = **62 nutzbare Hosts**
- Netzadresse: 192.168.1.0
- Broadcast: 192.168.1.63
- Erste nutzbare IP: 192.168.1.1
- Letzte nutzbare IP: 192.168.1.62

### CIDR-Notation (AUSWENDIG LERNEN!)

| CIDR | Subnetzmaske | Binär (letzte 8 Bit) | Hosts (nutzbar) | Hosts (total) |
|------|--------------|----------------------|-----------------|---------------|
| /24 | 255.255.255.0 | 00000000 | 254 | 256 |
| /25 | 255.255.255.128 | 10000000 | 126 | 128 |
| /26 | 255.255.255.192 | 11000000 | 62 | 64 |
| /27 | 255.255.255.224 | 11100000 | 30 | 32 |
| /28 | 255.255.255.240 | 11110000 | 14 | 16 |
| /29 | 255.255.255.248 | 11111000 | 6 | 8 |
| /30 | 255.255.255.252 | 11111100 | 2 | 4 |
| /31 | 255.255.255.254 | 11111110 | 2 (Punkt-zu-Punkt) | 2 |
| /32 | 255.255.255.255 | 11111111 | 1 (Host-Route) | 1 |

### Erweiterte CIDR-Tabelle (alle Klassen)

| CIDR | Subnetzmaske | Netzwerke (Klasse C) | Hosts |
|------|--------------|----------------------|-------|
| /8 | 255.0.0.0 | 1 × Klasse A | 16.777.214 |
| /16 | 255.255.0.0 | 1 × Klasse B | 65.534 |
| /17 | 255.255.128.0 | 2 × /17 | 32.766 |
| /18 | 255.255.192.0 | 4 × /18 | 16.382 |
| /19 | 255.255.224.0 | 8 × /19 | 8.190 |
| /20 | 255.255.240.0 | 16 × /20 | 4.094 |
| /21 | 255.255.248.0 | 32 × /21 | 2.046 |
| /22 | 255.255.252.0 | 64 × /22 | 1.022 |
| /23 | 255.255.254.0 | 128 × /23 | 510 |

### Subnetz-Schrittweite berechnen

**Formel:** Schrittweite = 256 - Oktettwert der Subnetzmaske

**Beispiel:**
- /26 = 255.255.255.192
- Schrittweite = 256 - 192 = **64**
- Subnetze: 0, 64, 128, 192

### Netzwerk-Berechnung

- **Netzadresse**: Erste IP im Subnetz (Host-Teil = alle Bits 0)
- **Broadcast-Adresse**: Letzte IP im Subnetz (Host-Teil = alle Bits 1)
- **Erste nutzbare IP**: Netzadresse + 1
- **Letzte nutzbare IP**: Broadcast-Adresse - 1

## Netzplantechnik

| Abkürzung | Formel | Beschreibung |
|-----------|--------|--------------|
| FAZ | max(FEZ aller Vorgänger) | Frühester Anfangszeitpunkt |
| FEZ | FAZ + Dauer | Frühester Endzeitpunkt |
| SEZ | min(SAZ aller Nachfolger) | Spätester Endzeitpunkt |
| SAZ | SEZ - Dauer | Spätester Anfangszeitpunkt |
| GP | SAZ - FAZ = SEZ - FEZ | Gesamtpuffer |
| FP | FAZ(Nachfolger) - FEZ | Freier Puffer |

## Wirtschaftlichkeitsrechnung

### Nutzwertanalyse 🔴

**Grundformel:**
```
Gewichtete Punktzahl = Punkte × Gewichtung
Gesamtnutzwert = Summe aller gewichteten Punktzahlen
```

**Vorgehen:**
1. Kriterien definieren
2. Gewichtung festlegen (Summe = 100% oder 1,0)
3. Alternativen bewerten (z.B. 1-10 Punkte)
4. Gewichtete Punktzahlen berechnen
5. Gesamtnutzwert ermitteln
6. Alternative mit höchstem Nutzwert wählen

**Beispiel:**

| Kriterium | Gewichtung | Alternative A | Gewichtet A | Alternative B | Gewichtet B |
|-----------|------------|---------------|-------------|---------------|-------------|
| Preis | 40% | 8 | 3,2 | 6 | 2,4 |
| Leistung | 30% | 7 | 2,1 | 9 | 2,7 |
| Qualität | 30% | 9 | 2,7 | 7 | 2,1 |
| **Gesamt** | **100%** | - | **8,0** | - | **7,2** |

**Entscheidung:** Alternative A (höherer Nutzwert)

### Kostenrechnung

| Formel | Beschreibung |
|--------|--------------|
| Gesamtkosten = Fixkosten + Variable Kosten | Vollkosten |
| Stückkosten = Gesamtkosten / Menge | Kosten pro Einheit |
| DB = Erlös - Variable Kosten | Deckungsbeitrag |
| DB% = (DB / Erlös) × 100% | Deckungsbeitragsquote |

### Angebotsvergleich

**Gesamtkosten über Nutzungsdauer:**
```
Gesamtkosten = Anschaffungskosten + (Laufende Kosten × Nutzungsjahre)
```

**Beispiel:**
- Alternative A: 10.000 € Kauf + (500 €/Jahr × 5 Jahre) = 12.500 €
- Alternative B: 2.000 € Kauf + (2.500 €/Jahr × 5 Jahre) = 14.500 €
- **Entscheidung:** Alternative A günstiger

### Amortisation

| Formel | Beschreibung |
|--------|--------------|
| Amortisationszeit = Investition / Jährliche Einsparung | Rückflusszeit |

**Beispiel:**
- Investition: 30.000 €
- Jährliche Einsparung: 10.000 €
- Amortisationszeit: 30.000 / 10.000 = **3 Jahre**

## RAID-Level

| Level | Mindest-Festplatten | Speichereffizienz | Ausfall-Toleranz |
|-------|-------------------|-------------------|------------------|
| RAID 0 | 2 | 100% | 0 Festplatten |
| RAID 1 | 2 | 50% | 1 Festplatte |
| RAID 5 | 3 | (n-1)/n | 1 Festplatte |
| RAID 6 | 4 | (n-2)/n | 2 Festplatten |
| RAID 10 | 4 | 50% | 1 pro Spiegelpaar |

## Verfügbarkeit

| Formel | Beschreibung |
|--------|--------------|
| Verfügbarkeit = (Betriebszeit / Gesamtzeit) × 100% | Verfügbarkeit in Prozent |
| Ausfallzeit = Gesamtzeit - Betriebszeit | Downtime |

### Verfügbarkeitsklassen

| Verfügbarkeit | Ausfallzeit/Jahr | Bezeichnung |
|---------------|------------------|-------------|
| 99% | 3,65 Tage | Zwei Neuner |
| 99,9% | 8,76 Stunden | Drei Neuner |
| 99,99% | 52,56 Minuten | Vier Neuner |
| 99,999% | 5,26 Minuten | Fünf Neuner |

## Quellen

- [01_Projektmanagement](../01_Projektmanagement/)
- [04_Netzwerktechnik](../04_Netzwerktechnik/)
- [12_Wirtschaft_Recht](../12_Wirtschaft_Recht/)

---

## 🔗 Navigation

- [Zum Lernplan](./AP1_Lernplan.md)
- [Zur AP1 Checkliste](./AP1_Checkliste.md)
- [Zu Ressourcen und Links](./Ressourcen_und_Links.md)
- [Zur Befehlsreferenz](./Befehlsreferenz_CLI.md)

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](AP2_Checkliste.md) | [Nächstes Thema](Befehlsreferenz_CLI.md)
