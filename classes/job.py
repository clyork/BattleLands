import time
import random

from classes import player
from classes.game import Game


class Job:
    def choose_town_job(self):
        print("=========================================================================")
        print("Which job would you like to perform?\n\t<1> Help the guards clean up town\n\t<2> Gamble in the casino"
              "\n\t<3> Beg for money \n\t<h> Help \n\t<t> Go back to town \n\t<q> Quit ")
        job_choice = input("Input: ")
        if job_choice == "1":
            pass
        elif job_choice == "2":
            Job.gamble(self)
        elif job_choice == "3":
            Job.beg_for_money(self)
        elif job_choice.lower() == "h":
            print("=========================================================================")
            print("\t-Helping the guards involves doing smaller jobs for money.\n\t-Gambling in the casino"
                  " takes a random luck roll and rewards you \n\twell or hurts you\n\t-Begging for money takes a "
                  "random charisma roll and can cause \n\tsome odd effects...")
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

    def help_gaurds(self):
        # if 1 <= player.get_level() <= 3:
        pass

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
            Job.choose_town_job(self)

    def gamble(self):
        print("Welcome to the casino! Would you like to play:\n\t<1> Play the slots \n\t<2> Guess the number"
              "\n\t<h> Help \n\t<q> Quit")
        game_chosen = input("Input: ")
        if game_chosen == "1":
            Job.slots(self)
        elif game_chosen == "2":
            Job.guess_the_number(self)
        elif game_chosen.lower() == "h":
            print("=========================================================================")
            print("Playing the slots allows you bet a certain amount of money and with luck\n\t you will make money."
                  "\n Guess the number is a simple guessing game where you bet money and\n\t and guess a number between"
                  " 1 and 10.")
            print("=========================================================================")
            time.sleep(3)
            Job.gamble(self)
        elif game_chosen.lower() == "q":
            exit()
        else:
            Job.gamble(self)

    def slots(self):
        print("Welcome to slots! How much would you like to bet?")
        bet_amount = input("Input: ")
        spun_numbers = [random.randint[1, 7], random.randint[1, 7], random.randint[1, 7]]
        print("You rolled " + str(spun_numbers.index(0)) + "" + str(spun_numbers.index(1)) + "" +
              str(spun_numbers.index(2)) + ".")
        if spun_numbers.index(0) == spun_numbers.index(1) and spun_numbers.index(0) == spun_numbers.index(2):
            print("You hit the jackpot!!\n You have earned five times your bet amount!!")
            bet_amount *= 5
            player.add_money(bet_amount)
            print("You won " + bet_amount + " coins. You now have " + player.get_money() + " coins!")
            Job.gamble(self)
        elif spun_numbers.index(0) == spun_numbers.index(1) or spun_numbers.index(0) == spun_numbers.index(
                2) or spun_numbers.index(1) == spun_numbers.index(2):
            print("You won!!\n You have earned three times your bet amount!!")
            bet_amount *= 3
            player.add_money(bet_amount)
            print("You won " + bet_amount + " coins. You now have " + player.get_money() + " coins!")
            Job.gamble(self)
        else:
            print("You did not win!!\n You have lost your bet amount!!")
            player.lose_money(bet_amount)
            print("You lost " + bet_amount + " coins. You now have " + player.get_money() + " coins!")
            Job.gamble(self)

    def guess_the_number(self):
        print("Welcome to Guess the Number! It's simple just guess a number between\n 1 and 10 and if your close enough"
              "you can win money!\n It costs 2 coins to play!\n Enter a number between 1 and 10.")
        number_guessed = input("Input: ")
        random_number = random.randint[1, 10]
        player.lose_money(2)
        if number_guessed == random_number:
            print("Congrats you guessed the right number!!!\n You won 12 coins!")
            player.add_money(12)
            print("You currently have " + player.get_money() + " coins!")
            Job.gamble(self)
        elif number_guessed == random_number - 1 or number_guessed == random_number + 1:
            print("You guessed 1 away from the number!\n You won 6 coins!")
            player.add_money(6)
            print("The number was " + random_number + " . You guessed " + number_guessed + ". You currently have "
                  + player.get_money() + " coins!")
            Job.gamble(self)
        elif number_guessed == random_number - 2 or number_guessed == random_number + 2:
            print("You guessed 2 away from the number!\n You got your money back!")
            player.add_money(2)
            print("The number was " + random_number + " . You guessed " + number_guessed + ". You currently have "
                  + player.get_money() + " coins!")
            Job.gamble(self)
        else:
            print("You did not win! Maybe try again ;)\n" + "The number was " + random_number + " . You guessed "
                  + number_guessed + ". You currently have " + player.get_money() + " coins!")
            Job.gamble(self)
