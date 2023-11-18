text = str(input("Enter Text : "))

def charCounter(input : str):
  noSpaceString = input.replace(" ", "")
  CharCount = len(noSpaceString)
  wordCount = len(input.split())
  print("You have ", wordCount, " Words")
  print("You have ", CharCount, " Characters with no whitespaces")
  print("You have ", len(input), " Characters including whitespaces")

charCounter(text)
