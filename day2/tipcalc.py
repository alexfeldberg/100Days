def tip_calc():

	print("Welcome to the tip calculator!")
	total = float(input("What was the total bill?\n$"))
	tip = int(input("What percent tip would you like to give?\n"))
	num_people = int(input("How many people were at dinner?\n"))

	bill_with_tip = total + total*(tip/100)
	amount_per_person = bill_with_tip/num_people

	final_amount = round(amount_per_person, 2)

	print(f"Each person should pay: ${final_amount}")

tip_calc()