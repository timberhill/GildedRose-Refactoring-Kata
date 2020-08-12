# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_validation(self):
        gilded_rose = GildedRose([
            Item("Aged Brie", 0, 49),
            Item("FOO", 0, 1)
        ])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[1].quality)

if __name__ == '__main__':
    unittest.main()
