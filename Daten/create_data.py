import csv
import pandas as pd
import create_buecher
import create_kunden
import create_verlag
import create_rueckgabedatum



## pands nutzen, um die daten anzuschauen -> besser in jupyter arbeiten? ist aber erstmal nur hilfe, um alles richtig zu bekommen
# setup pandas
# Alle Spalten anzeigen (auch wenn sie lang sind)
pd.set_option('display.max_columns', None)

# Optional: Alle Spalten komplett anzeigen, ohne abzuschneiden
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

## DataFrame für die Bücher erstellen
# buecher ist eine Liste mit Listen, deshalb muss columns(= erste Liste in der Liste) definiert werden
df_buecher = pd.DataFrame(create_buecher.buecher[1:], columns=create_buecher.buecher[0])

print("-------")
print("Dataframe")
print("-------")
print(df_buecher)

## DataFrame für die Kunden erstellen
# kunden_liste ist eine Liste mit dicts
df_kunde = pd.DataFrame(create_kunden.kunden_liste)

print("-------")
print("Dataframe")
print("-------")
print(df_kunde)

## DataFrame für die Verlage erstellen
# verlage ist eine Liste mit dicts
df_verlage = pd.DataFrame(create_verlag.verlagsdaten)

print("-------")
print("Dataframe")
print("-------")
print(df_verlage)

## DataFrame für die rückgabedatum erstellen
# buecher_ausgeliehen_rueckgabe ist eine Liste mit tupeln
df_buecher_rueckgabe = pd.DataFrame(create_rueckgabedatum.buecher_ausgeliehen_rueckgabe, columns=["verliehene Buecher", "Rückgabedatum"])

print("-------")
print("Dataframe")
print("-------")
print(df_buecher_rueckgabe)

## export zu dateien
datensaetze = {"buecher": create_buecher.buecher,
              "kundenliste": create_kunden.kunden_liste,
              "verlage": create_verlag.verlagsdaten,
              "rückgabeliste":create_rueckgabedatum.buecher_ausgeliehen_rueckgabe,
               }


for name, datensatz in datensaetze.items():
    erster_eintrag = datensatz[0]
    with open(f'{name}.csv', 'w', newline='', encoding="utf-8") as csvfile:

        if isinstance(erster_eintrag, dict):
            fieldnames = list(datensatz[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datensatz)

        elif isinstance(erster_eintrag, (list, tuple)):
            writer = csv.writer(csvfile)
            writer.writerows(datensatz)

        else:
            writer = csv.writer(csvfile)
            for eintrag in datensatz:
                writer.writerow([eintrag])

    print(f"{name}.csv erfolgreich exportiert.")