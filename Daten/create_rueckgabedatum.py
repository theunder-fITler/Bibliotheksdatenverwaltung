from create_kunden import kunden_liste
from create_buecher import buecher
from datetime import timedelta
import create_buecher



# Liste aller ausgeliehenen Bücher in komischen Format (tupel) erstellen:
buecher_ausgeliehen_aktuell = []

for kunde in kunden_liste:
    # Wenn ein Kunde mindestens ein Buch ausgeliehen hat, wird es hier aus dem Dict herausgesucht (Format: (ISBN, Ausleihdatum)
    if kunde["Ausgeliehen"]:
        for buch_datum in kunde["Ausgeliehen"]:
            buecher_ausgeliehen_aktuell.append(buch_datum)
    else:
        pass

## Debugg Ausgabe
# print(f"derzeit verliehene bücher: {buecher_ausgeliehen_aktuell}")

# Neue Liste mit verliehenen Büchern und derem Rückgabedatum (Format: (ISBN, Rückgabedatum)
buecher_ausgeliehen_rueckgabe = []

for buch_datum in buecher_ausgeliehen_aktuell:
    ## Debugg Ausgabe
    # print(f"buch_datum: {buch_datum}")
    for buch in create_buecher.buecher:
        # mit Hilfe der ISBN das Buch in der buecher-Liste finden
        if buch_datum[0] in buch[2]:
            # die Leihfrist für dieses Buch bestimmen
            leihfrist = buch[10]
        else:
            pass
    # Versuche über die Leihfrist das Rückgabedatum festzulegen
    try:
        buch_rueckgabedatum = (buch_datum[0], buch_datum[1] + timedelta(days=leihfrist))
        ## Debugg Ausgabe
        # print(f"buch_datum nach änderung: {buch_datum}")
        buecher_ausgeliehen_rueckgabe.append(buch_rueckgabedatum)
    except TypeError:
        print("Fehler beim Datentyp: Eintrag konnte nicht verändert werden")
        buch_rueckgabedatum = (buch_datum[0], None)
        buecher_ausgeliehen_rueckgabe.append(buch_rueckgabedatum)

## Debugg Ausgabe
print(f"Liste der verliehenen Bücher mit Rückgabedatum: {buecher_ausgeliehen_rueckgabe}")