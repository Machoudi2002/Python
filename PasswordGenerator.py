######################################### Password Generator #################################
import random


def passGenerator(length):
    password = ""
    trueOrFalse = ["Y", "N"]
    ALPHABETS = "abcdefghigklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    SYMBOLS = "~!#$%&'()*+,-./^{}[><|?]ª·¨Ñ;_¿:"

    isLower = {
        "Char": ALPHABETS,
        "Input": input("Include Lowercase Characters (Y/N): ").upper()
    }
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

    charTypes = [isLower, isUpper, isNumber, isSymbol]

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
    print("\nYour Password : " + passString)
