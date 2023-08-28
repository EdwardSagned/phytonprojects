import random
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
print(chosen_word)
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#print(word_completed())
display=[]
lives=6
word_completed=False

for _ in range(len(chosen_word)):
    display.append("_")
print(display)

while word_completed==False:
    guess=input("What is your guess?").lower()
    for pos in range(len(chosen_word)):
        char=chosen_word[pos]
        if guess==char:
            display[pos]=char
    print(display)

    if guess not in chosen_word:
        lives-=1
        #print(stages[lives+1])
        #print(lives)
        if lives==0:
            print("You lose")
            exit()      
    if "_" in display:
        word_completed=False
    else:
        print("You Win!")
        word_completed=True
    print(stages[lives])


# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

