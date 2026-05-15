# Kniffel

## Beschreibung
Ein digitales Kniffel‑Spiel mit Pygame, das das klassische Würfelerlebnis mit einem modernen Dark‑UI, animierten Würfeln und einer übersichtlichen Punkteverwaltung kombiniert.

## Features
- Mehrspielermodus, 1 - 4 Spieler möglich
- Namenseingabe für jeden Spieler
- Drei Würfe pro Runde mit frei wählbaren gehaltenen Würfeln
- Kreisförmig angeordnete Würfel im modernen Dark‑UI
- Vollständige Kniffel‑Punkteberechnung
- Ausgegraute Kategorien nach Auswahl
- Gewinneranzeige am Spielende

## Grundregeln
- Es wird mit 5 Würfeln gespielt
- Pro Runde sind bis zu 3 Würfe möglich
- Nach jedem Wurf können beliebige Würfel gehalten oder gelöst werden
- Am Ende jeder Runde wird eine freie Kategorie ausgewählt
- Der obere Block gibt bei 63+ Punkten einen Bonus von 35 Punkten
- Jede Kategorie kann nur einmal genutzt werden
- Am Ende gewinnt der Spieler mit der höchsten Gesamtpunktzahl

## Projektstruktur
main.py        # Hauptprogramm und Start des Main-Loops
cup.py         # Definition der Cup-Klasse (Würfelbecher)
dice.py        # Definition der Dice-Klasse (einzelner Würfel)
game.py        # Definition der Game-Klasse (Spielablauf)
player.py      # Definition der Player-Klasse (Spieler & Daten)
scorecard.py   # Definition der Scorecard-Klasse (Punkte & Kategorien)
