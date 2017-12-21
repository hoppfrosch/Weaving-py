# -*- coding: utf-8 -*-
"""Implementation of Class <Card>"""

# pylint: disable=W0611
import __future__
import re
from version import Version
from collections import OrderedDict

__version__ = str(Version('0.1.0-alpha.4'))


class Card(object):
    """
    Definition of a card for tablet weaving
    """

    def __init__(self, holes=4, SZ="S"):
        """
        Constructor - generate new card for tablet weaving

        @param    holes   Number of holes within the tablet
        @param    SZ      Threading direction of the tablet (S or Z)
        """

        # ##############################################################################################################
        # Initialize properties

        # Max number of holes within card which can be handled with this class
        self._max_holes = 6

        # Properties for n-holed cards
        # * incAngle: Regular angle a tablet is turned (e.g. a 4holed tablet is turned a quarter turn regulary)
        # * incAngleMin: Minimum angle a tablet can be turned
        self.__prop__ = {
            3: {'incAngle': 120, 'incAngleMin': 30, 'startAngle': 270},
            4: {'incAngle': 90, 'incAngleMin': 45, 'startAngle': 225},
            5: {'incAngle': 72, 'incAngleMin': 18, 'startAngle': 270},
            6: {'incAngle': 60, 'incAngleMin': 30, 'startAngle': 255}
        }

        # motion_sequence records all motions made with a card:
        # "F", "B": regular Turns
        # "f", "b": elemental Turns
        # "TwL", "TwR": twist (rotate the Card along threading direction - Right <-> Left )
        # "FlCw" "FlCcw": flip (flip the card along axis perpendicular to threading direction - Clockwise - Counter-Clockwise)
        self.motion_sequence = []

        # Twists on far side indicate whether the far side has twisted threads or not (in units of incAngleMin)
        self.twists_on_farside = 0

        # ##############################################################################################################
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
        """Getter for incrementation angle when rotating an n-holed card regulary"""
        return self.__prop__[self.holes]['incAngle']

    @property
    def inc_angle_min(self):
        """Getter for incrementation angle when rotating an n-holed card elementary"""
        return self.__prop__[self.holes]['incAngleMin']

    @property
    def start_angle(self):
        """Getter for incrementation angle when rotating an n-holed card"""
        return self.__prop__[self.holes]['startAngle']

    @property
    def current_angle(self):
        """Returns the current angle of hole A"""
        curr_angle = self.__prop__[self.holes]['startAngle']
        for i in self.motion_sequence:
            print (i)
        return curr_angle

    def turn(self, direction="F"):
        """
        Turning a tablet in a given direction

        @param    direction   Turning direction (Regular turn: "F" or "B" (Forward or Backward), elementary turn: "f" or "b")
        """
        if not direction is "F" and not direction is "B" and not direction is "f" and not direction is "b":
            raise ValueError("Turning direction must either be <F> (regular Forward) (default) or <B> " + \
                             "(regular Backward) or <f> (elemental Forward) (default) or <b> (elemental Backward)")

        # Number of elementary turns caused by the current turn
        amount = self.inc_angle/self.inc_angle_min

        # Build up the twist on the far side
        if direction is "F":
            self.twists_on_farside = self.twists_on_farside + amount
        elif direction is "f":
            self.twists_on_farside = self.twists_on_farside + 1
        elif direction is "B":
            self.twists_on_farside = self.twists_on_farside - amount
        elif direction is "b":
            self.twists_on_farside = self.twists_on_farside - 1

        # Store twist in motion sequence
        self.motion_sequence.append(direction)


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
    print ("Finished")
