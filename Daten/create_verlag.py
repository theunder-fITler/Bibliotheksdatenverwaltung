import random
from faker import Faker
import selection_pool as s_p



## Verlage faken
fake_verlag = Faker("de_DE")
ANZAHL_VERLAGE = 100

# Feste Liste einiger realistischer (oder anmutender) Verlagsnamen
def generiere_verlag(verlag_id, fehlerquote=0.1):
    fehlerhaft = random.random() < fehlerquote

    # Name
    name = random.choice(s_p.verlage)
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

# Generieren
verlage = [generiere_verlag(i + 1) for i in range(ANZAHL_VERLAGE)]
