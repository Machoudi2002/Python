######################################### Password Generator #################################
# steps :
# step 1 => defining the types of character that we gonna work with.
# step 2 =? defining the choices.
# step 3 => Randomly select computer choice.
# step 4 => every choice has a character type and input.
# step 5 => loop over all choices and checking if input of choice equal "Y" == true.
# step 6 => if choice equal == "Y" add the char of the choice to the defualt LowerCase Alphabets String. 
# step 7 => add atleast one item from every choice char.
# step 8 => using the string made by choices complete the length with random char from the string.
# step 9 => shuffle the string for more randomize.
# step 10 => print the password.
import random


def passGenerator(length):
    password = ""
    choiceSTR = ""
    ALPHABETS = "abcdefghigklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    SYMBOLS = "~!#$%&'()*+,-./^{}[><|?]ª·¨Ñ;_¿:"

    isUpper = {
        "Char": ALPHABETS.upper(),
        "Input": input("Include Uppercase Characters (Y/N): ").upper()
    }
    isNumber = {
        "Char": NUMBERS,
        "Input": input("Include Numbers (Y/N): ").upper()
    }
    isSymbol = {
        "Char": SYMBOLS,
        "Input": input("Include Symbols (Y/N): ").upper()
    }

    charTypes = [isUpper, isNumber, isSymbol]

    trueChoiceCount = 0
    for charType in charTypes:
        if charType["Input"] == "Y":
            ALPHABETS += charType["Char"]
            password += random.choice(charType["Char"])
            trueChoiceCount += 1

    rangeValue = length - trueChoiceCount
    for i in range(rangeValue):
       password += random.choice(ALPHABETS)

    passArr = list(password.replace(" ", ""))
    random.shuffle(passArr)
    passString = "".join(passArr)
    print(f"\nYour {len(passString)} Char Password :" + passString + "\n")
