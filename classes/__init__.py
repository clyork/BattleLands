from classes.magic import Spell
from classes.inventory import Item
from classes.adventurer import Person
from classes.game import Game
from classes.monster import Monster
from classes.weapon import Weapon
import time

# Create Damage Magic
fireball = Spell("Fireball", 25, 6, "black", 1)
thunder = Spell("Thunder", 25, 6, "black", 1)
chain_lightning = Spell("Chain Lightning", 25, 6, "black", 2)
blizzard = Spell("Blizzard", 25, 6, "black", 1)
gust = Spell("Gust", 25, 6, "black", 1)
meteor = Spell("Meteor", 40, 12, "black", 2)
quake = Spell("Quake", 14, 14, "black", 2)

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
basic_sword = Weapon("Basic Sword", 1, 3, "sword")
sharp_sword = Weapon("Sharp Sword", 3, 6, "sword")
basic_bow = Weapon("Basic Bow", 0, 4, "bow")
long_bow = Weapon("Long Bow", 2, 7, "bow")

# Instantiate Monsters
skeleton_soldier = Monster("Skeleton Soldier", 10, 1, basic_sword, "none", 3)
skeleton_archer = Monster("Skeleton Archer", 12, 0, basic_bow, "none", 2)
skeleton_leader = Monster("Skeleton Leader", 15, 1, sharp_sword, "none", 8)
skeleton_sniper = Monster("Skeleton Sniper", 14, 1, long_bow, "none", 9)

# Instantiate Monster Rank Lists
skeleton_list_rank_1 = [skeleton_soldier, skeleton_archer]
skeleton_list_rank_2 = [skeleton_leader, skeleton_sniper]

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
