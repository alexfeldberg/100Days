import os
from random import randint
from art import logo

EASY_LIVES = 10
HARD_LIVES = 5

def set_difficulty(diff):
	if diff == 'easy':
		return EASY_LIVES
	else:
		return HARD_LIVES


def num_guess():

	print(logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

	num = randint(1, 100)
	lives = set_difficulty(difficulty)


	while lives > 0:
		print(f"You have {lives} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))

		if guess == num:
			print("That's correct, you win!!")
			break
		elif guess < num:
			print("Too low.")
			lives -= 1
		else:
			print("Too high.")
			lives -= 1

		if lives > 0:
			print("Guess again.")
		elif lives == 0:
			print("You've run out of guesses!")

	again = input("Would you like to play again? Please type 'y' or 'n': ")
	if again == 'y':
		os.system('clear')
		num_guess()
	else:
		print("Thanks for playing!")
		return

num_guess()