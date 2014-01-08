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


if __name__ == '__main__':
    unittest.main()
