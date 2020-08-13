# GildedRose-Refactoring-Kata / `python`

[How to use this Kata](https://github.com/timberhill/GildedRose-Refactoring-Kata#how-to-use-this-kata)
/
[Gilded Rose requirements](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt)

There are several ways to make this code better.
Even inverting some `if` statements in `GildedRose.update_quality()` will make it much more easy to comprehend and expand.
The most obvious way would probably be moving this functionality to the `Item` class, as expiration is an intrinsic property of an item.
This, however, is explicitly forbidden. Considering this I see two simple ways of making the code more readable and modular.

#### 1. Inheriting `Item`

Create separate classes for special items, e.g.

```python
class AgedItem(Item):
    def __init__(self):
        super(Item, self).__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1
        self.quality += 1

        if self.quality > 50:
            self.quality  = 50
```

This way every special item will have its own `update_quality` method and adding a new type is as simple as creating new class with its own quality logic.
The default item logic, however, will have to be a part of `GildedRose` class, which is suboptimal.
One way around it is to create a `DefaultItem(Item)` class with the default behaviour.

__Pro__: highly modular

__Con__: requires integration of the features in the existing code that uses these classes

#### 2. Adding new functions to `GildedRose` class

Another way is to add item types (e.g. `default`, `inverse` (Aged Brie), etc.) with a function associated with each of them.
The item type can be determined from its name, e.g.

```python
self.special_items = {
    "inverse"   : ("Aged Brie",),
    "legendary" : ("Sulfuras",),
    "pass"      : ("Backstage",),
    "conjured"  : ("Conjured",),
}
```

__Pro__: no need to alter any code outside `GildedRose` class

__Con__: large `GildedRose` class

---

I have adopted the latter approach here as it won't break any _(hypothetical production)_] code that might depend on `GildedRose`.
First, I have implemented the tests that should be passed according to the requirements.
Second, added the functions to handle the default and special item cases, along with the a lookup of item types and item names that belong to that type.

`GildedRose.` is reduced to

```python
def update_quality(self):
    for item in self.items:
        update = self._special_function(item)
        update(item)
```
