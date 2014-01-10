# -*- coding: utf-8 -*-
"""Implementation of Class <Card>"""

# pylint: disable=W0611
import __future__
import re
from version import Version

__version__ = str(Version('0.1.0-alpha.1'))


class Card(object):
    """
    Definition of a card for tablet weaving
    """
    _max_holes = 6

    def __init__(self, holes=4, SZ="S"):
        """
        Constructor - generate new card for tablet weaving

        @param    holes   Number of holes within the tablet
        """
        # Validate number of holes
        if not isinstance(holes, int):
            raise TypeError("Number of holes can only be an integer")
        if not 2 <= holes <= self._max_holes:
            raise ValueError("Given Number of " + str(holes) + " holes must be in range [2.." + str(self._max_holes) + "]")
        self.holes = holes
        self.sz = SZ  # pylint: disable=C0103
        return

    @property
    def sz(self):  # pylint: disable=C0103
        """Getter for property SZ"""
        return self._sz

    @sz.setter
    def sz(self, value):  # pylint: disable=C0103
        """Setter for property SZ"""
        if not isinstance(value, basestring):
            raise TypeError("SZ can only be an string")
        if not value is "S" and not value is "Z":
            raise ValueError("SZ must either be S or Z")
        self._sz = value  # pylint: disable=C0103
