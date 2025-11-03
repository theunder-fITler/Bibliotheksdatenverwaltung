# Exploration von der Datei buecher.csv
## Lesen in pandas

Entity: buecher
Attributes:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1313 entries, 0 to 1312
Data columns (total 11 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Titel             1313 non-null   object 
 1   Autor             1313 non-null   object 
 2   ISBN              1313 non-null   object 
 3   Erscheinungsjahr  1313 non-null   object 
 4   Auflage           1313 non-null   int64  
 5   Zustand           1313 non-null   object 
 6   Verlag            1313 non-null   object 
 7   Preis             1313 non-null   float64
 8   Bestand           1313 non-null   int64  
 9   Status            1313 non-null   object 
 10  Leihfrist         1286 non-null   object  
dtypes: float64(1), int64(2), object(8)
memory usage: 123.2+ KB

## Titel

Längster Titel:
```"Lange der Verstecken, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']"```

- Buchtitel
- Liste mit zweimal dem gleichen Eintrag
- nicht atomar
- nicht wiederholungsgruppenfrei
--> !Spalten aufteilen!

```
1312    Lange der Verstecken, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
18       Halten der Schicken, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
1305      Weiß der Natürlich, ['Kinder- und Jugendbücher', 'Religion & Spiritualität']
1256       Wasser der Straße, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
1238       Schwer der Platz, ['Kinder- und Jugendbücher', 'Fantasy & Science-Fiction']
803        Vier der Zwischen, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
421        Tante der Leicht, ['Fantasy & Science-Fiction', 'Kinder- und Jugendbücher']
713         Brot der Fußball, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
294         Darin der Küche, ['Kinder- und Jugendbücher', 'Fantasy & Science-Fiction']
1300         Blau der Brief, ['Religion & Spiritualität', 'Fantasy & Science-Fiction']
662          Gibt der Wohnen, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
617          Sich der Kein, ['Fantasy & Science-Fiction', 'Fantasy & Science-Fiction']
777          Essen der Kam, ['Fantasy & Science-Fiction', 'Fantasy & Science-Fiction']
104          Draußen der Uns, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
449             Junge der Schlafen, ['Kochen & Ernährung', 'Kinder- und Jugendbücher']
409             Und der Eigentlich, ['Kinder- und Jugendbücher', 'Kochen & Ernährung']
874             Fuß der Sich, ['Kinder- und Jugendbücher', 'Kinder- und Jugendbücher']
554             Zeit der Schenken, ['Kinder- und Jugendbücher', 'Naturwissenschaften']
814             Wirklich der Will, ['Kochen & Ernährung', 'Fantasy & Science-Fiction']
808              Glück der Halten, ['Fantasy & Science-Fiction', 'Kochen & Ernährung']
```

- manche Buecher haben mehrere Kategorien
?? Ist das beabsichtigt?

## Autor

- vorname nachname
- nachname, vorname (id: 3 - Atzler, Janna)
- 3 von 50 zufälligen Einträgen weisen "nachname, vorname -  Struktur" auf

--> !Struktur vereinheitlichen!

## ISBN

1202    978-1-176-72953-7
247     978-1-74951-823-0
112         0-491-41773-X
94          0-01-866209-9

- die meisten ISBNn fangen mit 3 Ziffern an und haben keine Buchstaben
  - Aufbau ist auch inenrhalb dieser unterschiedlich
- 2/50 zufälligen ISBNn in Form mit einer Ziffer am Anfang und einem Buchstaben am Ende
- 1/50 zufälligen ISBN in Form mit einer Ziffer am Anfang und einer Ziffer am Ende
- is_unique: true

## Erscheinungsjahr

- kein NaN
- meist in Form von STR(ddmmyyyy) aber auch yyyymmdd
- z.T. YYYY-MM-DD (2004-05-13)

?? yyyymmdd /ddmmyyyy für Datenbank unproblematisch?
--> !recherchieren, ob Datenbank automatisch erkennt, ob ein Datum gemeint ist, wenn sie einen String mit 8 Ziffern bekommt!

## Auflage
```
array([20, 20, 50, 70, 70, 80, 20, 10, 60, 50, 80, 60, 60, 80, 10, 20, 60,
       20, 30, 20, 50, 30, 50, 90, 90, 90, 30, 70, 60, 80, 30, 50, 90, 50,
       40, 20, 60, 20, 40, 30, 20, 80, 20, 90, 40, 90, 60, 30, 90, 10, 20,
       70, 80, 60, 30, 10, 10, 20, 80, 20, 50, 80, 40, 50, 20, 50, 20, 90])
```

?? Warum gibt es ab 10 nur noch runde Auflagenwerte?

--> !Wegen den Auflagewerten nachfragen!