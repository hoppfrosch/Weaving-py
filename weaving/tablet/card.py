# -*- coding: utf-8 -*-
"""Implementation of Class <Card>"""

# pylint: disable=W0611
import __future__


class Card(object):
    """
    Definition of a card for tablet weaving
    """
    _max_holes = 6

    def __init__(self, holes=4):
        """
        Constructor - generate new card for tablet weaving

        @param    holes   Number of holes within the tabletin the sequence to return
        """
        # Validate number of holes
        if not isinstance(holes, int):
            raise TypeError("Number of holes can only be an integer")
        if not 2 <= holes <= self._max_holes:
            raise ValueError("Given Number of " + str(holes) + " holes must be in range [2.." + str(self._max_holes) + "]")
        self.holes = holes
