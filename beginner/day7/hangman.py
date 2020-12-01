import random
from hangman_art import logo, stages
from hangman_words import word_list

def hangman():

	print(logo)
	end_of_game = False
	lives = len(stages) - 1 #one life per body part
	#Choose random word from hangman_words.py
	chosen_word = random.choice(word_list)
	print(f'Pssst, the solution is {chosen_word}.') #used for testing

	#added extra functionality to not remove a life for a wrong guess that was already guessed
	wrong_guesses = set([])
	
	#Creating blanks
	display = []
	for _ in chosen_word:
		display.append("_")
	#Print to show length of word
	print(display)

	while not end_of_game:
		guess = input("Guess a letter: ").lower()

		if guess in display:
			print(f"You've already guessed {guess}, it is in the word. Try again.")
		#Check guessed letter
		for pos in range(len(chosen_word)):
			if chosen_word[pos] == guess:
				display[pos] = guess

		if guess not in chosen_word:
			if guess in wrong_guesses:
				print(f"You've already guessed {guess}, it is not in the word. Try again.")
			else:
				wrong_guesses.add(guess)
				lives -= 1
				print(f"Oh no! That letter is not in the word, you lose a life! You have {lives} lives left.")
				if lives == 0:
					end_of_game = True
					print(f"Sorry, you lost! The word was: {chosen_word}")


		print(display)

		if "_" not in display:
			end_of_game = True
			print("Congratulations! You won!")

		#print hangman regardless of if guess is correct
		print(stages[lives])


hangman()
