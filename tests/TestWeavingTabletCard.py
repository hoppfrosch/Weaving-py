"""UnitTest"""
# -*- coding: utf-8 -*-

import sys
import os
import unittest
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

# pylint: disable=F0401
import weaving


# pylint: disable=R0904
class TestWeavingTabletCardHoles(unittest.TestCase):
    """Unittest concerning joles of a card"""

    def setUp(self):
        self.test = 0

    def test_holes_4(self):
        """Successful test on 4 hole card"""

        mycard = weaving.tablet.card.Card()
        self.assertEqual(mycard.holes, 4)
        return

    def test_holes_2(self):
        """Successful test on 2 hole card"""
        mycard = weaving.tablet.card.Card(2)
        self.assertEqual(mycard.holes, 2)

    def test_holes_1(self):
        """Failure test on 1 hole card (too less holes)"""
        self.assertRaises(ValueError, weaving.tablet.card.Card, (1))

    def test_holes_25(self):
        """Failure test on 25 hole card (too many holes)"""
        self.assertRaises(ValueError, weaving.tablet.card.Card, (25))

    def test_holes_string(self):
        """Failure test on unknown hole card (number of holes is not an integer)"""
        self.assertRaises(TypeError, weaving.tablet.card.Card, ("STRING"))


class TestWeavingTabletCardSZ(unittest.TestCase):
    """Unittest concerning joles of a card"""

    def setUp(self):
        self.test = 0

    def test_s(self):
        """Successful test on S-threaded card"""
        mycard = weaving.tablet.card.Card()
        self.assertEqual(mycard.sz, "S")

    def test_z(self):
        """Successful test on Z-threaded card"""
        mycard = weaving.tablet.card.Card(SZ="Z")
        self.assertEqual(mycard.sz, "Z")

    def test_z_set(self):
        """Successful test on Z-threaded card"""
        mycard = weaving.tablet.card.Card()
        self.assertEqual(mycard.sz, "S")
        mycard.sz = "Z"
        self.assertEqual(mycard.sz, "Z")

    def test_wrongdatatype(self):
        """Failure test on wrong SZ-Type (SZ is not a string)"""
        self.assertRaises(TypeError, lambda: weaving.tablet.card.Card(SZ=1))

    def test_wrongdatavalue(self):
        """Failure test on wrong SZ-Type (SZ is not a string)"""
        self.assertRaises(ValueError, lambda: weaving.tablet.card.Card(SZ="A"))


if __name__ == '__main__':
    unittest.main()
