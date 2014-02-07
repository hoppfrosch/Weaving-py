# -*- coding: utf-8 -*-
"""Implementation of Class <Card>"""

# pylint: disable=W0611
import __future__
import re
from version import Version
from collections import OrderedDict

__version__ = str(Version('0.1.0-alpha.2'))


class Card(object):
    """
    Definition of a card for tablet weaving
    """
    # Max number of holes within card which can be handled with this class
    _max_holes = 6
    # Properties for n-holed cards
    _prop = {
        3: {'incAngle': 30, 'startAngle': 270},
        4: {'incAngle': 45, 'startAngle': 225},
        5: {'incAngle': 18, 'startAngle': 270},
        6: {'incAngle': 30, 'startAngle': 255}
    }
    # motion_sequence records all motions made with a card:
    # "F", "B": Turns
    # "TwL", "TwR": twist (rotate the Card along threading direction - Right <-> Left )
    # "FlCw" "FlCcw": flip (flip the card along axis perpendicular to threading direction - Clockwise - Counter-Clockwise)
    motion_sequence = []
    twists_on_farside = 0

    def __init__(self, holes=4, SZ="S"):
        """
        Constructor - generate new card for tablet weaving

        @param    holes   Number of holes within the tablet
        @param    SZ      Threading direction of the tablet (S or Z)
        """
        # Validate number of holes
        if not isinstance(holes, int):
            raise TypeError("Number of holes can only be an integer")
        if not 2 <= holes <= self._max_holes:
            raise ValueError("Given Number of " + str(holes) + " holes must be in range [2.." + str(self._max_holes) + "]")
        self.holes = holes
        self.sz = SZ  # pylint: disable=C0103

        self.threading = OrderedDict()
        for i in range(ord('A'), ord('A') + holes):
            self.threading[chr(i)] = Thread()
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
        self._sz = value  # pylint: disable=C0103, W0201

    @property
    def inc_angle(self):
        """Getter for incrementation angle when rotating an n-holed card"""
        return self._prop[self.holes]['incAngle']

    @property
    def start_angle(self):
        """Getter for incrementation angle when rotating an n-holed card"""
        return self._prop[self.holes]['startAngle']

    @classmethod
    def turn(cls, direction="F"):
        """
        Turning a tablet in a given direction

        @param    direction   Turning direction ("F" or "B" (Forward or Backward))
        """
        if not direction is "F" and not direction is "B":
            raise ValueError("Turning direction must either be F (Forward) or B (Backward)")

        if direction is "F":
            cls.twists_on_farside = cls.twists_on_farside + 1
        else:
            cls.twists_on_farside = cls.twists_on_farside - 1

        cls.motion_sequence.append(direction)


class Thread(object):
    """
    Definition of a thread

    @Todo More complete implementation
    """

    def __init__(self, color=(0, 0, 0), twistdir="UNKNOWN", material="UNKNOWN", singlethreads=1):
        """
        Constructor - generate new thread

        @param color            Color of the thread as List of decimal RGB-values
        @param twistdir         Twisting direction of the thread
        @param material         Material of the thread
        @param singlethreads    Number of single threads within the thread
        """
        self.color = color
        self.twistdir = twistdir
        self.material = material
        self.singlethreads = singlethreads
        return


if __name__ == '__main__':
    mycard = Card(holes=6)
    print "Finished"
