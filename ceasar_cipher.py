alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# T0D0-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(input_text, shift_amount, mode):
    # if mode == 'encode':
    #     code_shift = shift_amount
    # elif mode == 'decode':
    #     code_shift = 26 - shift_amount
    # cipher_text = [alphabet[(alphabet.index(letter) + code_shift) % 26] for letter in input_text]
    cipher_text = [alphabet[(alphabet.index(letter) + shift_amount) % 26] if mode == 'encode' else alphabet[(alphabet.index(letter) - shift_amount)] for letter in input_text]
    print("The " + mode + "d text is " + "".join(cipher_text))


# T0D0-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
