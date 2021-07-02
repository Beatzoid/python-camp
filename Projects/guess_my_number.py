# guess_my_number.py
# By Beatzoid
# 6/29/21

import random
import os

playAgain = "y"
computerScore = 0
playerScore = 0

def play(againstComputer):
		global playAgain
		global computerScore
		global playerScore

		if againstComputer:
			os.system("clear") # Clear the screen
			print("\tWelcome to Guess My Number!")
			print("\nI'm thinking of a number between 1 and 100.")
			print("You have ten tries. Everytime you guess a number, I guess one too\nGood luck.\n")

			# set the initial values
			number = random.randint(1, 100)
			computerGuess = random.randint(1, 100)

			# Get a valid guess
			guess = input("Take a guess: ")
			while not guess.isdigit():
				guess = input("Invalid input, take another guess: ")

			tries = 1
			computerTries = 1

			# guessing loop
			while int(guess) != number and tries != 10 and computerTries != 10 and computerGuess != number:
				# Make the computer guess
				computerGuess = random.randint(1, 100)
				computerTries += 1

				# Give the user clues
				if int(guess) > number:
					print("Lower...")
				else:
					print("Higher...")
				
				# Get a valid guess
				guess = input("Take a guess: ")
				while not guess.isdigit():
					guess = input("Invalid input, take another guess: ")

				tries += 1

			# If the computer guessed the number
			if computerGuess == number:
				print("The computer guessed it before you, bummer!")
				computerScore += 1
			# if the user ran out of tries
			elif tries >= 10:
				print("You ran out of tries. The number was", number)
				computerScore += 1
			# If both the player and the computer ran out of tries
			elif tries >= 10 and computerTries >= 10:
				print("It was a tie, the number was ", number)
			# If the user guessed the number
			elif int(guess) == number:
				print("You guessed it! The number was", number)
				print("And it only took you", tries, "tries!\n")
				playerScore += 1

			playAgain = input("Would you like to play again? (y/n) ").lower()

		else:
			os.system("clear") # Clear the screen
			print("\tWelcome to Guess My Number!")
			print("\nI'm thinking of a number between 1 and 100.")
			print("You have ten tries. Good luck.\n")

			# set the initial values
			number = random.randint(1, 100)

			# Get a valid guess
			guess = input("Take a guess: ")
			while not guess.isdigit():
				guess = input("Invalid input, take another guess: ")

			tries = 1

			# guessing loop
			while int(guess) != number and tries != 10:

				# Give the user clues
				if int(guess) > number:
					print("Lower...")
				else:
					print("Higher...")
				
				# Get a valid guess
				guess = input("Take a guess: ")
				while not guess.isdigit():
					guess = input("Invalid input, take another guess: ")

				tries += 1

			# if the user ran out of tries
			if tries >= 10:
				print("You ran out of tries. The number was", number)
				computerScore += 1
			# if the user guessed the number
			elif int(guess) == number:
				print("You guessed it! The number was", number)
				print("And it only took you", tries, "tries!\n")
				playerScore += 1

			playAgain = input("Would you like to play again? (y/n) ").lower()

def computeStats():
	# Print out the stats
	print("\n\tFinal Stats:")
	print("Computer: ", computerScore)
	print("Player: ", playerScore)

	if playerScore > computerScore:
		print("Congrats, you beat the computer!")
	elif computerScore > playerScore:
		print("Bummer, the computer beat you, better luck next time!")
	else:
		print("It was a tie!")

while playAgain.lower() == "y":
	os.system("clear") # Clear the screen

	playAgainstComputerInput = input("Would you like to play against the computer?\nThis means that every time you guess a number, the computer also guesses one. (y/n) ")

	playAgainstComputer = playAgainstComputerInput.lower() == "y"

	play(playAgainstComputer)

computeStats()
