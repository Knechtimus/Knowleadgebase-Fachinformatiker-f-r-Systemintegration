# AP1 Fruehjahr 2022 Aufgabe 2 Lösung
#### Von [Vrbanic](<../../../../user/Auszubildende Michel/vrbanic.md>)

----

## Aufgabe 4 - SQL und Diagramme - 24 Punkte:
### Aufgabe 4a) - Walzanlage
![Aufgabe 4a Aufgabenstellung](image-137.png)
### Aufgabe 4aa) - Output ohne ID - 3 Punkte
![Aufgabe 4aa](image-138.png)
### Aufgabe 4ab) - Spezfizierte Dicke - 4 Punkte
![Aufgabe 4ab](image-139.png)
### Aufgabe 4ac) - Produktionsanzahl - 4 Punkte
![Aufgabe 4ac](image-140.png)
### Aufgabe 4b) - Struktogramm - 7 Punkte
![Aufgabe 4b](image-141.png)
### Aufgabe 4b Vorlage) - Struktogramm Vorlage
![Aufgabe 4b Vorgabe](image-142.png)
### Aufgabe 4c) - Entity-Relationship-Modell - 6 Punkte
![Aufgabe 4c](image-143.png)
### Aufgabe 4c Vorlage) - Entity-Relationship-Modell Vorlage
![Aufgabe 4c Vorgabe](image-144.png)

----

## Lösung zur Aufgabe 4:
### Aufgabe 4aa)
SELECT Width, Length, Thickness, Quantity FROM ProductionData WHERE OrderID = 736298;

### Aufgabe 4ab)
SELECT COUNT(*) FROM ProductionData WHERE Thickness = 2;

### Aufgabe 4ac)
SELECT SUM(Quantity) FROM ProductionData WHERE Thickness = 2 AND Width = 200 AND Length = 300;

### Aufgabe 4b)
![Aufgabe 4b Solution](image-145.png)

### Aufgabe 4c)
![Aufgabe 4c Solution](image-146.png)

----

## Selbsterstellte Aufgabe:
###### Selbsterstellte Aufgabe Vrbanic
### Aufgabe Xa)
>**Xa)** Sie erhalten den Auftrag sich um die Lagerverwaltung einer Firma zu kümmern. Die Lagerdaten werden in einer SQL-Datenbank gespeichert. Zahlen wurden als Ganzzahlen eingetragen.
>
>Die Tabelle ProductList hat folgenden Aufbau
>
>>ProductID (PK)
>>Productname
>>Stock
>>Minimumstock
>>Supplier

### Aufgabe Xaa)
>**Xaa)** Finden sie alle Produkte, deren Lagerbestand unter dem Mindestbestand liegt.
>
> Geben sie dazu den entsprechenden SQL-Befehl an.

### Aufgabe Xab)
>**Xab)** Bestimme die Gesamtzahl an Produkten des Lieferanten "Firefly".
>
> Geben sie dazu den entsprechenden SQL-Befehl an.

### Aufgabe Xac)
>**Xac)** Bereche den durchschnittlichen Lagerbestand aller Produkte.
>
> Geben sie dazu den entsprechenden SQL-Befehl an.

### Aufgabe Xad)
>**Xad)** Der Mindestbestand für alle Produkte wird um 5 erhöht.
>
> Geben sie dazu den entsprechenden SQL-Befehl an.

### Aufgabe Xae)
>**Xae)** Es wurde das Produkt mit der ID '42' aus dem Sortiment genommen und nun muss die Datenbank angepasst werden.
>
> Geben sie dazu den entsprechenden SQL-Befehl an.

### Aufgabe Xb)
>**Xb)** Erstellen sie ein Struktogramm für die Erfassung einer Produktliste die besagt welche Produkte unter ihrem Mindestwert sind. Die Firma besitzt zurzeit 26 verschiedene Produkte.
>
> Erstellen sie die Funktion createOrderList(products[])
>
> **fetchMinStock(int)** - Übergeben wird ein Produkt. Gibt den Minimumswert eines Produkts wieder.
> 
> **fetchStock(int)** - Übergeben wird ein Produkt. Gibt den momentanen Inventarstand wieder.
>
> Ergänzen sie das gegebene Struktogramm durch die entsprechenden Befehle um eine Liste zum Bestellen von Produkten zu erstellen.

![Aufgabe 4c](image-147.png)

----

## Lösung zur Selbsterstellten Aufgabe:
### Aufgabe Xaa)
SELECT `ProductID` FROM `ProductList` WHERE `Stock` < `Minimumstock`;

### Aufgabe Xab)
SELECT COUNT(`ProductID`) FROM `ProductList` WHERE `Supplier` = 'Firefly';

### Aufgabe Xac)
SELECT AVG(`Stock`) FROM `ProductList`;

### Aufgabe Xad)
UPDATE `ProductList` SET `Minimumstock` = `Minimumstock` + 5;

### Aufgabe Xae)
DELETE FROM `ProductList` WHERE `ProductID` = '42';

### Aufgabe Xb)
![Aufgabe Xb](image-148.png)
