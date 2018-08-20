from classes.job import Job
import time


class Game:
    def choose_place(self):
        print("Enter the number of the place where you would like to go below\n" 
              "\t<1> Oceans Tide\n \t<2> Reinstald\n \t<3> The Windy Plains\n" 
              "\t<4> The Deadlands\n \t<5> Dead Coast\n \t<6> Disputed Territory\n" 
              "\t<7> Gaurdia\n \t<q> Quit")
        area_chosen = input("Input: ")

        if area_chosen == "1":
            print("=========================================================================")
            print("\tOceans Tide is a neutral area in regards to the ongoing war between \nReinstald and Gaurdia." 
                  " That being said a lot of refugees from both sides \nhave moved to the coast here to create their" 
                  " own neutral ports with \nwhich to trade with the other continents. That being said there are a " 
                  "\nlot of not so good people in the area. You will start in the harbor \ntown of Tiding.")
            print("=========================================================================")
            time.sleep(3)
            Game.town_actions(self)
        elif area_chosen == "2":
            print("here 1")
        elif area_chosen == "3":
            print("here 1")
        elif area_chosen == "4":
            print("here 1")
        elif area_chosen == "5":
            print("here 1")
        elif area_chosen == "6":
            print("here 1")
        elif area_chosen == "7":
            print("here 1")
        elif area_chosen == "q":
            exit()
        else:
            print("Bad Input. Try again or type 'q' to exit the game.")
            Game.choose_place(self)

    def town_actions(self):
        time.sleep(6)
        print("=========================================================================")
        print("You have arrived in town. Would you like to: "
              "\n\t<1> Visit the shop \n\t<2> Battle \n\t<3> Explore the town \n\t<4> Perform "
              "odd jobs \n\t<q> Quit")
        action_chosen = input("Input: ")
        if action_chosen == "1":
            pass
        elif action_chosen == "2":
            pass
        elif action_chosen == "3":
            pass
        elif action_chosen == "4":
            job = Job()
            job.choose_town_job()
        elif action_chosen.lower() == "q":
            exit()
        else:
            Game.town_actions(self)
