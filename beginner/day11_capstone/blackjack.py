from art import logo
import random
import os
import math

def deal_card():
	#Return random card from the deck
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #ACE to K point values
	return random.choice(cards)

def calc_score(cards):
	#Returns calculated score of current cards in hand
	
	#0 represents blackjack in this case
	if sum(cards) == 21 and len(cards) == 0:
		return 0
	#if we get an Ace but the total > 21, the Ace is worth 1 instead of 11
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)

	#after dealing with edge cases, we return sum of cards
	return sum(cards)

def compare(user_total, comp_total):
	#if you and the computer both go over, you lose
	if user_total > 21 and comp_total > 21:
		return "You went over. You lose!"

	if user_total == comp_total:
		return "It's a draw!"
	elif comp_total == 0: #comp gets blackjack (Ace and 10 on first hand)
		return "You lose, opponent has a Blackjack!"
	elif user_total == 0:
		return "You win with a Blackjack!"
	elif user_total > 21:
		return "You went over. You lose!"
	elif comp_total > 21:
		return "You opponent went over. You win! "
	elif user_total > comp_total:
		return "You win!!"
	else:
		return "You lose!!"

def blackjack():

	play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
	if play == 'y':
		os.system('clear')
		print(logo)

		user_cards = []
		comp_cards = []
		game_over = False

		#get first two cards
		for _ in range(2):
			user_cards.append(deal_card())
			comp_cards.append(deal_card())


		while not game_over:
			user_total = calc_score(user_cards)
			comp_total = calc_score(comp_cards)

			#added tabs to make more readable
			print(f"	Your cards: [{user_cards}], current score: {user_total}")
			print(f"	Computer's first card: {comp_cards[0]}")

			if user_total > 21 or user_total == 0 or comp_total == 0:
				game_over = True
			else:
				add_card = input("Type 'y' to get another card, type 'n' to pass: ")
				if add_card == 'y':
					user_cards.append(deal_card())
				else:
					game_over = True

		while comp_total != 0 and comp_total <= 16:
			comp_cards.append(deal_card())
			comp_total = calc_score(comp_cards)

		print(f"Your final hand: [{user_cards}], final score: {user_total}")
		print(f"Computer's final hand: [{comp_cards}], final score: {comp_total}")
		print(compare(user_total, comp_total))
		blackjack()


blackjack()
