###################### character words counter ###########################

def charCounter():
  text = str(input("Enter Text : "))
  noSpaceString = text.replace(" ", "")
  CharCount = len(noSpaceString)
  wordCount = len(text.split())
  print("You have ", wordCount, " Words")
  print("You have ", CharCount, " Characters with no whitespaces")
  print("You have ", len(text), " Characters including whitespaces")

charCounter()
