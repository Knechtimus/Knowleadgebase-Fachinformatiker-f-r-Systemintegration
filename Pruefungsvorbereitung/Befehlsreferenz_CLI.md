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

## Netzwerk-Befehle (Universal)

### Diagnose-Befehle

| Befehl | Betriebssystem | Beschreibung |
|--------|----------------|--------------|
| `ping <Host>` | Windows/Linux | ICMP Echo Request |
| `tracert <Host>` | Windows | Route verfolgen |
| `traceroute <Host>` | Linux | Route verfolgen |
| `pathping <Host>` | Windows | Kombiniert ping und tracert |
| `nslookup <Domain>` | Windows/Linux | DNS-Abfrage |
| `dig <Domain>` | Linux | Erweiterte DNS-Abfrage |
| `arp -a` | Windows/Linux | ARP-Cache anzeigen |
| `netstat -an` | Windows/Linux | Netzwerkverbindungen |
| `telnet <Host> <Port>` | Windows/Linux | Port-Test |
| `nc -zv <Host> <Port>` | Linux | Port-Scanner (netcat) |

## Quellen

- [ ] Noch keine Quellen

---
[↩ Zurück zur Übersicht](../README.md) | [Vorheriges Thema](Formelsammlung.md) | [Nächstes Thema](Abkuerzungsverzeichnis.md)
