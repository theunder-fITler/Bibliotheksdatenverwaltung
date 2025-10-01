from faker import Faker


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

# pool für Autoren wird generiert
fake_autoren = Faker('de_DE')

autoren_vorname = [f"{fake_autoren.first_name()}" for i in range(100)]
autoren_nachname = [f"{fake_autoren.last_name()}" for i in range(100)]