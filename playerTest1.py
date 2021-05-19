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

    def removeFromInventory(self, item):
        itemToRemove = self.checkInventory(item)
        del self.inventory[itemToRemove.name]

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

    def printAllItems(self):
        self.printInventory()
        print()
        self.printEquippedItems()

class Item:
    def __init__(self, name, slot=[]):
        self.name = name
        self.slot = slot

class Weapon(Item):
    def __init__(self, name, slot, damage):
        super().__init__(name, slot)
        self.damage = damage

testPlayer = Player("testPlayer")
Sword = Weapon("Sword", "Main Hand", 2)
Spear = Weapon("Spear", "Main Hand", 4)
Shield = Item("Shield", "Off Hand")

testPlayer.addToInventory(Spear)
testPlayer.addToInventory(Sword)
testPlayer.addToInventory(Shield)
testPlayer.equipItem(Sword)
testPlayer.equipItem(Shield)
testPlayer.printAllItems()
testPlayer.removeFromInventory(Spear)
testPlayer.printAllItems()