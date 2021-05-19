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
            "Armour" : None,
            "Main Hand" : None,
            "Off Hand" : None
        }

    def addToInventory(self, item):
        if isinstance(item, Item):
            self.inventory.update({item.name : item})
            #self.inventory[item.name] = item
            print(str(item.name) + " added to inventory")
        else:
            print("item cannot be added to inventory")

    #checks whether the object's inventory contains the
    #object specified in the parameter.  Returns None if
    #the object is not in the Player object's inventory,
    #otherwise it returns the object.
    def checkInventory(self, item):
        ItemFound = None
        if item in self.inventory.values():
            return item
        else:
            return None
    
    def printInventory(self):
        print(self.name + " Inventory:")
        for item in self.inventory.values():
            print(item.name + " (" + type(item).__name__ + ")")

    def equipItem(self, item):
        itemSlot = self.equipmentSlots[item.slot]
        if self.checkInventory(item):
            if itemSlot != None:
                self.addToInventory(itemSlot)
            self.equipmentSlots[item.slot] = item
            del self.inventory[item.name]
        else:
            print("Item not in player inventory")

    def printEquippedItems(self):
        print(str(self.name) + " Equipped Items:")
        for key in self.equipmentSlots:
            if self.equipmentSlots[key] != None:
                print(key + ": " + self.equipmentSlots[key].name)
            else:
                print(key + ": " + "None")

class Item:
    def __init__(self, name, slot):
        self.name = name
        self.slot = slot

testPlayer = Player("testPlayer")
Sword = Item("Sword", "Main Hand")
Spear = Item("Spear", "Main Hand")

testPlayer.addToInventory(Sword)
#testPlayer.addToInventory("test")
#print(testPlayer.checkInventory(Spear))
#print(testPlayer.checkInventory(Sword))

testPlayer.equipItem(Sword)
testPlayer.printInventory()
testPlayer.printEquippedItems()
print()
testPlayer.addToInventory(Spear)
testPlayer.equipItem(Spear)
print("Player Inventory after spear:")
testPlayer.printInventory()
print("Player equipment after spear:")
testPlayer.printEquippedItems()