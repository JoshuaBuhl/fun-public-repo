#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

available_chars = []
for number in [nr_letters, nr_numbers, nr_symbols]:
    if number > 0:
        available_chars.append(number)

password = ""

for character in range(nr_letters):
    which_kind = random.randrange(len(available_chars))
    if which_kind == 0:
        password += random.choice(letters)
    elif which_kind == 1:
        password += random.choice(numbers)
    else:
        password += random.choice(symbols)
    available_chars[which_kind] -= 1
    if available_chars[which_kind] == 0:
        available_chars.remove(0)

print(password)
