import random
from faker import Faker
from faker import providers
import selection_pool as s_p



# Bücher in der Bib
fake_buecher = Faker('de_DE')
fake_isbn = Faker()
# für den Preis eine bessere funktion, die dafür sorgt, dass die meisten bücher einen ähnlichen preis haben:
def gauss_range_sample(mu=3000, sigma=1000, lower=1200, upper=99999):
    while True:
        value = random.gauss(mu, sigma)
        if lower <= value <= upper:
            return int(value)

buecher = [["Titel", "Autor", "ISBN", "Erscheinungsjahr", "Auflage", "Zustand", "Verlag", "Preis", "Bestand", "Status", "Leihfrist"]]
for i in range(20):

    # 8. Bestand
    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        bestand = 0
    else:
        bestand = random.randint(1, 9)
    # 1. Autor
    fehlerhaft = random.random() < 0.1
    if fehlerhaft:
        autor = f"{random.choice(s_p.autoren_nachname)}, {random.choice(s_p.autoren_vorname)}"
    else:
        autor = f"{random.choice(s_p.autoren_vorname)} {random.choice(s_p.autoren_nachname)}"
    # 2. ISBN
    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        isbn = fake_isbn.isbn10()
    else:
        isbn = fake_isbn.isbn13()
    # 3. Erscheinungsjahr
    fehlerhaft = random.random() < 0.1
    if fehlerhaft:
        if 0.499 <= random.random():
            erscheinungsjahr = fake_buecher.date_of_birth(minimum_age=0, maximum_age=150).strftime("%Y%m%d")
        else:
            erscheinungsjahr = fake_buecher.date_of_birth(minimum_age=0, maximum_age=150).strftime("%Y-%m-%d")
    else:
        erscheinungsjahr = fake_buecher.date_of_birth(minimum_age=0, maximum_age=150).strftime("%d%m%Y")
    # 4. Auflage
    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        auflage = random.randint(1, 9) *10
    else:
        auflage = random.randint(1, 9)
    # 5. Zustand
    fehlerhaft = random.random() < 0.2
    if fehlerhaft:
        zustand = f"{random.choices(s_p.zustaende, s_p.zustaende_gewichte, k=bestand - random.randint(0,bestand))}}"
    else:
        zustand = random.choices(s_p.zustaende, s_p.zustaende_gewichte, k=bestand)
    # 6. Verlag
    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        verlag = random.choice(s_p.verlage).upper()
    else:
        verlag = random.choice(s_p.verlage)
    # 7. Preis
    fehlerhaft = random.random() < 0.05
    if fehlerhaft:
        preis = gauss_range_sample()
    else:
        preis = gauss_range_sample() / 100
    # 9. Status
    fehlerhaft = random.random() < 0.3
    if fehlerhaft:
        status = random.choices(s_p.stati, s_p.stati_gewichte, k=bestand - random.randint(0,bestand))
    else:
        status = random.choices(s_p.stati, s_p.stati_gewichte, k=bestand)
    # 10. Titel
    fehlerhaft = random.random() < 0.3
    if fehlerhaft:
        titel = f"{fake_buecher.word().capitalize()} der {fake_buecher.word().capitalize()}, {random.choices(s_p.sparten, s_p.sparten_gewichte, k=2)}"
    else:
        titel = f"{fake_buecher.word().capitalize()} der {fake_buecher.word().capitalize()}, {random.choices(s_p.sparten, s_p.sparten_gewichte, k=1)}"
    # 11. Ausleihfrist
    try:
        extrahierte_roh = titel.split(", ")[-1]
        # Öffnen der Ziehen, ['Krimis & Thriller', 'Naturwissenschaften'] --> Naturwissenschaften
        extrahierte_sparte = extrahierte_roh.strip("[]'\" ")

        korrekt = random.random() < 0.9  # 90 % korrekt, 10 % absichtlich falsch

        if korrekt and extrahierte_sparte in s_p.leihfristen_nach_sparte:
            leihfrist = s_p.leihfristen_nach_sparte[extrahierte_sparte]
        else:
            # absichtlich fehlerhafte oder unpassende Werte
            leihfrist = random.choice(["", "unbekannt", 7, 999, "14 Tage"])
    except:
        # Parsing hat komplett versagt
        leihfrist = random.choice(["", "fehlerhaft", None])

    buecher.append([titel, autor, isbn, erscheinungsjahr, auflage, zustand, verlag, preis, bestand, status, leihfrist])
