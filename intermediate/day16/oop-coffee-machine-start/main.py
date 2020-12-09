from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

off = False
while not off:
	options = Menu.get_items()
	order = input(f"What would you like to order? ({items}): ")
	if order == "report":
		coffee_maker.report()
		money.report()
	elif order == "off":
		off = True
		print("Turning coffee machine off.")
	else
		drink = menu.find_drink(order)
		enough_resources = coffee_machine.is_resource_sufficient(drink)
		enough_money = money.make_payment(drink.cost)
		if enough_resources and enough_money:
			coffee_machine.make_coffee(drink)

