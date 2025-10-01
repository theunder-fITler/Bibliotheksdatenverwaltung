from faker import Faker
import selection_pool as s_p
from datetime import datetime, timedelta    # kurze schreibweise dadurch möglich!
import random



## Kunden der Bib faken
fake_kunde = Faker('de_DE')
ANZAHL_KUNDEN = 364
FEHLERQUOTE = 0.15  # 15 % der Kunden erhalten Fehler

def zufaelliges_datum(start_year=1950, end_year=2009):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    return fake_kunde.date_between(start_date=start_date, end_date=end_date)

def generiere_kunde(kunden_id):
    fehlerhaft = random.random() < FEHLERQUOTE

    # Name
    name = fake_kunde.name()
    if fehlerhaft and random.random() < 0.3:
        name = random.choice(["", "???", name.split(" ")[0]])  # leer, unvollständig, komisch

    # Geburtsdatum
    geburtsdatum = zufaelliges_datum().strftime("%Y-%m-%d")
    if fehlerhaft and random.random() < 0.4:
        geburtsdatum = random.choice(["", "1900-00-00", "31.02.2000", "NULL"])

    # Adresse
    adresse = fake_kunde.address().replace("\n", ", ")
    if fehlerhaft and random.random() < 0.4:
        adresse = random.choice(["", "unbekannt", None])

    # Ende der Mitgliedschaft
    if random.random() < 0.7:
        end_jahr = random.randint(2021, 2025)
        end_monat = random.randint(1, 12)
        end_tag = random.randint(1, 28)
        ende_mitgliedschaft = f"{end_jahr:04d}-{end_monat:02d}-{end_tag:02d}"
    else:
        ende_mitgliedschaft = ""

    if fehlerhaft and random.random() < 0.3:
        ende_mitgliedschaft = random.choice(["gestorben", "unbekannt", "9999-99-99", None])

    # Ausgeliehene Bücher
    if fehlerhaft:
        buecher_ausgeliehen = []
        for i in range(1,random.randint(1,5)):
            buecher_ausgeliehen.append(random.choice(Buecher)) # hier sollen zu 95% ausgeliehne bücher eingefügt werden
    else:
        buecher_ausgeliehen = []

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