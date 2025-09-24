import random
import csv
from datetime import datetime, timedelta
import faker.providers.isbn
import pandas as pd
from faker import Faker



# set up Faker
fake_buecher = Faker()
fake_kunde = Faker('de_DE')

## Listen für die Generierung
zustaende = [
    "Neu",
    "Sehr gut",
    "Gut",
    "In Ordnung",
    "Abgenutzt",
    "Beschädigt",
    "Unvollständig",
    "In Reparatur",
    "Verloren",
    "Ausgemustert"
]
zustaende_gewichte = [
    20,  # Neu
    18,  # Sehr gut
    15,  # Gut
    12,  # In Ordnung
    10,  # Abgenutzt
    8,   # Beschädigt
    6,   # Unvollständig
    5,   # In Reparatur
    3,   # Verloren
    3    # Ausgemustert
]
verlage = [
    "Rowohlt Verlag",
    "Suhrkamp Verlag",
    "Fischer Verlage",
    "dtv Verlagsgesellschaft",
    "C.H. Beck",
    "Hanser Verlag",
    "Kiepenheuer & Witsch",
    "Droemer Knaur",
    "Heyne Verlag",
    "Piper Verlag",
    "Carlsen Verlag",
    "Ullstein Buchverlage",
    "Campus Verlag",
    "Goldmann Verlag",
    "O'Reilly Media",
    "Springer Fachmedien",
    "Reclam Verlag",
    "Thienemann-Esslinger",
    "Cornelsen Verlag",
    "Beltz & Gelberg"
]
stati = ["verliehen", "vorgemerkt", "verfügbar", "verloren", "???", "ausgeliehen", "grün", "gelb", "rot"]
stati_gewichte = [100, 30, 200, 10, 5, 20, 100, 30, 200]

sparten = [
    "Belletristik",
    "Kinder- und Jugendbücher",
    "Sachbücher",
    "Wissenschaft",
    "Geschichte",
    "Reiseliteratur",
    "Kunst und Kultur",
    "Biografien",
    "Philosophie",
    "Technik",
    "Psychologie",
    "Gesundheit",
    "Computer & IT",
    "Naturwissenschaften",
    "Sprachen",
    "Krimis & Thriller",
    "Fantasy & Science-Fiction",
    "Religion & Spiritualität",
    "Kochen & Ernährung",
    "Sport"
]
leihfristen_nach_sparte = {
    "Belletristik": 14,
    "Kinder- und Jugendbücher": 14,
    "Sachbücher": 21,
    "Wissenschaft": 28,
    "Geschichte": 28,
    "Reiseliteratur": 10,
    "Kunst und Kultur": 21,
    "Biografien": 21,
    "Philosophie": 28,
    "Technik": 28,
    "Psychologie": 21,
    "Gesundheit": 21,
    "Computer & IT": 28,
    "Naturwissenschaften": 28,
    "Sprachen": 21,
    "Krimis & Thriller": 14,
    "Fantasy & Science-Fiction": 14,
    "Religion & Spiritualität": 21,
    "Kochen & Ernährung": 10,
    "Sport": 14
}
sparten_gewichte = [
    20,  # Belletristik
    15,  # Kinder- und Jugendbücher
    10,  # Sachbücher
    8,   # Wissenschaft
    7,   # Geschichte
    6,   # Reiseliteratur
    5,   # Kunst und Kultur
    5,   # Biografien
    4,   # Philosophie
    4,   # Technik
    4,   # Psychologie
    3,   # Gesundheit
    3,   # Computer & IT
    3,   # Naturwissenschaften
    3,   # Sprachen
    6,   # Krimis & Thriller
    6,   # Fantasy & Science-Fiction
    2,   # Religion & Spiritualität
    2,   # Kochen & Ernährung
    2    # Sport
]
autoren_vorname = [f"{fake_buecher.first_name()}" for i in range(100)]
autoren_nachname = [f"{fake_buecher.last_name()}" for i in range(100)]

# Bücher ##  Titel | Autor | ISBN | Erscheinungsjahr | Auflage | Zustand | Verlag | Preis | Menge | Status |
autor = f"{random.choice(autoren_vorname)} {random.choice(autoren_nachname)}"
erscheinungsjahr = fake_buecher.date_of_birth(minimum_age=18, maximum_age=99).strftime("%d%m%Y")
isbn = faker.providers.isbn.ISBN13
auflage = random.randint(1,10)
zustand = random.choices(zustaende, zustaende_gewichte, k=1)
verlag = random.choice(verlage)
preis = random.randint(1200,99999) /10
bestand = random.randint(0,9)
status = random.choices(stati, stati_gewichte, k=1)
titel = f"{fake_buecher.word().capitalize()} der {fake_buecher.word().capitalize()}, {random.choices(sparten, sparten_gewichte, k=1)}"

# Bücher in der Bib
Buecher = ["Titel", "Autor", "ISBN", "Erscheinungsjahr", "Auflage", "Zustand", "Verlag", "Preis", "Bestand", "Status"]
for i in range(1000):
    fehlerhaft = random.random() < 0.1
    if fehlerhaft:
        autor = f"{random.choice(autoren_nachname)}, {random.choice(autoren_vorname)}"
    else:
        autor = f"{random.choice(autoren_vorname)} {random.choice(autoren_nachname)}"

    fehlerhaft = random.random() < 0.1
    if fehlerhaft:
        erscheinungsjahr = fake_buecher.date_of_birth(minimum_age=16, maximum_age=99).strftime("%Y%m%d")
    else:
        erscheinungsjahr = fake_buecher.date_of_birth(minimum_age=18, maximum_age=99).strftime("%d%m%Y")

    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        isbn = faker.providers.isbn.ISBN10
    else:
        isbn = faker.providers.isbn.ISBN13

    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        auflage = random.randint(1, 9) *10
    else:
        auflage = random.randint(1, 9)

    fehlerhaft = random.random() < 0.2
    if fehlerhaft:
        zustand = f"{random.choices(zustaende, zustaende_gewichte, k=1)}, {random.choices(zustaende, zustaende_gewichte, k=1)}"
    else:
        zustand = random.choices(zustaende, zustaende_gewichte, k=1)

    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        verlag = random.choice(verlage).upper()
    else:
        verlag = random.choice(verlage)

    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        preis = random.randint(1200, 99999)
    else:
        preis = random.randint(1200, 99999) / 10

    fehlerhaft = random.random() < 0.15
    if fehlerhaft:
        bestand = 0
    else:
        bestand = random.randint(1, 9)

    fehlerhaft = random.random() < 0.3
    if fehlerhaft:
        status = random.choices(stati, stati_gewichte, k=2)
    else:
        status = random.choices(stati, stati_gewichte, k=1)

    fehlerhaft = random.random() < 0.3
    if fehlerhaft:
        titel = f"{fake_buecher.word().capitalize()} der {fake_buecher.word().capitalize()}, {random.choices(sparten, sparten_gewichte, k=2)}"
    else:
        titel = f"{fake_buecher.word().capitalize()} der {fake_buecher.word().capitalize()}, {random.choices(sparten, sparten_gewichte, k=1)}"

    try:
        extrahierte_roh = titel.split(", ")[-1]
        # z.B. aus ['Fachbuch'] → Fachbuch
        extrahierte_sparte = extrahierte_roh.strip("[]'\" ")

        korrekt = random.random() < 0.9  # 90 % korrekt, 10 % absichtlich falsch

        if korrekt and extrahierte_sparte in leihfristen_nach_sparte:
            leihfrist = leihfristen_nach_sparte[extrahierte_sparte]
        else:
            # absichtlich fehlerhafte oder unpassende Werte
            leihfrist = random.choice([
                "", "unbekannt", 0, 999, "14 Tage", random.randint(1, 60)
            ])
    except:
        # Parsing hat komplett versagt
        leihfrist = random.choice([
            "", "fehlerhaft", None, 14, 21
        ])

    Buecher.append([titel, autor, erscheinungsjahr, isbn, auflage, zustand, verlag, preis, bestand, status, leihfrist])

# Kunden der bib

# Anzahl Kunden
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
            buecher_ausgeliehen.append(random.choice(Buecher))
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


# Verlag

fake_verlag = Faker("de_DE")

# Feste Liste einiger realistischer (oder anmutender) Verlagsnamen
def generiere_verlag(verlag_id, fehlerquote=0.1):
    fehlerhaft = random.random() < fehlerquote

    # Name
    name = random.choice(verlage)
    if not name or random.random() < 0.3:
        # 30 % Chance für generierten Verlag
        name = fake_verlag.company() + " Verlag"

    if fehlerhaft and random.random() < 0.4:
        name = random.choice(["", "Verlag ???", None])

    # Adresse
    adresse = fake_verlag.address().replace("\n", ", ")
    if fehlerhaft and random.random() < 0.4:
        adresse = random.choice(["", None, "Unbekannt"])

    # Kontakt: Entweder Telefonnummer oder E-Mail
    if random.random() < 0.5:
        kontakt = fake_verlag.phone_number()
    else:
        kontakt = fake_verlag.company_email()

    if fehlerhaft and random.random() < 0.3:
        kontakt = random.choice(["", None, "keine Angabe"])

    return {
        "VerlagID": verlag_id,
        "Name": name,
        "Adresse": adresse,
        "Kontakt": kontakt
    }

# Anzahl der Verlage
ANZAHL_VERLAGE = 100

# Generieren
verlage = [generiere_verlag(i + 1) for i in range(ANZAHL_VERLAGE)]


## export zu dateien