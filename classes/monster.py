'''
Created on Aug 4, 2018

@author: Cody York
'''

import random

class Monster:
    skeleton_list_rank_1 = [
                            {'name': 'Skeleton Soldier', 'hp': '10', 'df': '1', 'weapon': 'basic sword', 'magic': 'none', 'gold': '3'},
                            {'name': 'Skeleton Archer', 'hp': '12', 'df': '0', 'weapon': 'basic bow', 'magic': 'none', 'gold': '2'}    
                        ]
    skeleton_list_rank_2 = [
                            {'name': 'Skeleton Leader', 'hp': '15', 'df': '1', 'weapon': 'sharp sword', 'magic': 'none', 'gold': '8'},
                            {'name': 'Skeleton Sniper', 'hp': '14', 'df': '1', 'weapon': 'long bow', 'magic': 'none', 'gold': '9'}    
                        ]
    skeleton_list_rank_3 = [
                            {'name': 'Captain Keg Beard', 'hp': '20', 'df': '1', 'weapon': 'Keg\'s Cutless', 'magic': 'none', 'gold': '18'}
                        ]
    bandit_list_rank_1 = [
                            {'name': 'Bandit Pillager', 'hp': '11', 'df': '0', 'weapon': 'basic axe', 'magic': 'none', 'gold': '4'},
                            {'name': 'Bandit Archer', 'hp': '14', 'df': '0', 'weapon': 'basic bow', 'magic': 'none', 'gold': '5'},
                            {'name': 'Bandit Mage', 'hp': '9', 'df': '0', 'weapon': 'basic staff', 'magic': 'fireball, thunder, gust', 'gold': '6'},              
                        ]
    bandit_list_rank_2 = [
                            {'name': 'Bandit Leader', 'hp': '17', 'df': '1', 'weapon': 'hand axe', 'magic': 'none', 'gold': '9'},
                            {'name': 'Bandit Sniper', 'hp': '16', 'df': '1', 'weapon': 'crossbow', 'magic': 'none', 'gold': '11'},
                            {'name': 'Bandit Wizard', 'hp': '15', 'df': '0', 'weapon': 'basic staff', 'magic': 'fireball, thunder, gust, chain lightining', 'gold': '14'},              
                        ]
    bandit_list_rank_3 = [
                            {'name': 'Bandit Keith', 'hp': '23', 'df': '1', 'weapon': 'Tomahawk', 'magic': 'none', 'gold': '21'},
                            {'name': 'Slimy Katria', 'hp': '22', 'df': '1', 'weapon': 'Crossbolt', 'magic': 'none', 'gold': '22'},
                            {'name': 'Lex Chance', 'hp': '24', 'df': '0', 'weapon': 'Lex\'s Rapier'  , 'magic': 'none', 'gold': '36'},              
                        ]
    
    
    
    def __init__(self, name, hp, df, weapon, gold):
        self.name = name
        self.hp = hp
        self.df = df
        self.weapon = weapon
        self.gold = gold
        
    def chooseEnemySpell(self):
        magicChoice = random.randrange(0, len(self.magic))
        spell = self.magic[magicChoice]
        magicDmg = spell.generateDamage()
        pct = self.hp/self.maxHp* 100
        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.chooseEnemySpell()
        else:
            return spell, magicDmg
