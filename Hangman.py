####
### Hangman Game


import sys
## start variables
blanks = []
guess = ""
wrongGuesses = []

## word input
word = input('''Welcome to Hangman!
What word would you like to use: ''')
print("\nYou have 5 guesses\nGuess only letters, unless you know the full word") 

## making the blanks for the word
for ch in word:
  blanks.append("_")

## hangman emoticons

hm1 = ('''
   ____
   /    |
  |    \O/
  |     |
  |    / \\
''')
hm2 = ('''
    ____
   /    |
  |    \O
  |     |
  |    / \\
''')
hm3 = ('''
    ____
   /    |
  |     O
  |     |
  |    / \\
''')
hm4 = ('''
    ____
   /    |
  |     O
  |     |
  |    / 
''')
hm5 = ('''
    ____
   /    |
  |     O
  |     |
  |      
''')
hm6 = ('''
    ____
   /    |
  |     
  |     
  |      
''')

## making words into lists
def split(word):
  return list(word)

## turning strings back into lists
def listToString(s): 
  str1 = "" 
  for ele in s: 
        str1 += ele    
  return str1 

## displaying hung men
def hmCount(count):
  if count == 0:
    return hm6
  elif count == 1:
    return hm5
  elif count == 2:
    return hm4
  elif count == 3:
    return hm3
  elif count == 4:
    return hm2
  else:
    return "fail"

## using functions/ making variables for while loop
chs = split(word)
final = blanks.copy()
incCount = 0
dmg = False
firstTry = False

## main line
while True:
  # if word is fully guessed
  if guess == word:
    firstTry = True
    break
  # condition for a wrong guess
  if dmg == True:
    wrongGuesses.append(guess)
    incCount+=1
    print("\nWrong!")
  dmg = True

  # displaying correct hung man
  re = (hmCount(incCount))
  # condition for if player fails
  if re != "fail":
    print(re)
  else:
    print(hm1)
    print("\nYour man died :(")
    print(f"The Word was {word.lower}")
    sys.exit()
  # condition for if all letters are guessed
  if listToString(final) == word:
    break
  # variable for for loop
  i = 0
  # printing letters guessed with _'s
  print(listToString(final))
  # displays wrong guesses
  print("                             Wrong Guesses: ["+ ', '.join(wrongGuesses)+"]")
  # guess input
  guess = input("Guess: ")
  # damage control
  if guess == "":
    fakeInput = input("\nThat is not a valid input, press ENTER to continue")
    dmg = False
    continue
  ## main function for replacing letters
  for ch in word:
    if guess.lower() == ch.lower():
      del final[i]
      final.insert(i, ch)
      i+=1
      dmg = False
    else:
      i+=1
  # displays correctly guessed letter
  if dmg == False:
    print(f'\nYou got the letter "{guess}"')
## condition for if word was fully guessed
if firstTry == True:
  print(word)
else:
  print(listToString(final))
## win screen
print("\nYou Win!")

### Completed in about 2 hours
### Not many errors or mess ups
### Take Aways:
### import sys, sys.exit(), del function, .insert(), .join(), return function
####