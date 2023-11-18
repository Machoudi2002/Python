########################## rock paper scissors ##########################
# steps :
# step 1 => define the initial number of tries, win, lose, draw.
# step 2 =? Read the userChoice.
# step 3 => Randomly select computer choice.
# step 4 => create a loop that keep looping until it hit the number of max tries.
# step 5 => check Tries number left.
# step 6 => define conditions : invalid input, draw scenario, winning scenarios, losing scenarios. 
# step 7 => add win +1, lose +1, draw +1 for specific cases.
# step 8 => add tries + 1 upon every loop.
# step 9 => repeat the steps until tries hit the max.
# step 10 => when the looping stops. give the user the final score.

import random

MAX_TRIES = 6
win = 0
lose = 0
draw = 0

def rockPaperScissors():
    global tries, win, lose, draw
    tries = 0

    while tries < MAX_TRIES:
        userChoice = input("Enter R, P, S: ").upper()
        choicesArray = ["R", "P", "S"]
        computerChoice = random.choice(choicesArray)

        print(computerChoice, " vs ", userChoice)
        print((MAX_TRIES - 1) - tries , "Tries Left")

        if userChoice not in choicesArray:
            print("Invalid Input")

        elif computerChoice == userChoice:
            print("It's a Draw!!")
            draw += 1

        elif (
                (computerChoice == "R" and userChoice == "P") or
                (computerChoice == "P" and userChoice == "S") or
                (computerChoice == "S" and userChoice == "R")
        ):
            print("You win!!")
            win += 1

        else:
            print("You Lose!!")
            lose += 1
    
        print("----------------------------------------------------------------")
        tries += 1
    
    print("\n------------ Game over -------------")
    print("Wins:", win)
    print("Loses:", lose)
    print("Draws:", draw)
    print("\n")
    
rockPaperScissors()
