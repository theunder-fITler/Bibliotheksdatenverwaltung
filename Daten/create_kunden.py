from faker import Faker
import selection_pool as s_p
from datetime import datetime, timedelta    # kurze schreibweise dadurch möglich!
import random
from create_buecher import buecher



## Faker und random seed
Faker.seed(12345)
random.seed(12345)

## Ausgeliehene Bücher vorbereiten
buecher_verliehen = []
for buch in buecher:
    status_liste = buch[9]  # z. B. ["verfügbar", "verliehen", "verliehen"]
    anzahl_verliehen = sum(status in ["ausgeliehen", "verliehen", "rot"] for status in status_liste)

    if anzahl_verliehen > 0:
        # Optional: kopiere das Buch, um nichts im Original zu verändern
        buch_kopie = buch.copy()
        # Wenn buch[8] dein "Bestand" oder "verliehen"-Zähler ist:
        buch_kopie[8] = anzahl_verliehen
        buecher_verliehen.append(buch_kopie)


## Kunden der Bib faken
fake_kunde = Faker('de_DE')
ANZAHL_KUNDEN = 3
FEHLERQUOTE = 0.15  # 15 % der Kunden erhalten Fehler

def zufaelliges_datum(start_year=1900, end_year=2007):
    start_datum = datetime(start_year, 1, 1)
    end_datum = datetime(end_year, 12, 31)
    return fake_kunde.date_between(start_date=start_datum, end_date=end_datum)

def zufaelliges_ausleihdatum():
    return fake_kunde.date_between(start_date='-3w')

def generiere_kunde(kunden_id):
    fehlerhaft = random.random() < FEHLERQUOTE

    # 1. Name
    name = " ".join([fake_kunde.first_name(), fake_kunde.last_name()])
    if fehlerhaft and random.random() < 0.3:
        name = random.choice(["", "???", name.split(" ")[0]])  # leer, unvollständig, komisch

    # 2. Geburtsdatum
    geburtsdatum = zufaelliges_datum().strftime("%d-%m-%Y")
    if fehlerhaft and random.random() < 0.4:
        geburtsdatum = random.choice(["", zufaelliges_datum().strftime("%Y%m%d"), "NULL"])

    # 3. Adresse
    adresse = fake_kunde.address().replace("\n", ", ")
    if fehlerhaft and random.random() < 0.4:
        adresse = random.choice(["", "unbekannt", None])

    # 4. Ende der Mitgliedschaft
    end_jahr = random.randint(2026, 2030)
    end_monat = random.randint(1, 12)
    end_tag = random.randint(1, 28)
    if random.random() < 0.85:
        ende_mitgliedschaft = f"{end_tag:02d}.{end_monat:02d}.{end_jahr:04d}"
    else:
        ende_mitgliedschaft = f"{end_jahr:04d}-{end_monat:02d}-{end_tag:02d}"

    if fehlerhaft and random.random() < 0.3:
        ende_mitgliedschaft = random.choice(["gestorben", "unbekannt", "9999-99-99", None, "30-04-2026"])

    # 5. Ausgeliehene Bücher
    # irgendein oder mehere Bücher werden dem Kunden zugeordnet
    if fehlerhaft:
        buecher_ausgeliehen = []
        for i in range(random.randint(0, 5)):
            buch_ausgeliehen_datum = (random.choice(buecher)[2], None)
            buecher_ausgeliehen.append(buch_ausgeliehen_datum)

    # Kunde erhält Bücher mit Ausleihdatum, deren Status was mit "ausgeliehen" zu tun hat.
    else:
        # Liste der ausgeliehenden Bücher leeren und die anzahl der Bücher bestimmen, die ausgeliehen werden sollen
        buecher_ausgeliehen = []
        anzahl_buecher_ausgeliehen = random.randint(1, min(5, len(buecher_verliehen)))
        # Bücher auswählen und den Bestand verringern oder aus Liste entfernen
        buecher_verliehen_auswahl = random.sample(buecher_verliehen, k=anzahl_buecher_ausgeliehen)
        for buch in buecher_verliehen_auswahl:
            if buch[8] > 1:
                buch[8] = buch[8] - 1
                 # if buch in buecher_verliehen: - Unnötig, da random.sample mir referenz auf die ursprüngliche lsite erzeugt, keinen auszug aus der Liste
                    # index = buecher_verliehen.index(buch)
                    # buecher_verliehen[index] = buch
            else:
                buecher_verliehen.remove(buch)
        # Vom Kunden ausgeliehne Bücher mit Datum versehen
        buecher_verliehen_auswahl_datum = []
        for buch in buecher_verliehen_auswahl:
            buch_datum = (buch[2], zufaelliges_ausleihdatum()) # buch[2] == ISBN
            buecher_verliehen_auswahl_datum.append(buch_datum)
        buecher_ausgeliehen = buecher_verliehen_auswahl_datum

    # Kundeninformationen zurückgeben
    return {
        "KundenID": kunden_id,
        "Name": name,
        "Geburtsdatum": geburtsdatum,
        "Adresse": adresse,
        "EndeMitgliedschaft": ende_mitgliedschaft,
        "Ausgeliehen": buecher_ausgeliehen
    }

# Daten generieren
kunden_liste = [generiere_kunde(i+1) for i in range(ANZAHL_KUNDEN)]
# Liste mischen, damit nich alle Kunden die ein Buch ausgeliehen haben am Anfang stehen
random.shuffle(kunden_liste)