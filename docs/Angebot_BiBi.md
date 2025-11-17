# Angebot: Digitalisierung der Bibliotheksdaten 
**für die Gemeindebücherei „Im Anfang war das Wort“**

## 1. Ausgangssituation

Die Gemeindebücherei „Im Anfang war das Wort“ verwaltet derzeit rund 250 Kund:innen und einen Bestand von rund 1.200 unterschiedlichen Büchern.  
Die vorhandenen Datensätze liegen in uneinheitlicher Form vor und weisen teils erhebliche Qualitätsprobleme auf (fehlende, doppelte oder fehlerhafte Einträge).  

Gemäß der Anfrage der Gemeindebücherei vom 10.10.2025 bieten wir die Bereinigung und Strukturierung der Daten in einer Datenbank als saubere Basis für die Datenverwaltung an. 
Optional bieten wir eine digitale Abbildung der Verwaltungsprozesse an. Diese ermöglicht eine einfache und fehlerresistente Ausleihe, Rückgabe und Stammdatenpflege.

## 2. Leistungsumfang 

| **Modul**                                               | **Beschreibung**                                                                    | **Leistungsumfang / Arbeitsschritte**                                                                                                                                                                       | **Status**   |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Modul 1 – Datenexploration & Bewertung**              | Sichtung der bereitgestellten Kund*innen- und Buchdaten                             | • Struktur- und Formatprüfung (CSV/Excel/sonstige)<br>• Identifikation von Dubletten, fehlenden Werten, Inkonsistenzen<br>• Bewertung des Bereinigungsaufwands<br>• Erstellen eines kurzen Ergebnisberichts | verbindlich  |
| **Modul 2 – Datenbereinigung**                          | Bereinigung und Vereinheitlichung der Datensätze                                    | • Entwicklung von Skripten zur automatisierten Korrektur<br>• manuelle Nachpflege bei unlösbaren Fehlern<br>• Erstellung eines Bereinigungsprotokolls                                                       | verbindlich  |
| **Modul 3 – Datenmodellierung & Datenbankaufbau**       | Erstellung eines Datenmodells (ER-Diagramm) und Aufbau einer relationalen Datenbank | • Entwurf des ER-Diagramms<br>• Implementierung in MariaDB<br>• Import der bereinigten Daten<br>• Test der Konsistenz und Integrität                                                                        | verbindlich  |
| **Modul 4 – Backup-Skript**                             | Automatisierte Datensicherung                                                       | • Entwicklung eines einfachen Backup-Skripts<br>• Speicherung als zeitgestempelte Kopie der DB<br>• Dokumentation der Anwendung                                                                             | verbindlich  |
| **Modul 5 – Verwaltungsprozesse (Ausleihe / Rückgabe)** | Abbildung der Kernprozesse der Bibliothek                                           | • Anlegen neuer Kund*innen und Bücher<br>• Buchung von Ausleihe und Rückgabe (optional mit Scanner-Unterstützung)<br>• Verwaltung von Rückgabefristen                                                       | optional     |
| **Modul 6 – Benutzeroberfläche (Tkinter)**              | Entwicklung einer grafischen Oberfläche                                             | • Einfache GUI auf Basis von Python/Tkinter<br>• Zugriff auf die Datenbankfunktionen<br>• Benutzerfreundliche Darstellung und Eingabe                                                                       | optional     |
| **Modul 7 – Dokumentation & Übergabe**                  | Abschluss und Dokumentation                                                         | • Technische Dokumentation (Installations- und Nutzungshinweise)<br>• Kurze Projektdokumentation / README                                                                                                   | verbindlich  |

## 3. Leistungsgrenzen und Annahmen

- Die Qualität und Vollständigkeit der Daten kann erst nach Modul 1 verbindlich bewertet werden.  
- Der Bereinigungsaufwand (Modul 2) hängt maßgeblich von der Datenstruktur und Fehlerquote ab.  
- Optionale Module (5 + 6) werden erst nach erfolgreichem Abschluss der Basisphasen konkretisiert.  
- Alle Arbeiten erfolgen lokal bzw. mit lokal bereitgestellten Daten; keine Cloud-Dienste oder Online-Komponenten sind vorgesehen.  


## 4. Zeit- und Aufwandsschätzung

| **Modul**                        | **geschätzter Aufwand (Std.)** | **Bemerkung**           |
| -------------------------------- | ------------------------------ | ----------------------- |
| 1. Datenexploration & Bewertung  | 8 – 10                         | abhängig von Daten      |
| 2. Datenbereinigung              | 12 – 18                        | je nach Fehlerquote     |
| 3. Datenmodellierung & DB-Aufbau | 4 – 6                          | inkl. ER-Diagramm       |
| 4. Backup-Skript                 | 1 – 2                          | einfaches Python-Skript |
| 5. Prozesse Ausleihe/Rückgabe    | 6 – 10                         | optionale Erweiterung   |
| 6. GUI (Tkinter)                 | 8 – 12                         | optional                |
| 7. Dokumentation & Übergabe      | 2 – 3                          |                         |

**Gesamtschätzung (verbindliche Module 1, 2, 3, 4, 7):**  ca. **28 Stunden**  

Bei einem Stundensatz von **90 €** ergibt sich ein Richtwert von  
**2500 €** (zzgl. optionaler Module nach Aufwand).


## 6. Vorgehensweise

1. **Datenanalyse** (Modul 1)  
   Erstellung eines kurzen Ergebnisberichts.
2. **Datenbereinigung** (Modul 2)
   Aufbau der sauberen Datenbasis
3. **Aufbau der Datenbank** (1, 2, 3, 4, 7)  
   Aufbau der Datenbank und Einlesen der Daten.
4. **Optionale Erweiterungen** (nach Freigabe)  
   Umsetzung der Bereinigung, Buchungsprozesse und GUI.

## 7. Liefergegenstände

- Bereinigte, strukturierte Datenbankdatei (.sql) auf zwei verschlüsselten Datenträgern
- Backup-Skript (Python)
- ER-Diagramm (PNG/PDF)
- Technische Dokumentation / README
- Optional: GUI (Tkinter) und Prozessskripte

## 8. Hinweise zur Datenverarbeitung (DSGVO)

Die Verarbeitung der von der Gemeindebücherei bereitgestellten personenbezogenen Daten (z. B. Kundendaten, Ausleihinformationen) erfolgt ausschließlich zum Zweck der Projektumsetzung und gemäß den geltenden Datenschutzbestimmungen (DSGVO).

Die Einzelheiten der Datenverarbeitung, insbesondere Art, Umfang und Dauer der Verarbeitung sowie die Verpflichtungen der Auftragnehmerin, sind in einem gesonderten Auftragsverarbeitungsvertrag (AVV) geregelt.  

Nach Abschluss des Projekts werden alle personenbezogenen Rohdaten sowie temporäre Arbeitskopien gelöscht, sofern keine anderslautende Vereinbarung besteht.

## 9. Gültigkeit und Annahme

Dieses Angebot bildet die Grundlage für eine verbindliche Zusammenarbeit zwischen der Auftraggeberin (Gemeindebücherei „Im Anfang war das Wort“) und dem Auftragnehmer.  

Mit Unterzeichnung erklären beide Parteien, dass sie die im Angebot genannten Leistungen, Konditionen und Rahmenbedingungen verstanden und akzeptiert haben.  
Etwaige Änderungen oder Erweiterungen des Leistungsumfangs bedürfen der **schriftlichen Vereinbarung**.

Dieses Angebot ist gültig bis zum 31. Dezember 2025.


**Ort, Datum:** .............................................

**Unterschrift Auftraggeber:in:**   .............................................

**Unterschrift Auftragnehmer:in:** .............................................





