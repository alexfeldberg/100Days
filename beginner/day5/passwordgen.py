import random
import pyperclip

def passwordgen():

	password = ""
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	print("Welcome to the PyPassword Generator!")
	num_letters = int(input("How many letters would you like in your password?\n"))
	num_numbers = int(input("How many numbers would you like in your password?\n"))
	num_symbols = int(input("How many symbols would you like in your password?\n"))

	# total_len = num_letters + num_numbers + num_symbols
	for x in range(num_letters):
		password += random.choice(letters)

	for x in range(num_numbers):
		password += random.choice(numbers)

	for x in range(num_symbols):
		password += random.choice(symbols)

	l = list(password)
	random.shuffle(l)
	final = "".join(l)


	print(f"Your password is: {final}")
	pyperclip.copy(final)
	
passwordgen()