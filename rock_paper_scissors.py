import random

print("Welcome to my little rock/paper/scissors game!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
print(choices[player_choice])

com_choice = random.randint(0, 2)
print("Computer chose:")
print(choices[com_choice])

#making use of the fact that 'choices' has it's Elements ordered in a way that Element x beats Elements x - 1.
if choices[player_choice] == choices[(com_choice + 1) % 3]:
    print("You lose")
elif player_choice == com_choice:
    print("You tie")
else:
    print("You win")