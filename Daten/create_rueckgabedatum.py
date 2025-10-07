from create_kunden import kunden_liste
from create_buecher import buecher
from datetime import timedelta


# Liste aller ausgeliehenen Bücher in komischen Format:
buecher_ausgeliehen_aktuell = []

for kunde in kunden_liste:
    if kunde["Ausgeliehen"]:
        for buch_datum in kunde["Ausgeliehen"]:
            buecher_ausgeliehen_aktuell.append(buch_datum)
    else:
        pass

print(f"derzeit verliehene bücher: {buecher_ausgeliehen_aktuell}")

for buch in buecher_ausgeliehen_aktuell:
    if buch in buecher:
        buch