########################## rock paper scissors ##########################
# steps :
# step 1 => define the initial number of tries, win, lose, draw.
# step 2 =? Read the userChoice.
# step 3 => Randomly select computer choice.
# step 4 => Read Tries number left
# step 5 => define conditions : tries >= 6, invalid input, draw scenario, winning scenarios, losing scenarios. 
# step 6 => add tries++ in every scenario. add win, lose, draw for specific cases
# step 7 => repeat the steps until tries hit the max.


import random

tries = 0
win = 0
lose = 0
draw = 0

def rockPaperScissors():
    global tries, win, lose, draw

    userChoice = input("Enter R, P, S: ").upper()
    choicesArray = ["R", "P", "S"]
    computerChoice = random.choice(choicesArray)
    print(computerChoice, " vs ", userChoice)
    print("Tries Left", 6 - tries)

    if tries >= 6:
        print("\n**** Game over  ****")
        print("Wins:", win)
        print("Loses:", lose)
        print("Draws:", draw)
    elif userChoice not in choicesArray:
        print("Invalid Input")
        tries += 1
        print("----------------------------------------------------------------")
        rockPaperScissors()
    elif computerChoice == userChoice:
        print("It's a Draw!!")
        tries += 1
        draw += 1
        print("----------------------------------------------------------------")
        rockPaperScissors()
    elif (
            (computerChoice == "R" and userChoice == "P") or
            (computerChoice == "P" and userChoice == "S") or
            (computerChoice == "S" and userChoice == "R")
    ):
        print("You win!!")
        tries += 1
        win += 1
        print("----------------------------------------------------------------")
        rockPaperScissors()
    else:
        print("You Lose!!")
        tries += 1
        lose += 1
        print("----------------------------------------------------------------")
        rockPaperScissors()

rockPaperScissors()
