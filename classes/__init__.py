from classes.magic import Spell
from classes.inventory import Item
from classes.adventurer import Person
from classes.game import Game
from classes.monster import Monster
from classes.weapon import Staff, Sword, Axe, Bow, Crossbow
import time

# Create Damage Magic
fireball = Spell("Fireball", 25, 6, "black", 1)
thunder = Spell("Thunder", 25, 6, "black", 1)
chain_lightning = Spell("Chain Lightning", 25, 6, "black", 2)
blizzard = Spell("Blizzard", 25, 6, "black", 1)
gust = Spell("Gust", 25, 6, "black", 1)
meteor = Spell("Meteor", 40, 12, "black", 2)
quake = Spell("Quake", 14, 14, "black", 2)
no_magic = Spell("", 0, 0, "none", 0)

# Create Healing Magic
cure = Spell("Cure", 25, 6, "white", 1)
cura = Spell("Cura", 32, 15, "white", 2)
drain = Spell("Drain", 12, 12, "white", 1)

# Create Item
potion = Item("Potion", "potion", "Heals 5 HP", 5)
hiPotion = Item("Hi-Potion", "potion", "Heals 10 HP", 10)
superPotion = Item("Super Potion", "potion", "Heals 50 HP", 50)
elixir = Item("Elixir", "elixir", "Restores 5 MP", 5)
megaElixir = Item("MegaElixir", "elixir", "Fully restores MP", 9999)
grenade = Item("Grenade", "attack", "Deals 5 damage", 5)

# Instantiate People
playerSpells = [fireball, cure]
playerItems = [{"item": potion, "quantity": 2}, {"item": elixir, "quantity": 1}, {"item": grenade, "quantity": 1}]
player = Person("Valos:", 3260, 132, 300, 34, playerSpells, playerItems, 10, 1)

# Instantiate Weapons
basic_sword = Sword("Basic Sword", 1, 2, "sword", "Basic sword. Has average strength.")
sharp_sword = Sword("Sharp Sword", 4, 5, "sword", "Sharper sword. Has average strength.")
cutlass = Sword("Cutlass", 5, 7, "sword", "A cutlass. HAs average strength.")
kegs_cutlass = Sword("Keg's Cutlass", 7, 10, "sword", "Keg's unique cutlass.\n This was one of the terror of the seas"
                                                      "when he was alive. \nHas good strength.")
lex_rapier = Sword("Lex's Rapier", 8, 9, "sword", "Lex's prized rapier. How did you get this? Has great attack for a "
                                                  "sword.")

basic_axe = Axe("Basic Axe", 1, 5, 1, "axe", "Basic axe. Lowers defense by 1 but has high attack.")
large_axe = Axe("Large Axe", 4, 8, 1, "axe", "Large axe. Lowers defense by 1 but has high attack.")
great_axe = Axe("Great Axe", 7, 10, 2, "axe", "Great axe. Lowers defense by 1 but has high attack.")

basic_bow = Bow("Basic Bow", 0, 4, "bow", "Basic bow. Has good range of attack but can miss and requires arrows.")
long_bow = Bow("Long Bow", 2, 7, "bow", "Long bow. Has good range of attack but can miss and requires arrows.")

crossbow = Crossbow("Crossbow", 4, 7, "crossbow", "Crossbow. Has good range of attack but can miss and requires bolts.")
crossbolt = Crossbow("Crossbolt", 5, 8, "crossbow", "A better crossbow. Has a good of attack but can miss and requires "
                                                    "bolts.")

basic_staff = Staff("Basic Staff", 0, 2, 1, "staff", "Basic Staff. Increases magic damage but doesn't do much damage")
twisted_staff = Staff("Twisted Staff", 2, 3, 2, "staff", "A twisted wood Staff. Increases magic damage but doesn't do "
                                                         "much damage")

# Instantiate Monsters
skeleton_soldier = Monster("Skeleton Soldier", 10, 1, basic_sword, no_magic, 3)
skeleton_archer = Monster("Skeleton Archer", 12, 0, basic_bow, no_magic, 2)
skeleton_leader = Monster("Skeleton Leader", 15, 1, sharp_sword, no_magic, 8)
skeleton_sniper = Monster("Skeleton Sniper", 14, 1, long_bow, no_magic, 9)
skeleton_captain = Monster("Skeleton Captain", 20, 1, cutlass, no_magic, 18)
captain_keg_beard = Monster("Captain Keg Beard", 20, 1, kegs_cutlass, no_magic, 18)
bandit_pillager = Monster("Bandit Pillager", 11, 0, basic_axe, no_magic, 4)
bandit_archer = Monster("Bandit Archer", 14, 0, basic_bow, no_magic, 5)
bandit_mage = Monster("Bandit Mage", 9, 0, basic_staff, [fireball, thunder, gust], 6)
bandit_leader = Monster("Bandit Leader", 17, 1, large_axe, no_magic, 9)
bandit_sniper = Monster("Bandit Sniper", 16, 1, crossbow, no_magic, 11)
bandit_wizard = Monster("Bandit Wizard", 15, 0, twisted_staff, [fireball, thunder, gust, chain_lightning], 14)
bandit_commander = Monster("Bandit Commander", 23, 1, great_axe, no_magic, 20)
bandit_keith = Monster("Bandit Keith", 23, 2, great_axe, no_magic, 21)
slimy_katria = Monster("Slimy Katria", 22, 1, crossbolt, no_magic, 22)
lex_chance = Monster("Lex Chance", 24, 0, lex_rapier, no_magic, 36)


# Instantiate Monster Rank Lists
skeleton_list_rank_1 = [skeleton_soldier, skeleton_archer]
skeleton_list_rank_2 = [skeleton_leader, skeleton_sniper]
bandit_list_rank_1 = [bandit_archer, bandit_mage, bandit_pillager]
bandit_list_rank_2 = [bandit_leader, bandit_sniper, bandit_wizard]

print("=========================================================================")
print("==================== Welcome to the Kingdom of Tera  ====================")
print("=====  If you would like to view the map check the resources folder =====")
print("==  Anytime you are asked for input you can type 'q' to quit the game! ==")
print("=========================================================================")
time.sleep(5)
print("=========================================================================")
print("\tThe kingdom of Grandia is in trouble so you need to go to each "
      "\nprovidence to save the day. "
      "The different providences you can go to are \n'Oceans Tide', 'Reinstald', "
      "'The Windy Plains', 'The Deadlands', \n'Dead Coast', 'Disputed Territory', "
      "and 'Gaurdia'.")
print("=========================================================================")
time.sleep(10)
game = Game()
game.choose_place()
