from faker import Faker



## Faker und random seed
Faker.seed(12345)

## Listen für die Generierung
# pool für Zustände
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
# pool für Verlage
verlagsnamen = [
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
    "Beltz & Gelberg",
    "Bastei Lübbe",
    "Bonnier Verlagsgruppe",
    "Cornelsen Verlag",
    "Eulenspiegel Verlagsgruppe",
    "Hubert Burda Media",
    "Hans Gerig Musikverlage",
    "Haufe Mediengruppe",
    "Ernst Klett Verlag",
    "MairDumont",
    "Medien Union",
    "Münchner Verlagsgruppe",
    "Südwestdeutsche Medien Holding",
    "Verlag C.H. Beck",
    "Verlagsgruppe Georg von Holtzbrinck",
    "Verlagsgruppe Handelsblatt",
    "Verlagsgruppe Herder",
    "Verlagsgruppe Husum",
    "Verlagsgruppe Hüthig Jehle Rehm",
    "Verlagsgruppe Ippen",
    "Verlagsgruppe Random House",
    "Verlagsgruppe Weltbild",
    "Verlagshaus Römerweg",
    "WEKA-Verlagsgruppe",
    "Verlag Moderne Industrie",
    "Redline Verlag",
    "Nomos Verlagsgesellschaft",
    "Oldenbourg Verlag",
    "Verlag J. Neumann",
    "Reinhold Kühn Verlag",
    "Münchener Verlagsgruppe",
    "Verlag Gerhard Rautenberg",
    "Silberschnur Verlag",
    "SingLiesel Verlag",
    "Thomas Kettler Verlag",
    "MM Verlag",
    "Diederichs Verlag",
    "Gräfe und Unzer Verlag",
    "MM Verlag"
    ]

# pool für stati
stati = ["verliehen", "vorgemerkt", "verfügbar", "verloren", "???", "ausgeliehen", "grün", "gelb", "rot"]
stati_gewichte = [100, 30, 200, 10, 5, 20, 100, 30, 200]

# pool für Sparten
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

# pool für namen wird generiert
fake_namen = Faker('de_DE')

vornamen = [f"{fake_namen.first_name()}" for i in range(100)]
nachnamen = [f"{fake_namen.last_name()}" for i in range(100)]

# pool für Adressen
fake_adressen = Faker('de_DE')

adressen = []
for i in range(len(verlagsnamen)):
    adresse = fake_adressen.address().replace("\n", ", ")
    adressen.append(adresse)

# pool für telefonnummern
fake_telefonnummern = Faker('de_DE')

telefonnummern = [f"{fake_telefonnummern.phone_number()}" for i in range(len(verlagsnamen))]