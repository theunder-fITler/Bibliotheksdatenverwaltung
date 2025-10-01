import random
import csv
import pandas as pd
import create_buecher


## pands nutzen, um die daten anzuschauen -> besser in jupyter arbeiten? ist aber erstmal nur hilfe, um alles richtig zu bekommen --> faker.isbn ist ein problem
# setup pandas
# Alle Spalten anzeigen (auch wenn sie lang sind)
pd.set_option('display.max_columns', None)

# Optional: Alle Spalten komplett anzeigen, ohne abzuschneiden
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# DataFrame erstellen
df = pd.DataFrame(create_buecher.buecher[1:], columns=create_buecher.buecher[0])

print(df.head(20))


## export zu dateien