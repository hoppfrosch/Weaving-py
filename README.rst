Weaving - A Library for Tablet-Weavers
======================================

ToDo
----
* Tablet manipulation
  * "Turn" - Drehung um die Rotations-Achse (in unterschiedlichen Winkelgraden)
  * "Twist" - Drehung um die Längsachse
  * "Flip" - Umklappen (Drehung um die Hochachse)
  
* Wie soll die Notation aussehen, damit die Position des Brettchens eindeutig beschrieben ist?
  Idee:
  * S/Z beschreibt das Threading
  * Aktueller Winkel des Loches "A" beschreibt die Lage des Brettchens relativ zum Weber
  * Vorsicht "FLIP" ändert die Reihenfolge der Löcher
    => AB   -> Flip -> BA
       DC              CD
      Vorher ABCD , nach flip  ADCB!

* Bezeichnung der Löcher?
  AB  oder AD
  CD       BC

  Wenn man ADBC vorwärts dreht, dann ist kommen nacheinader die Löcher A - B - C - D in die upper-nearside position
  Wenn man ABCD vorwärts dreht, dann ist kommen nacheinader die Löcher A - C - D - B in die upper-nearside position