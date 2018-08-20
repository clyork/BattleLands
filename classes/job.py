import time
import random

from classes import player
from classes.game import Game


class Job:
    def choose_town_job(self):
        print("=========================================================================")
        print("Which job would you like to perform?\n\t<1> Odd jobs for the lazy citizens"
              "\n\t<2> Help the guards clean up town\n\t<3> Gamble in the casino\n\t<4> Beg for money"
              "\n\t<h> Help \n\t<t> Go back to town \n\t<q> Quit ")
        job_choice = input("Input: ")
        if job_choice == "1":
            pass
        elif job_choice == "2":
            pass
        elif job_choice == "3":
            pass
        elif job_choice == "4":
            Job.beg_for_money(self)
        elif job_choice.lower() == "h":
            print("=========================================================================")
            print("\t-Odd jobs involves no luck or skill but gets you little money.\n\t-Helping the guards involves "
                  "doing smaller jobs for money.\n\t-Gambling in the casino takes a random luck roll and rewards you "
                  "\n\twell or hurts you\n\t-Begging for money takes a random charisma roll and can cause "
                  "\n\tsome odd effects...")
            print("=========================================================================")
            time.sleep(3)
            Job.choose_town_job(self)
        elif job_choice.lower() == "t":
            game = Game()
            game.town_actions()
        elif job_choice.lower() == "q":
            exit()
        else:
            Job.choose_town_job(self)

    def beg_for_money(self):
        rand_int = random.randint(1, 10)
        if rand_int == 1:
            print("Your begging attempts were an absolute failure. So much of a failure that\n people beat you up.")
            rand_damage = random.randint(1, 10)
            player.take_damage(rand_damage)
            print(player.get_name() + " took" + rand_damage + " damage!!!")
            Job.choose_town_job(self)
        elif rand_int == 2 or rand_int == 3:
            print("Your begging attempts were not a total failure. Some people took mercy on you\n (But not much).")
            rand_coin = random.randint(1, 3)
            player.add_money(rand_coin)
            print(player.get_name() + " got" + rand_coin + " coins! You now have " + player.get_money() + " coins.")
            Job.choose_town_job(self)
        elif 4 <= rand_int < 8:
            print("You actually managed to make some people give up their hard earned cash. \nGo you!")
            rand_coin = random.randint(3, 8)
            player.add_money(rand_coin)
            print(player.get_name() + " got" + rand_coin + " coins! You now have " + player.get_money() + " coins.")
            Job.choose_town_job(self)
        elif rand_int == 8 or rand_int == 9:
            print("Your begging skills were down right impressive this time. \nCongrats you got some coin!")
            rand_coin = random.randint(8, 10)
            player.add_money(rand_coin)
            print(player.get_name() + " got" + rand_coin + " coins! You now have " + player.get_money() + " coins.")
            Job.choose_town_job(self)
        elif rand_int == 10:
            print("Wow your begging skills were amazing! And with skills like those no one\n believed you needed"
                  " money :P")
            print(player.get_name() + " got no coins hehehe")
            Job.choose_town_job()

    def gamble(self):
        print("Welcome to the casino! Would you like to play:\n\t<1> Play the slots \n\t<2> Guess the number"
              "\n\t<3> Dice Game \n\t<h> Help \n\t<q> Quit")
        game_chosen = input("Input: ")
        if game_chosen == "1":
            pass
        elif game_chosen == "2":
            pass
        elif game_chosen == "3":
            pass
        elif game_chosen.lower() == "h":
            pass
        elif game_chosen.lower() == "q":
            exit()
        else:
            Job.gamble()
