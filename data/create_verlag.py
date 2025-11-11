import random
import selection_pool as s_p



def FehlerhaftGenerieren(id):
    id = id
    # eintrag = []
    name = s_p.verlagsnamen[id - 1]
    name = name.encode("utf-8")
    #name = bytearray(name)
    #name[1] = (name[1] - 1) % 256
    name = name.decode("latin-1")
    adresse = random.choice(s_p.adressen)
    s_p.adressen.remove(adresse)
    adresse = adresse.encode("utf-8")
    #adresse = bytearray(adresse)
    #adresse[1] = (adresse[1] - 1) % 256
    adresse = adresse.decode("latin-1")
    nachname = random.choice(s_p.nachnamen)
    s_p.nachnamen.remove(nachname)
    vorname = random.choice(s_p.vornamen)
    kontaktperson = nachname + "," + vorname
    kontaktperson = kontaktperson.encode("utf-8")
    #kontaktperson = bytearray(kontaktperson)
    #kontaktperson[1] = (kontaktperson[1] - 1) % 256
    kontaktperson = kontaktperson.decode("latin-1")
    telefon = random.choice(s_p.telefonnummern)
    s_p.telefonnummern.remove(telefon)
    # eintrag.append({"id": id, "name": name, "adresse": adresse, "kontaktperson": kontaktperson, "telefon": telefon})
    eintrag = {                                         # Dictionary anstelle einer Liste
        "ID": id,
        "Verlagsname": name,
        "Adresse": adresse,
        "Kontaktperson": kontaktperson,
        "Telefonnummer": telefon
    }
    return eintrag

# print(FehlerhaftGenerieren(21))

def Generieren(id):
    id = id
    # eintrag = []
    name = s_p.verlagsnamen[id - 1]
    adresse = random.choice(s_p.adressen)
    s_p.adressen.remove(adresse)
    nachname = random.choice(s_p.nachnamen)
    s_p.nachnamen.remove(nachname)
    vorname = random.choice(s_p.vornamen)
    kontaktperson = vorname + " " + nachname
    telefon = random.choice(s_p.telefonnummern)
    s_p.telefonnummern.remove(telefon)
    # eintrag.append({"id": id, "name": name, "adresse": adresse, "kontaktperson": kontaktperson, "telefon": telefon})
    eintrag = {                                     # Dictionary anstelle einer Liste
        "ID": id,
        "Verlagsname": name,
        "Adresse": adresse,
        "Kontaktperson": kontaktperson,
        "Telefonnummer": telefon
    }
    return eintrag

# print(Generieren(21))


# Leere Liste erstellen
verlagsdaten = []

fehlerhaft = 1
i = 1
falsch_zaehler = 0                                                                      # ZUSATZ
richtig_zaehler = 0                                                                     # ZUSATZ
# Schleife in der Länge der Liste aus dem selection_pool erstellen
while i <= len(s_p.verlagsnamen):                                                        # wie im PAP
# for i in range(i, len(sp.verlagsnamen) + 1):                                          # Andere Lösung
    if fehlerhaft == random.randint(1, 10):
        falsch = FehlerhaftGenerieren(i)                                           # Funktion FehlerhaftGenerieren einfügen
        verlagsdaten.append(falsch)
        falsch_zaehler = falsch_zaehler + 1
        i = i + 1                                                                       # Bei anderer lösung muss das gelöscht werden
    else:
        richtig = Generieren(i)                                                     # Funktion FehlerhaftGenerieren einfügen
        verlagsdaten.append(richtig)
        richtig_zaehler = richtig_zaehler + 1
        i = i + 1                                                                       # Bei anderer lösung muss das gelöscht werden

# print(verlagsdaten)
# Zähler printen
print("Falsch:", falsch_zaehler, "\nRichtig:", richtig_zaehler)