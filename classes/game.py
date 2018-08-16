'''
Created on Aug 5, 2018

@author: Cody York
'''


class Game:
    def choose_place(self):
        area_chosen = input("Enter the number where you would like to go below\n" +
                            "<1> Oceans Tide\n <2> Reinstald\n <3> The Windy PLains\n" +
                            "<4> The Deadlands\n <5> Dead Coast\n <6> Disputed Territory\n" +
                            "<7> Gaurdia")

        if area_chosen == "1":
            print("=========================================================================")
            print("Oceans Tide is a neutral area in regards to the ongoing war between Reinstald and Gaurdia." +
                  "\nThat being said a lot of refugees from both sides have moved to the coast here to create their" +
                  "\nown neutral ports with which to trade with the other continents. That being said there are a lot" +
                  "\nof not so good people in the area.")
            print("=========================================================================")

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
        elif area_chosen == "quit":
            exit()
        else:
            print("Bad Input. Try again or type 'quit' to exit the game.")
            Game.choose_place()

    def town_actions(self):
        print("=========================================================================")
        action_chosen = input("Would you like to: \nVisit the shop <1> \nBattle <2> \nExplore the town <3> \nPerform"
                              +"odd jobs <4>\n")
        if action_chosen == "1":
            pass
        elif action_chosen == "2":
            pass
        elif action_chosen == "3":
            pass
        elif action_chosen == "4":
            pass
        elif action_chosen.lower() == "quit":
            exit()
        else:
            town_actions()

