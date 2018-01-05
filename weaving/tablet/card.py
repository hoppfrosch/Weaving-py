# -*- coding: utf-8 -*-
"""Implementation of Class <Card>"""

# pylint: disable=W0611
import __future__
import re
from version import Version
from collections import OrderedDict
import pprint

__version__ = str(Version('0.2.0-alpha.1'))

def sign(x): return 1 if x >= 0 else -1

class Card(object):
    """
    Definition of a card for tablet weaving
    """

    def __init__(self, holes=4, slant="S"):
        """
        Constructor - generate new card for tablet weaving

        @param    holes   Number of holes within the tablet
        @param    slant   Direction of the tablet (S or Z)
        """

        # ##############################################################################################################
        # Initialize properties

        # Max number of holes within card which can be handled with this class
        self._max_holes = 6

        # Properties for n-holed cards
        # * incAngle: Regular angle a tablet is turned (e.g. a 4holed tablet is turned a quarter turn regulary)
        # * incAngleMin: Minimum angle a tablet can be turned
        self.__prop__ = {
            3: {'incAngle': 120, 'incAngleMin': 30, 'startAngle': 0},
            4: {'incAngle': 90, 'incAngleMin': 45, 'startAngle': 315},
            5: {'incAngle': 72, 'incAngleMin': 18, 'startAngle': 0},
            6: {'incAngle': 60, 'incAngleMin': 30, 'startAngle': 330}
        }

        # motion_sequence records all motions made with a card:
        # "F", "B": regular Turns
        # "f", "b": elemental Turns
        # "TwL", "TwR": twist (rotate the Card along threading direction - Right <-> Left )
        # "FlCw" "FlCcw": flip (flip the card along axis perpendicular to threading direction - Clockwise - Counter-Clockwise)
        self.motion_sequence = []
        self.motion_sequence.append("I")

        # Twists on far side indicate whether the far side has twisted threads or not (in units of incAngleMin)
        self.twists_on_farside = 0

        # ##############################################################################################################
        # Validate number of holes
        if not isinstance(holes, int):
            raise TypeError("Number of holes can only be an integer")
        if not 2 <= holes <= self._max_holes:
            raise ValueError("Given Number of " + str(holes) + " holes must be in range [2.." + str(self._max_holes) + "]")
        self.holes = holes
        self.slant = slant  # pylint: disable=C0103
        self.holesnumbering = "CCW"  # pylint: disable=C0103

        self.threading = OrderedDict()
        for i in range(ord('A'), ord('A') + holes):
            self.threading[chr(i)] = Thread()
        return

    @property
    def slant(self):  # pylint: disable=C0103
        """Getter for property slant"""
        return self._carddirection

    @slant.setter
    def slant(self, value):  # pylint: disable=C0103
        """Setter for property slant"""
        if not isinstance(value, basestring):
            raise TypeError("slant can only be an string")
        if not value is "S" and not value is "Z":
            raise ValueError("slant must either be S or Z")
        self._carddirection = value  # pylint: disable=C0103, W0201

    @property
    def holesnumbering(self):  # pylint: disable=C0103
        """Getter for property holesnumbering

        In normal case the threads are numbered counterclockwise (CCW). If a tablet is flipped, the holesnumbering
        changes to clockwise (CW).
        """
        return self._arrangement

    @holesnumbering.setter
    def holesnumbering(self, value):  # pylint: disable=C0103
        """Setter for property holesnumbering"""
        if not isinstance(value, basestring):
            raise TypeError("holesnumbering can only be an string")
        if not value is "CW" and not value is "CCW":
            raise ValueError("holesnumbering must either be CW or CCW")
        self._arrangement = value  # pylint: disable=C0103, W0201

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


    def inc_on_turn(self, direction="F"):
        """Returns the angle increment when turning a card into a given direction

        @param    direction   Turning direction (Regular turn: "F" or "B" (Forward or Backward), elementary turn: "f" or "b")
        """
        if not direction in  ["F", "B", "f", "b", "I"]:
            raise ValueError("Turning direction must either be <F> (regular Forward) (default) or <B> " + \
                             "(regular Backward) or <f> (elemental Forward) (default) or <b> (elemental Backward)" + \
                             "or <I> (Initial)")

        sign = 1
        if (direction in ["B","b"]):
          sign = -1

        if (direction in ["F","B"]):
            return sign * self.inc_angle
        elif (direction in ["f","b"]):
            return sign * self.inc_angle_min

        return 0


    def turn(self, direction="F"):
        """
        Turning a tablet in a given direction

        @param    direction   Turning direction (Regular turn: "F" or "B" (Forward or Backward), elementary turn: "f" or "b")
        """
        if not direction is "F" and not direction is "B" and not direction is "f" and not direction is "b":
            raise ValueError("Turning direction must either be <F> (regular Forward) (default) or <B> " + \
                             "(regular Backward) or <f> (elemental Forward) (default) or <b> (elemental Backward)")

        # Each regular turn increases/decreases the twists on the farSide by 1
        # Each elemental turn increases/decreases the twists on the farSide by a fraction of 1

        amount  = 1
        if (direction is "B" ) or (direction is "F" ):
            amount = int(self.inc_angle/self.inc_angle_min)

        # Build up the twist on the far side
        # A positive value means: there are s-twists on the far side
        # A negative value means: there are z-twists on the far side
        # A 0 value means: no twists on the far side
        # self.twists_on_farside = self.twists_on_farside + sign(self.inc_on_turn(direction)) * amount
        self.twists_on_farside = self.twists_on_farside + amount

        # Store twist in motion sequence
        self.motion_sequence.append(direction)
        return

    def holepositions(self, motion_id=-1):
        """Returns positions (angles) of the holes on given motion

        @param    motion_id   id of the motion (-1: latest motion)
        """
        if motion_id > len(self.motion_sequence):
            raise ValueError("motion_id is out of range")

        # Get all motions from the start to the requested motion
        id = motion_id
        if (id >= 0):
          id = id + 1
        motion_seq = self.motion_sequence[:id]

        # Starting angle for hole 1
        curr_angle_hole1 = self.__prop__[self.holes]['startAngle']

        # Do all the motions to the requested motions for hole 1
        for i in motion_seq:
            inc = self.inc_on_turn(i)
            curr_angle_hole1 = (curr_angle_hole1 + inc) % 360

            angles = {}
            angles[1] = curr_angle_hole1

            # holes are numbered counterclockwise:
            if (self.holesnumbering is "CCW"):
                sign = 1
            elif (self.holesnumbering is "CW"):
                sign = -1

            for j in range(2,self.holes+1):
                angles[j] = (angles[j-1] + sign * self.inc_angle) % 360

            print (i + " -> " + pprint.pformat(angles))

        return angles


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
    mycard = Card(holes=4)
    mycard.turn("F")
    mycard.turn("B")
    mycard.turn("F")
    mycard.turn("F")
    mycard.turn("B")
    mycard.turn("B")
    mycard.turn("F")
    mycard.turn("F")
    mycard.turn("F")
    mycard.turn("F")
    mycard.turn("f")
    mycard.turn("b")

    print '[%s]' % ', '.join(map(str, mycard.motion_sequence))

    mycard.holepositions(2)

    print ("Finished")
