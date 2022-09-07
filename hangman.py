# Step 3
import random

word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
# display = []
# for element in range(len(chosen_word)):
#     display.append('_')
display = ["_" for x in chosen_word]

# T0D0-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while '_' in display:

    guess = input("What is your guess?\n").lower()

    # Check guessed letter
    # for index in range(len(chosen_word)):
    #     if chosen_word[index] == guess:
    #         display[index] = guess

    display = [guess if character == guess else display[index] for index, character in enumerate(chosen_word)]

    print(display)
else:
    print("Congratulations, you have won!")