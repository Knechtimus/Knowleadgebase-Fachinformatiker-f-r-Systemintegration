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

### IPv4 Subnetting

| Formel | Beschreibung |
|--------|--------------|
| Anzahl Subnetze = 2^n | n = Anzahl der geliehenen Bits |
| Anzahl Hosts = 2^h - 2 | h = Anzahl der Host-Bits |
| Subnetzmaske = 255.255.255.x | x basierend auf CIDR |

### CIDR-Notation

| CIDR | Subnetzmaske | Hosts |
|------|--------------|-------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

### Netzwerk-Berechnung

- **Netzadresse**: Erste IP im Subnetz (Host-Teil = 0)
- **Broadcast-Adresse**: Letzte IP im Subnetz (Host-Teil = 1)
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

### Kostenrechnung

| Formel | Beschreibung |
|--------|--------------|
| Gesamtkosten = Fixkosten + Variable Kosten | Vollkosten |
| Stückkosten = Gesamtkosten / Menge | Kosten pro Einheit |
| DB = Erlös - Variable Kosten | Deckungsbeitrag |

### Amortisation

| Formel | Beschreibung |
|--------|--------------|
| Amortisationszeit = Investition / Jährliche Einsparung | Rückflusszeit |

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

- [ ] Noch keine Quellen

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](AP2_Checkliste.md) | [Nächstes Thema](Befehlsreferenz_CLI.md)
