# dice_game.py
# By Beatzoid
# 6/28/2021

import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

rerolled = False

if die1 <= 3:
	reroll1 = input("Would you like to reroll dice #1 (yes/no, I recommend yes)? ")
else:
	reroll1 = input("Would you like to reroll dice #1 (yes/no)? ")

if reroll1.lower() == "y" or reroll1.lower() == "yes":
	die1 = random.randint(1, 6)
	rerolled = True
	print("Dice #1 rerolled to " + str(die1))

if die2 <= 3:
	reroll2 = input("Would you like to reroll dice #2 (yes/no, I recommend yes)? ")
else:
	reroll2 = input("Would you like to reroll dice #2 (yes/no)? ")

if reroll2.lower() == "y" or reroll2.lower() == "yes":
	die2 = random.randint(1, 6)
	rerolled = True
	print("Dice #2 rerolled to " + str(die2))

if rerolled:
	total = die1 + die2
	print("The final total is " + str(total))
