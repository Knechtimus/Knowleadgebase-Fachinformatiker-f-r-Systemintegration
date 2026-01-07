# Befehlsreferenz CLI

> 📝 **Prüfungsrelevanz:** AP1 + AP2
> 🔖 **Lernstatus:** ⬜ Nicht begonnen | 🔄 In Bearbeitung | ✅ Abgeschlossen

## Windows-Befehle (CMD/PowerShell)

### Dateisystem

| Befehl | Beschreibung |
|--------|--------------|
| `dir` | Verzeichnisinhalt anzeigen |
| `cd <Pfad>` | Verzeichnis wechseln |
| `mkdir <Name>` | Verzeichnis erstellen |
| `rmdir <Name>` | Verzeichnis löschen |
| `del <Datei>` | Datei löschen |
| `copy <Quelle> <Ziel>` | Datei kopieren |
| `move <Quelle> <Ziel>` | Datei verschieben |
| `ren <Alt> <Neu>` | Datei umbenennen |
| `type <Datei>` | Dateiinhalt anzeigen |
| `attrib` | Dateiattribute anzeigen/ändern |

### Netzwerk

| Befehl | Beschreibung |
|--------|--------------|
| `ipconfig` | IP-Konfiguration anzeigen |
| `ipconfig /all` | Detaillierte IP-Konfiguration |
| `ipconfig /release` | IP-Adresse freigeben |
| `ipconfig /renew` | IP-Adresse erneuern |
| `ipconfig /flushdns` | DNS-Cache leeren |
| `ping <Host>` | Erreichbarkeit testen |
| `tracert <Host>` | Route zu Host verfolgen |
| `nslookup <Domain>` | DNS-Abfrage |
| `netstat` | Netzwerkverbindungen anzeigen |
| `netstat -an` | Alle Verbindungen und Ports |
| `arp -a` | ARP-Tabelle anzeigen |
| `route print` | Routing-Tabelle anzeigen |
| `net use` | Netzlaufwerke verbinden |
| `net user` | Benutzer verwalten |

### System

| Befehl | Beschreibung |
|--------|--------------|
| `systeminfo` | Systeminformationen anzeigen |
| `tasklist` | Laufende Prozesse anzeigen |
| `taskkill /PID <PID>` | Prozess beenden |
| `shutdown /s` | System herunterfahren |
| `shutdown /r` | System neu starten |
| `gpupdate /force` | Gruppenrichtlinien aktualisieren |
| `sfc /scannow` | Systemdateien prüfen |
| `chkdsk` | Datenträger prüfen |

### PowerShell-spezifisch

| Befehl | Beschreibung |
|--------|--------------|
| `Get-Command` | Befehle auflisten |
| `Get-Help <Cmdlet>` | Hilfe anzeigen |
| `Get-Service` | Dienste anzeigen |
| `Start-Service <Name>` | Dienst starten |
| `Stop-Service <Name>` | Dienst stoppen |
| `Get-Process` | Prozesse anzeigen |
| `Get-EventLog` | Ereignisprotokoll anzeigen |

## Linux-Befehle (Bash)

### Dateisystem

| Befehl | Beschreibung |
|--------|--------------|
| `ls` | Verzeichnisinhalt anzeigen |
| `ls -la` | Detaillierte Anzeige inkl. versteckter Dateien |
| `cd <Pfad>` | Verzeichnis wechseln |
| `pwd` | Aktuelles Verzeichnis anzeigen |
| `mkdir <Name>` | Verzeichnis erstellen |
| `rmdir <Name>` | Leeres Verzeichnis löschen |
| `rm <Datei>` | Datei löschen |
| `rm -r <Verzeichnis>` | Verzeichnis rekursiv löschen |
| `cp <Quelle> <Ziel>` | Datei kopieren |
| `mv <Quelle> <Ziel>` | Datei verschieben/umbenennen |
| `cat <Datei>` | Dateiinhalt anzeigen |
| `less <Datei>` | Dateiinhalt seitenweise anzeigen |
| `head <Datei>` | Erste Zeilen anzeigen |
| `tail <Datei>` | Letzte Zeilen anzeigen |
| `tail -f <Datei>` | Datei fortlaufend anzeigen |
| `touch <Datei>` | Leere Datei erstellen |
| `nano <Datei>` | Datei bearbeiten (Editor) |
| `vi <Datei>` | Datei bearbeiten (Vi-Editor) |
| `find <Pfad> -name <Name>` | Dateien suchen |
| `grep <Muster> <Datei>` | Text in Datei suchen |

### Berechtigungen

| Befehl | Beschreibung |
|--------|--------------|
| `chmod <Rechte> <Datei>` | Berechtigungen ändern |
| `chmod 755 <Datei>` | rwxr-xr-x setzen |
| `chmod +x <Datei>` | Ausführbar machen |
| `chown <User> <Datei>` | Besitzer ändern |
| `chown <User>:<Gruppe> <Datei>` | Besitzer und Gruppe ändern |
| `chgrp <Gruppe> <Datei>` | Gruppe ändern |

### System & Prozesse

| Befehl | Beschreibung |
|--------|--------------|
| `ps` | Prozesse anzeigen |
| `ps aux` | Alle Prozesse detailliert |
| `top` | Prozesse live anzeigen |
| `htop` | Erweiterte Prozessanzeige |
| `kill <PID>` | Prozess beenden |
| `killall <Name>` | Alle Prozesse eines Namens beenden |
| `df -h` | Festplattenbelegung anzeigen |
| `du -sh <Verzeichnis>` | Verzeichnisgröße anzeigen |
| `free -h` | Speicher anzeigen |
| `uname -a` | Systeminformationen |
| `uptime` | Laufzeit des Systems |
| `date` | Datum und Uhrzeit anzeigen |
| `whoami` | Aktuellen Benutzer anzeigen |
| `w` | Angemeldete Benutzer |
| `history` | Befehlshistorie |

### Netzwerk

| Befehl | Beschreibung |
|--------|--------------|
| `ifconfig` | Netzwerkinterfaces anzeigen (alt) |
| `ip addr` | IP-Adressen anzeigen |
| `ip link` | Netzwerkinterfaces anzeigen |
| `ip route` | Routing-Tabelle anzeigen |
| `ping <Host>` | Erreichbarkeit testen |
| `traceroute <Host>` | Route zu Host verfolgen |
| `nslookup <Domain>` | DNS-Abfrage |
| `dig <Domain>` | DNS-Abfrage (detailliert) |
| `netstat -tulpn` | Netzwerkverbindungen |
| `ss -tulpn` | Socket-Statistiken |
| `arp` | ARP-Tabelle anzeigen |
| `wget <URL>` | Datei herunterladen |
| `curl <URL>` | HTTP-Anfrage senden |

### Paketverwaltung

#### Debian/Ubuntu (apt)

| Befehl | Beschreibung |
|--------|--------------|
| `apt update` | Paketlisten aktualisieren |
| `apt upgrade` | Pakete aktualisieren |
| `apt install <Paket>` | Paket installieren |
| `apt remove <Paket>` | Paket entfernen |
| `apt search <Begriff>` | Paket suchen |

#### RedHat/CentOS (yum/dnf)

| Befehl | Beschreibung |
|--------|--------------|
| `yum update` | Pakete aktualisieren |
| `yum install <Paket>` | Paket installieren |
| `yum remove <Paket>` | Paket entfernen |
| `dnf install <Paket>` | Paket installieren (neuere Systeme) |

### Dienste (systemd)

| Befehl | Beschreibung |
|--------|--------------|
| `systemctl status <Dienst>` | Dienststatus anzeigen |
| `systemctl start <Dienst>` | Dienst starten |
| `systemctl stop <Dienst>` | Dienst stoppen |
| `systemctl restart <Dienst>` | Dienst neu starten |
| `systemctl enable <Dienst>` | Dienst beim Boot starten |
| `systemctl disable <Dienst>` | Autostart deaktivieren |
| `journalctl -u <Dienst>` | Dienst-Logs anzeigen |

### Archivierung & Kompression

| Befehl | Beschreibung |
|--------|--------------|
| `tar -czf archiv.tar.gz <Dateien>` | TAR.GZ erstellen |
| `tar -xzf archiv.tar.gz` | TAR.GZ entpacken |
| `zip -r archiv.zip <Dateien>` | ZIP erstellen |
| `unzip archiv.zip` | ZIP entpacken |
| `gzip <Datei>` | Datei komprimieren |
| `gunzip <Datei.gz>` | Datei entpacken |

## 🔄 Windows vs. Linux - Vergleichstabelle

**Für die Prüfung wichtig:** Befehle vergleichen können! 🔴

### Dateisystem-Befehle

| Aktion | Windows (CMD) | Linux (Bash) | Beschreibung |
|--------|---------------|--------------|--------------|
| Verzeichnis auflisten | `dir` | `ls` / `ls -la` | Dateien anzeigen |
| Verzeichnis wechseln | `cd <Pfad>` | `cd <Pfad>` | Navigation |
| Aktuelles Verzeichnis | `cd` | `pwd` | Wo bin ich? |
| Verzeichnis erstellen | `mkdir <Name>` | `mkdir <Name>` | Ordner anlegen |
| Datei löschen | `del <Datei>` | `rm <Datei>` | Datei entfernen |
| Verzeichnis löschen | `rmdir <Name>` | `rm -r <Name>` | Ordner löschen |
| Datei kopieren | `copy <Q> <Z>` | `cp <Q> <Z>` | Kopie erstellen |
| Datei verschieben | `move <Q> <Z>` | `mv <Q> <Z>` | Datei bewegen |
| Datei umbenennen | `ren <Alt> <Neu>` | `mv <Alt> <Neu>` | Namen ändern |
| Datei anzeigen | `type <Datei>` | `cat <Datei>` | Inhalt ausgeben |
| Datei suchen | `dir /s <Name>` | `find / -name <Name>` | Datei finden |
| Text suchen | `findstr <Text>` | `grep <Text>` | Inhalt durchsuchen |

### Netzwerk-Diagnose

| Aktion | Windows | Linux | Beschreibung |
|--------|---------|-------|--------------|
| IP-Konfiguration anzeigen | `ipconfig` | `ip a` / `ifconfig` | IP-Adresse anzeigen |
| IP-Details anzeigen | `ipconfig /all` | `ip addr show` | Detaillierte Info |
| IP-Adresse freigeben | `ipconfig /release` | `dhclient -r` | DHCP-Lease freigeben |
| IP-Adresse erneuern | `ipconfig /renew` | `dhclient` | DHCP neu anfragen |
| DNS-Cache leeren | `ipconfig /flushdns` | `systemd-resolve --flush-caches` | DNS zurücksetzen |
| Erreichbarkeit testen | `ping <Host>` | `ping <Host>` | ICMP-Test |
| Route verfolgen | `tracert <Host>` | `traceroute <Host>` | Weg zum Ziel |
| DNS-Abfrage | `nslookup <Domain>` | `nslookup <Domain>` / `dig <Domain>` | DNS auflösen |
| ARP-Tabelle | `arp -a` | `arp -a` / `ip neigh` | MAC-Zuordnung |
| Routing-Tabelle | `route print` | `ip route` / `route -n` | Routen anzeigen |
| Netzwerkverbindungen | `netstat -an` | `netstat -tulpn` / `ss -tulpn` | Offene Ports |

### System & Prozesse

| Aktion | Windows | Linux | Beschreibung |
|--------|---------|-------|--------------|
| Systeminformationen | `systeminfo` | `uname -a` | Systemdetails |
| Prozesse anzeigen | `tasklist` | `ps aux` | Laufende Prozesse |
| Prozess beenden | `taskkill /PID <PID>` | `kill <PID>` | Prozess stoppen |
| Dienste anzeigen | `sc query` | `systemctl list-units` | Services auflisten |
| Dienst starten | `net start <Name>` | `systemctl start <Name>` | Service starten |
| Dienst stoppen | `net stop <Name>` | `systemctl stop <Name>` | Service stoppen |
| Festplatte anzeigen | `wmic logicaldisk get size,freespace` | `df -h` | Speicherplatz |
| Aktueller Benutzer | `whoami` | `whoami` | Username anzeigen |
| System herunterfahren | `shutdown /s` | `shutdown -h now` | Ausschalten |
| System neu starten | `shutdown /r` | `shutdown -r now` / `reboot` | Neustart |

### Berechtigungen & Besitz

| Aktion | Windows | Linux | Beschreibung |
|--------|---------|-------|--------------|
| Berechtigungen anzeigen | `icacls <Datei>` | `ls -l <Datei>` | ACL/Permissions |
| Berechtigungen ändern | `icacls <Datei> /grant` | `chmod 755 <Datei>` | Rechte setzen |
| Besitzer ändern | `takeown /f <Datei>` | `chown <User> <Datei>` | Ownership |
| Ausführbar machen | (nicht nötig) | `chmod +x <Datei>` | Script ausführbar |

### Nützliche Zusatzbefehle

| Aktion | Windows | Linux | Beschreibung |
|--------|---------|-------|--------------|
| Hilfe anzeigen | `<Befehl> /?` | `man <Befehl>` / `<Befehl> --help` | Befehlshilfe |
| Befehlshistorie | `doskey /history` | `history` | Letzte Befehle |
| Ausgabe umleiten | `<Befehl> > datei.txt` | `<Befehl> > datei.txt` | In Datei schreiben |
| Ausgabe anhängen | `<Befehl> >> datei.txt` | `<Befehl> >> datei.txt` | An Datei anhängen |
| Pipe (Verkettung) | `<Befehl1> | <Befehl2>` | `<Befehl1> | <Befehl2>` | Befehle verbinden |

---

## 📝 Wichtige Hinweise für die Prüfung

### Häufige Prüfungsfragen

1. **"Welcher Befehl zeigt die IP-Konfiguration an?"**
   - Windows: `ipconfig`
   - Linux: `ip a` oder `ifconfig`

2. **"Wie testet man die Erreichbarkeit eines Hosts?"**
   - Beide: `ping <Host>`

3. **"Wie setzt man Linux-Berechtigungen?"**
   - `chmod 755 datei.sh` (rwxr-xr-x)
   - `chmod +x datei.sh` (ausführbar machen)

4. **"Wie zeigt man Netzwerkverbindungen an?"**
   - Windows: `netstat -an`
   - Linux: `netstat -tulpn` oder `ss -tulpn`

5. **"Wie startet man einen Dienst?"**
   - Windows: `net start <Dienst>`
   - Linux: `systemctl start <Dienst>`

### Linux-Berechtigungen (chmod)

```
rwx rwx rwx  (r=read, w=write, x=execute)
│   │   │
│   │   └── Andere (others)
│   └────── Gruppe (group)
└────────── Besitzer (owner)

Zahlenwerte:
r = 4
w = 2
x = 1

Beispiele:
755 = rwxr-xr-x (Besitzer: alles, Gruppe/Andere: lesen+ausführen)
644 = rw-r--r-- (Besitzer: lesen+schreiben, Gruppe/Andere: nur lesen)
700 = rwx------ (Nur Besitzer hat alle Rechte)
```

---

## Quellen

- [05_Betriebssysteme/Windows](../05_Betriebssysteme/Windows/)
- [05_Betriebssysteme/Linux](../05_Betriebssysteme/Linux/)
- Microsoft Documentation
- Linux man pages

---

## 🔗 Navigation

- [Zum Lernplan](./AP1_Lernplan.md)
- [Zur AP1 Checkliste](./AP1_Checkliste.md)
- [Zur Formelsammlung](./Formelsammlung.md)
- [Zum Abkürzungsverzeichnis](./Abkuerzungsverzeichnis.md)

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](Formelsammlung.md) | [Nächstes Thema](Abkuerzungsverzeichnis.md)
