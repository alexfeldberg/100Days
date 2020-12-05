from art import logo, vs
from game_data import data
import random, os

def get_person():
	return random.choice(data)

def compare(person1, person2):

	if person1['follower_count'] > person2['follower_count']:
		return 'A'
	else:
		return 'B'

def higher_or_lower():

	score = 0
	wrong = False

	celeb1 = get_person()
	celeb2 = get_person()

	while not wrong:
		celeb1 = celeb2
		celeb2 = get_person()
		if celeb1 == celeb2:
			celeb2 = get_person()
			
		higher = compare(celeb1, celeb2)

		os.system('clear')
		# print(f"Hint: it's {higher}")
		print(logo)

		if score > 0:
			print(f"You're right! Current score: {score}")

		print(f"Compare A: {celeb1['name']}, a {celeb1['description']} from {celeb1['country']}")
		print(vs)
		print(f"Against B: {celeb2['name']}, a {celeb2['description']} from {celeb2['country']}")
		guess = input("Who has more followers? Type 'A' or 'B': ")

		if guess.upper() == higher:
			score += 1
		else:
			wrong = True
			os.system('clear')
			print(logo)
			print(f"Sorry, that's wrong. Final score: {score}")

	if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
		higher_or_lower()
	else:
		print("Thanks for playing!")

higher_or_lower()