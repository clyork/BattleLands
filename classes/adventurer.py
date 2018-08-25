import random


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, money, lvl):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkHigh = atk + lvl
        self.atkLow = atk - lvl
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.money = money
        self.lvl = lvl

    def generate_damage(self):
        return random.randrange(self.atkLow, self.atkHigh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def use_magic(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        for item in self.actions:
            print("    ", str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print("    ", str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        for item in self.items:
            print("    ", str(i) + ".", item["item"].name, ":", item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        for enemy in enemies:
            if enemy.getHp() != 0:
                print("     " + str(i) + ":" + enemy.name)
                i += 1
        choice = (int(input("Choose target:")) - 1)
        return choice

    def get_stats(self):
        # HP Bar
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHp) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        # MP Bar
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxMp) * 100 / 10
        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        # White Space
        hp_string = str(self.hp) + "/" + str(self.maxHp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string
        mp_string = str(self.mp) + "/" + str(self.maxMp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxHp) * 100 / 2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_string = str(self.hp) + "/" + str(self.maxHp)
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def add_money(self, amount):
        self.money = self.money + amount

    def lose_money(self, amount):
        self.money = self.money - amount

    def get_level(self):
        return self.lvl

    def level_up(self):
        self.lvl += self.lvl + 1
