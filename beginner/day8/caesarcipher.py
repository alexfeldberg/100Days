from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(cipher_direction, start_text, shift_amount):

	cipher_text = ""
	if cipher_direction == "decode":
		shift_amount *= -1
	for char in start_text:
		if char in alphabet:
			pos = alphabet.index(char)
			new_pos = (pos + shift_amount)	
			cipher_text += alphabet[new_pos]
		else:
			cipher_text += char
	print(f"Here's the {direction}d result: {cipher_text}")


print(logo)

replay = True
while replay:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	
	#checking for 25, not 26, because indeces are 0-25
	#don't need to check if shift > 25 because shift<25 won't be affected
	shift %= 25
	cipher(direction, text, shift)

	go_again = input("Would you like to go again? Type 'yes' or 'no'.\n")
	if go_again == 'no':
		replay = False
		print("Exit.")