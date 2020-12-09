from ingredients import MENU, resources
import math

def print_report():
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${resources['money']}")

def enough_ingredients(order_ingredients):
	"""Return True if enough ingredients for order"""
	for ingredient in order_ingredients:
		if resources[ingredient] < order_ingredients[ingredient]:
			print(f"Sorry, not enough {ingredient}.")
			return False
	return True

def request_payment(cost):
	print(f"Please insert coins")
	quarters = int(input("How many quarters?: "))
	dimes = int(input("How many dimes?: "))
	nickels = int(input("How many nickels?: "))
	pennies = int(input("How many pennies?: "))

	payment_given = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

	if payment_given > cost:
		print(f"Your change is ${round(payment_given - cost, 2)}.")
		resources['money'] += cost
		return True
	else:
		if payment_given < cost:
			print("Not enough money inserted. Refunding your money.")
			return False
			# request_payment(cost - payment_given)
		# resources['money'] += cost
		# return True


def coffee_machine(drink_name, ingredients_needed):
	for item in ingredients_needed:
		resources[item] -= ingredients_needed[item]
	print(f'Here is your {drink_name}!')


off = False
while not off:
	order = input("What would you like to order? (espresso/latte/cappuccino): ")

	if order == "report":
		print_report()
	elif order == "off":
		off = True
		print("Turning coffee machine off.")
	elif order == "espresso" or order == "latte" or order == "cappuccino":
		if enough_ingredients(MENU[order]['ingredients']):
			if request_payment(MENU[order]['cost']):
				coffee_machine(order, MENU[order]['ingredients'])
	else:
		print("Invalid order - please try again.")


"""
Want to add functionality to allow user to add more money if insufficient payment, 
as well as an alert to restart the program if any ingredient reaches 0.
"""