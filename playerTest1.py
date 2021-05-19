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
            "armour" : null,
            "mainHand" : null,
            "offhand" : null
        }


class Item():
    def __init__(self, name, slots=[]):
        self.name = name
        self.slots = slots

