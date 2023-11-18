###################### character words counter ###########################
# steps :
# step 1 => Read The Input.
# step 2 => Remove the whitespace.
# step 3 => Count character using length of string with no spaces.
# step 4 => Turn the string into array of words using .split().
# step 5 => Count the words using length of array of words.
# step 6 => Count characters with the whitspaces directly using length of string.

def charCounter():
  text = str(input("Enter Text : "))
  noSpaceString = text.replace(" ", "")
  CharCount = len(noSpaceString)
  wordCount = len(text.split())
  print("You have ", wordCount, " Words")
  print("You have ", CharCount, " Characters with no whitespaces")
  print("You have ", len(text), " Characters including whitespaces")

charCounter()
