# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
    

    def _validate_items(self):
        """
        Forces all item qualities to 0..50 range
        """
        for item in self.items:
            if item.quality < 0:
                item.quality = 0
            elif item.quality > 50:
                item.quality = 50


    def _update_quality_default(self, item):
        item.sell_by -= 1

        if item.sell_by >= 0:
            item.quality -= 1
        else:
            item.quality -= 2


    def _update_quality_inverse(self, item):
        item.sell_by -= 1
        item.quality += 1


    def _update_quality_legendary(self, item):
        item.quality = 80


    def _update_quality_pass(self, item):
        item.sell_by -= 1

        if item.sell_by > 10:
            item.quality += 1
        elif item.sell_by <= 10 and item.sell_by > 5:
            item.quality += 2
        elif item.sell_by <= 5 and item.sell_by >= 0:
            item.quality += 3
        else:
            item.quality = 0


    def _update_quality_conjured(self, item):
        item.sell_by -= 1

        if item.sell_by >= 0:
            item.quality -= 2
        else:
            item.quality -= 4



    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
