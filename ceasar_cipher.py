# T0D0-1: Import and print the logo from art.py when the program starts.
from art import logo
# T0D0-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
def caesar(input_text, shift_amount, mode):
    # if mode == 'encode':
    #     code_shift = shift_amount
    # elif mode == 'decode':
    #     code_shift = 26 - shift_amount
    # output_text = [alphabet[(alphabet.index(letter) + code_shift) % 26] if letter in alphabet else letter for letter in input_text]
    output_text = [letter if letter not in alphabet else (alphabet[(alphabet.index(letter) + shift_amount) % 26] if mode == 'encode' else alphabet[(alphabet.index(letter) - (shift_amount%26))]) for letter in input_text]
    print("The " + mode + "d text is " + "".join(output_text))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
user_interested = True
print(logo)


# T0D0-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
while user_interested:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # T0D0-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    caesar(text, shift, direction)

    if input("\nDo you want to keep de/encrypting?\nEnter 'yes'/'no'.\n").lower() != 'yes':
        user_interested = False
