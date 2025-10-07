import random
import csv
import pandas as pd
import create_buecher
import create_kunden


## pands nutzen, um die daten anzuschauen -> besser in jupyter arbeiten? ist aber erstmal nur hilfe, um alles richtig zu bekommen --> faker.isbn ist ein problem
# setup pandas
# Alle Spalten anzeigen (auch wenn sie lang sind)
pd.set_option('display.max_columns', None)

# Optional: Alle Spalten komplett anzeigen, ohne abzuschneiden
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# DataFrame für die Bücher erstellen
df_buecher = pd.DataFrame(create_buecher.buecher[1:], columns=create_buecher.buecher[0])

# DataFrame für die Kunden erstellen -->! geht nicht, da die Datenstruktur zu verschachtelt ist
df_kunde = pd.DataFrame(create_kunden.generiere_kunde(i+1 for i in range(20)))

print(df_kunde)

## export zu dateien