# Step 5
import random
import hangman_words
import hangman_art

# T0D0-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
guessed_words = []
word_length = len(chosen_word)
end_of_game = False
lives = 6
stages = hangman_art.stages
# T0D0-3: - Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(logo)

while not end_of_game:
    guess = input("What is your guess?\n").lower()

    # T0D0-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_words:
        print("You already guessed '" + guess + "'!")
    else:

        # T0Dß-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #Check if user is wrong.
        if guess not in chosen_word:
            print("'" + guess + "' is not in the word!")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose")

        # Check guessed letter
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if '_' not in display:
            end_of_game = True
            print("Congratulations, you won!")

        # T0D0-2: - Import the stages from hangman_art.py and make this error go away.
        print(stages[lives])
