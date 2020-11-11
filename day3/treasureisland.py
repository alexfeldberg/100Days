def treasure_island():

	print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************

		''')
	print("Welcome to Treasue Island! Your mission is to find the treasure.")
	direction = input("You're at a fork in the road. Would you like to go left or right?\n")

	if direction.lower() == "right":
		print("You fell into a hole. Game Over!")
	else:
		direction = input("You've reached a lake. Would you like to swim or wait for a boat?\n")
		if direction.lower() != "wait":
			print("You were attacked by a trout. Game over!")
		else:
			color = input("You've come across two doors. Would you like to open the red, yellow, or blue door?\n")
			if color.lower() == "red":
				print("You were burned by a fire. Game over!")
			elif color.lower() == "blue":
				print("You were eaten by wild beasts. Game over!")
			elif color.lower() == "yellow":
				print("Congratulations! You've found the treasure and won the game!")
			else:
				print("Game over!!")

treasure_island()