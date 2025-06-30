# This is the main file of hangman Game File
import random
from hang_db import logo,stages,word_list

# This Line print Logo of the Game
print(logo)

chosen_word = random.choice(word_list)

lives = 7
display = []
word_length = len(chosen_word)
test = []

# making blanks
for a in range(word_length):
    if random.randint(2,3) != 3:
        display += "_"
    else:
        display += chosen_word[a]

# take input by user
end_of_game = False
while not end_of_game:
    print(f"{''.join(display)}")
    print(stages[lives])
    guess = input("Guessed a letter :- ").lower()
    if guess in test:
        print(f"You've already guessed '{guess}'.")
    a = 0
    for position in range(word_length):
        if guess == chosen_word[position]:
            if  display[position] == "_":
                display[position] = chosen_word[position]
                if a<=0:
                    print("\n"*100)
                    print(f"\nYou choose correct word '{guess}'.\n")
                    a = 1
            if display[position] != "_" and guess == chosen_word[position] and a <= 0:
                print("\n"*100)
                print(f"You guessed '{guess}', You lose a life, because it doesn't fill in any blanks.\n")
                lives -= 1
                a = 1
                if lives == 0:
                    end_of_game = True
                    print("\n"*100)
                    print("\n--------------------------------------------You  lose.--------------------------------------------")
                    print(f"The word is = {chosen_word}")
    if guess not in chosen_word:
        print("\n"*100)
        print(f"You guessed '{guess}', that's not in the word. You loose a life.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\n"*100)
            print(stages[lives])
            print("\n-------------------------------------------- You Loose.--------------------------------------------")
            print(f"The word is = {chosen_word}")
    if "_" not in display:
        end_of_game = True
        print("\n"*100)
        print("\n--------------------------------------------You Win.--------------------------------------------")
    test += guess