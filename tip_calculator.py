#tip calculator
#this tool help you and your friends to easily tip a specific amount and split the bill evenly
#even if the wine menu got the better of you
print("Welcome to my tip calculator!")
original_bill = float(input("What was the total bill?\n$ "))
tip_percentage = int(input("What percentage would you like to tip?\n% "))
number_of_friends = int(input("How many people will split the bill?\n\U0001F91D "))
final_split = round(original_bill*(tip_percentage/100+1)/number_of_friends, 2)
print("Each person should pay: $ " + "{:.2f}".format(final_split))