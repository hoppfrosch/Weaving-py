Weaving - A Library for Tablet-Weavers
======================================

ToDo
----
* Tablet manipulation
  * "Turn" - Drehung um die Rotations-Achse (in unterschiedlichen Winkelgraden)
  * "Twist" - Drehung um die L�ngsachse
  * "Flip" - Umklappen (Drehung um die Hochachse)
  
* Wie soll die Notation aussehen, damit die Position des Brettchens eindeutig beschrieben ist?
  Idee:
  * S/Z beschreibt das Threading
  * Aktueller Winkel des Loches "A" beschreibt die Lage des Brettchens relativ zum Weber
  * Vorsicht "FLIP" �ndert die Reihenfolge der L�cher
    => AB   -> Flip -> BA
       DC              CD
      Vorher ABCD , nach flip  ADCB!

* Bezeichnung der L�cher?
  AB  oder AD
  CD       BC

  Wenn man ADBC vorw�rts dreht, dann ist kommen nacheinader die L�cher A - B - C - D in die upper-nearside position
  Wenn man ABCD vorw�rts dreht, dann ist kommen nacheinader die L�cher A - C - D - B in die upper-nearside position