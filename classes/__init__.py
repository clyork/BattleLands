import random
from classes.magic import Spell
from classes.inventory import Item
from classes.adventurer import Person
from classes.game import Game

#Create Damage Magic
fireball = Spell("Fireball", 25, 6, "black", 1)
thunder = Spell("Thunder", 25, 6, "black", 1)
chain_lightning = Spell("Chain Lightning", 25, 6, "black", 2)
blizzard = Spell("Blizzard", 25, 6, "black", 1)
gust = Spell("Gust", 25, 6, "black", 1)
meteor = Spell("Meteor", 40, 12, "black", 2)
quake = Spell("Quake", 14, 14, "black", 2)

#Create Healing Magic
cure = Spell("Cure", 25, 6, "white", 1)
cura = Spell("Cura", 32, 15, "white", 2)
drain = Spell("Drain", 12, 12, "white", 1)

#Create Item
potion = Item("Potion", "potion", "Heals 5 HP",  5)
hiPotion = Item("Hi-Potion", "potion", "Heals 10 HP",  10)
superPotion = Item("Super Potion", "potion", "Heals 50 HP", 50)
elixir = Item("Elixir", "elixir", "Restores 5 MP", 5)
megaElixir = Item("MegaElixir", "elixir", "Fully restores MP", 9999)
grenade = Item("Grenade", "attack", "Deals 5 damage", 5)

#Instantiate People
playerSpells = [fireball, cure]
playerItems = [{"item": potion, "quantity": 2}, {"item": elixir, "quantity": 1}, {"item": grenade, "quantity": 1}]
player = Person("Valos:", 3260, 132, 300 , 34, playerSpells, playerItems, 1)


print("=========================================================================")
print("==================== Welcome to the Kingdom of Tera  ====================")
print("=====  If you would like to view the map check the resources folder =====")
print("= Anytime you are asked for input you can type 'quit' to quit the game! =")
print("=========================================================================")

print("=========================================================================")
print("\tThe kingdom of Grandia is in trouble so you need to go to each providence \n" +
          "The different providences you can go to are 'Oceans Tide', 'Reinstald', \n" +
          "The Windy Plains', 'The Deadlands', 'Dead Coast', 'Disputed Territory', \n" +
          "and 'Gaurdia'.")
print("=========================================================================")
game = Game()
game.choose_place()
        
    