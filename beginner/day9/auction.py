from art import logo 
import os

def bid():

	bids = {}
	bidding_finished = False
	while not bidding_finished:
		name = input("What is your name?: ")
		price = int(input("What's your bid?: $"))
		bids[name] = price
		more_bidders = input("Does anyone else want to place a bid? Please type 'yes' or 'no'.\n")
		if more_bidders == "no":
			bidding_finished = True
		elif more_bidders == "yes":
			os.system('clear')

	highest_bidder(bids)

def highest_bidder(all_bids):

	highest_bid = 0
	highest_bidder = ""

	for bidder in all_bids:
		if all_bids[bidder] > highest_bid:
			highest_bid = all_bids[bidder]
			highest_bidder = bidder
	print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

print(logo)
bid()