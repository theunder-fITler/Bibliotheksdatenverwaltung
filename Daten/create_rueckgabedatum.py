from create_kunden import kunden_liste
from create_buecher import buecher
from datetime import timedelta
import create_buecher


# Liste aller ausgeliehenen Bücher in komischen Format:
buecher_ausgeliehen_aktuell = []

for kunde in kunden_liste:
    if kunde["Ausgeliehen"]:
        for buch_datum in kunde["Ausgeliehen"]:
            buecher_ausgeliehen_aktuell.append(buch_datum)
    else:
        pass

print(f"derzeit verliehene bücher: {buecher_ausgeliehen_aktuell}")

for buch_datum in buecher_ausgeliehen_aktuell:
    print(f"buch_datum: {buch_datum}")
    for buch in create_buecher.buecher:
        if buch_datum[0] in buch[2]:
            leihfrist = buch[10]
        else:
            pass
    try:
        buch_datum = (buch_datum[0], buch_datum[1] + timedelta(days=leihfrist))
        print(f"buch_datum nach änderung: {buch_datum}")
    except TypeError:
        print("Fehler beim Datentyp: Eintrag konnte nicht verändert werden")
