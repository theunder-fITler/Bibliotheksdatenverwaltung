from faker import Faker
import selection_pool as s_p
from datetime import datetime, timedelta    # kurze schreibweise dadurch möglich!
import random
from create_buecher import buecher



## Kunden der Bib faken
fake_kunde = Faker('de_DE')
ANZAHL_KUNDEN = 364
FEHLERQUOTE = 0.15  # 15 % der Kunden erhalten Fehler

def zufaelliges_datum(start_year=1900, end_year=2007):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return fake_kunde.date_between(start_date=start_date, end_date=end_date)

def generiere_kunde(kunden_id):
    fehlerhaft = random.random() < FEHLERQUOTE

    # Name
    name = " ".join([fake_kunde.first_name(), fake_kunde.last_name()])
    if fehlerhaft and random.random() < 0.3:
        name = random.choice(["", "???", name.split(" ")[0]])  # leer, unvollständig, komisch

    # Geburtsdatum
    geburtsdatum = zufaelliges_datum().strftime("%d-%m-%Y")
    if fehlerhaft and random.random() < 0.4:
        geburtsdatum = random.choice(["", zufaelliges_datum().strftime("%Y%m%d"), "NULL"])

    # Adresse
    adresse = fake_kunde.address().replace("\n", ", ")
    if fehlerhaft and random.random() < 0.4:
        adresse = random.choice(["", "unbekannt", None])

    # Ende der Mitgliedschaft
    if random.random() < 0.85:
        end_jahr = random.randint(2026, 2030)
        end_monat = random.randint(1, 12)
        end_tag = random.randint(1, 28)
        ende_mitgliedschaft = f"{end_tag:02d}.{end_monat:02d}.{end_jahr:04d}"
    else:
        ende_mitgliedschaft = f"{end_jahr:04d}-{end_monat:02d}-{end_tag:02d}"

    if fehlerhaft and random.random() < 0.3:
        ende_mitgliedschaft = random.choice(["gestorben", "unbekannt", "9999-99-99", None, "30-04-2026"])

    # Ausgeliehene Bücher
    if fehlerhaft:
        buecher_ausgeliehen = []
        for i in range(random.randint(1, 5)):
            buecher_ausgeliehen.append(random.choice(buecher))
    else:
        buecher_verliehen = []
        buecher_ausgeliehen = []
        for buch in buecher:
            if buch[9] in ["ausgeliehen", "verliehen", "rot"]:
                buecher_verliehen.append(buch)
        for i in range(random.randint(1, 5)):
            buecher_ausgeliehen.append(random.sample(buecher_verliehen, k=random.randint(1,5)))

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