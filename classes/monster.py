import random


class Monster:
    def __init__(self, name, hp, df, weapon, magic, gold):
        self.name = name
        self.hp = hp
        self.df = df
        self.weapon = weapon
        self.magic = magic
        self.gold = gold

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generateDamage()
        pct = self.hp / self.maxHp * 100
        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.chooseEnemySpell()
        else:
            return spell, magic_dmg
