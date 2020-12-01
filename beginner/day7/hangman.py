import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def hangman():

	word_list = ["ardvark", "baboon", "camel"]
	end_of_game = False
	chosen_word = random.choice(word_list)
	# print(f'Pssst, the solution is {chosen_word}.')

	lives = 6 #one life per body part

	#Creating blanks
	display = []
	for _ in chosen_word:
		display.append("_")
	print(display)

	while not end_of_game:
		guess = input("Guess a letter: ").lower()

		#Check guessed letter
		for pos in range(len(chosen_word)):
			if chosen_word[pos] == guess:
				display[pos] = guess

		if guess not in chosen_word:
			lives -= 1
			print(f"Oh no! That letter is not in the word, you lose a life! You have {lives} lives left.")
			print(stages[lives])
			if lives == 0:
				end_of_game = True
				print(f"Sorry, you lost! The word was: {chosen_word}")


		print(display)

		if "_" not in display:
			end_of_game = True
			print("Congratulations! You won!")


hangman()
