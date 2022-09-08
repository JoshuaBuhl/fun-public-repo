# Step 5
import random
# T0D0-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
# T0D0-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages

chosen_word = random.choice(word_list)

end_of_game = False
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ["_" for x in chosen_word]

print(logo)

while not end_of_game:
    guess = input("What is your guess?\n").lower()

    # T0D0-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")

    # T0D0-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word, you have lost one life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # Check guessed letter
    display = [guess if character == guess else display[index] for index, character in enumerate(chosen_word)]

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # T0D0-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
