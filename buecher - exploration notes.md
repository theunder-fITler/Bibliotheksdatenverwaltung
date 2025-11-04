# Exploration von der Datei buecher.csv
## Lesen in pandas

Entity: buecher
Attributes:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1313 entries, 0 to 1312
Data columns (total 11 columns):

|id |  Column  |          Non-Null Count | Dtype |  
|--- | ------  |          -------------- | ----- | 
|0  | Titel   |          1313 | non-null |  object |
|1  | Autor   |          1313 | non-null |  object |
|2  | ISBN     |         1313 | non-null |  object |
|3  | Erscheinungsjahr | 1313 | non-null |  object |
|4  | Auflage          | 1313 | non-null |  int64  |
|5  | Zustand          | 1313 | non-null |  object |
|6  | Verlag           | 1313 | non-null |  object |
|7  | Preis            | 1313 | non-null |  float64 |
|8  | Bestand          | 1313 | non-null |  int64  |
|9  | Status           | 1313 | non-null |  object |
|10 | Leihfrist        | 1286 | non-null |  object | 

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

## Zustand

```
0                                                      []
1                                                      []
2         ['Sehr gut', 'Beschädigt', 'In Ordnung', 'Neu']
3       ['Neu', 'In Ordnung', 'Sehr gut', 'In Ordnung'...
4                                ['Unvollständig', 'Neu']
```
- manche Bücher haben mehrere Zustände
  --> Exemplare der Buecher haben wahrscheinlich jeweils verschiedene Zustände
```
array([nan, 'Sehr gut', 'Beschädigt', 'In Ordnung', 'Neu', 'Gut',
       'Verloren', 'Unvollständig', 'Abgenutzt', 'Ausgemustert',
       'In Reparatur'], dtype=object)
```
- manche Bücher haben keinen Zustand
  

--> !Nachfragen, wegen der Bücher ohne Zustand!

## Verlag

FISCHER VERLAGE                         2
Fischer Verlage                        18
C.H. BECK                               1
C.H. Beck                              13
VERLAG C.H. BECK                        1
Verlag C.H. Beck                       22

- manche Verlage scheinen gleich aber unterschiedlich geschrieben

--> !alle fragwürdigen Fälle identifizeiren und nachfragen!

## Preis
```
array([3191.  , 3372.  , 4620.  , 5400.  , 3280.  , 3180.  , 4118.  ,
       1864.  , 1739.  , 2593.  , 2646.  , 2084.  , 5621.  , 4505.  ,
       3348.  , 3558.  , 2291.  , 2585.  , 2033.  , 2191.  , 4444.  ,
       3685.  , 1411.  , 3582.  , 2141.  , 3537.  , 1451.  , 2954.  ,
       4338.  , 3981.  , 3350.  , 1458.  , 3903.  , 2140.  , 2889.  ,
       1704.  , 2405.  , 2778.  , 3498.  , 5444.  , 2667.  , 5450.  ,
         64.91, 2182.  , 3728.  , 2429.  , 3525.  , 2360.  ,   61.09,
       2043.  , 4030.  , 4644.  , 1574.  , 3512.  , 2745.  , 2454.  ,
       4750.  , 3220.  , 1967.  , 1709.  , 3436.  , 1998.  ])
```

- Sprung von 60. auf > 1000.00
- alle Preise über 1000 haben keine Cent-Beträge
- scheinbar kein weiterer Zusammenhang der hohen Preise z.B. mit Erscheinungsjahr oder Kategorie oder Bestand

?? Preis in Cent eingetragen?

--> !Nachfragen und Preise korrigieren!

## Bestand

Bestand
5    148
8    146
3    145
6    143
7    141
9    134
1    131
2    130
4    128
0     67

- es gibt 67 Bücher mit Bestand 0
- alle Bücher mit Bestand 0 haben weder Status, noch Zustand

--> !Nachfragen ob die Bücher aus der DB gelöscht werden dürfen!

## Status

```
array(['verliehen', nan, 'rot', 'verfügbar', 'vorgemerkt', 'gelb',
       'ausgeliehen', 'grün', 'verloren', '???']
```
- verschiedene Systeme:
   - rot, geld, grün
   - verliehen/ausgeliehen, vorgemerkt, verfügbar
- verloren: das Buch ist pysisch verschwunden?
- ???

--> !ein einheitliches System für den Entleiohungen herstellen!
--> !verlorene-Bücher suchen (könnten sie verliehen sein?, sind sie evtl. in der Bibliothek?) - nachfragen und Ausleihungen checken!
--> !???-Bücher suchen (könnten sie verliehen sein?, sind sie evtl. in der Bibliothek?)- nachfragen und Ausleihungen checken!

## Leihfrist

14           496    entspricht 2 Wochen
21           333    entspricht 3 Wochen
28           275    entspricht 4 Wochen
10            73
unbekannt     32
999           29
7             27    entspricht einer Woche
14 Tage       21

- manche Leihfristen fallen aus dem Muster
- 14 Tage = 14?
- 999 ist valide?
- ist 10 eine valide Leihfrist?
- viele Bücher haben Leihfristen von 14, 21 und 28 sind das die einzigen gültigen Fristen?

?? Wie entstehen die Leihfristen?

--> !Nachfragen, wie Leihfristen entstehen und welche werte gültig sind!
--> !"14 Tage" zu 14 angleichen!
