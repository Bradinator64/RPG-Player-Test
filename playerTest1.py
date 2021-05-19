# -*- coding: utf-8 -*-

"""a test to create a player object for a text-based rpg"""


"""imports"""

import os

"""classes"""

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.equipmentSlots = {
            "armour" : None,
            "mH" : None,
            "oH" : None
        }

    def addToInventory(self, item):
        if isinstance(item, Item):
            self.inventory[item.name] = item
            print(str(item.name) + " added to inventory")
        else:
            print("item cannot be added to inventory")

class Item:
    def __init__(self, name, slots=[]):
        self.name = name
        self.slots = slots

testPlayer = Player("testPlayer")
Sword = Item("Sword", ["mH"])

testPlayer.addToInventory(Sword)
testPlayer.addToInventory("test")

print(testPlayer.inventory)