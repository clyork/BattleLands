'''
Created on Aug 4, 2018

@author: Cody York
'''

import random

class Spell:
    def __init__(self, name, magic_cost, dmg, magic_type, magic_level):
        self.name = name
        self.magic_cost = magic_cost
        self.dmg = dmg
        self.magic_type = magic_type
        self.magic_level = magic_level
        
    def generateDamage(self):
        #change this function to be more forgiving ect for different magic_level
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
        
        
