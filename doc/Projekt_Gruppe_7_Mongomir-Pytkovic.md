# Einführung

## Was ist der Kontext, warum ist das Projekt relevant, und worum geht es?

Datensätze von Fussballspielen von Kaggle (SQLite), Migration eines Teils davon nach MongoDB mit Python

# Datenmanagement

## Um welche Datenbanktechnologie handelt es sich?

SQLite -> MongoDB

## Welche Anwendungen (Use Case) unterstützt ihre Datenbank?

- Abfragen sämtlicher Spiele, in denen ein bestimmter Spieler zum Einsatz
  gekommen ist

## Welche Daten werden migriert/eingefügt, und wie genau?

Es sollen die relationalen Entitäten `Match`, `Player`, `Player_Attributes`,
`Team`, `Team_Attributes` zu einer JSON-Struktur namens `Match` kombiniert
werden. Dabei werden die an einem Spiel teilnehmenden Mannschaften mit ihren
Spielern nicht referenziert, sondern direkt mit allen relevanten Informationen
in einer hierarchischen Struktur abgelegt:

- `match`
    - `home_team`
        - `name`
        - `players`
            - `player_1`
            - `...`
            - `player_n`
    - `away_team`
        - `name`
        - `players`
            - `player_1`
            - `...`
            - `player_n`
    - `goals_home_team`
    - `goals_away_team`

Die Entitäten `League` und `Country` sollten zudem in eine `League`-Struktur
überführt werden:

- `league`
    - `id`
    - `name`
    - `country`

## Wie interagiert der Benutzer mit der Datenbank?

TODO: per Web-Schnittstelle

# Datenmodellierung

## Welches Datenmodell (ER) liegt ihrem Projekt zugrunde?

Dies ist ein Auszug aus dem ER-Modell, der nur die Tabellen und Spalten enthält,
die auch tatsächlich in die Dokumentdatenbank migriert werden sollen:

- `League`
    - TODO
- `Match`
- `Player`
- `Player_Attributes`
- `Team`
- `Team_Attributes`

Das komplette Schema ist auf
[Kaggle](https://www.kaggle.com/hugomathien/soccer/data) ersichtlich.

## Wie wird ihr Datenmodell in Ihrer Datenbank in ein Schema übersetzt?

# Datenbanksprachen

## Wie werden Daten anhand einer Query abgefragt?

# Konsistenzsicherung

## Wie wird die Datensicherheit gewährleistet?

Gar nicht; die Daten sind nicht sensibel. Evtl. Userkonfiguration, sodass nur
ein Benutzer die Migration vornehmen kann, der Enduser aber nur abfragen kann.

## Wie können Transaktionen parallel/konkurrierend verarbeitet werden?

Es sind nur lesende Abfragen möglich.

# Systemarchitektur

## Wie ist der Server aufgebaut und wie wurde er installiert?

Siehe Dockerfile

## Wie kann die Effizienz von Datenanfragen optimiert werden?

# Vergleich mit relationalen Datenbanken

## Vergleichen Sie ihre NoSQL-Technologie mit SQL-Datenbanken.

# Schlussfolgerungen

## Was haben Sie erreicht, und welche Erkenntnisse haben sie dabei gewonnen?

## Wie beurteilt ihre Gruppe die gewählte Datenbanktechnologie, und was sind Vor- und Nachteile?
