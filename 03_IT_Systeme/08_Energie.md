# Stromkosten berechen

## Formel zur Berechnung der Stromkosten

Die Stromkosten berechnen sich mit folgender Formel:

```
Stromkosten = (Watt / 1000) × Stunden × Tage × Preis (€/kWh)
```

**Beispielrechnung:**

Ein Gerät mit 300 W läuft 8 Stunden am Tag, an 200 Tagen im Jahr. Der Strompreis beträgt 0,40 €/kWh.

```
Stromkosten = (300 W / 1000) × 8 h × 200 × 0,40 €/kWh
            = 0,3 kW × 8 × 200 × 0,40 €
            = 192 €
```

> **Merke:**  
> 1 kW = 1000 W  
> Watt immer zuerst in kW umrechnen!

---

## Wirkungsgrad berechnen

Der Wirkungsgrad (𝜂) gibt an, wie effizient ein Gerät arbeitet:

```
𝜂 = Nutzleistung / Eingangsleistung
```

**Beispiel:**

- Nutzleistung: 450 W  
- Eingangsleistung: 500 W

```
𝜂 = 450 W / 500 W = 0,9 = 90 %
```

> **Merke:**  
> Je höher der Wirkungsgrad, desto geringer der Energieverlust.  
> Netzteile erreichen meist 80–95 % Wirkungsgrad.

---

## USV-Arten (Unterbrechungsfreie Stromversorgung)

| USV-Art           | Abkürzung | Eigenschaften                                         | Einsatzbereich                   |
|-------------------|-----------|-------------------------------------------------------|----------------------------------|
| **Offline**       | VFD       | Schaltet bei Stromausfall um, kurze Umschaltzeit      | Einfache PCs                     |
| **Line-Interactive** | VI     | Spannungsregelung, kurze Umschaltzeit                 | Server, Netzwerkgeräte           |
| **Online**        | VFI       | Dauerhafte Doppelwandlung, keine Umschaltzeit         | Kritische Systeme (Rechenzentrum) |

