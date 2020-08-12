# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_validation(self):
        gilded_rose = GildedRose([
            Item("Aged Brie", 0, 49),
            Item("Foo", 0, 1)
        ])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[1].quality)


    def test_sulfuras(self):
        gilded_rose = GildedRose([
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=30),
        ])
        gilded_rose.update_quality()
        self.assertEqual(80, gilded_rose.items[0].quality)
        self.assertEqual(80, gilded_rose.items[1].quality)


    def test_aged_brie(self):
        gilded_rose = GildedRose([
             Item(name="Aged Brie", sell_in=2, quality=0),
        ])
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[0].sell_in)


    def test_backstage_pass(self):
        gilded_rose = GildedRose([
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        ])
        gilded_rose.update_quality()
        self.assertEqual(21, gilded_rose.items[0].quality)
        self.assertEqual(50, gilded_rose.items[1].quality)


    def test_conjured(self):
        gilded_rose = GildedRose([
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),
        ])
        gilded_rose.update_quality()
        self.assertEqual(4, gilded_rose.items[0].quality)



if __name__ == '__main__':
    unittest.main()
