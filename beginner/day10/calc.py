import os
from art import logo

def add(a, b):
	return a+b

def sub(a, b):
	return a-b

def mult(a, b):
	return a*b

def div(a, b):
	return a/b

operations = {
	"+": add,
	"-": sub,
	"*": mult,
	"/": div
}

def calc():

	first_num = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)
	keep_calculating = True

	while keep_calculating:
		op = input("Pick an operation: ")
		second_num = float(input("What's the next number?: "))
		calc_func = operations[op]
		total = calc_func(first_num, second_num)
		print(f"{first_num} {op} {second_num} = {total}")

		next_move = input(f"Type 'y' to continue calculating with {total}, 'n' to start a new calculation, or 'exit' to quit: ")
		if next_move == 'y':
			first_num = total
		elif next_move == 'n':
			keep_calculating = False
			os.system('clear')
			calc() 
		else:
			return

print(logo)
calc()