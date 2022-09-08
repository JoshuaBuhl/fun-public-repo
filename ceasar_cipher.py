alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = [alphabet[(alphabet.index(letter)+shift_amount) % 26] for letter in plain_text]
    print("The encoded text is " + "".join(cipher_text))

# T0D0-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    # T0D0-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    # e.g.
    # cipher_text = "mjqqt"
    # shift = 5
    # plain_text = "hello"
    # print output: "The decoded text is hello"
    plain_text = [alphabet[(alphabet.index(letter)+(26 - shift_amount)) % 26] for letter in cipher_text]
    print("The decoded text is " + "".join(plain_text))

# T0D0-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
