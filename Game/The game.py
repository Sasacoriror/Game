import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

choices = ["rock", "paper", "scissors"]

#Keeps count of wins, loses, ties and rounds
computer_wins = 0
player_wins = 0
ties = 0
counter = 0
counter2 = 0
#The history of users choiches
user_history = []

#This one is used to print the stast every 5 rounds
def stats(computer, player, ties):

    y = np.array([computer, player, ties])

    plt.pie(y, labels=[f"Compuer{computer_wins}", f"Human{player_wins}", f"Ties{ties}"], autopct='%1.1f%%')
    plt.show()



while True:

    print("Choose rock, paper, scissors, or end")

    #User writes down their choice and it gets printet out
    user_choice = input("Choice: ")
    print("User choice ",user_choice)
    #Computer chooses one at random
    computer_choice = random.choice(choices)

    #When counter reaches 10 it goes back down to 0, since the first 3 are random and the next 7 are
    #based on the user history, so that we can get a mix of difficulty
    if counter == 10:
        counter=0

    #Print out the stats every 5 rounds
    if counter2 == 5:
        stats(computer_wins, player_wins, ties)
        counter2 = 0

    #Checks if the user wrote one og the available choices
    if user_choice not in choices and user_choice != "end":
        print(user_choice, "Spelled wrong. Try again")
    #If you write end as your choice computer won't choose an option, and collects user history
    elif user_choice != "end":
        print("Computer chose:", computer_choice)
        user_history.append(user_choice)
        counter2 += 1

        #If it is a both user and computer pick the same print tie and count it as a tie and stats
        if user_choice == computer_choice:
            ties += 1
            counter += 1
            print("Computer wins:", computer_wins, "Player wins:", player_wins, "Ties:", ties)
            print("Tie")
            print("")

        #First 3 rounds are random after that it will begin choosing based on your previous chioces
        elif counter > 3:
            most_popular_choice = max(set(user_history), key=user_history.count)
            computer_choice = {
                "rock": "paper",
                "paper": "scissors",
                "scissors": "rock",
            }[most_popular_choice]

            #Shows what choice beets the other choice
            if (
                (user_choice == "rock" and computer_choice == "scissors")
                or (user_choice == "paper" and computer_choice == "rock")
                or (user_choice == "scissors" and computer_choice == "paper")
                ):
                player_wins += 1
                counter += 1
                print("Computer wins:", computer_wins, "Player wins:", player_wins, "Ties:", ties)
                print("Player win")
                print("")

            else:
                computer_wins += 1
                counter += 1
                print("Computer wins:", computer_wins, "Player wins:", player_wins, "Ties:", ties)
                print("Computer win")
                print("")

        #While we are still under 3 rounds
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
            ):
            player_wins += 1
            counter += 1
            print("Computer wins:", computer_wins, "Player wins:", player_wins, "Ties:", ties)
            print("Player win")
            print("")

        else:
            computer_wins += 1
            counter += 1
            print("Computer wins:", computer_wins, "Player wins:", player_wins, "Ties:", ties)
            print("Computer win")
            print("")

    #end choice ends the loop and prints out the final stats
    elif user_choice == "end":

        y = np.array([computer_wins, player_wins, ties])

        plt.pie(y, labels=[f"Compuer{computer_wins}", f"Human{player_wins}", f"Ties{ties}"], autopct='%1.1f%%')
        plt.show()
        exit()