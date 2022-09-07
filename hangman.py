import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#T0D0-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#T0D0-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("What is your guess?\n").lower()

#T0D0-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for character in chosen_word:
#     if character == guess:
#         print("Right")
#     else:
#         print("Wrong")
guess_match_list = [character == guess for _, character in enumerate(chosen_word)]
print(["Right" if element else "Wrong" for element in guess_match_list])
