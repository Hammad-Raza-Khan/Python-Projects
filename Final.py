import random

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

end_of_game = False

import f
choosen_word = random.choice(f.word_list)
length_of_word = range(len(choosen_word))
print(choosen_word)
print("\n")
 
lives = 6
 
from f import logo 
print(logo)


#Creating blanks
display = []
for _ in length_of_word:
    display += '_'


#LOOP
while not end_of_game:
    
    guess = input("Guess a letter to save THE HANGMAN ! \n =>").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in length_of_word:
        letter = choosen_word[position]
        if letter == guess: 
            display[position] = letter
            
    if guess not in choosen_word:
        print(f"You guessed {guess}, that is not in the word. Hence, you lose a limb !")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose! Hangman shall be Hanged !")

    print(f"{" ".join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You Win !")

    print(stages[lives])