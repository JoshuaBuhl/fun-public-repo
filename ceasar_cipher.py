from art import logo
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


while user_interested:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    if input("\nDo you want to keep de/encrypting?\nEnter 'yes'/'no'.\n").lower() != 'yes':
        user_interested = False
