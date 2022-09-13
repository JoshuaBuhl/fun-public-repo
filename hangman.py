# Step 5
import random
from hangman_words import word_list
from hangman_art import logo, stages
import os

chosen_word = random.choice(word_list)

end_of_game = False
lives = 6
already_guessed = [/0001F496]

# Create blanks
display = ["_" for x in chosen_word]
os.system('cls')
print(logo)

while not end_of_game:
    guess = input("What is your guess?\n").lower()
    os.system('cls')

    if guess in already_guessed:
        print(f"You have already guessed {guess}")
    else:
        already_guessed.append(guess)
        # Check if user is wrong.
        if guess not in chosen_word:
            print(f"{guess} is not in the word, you have lost one life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose")
                print(f"The word was {chosen_word}.")

        # Check guessed letter
        display = [guess if character == guess else display[index] for index, character in enumerate(chosen_word)]

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

    print(stages[lives])
    print(f"Guessed letters: {already_guessed}\n")
