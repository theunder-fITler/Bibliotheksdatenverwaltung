# Exploration der Datei kundenliste.csv
## Überblick

Entität: kunden

RangeIndex: 252 entries, 0 to 251
Data columns (total 6 columns):
 id   Column              Non-Null Count  Dtype 
---  ------              --------------  ----- 
 0   KundenID            252 non-null    int64 
 1   Name                248 non-null    object
 2   Geburtsdatum        240 non-null    object
 3   Adresse             247 non-null    object
 4   EndeMitgliedschaft  250 non-null    object
 5   Ausgeliehen         252 non-null    object
dtypes: int64(1), object(5)

## KundenID
1. is unique
2. keine nullwerte
3. alle ids von 1-252 vergeben

## Name

0            ???
43           ???
74           NaN
76           NaN
80          Lena
109          ???
149          NaN
194    Madeleine
219     Eckehard
251          NaN

24     Hans-H. Dippel

1. 4 Kudnen haben keinen Eintrag in Name
2. 3 Kudnen haben "???" als Eintrag
3. 3 Kunden haben keinen Nachnamen
4. einer der Kunden hat einen .

## Geburtsdatum

## Adresse

## EndeMitgliedschaft

## Ausgeliehen





