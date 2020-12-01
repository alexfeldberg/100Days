import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def rps():

	user_choice = int(input("What do you choose? Choose 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
	comp_choice = random.randint(0,2)

	print_choice(user_choice)
	print("Computer chose:\n")
	print_choice(comp_choice)

	if user_choice >= 3 or user_choice < 0:
		print("You chose an invalid number, you lose!\n")
	elif user_choice == 0:
		if comp_choice == 1:
			print("You lose!")
		elif comp_choice == 2:
			print("You win!")
		else:
			print("It's a draw!")
	elif user_choice == 1:
		if comp_choice == 2:
			print("You lose!")
		elif comp_choice == 0:
			print("You win!")
		else:
			print("It's a draw!")
	else:
		if comp_choice == 0:
			print("You lose!")
		elif comp_choice == 1:
			print("You win!")
		else:
			print("It's a draw!")

def print_choice(choice):
	if choice == 0:
		print(rock)
	elif choice == 1:
		print(paper)
	elif choice == 2:
		print(scissors)
	else:
		print("Invalid choice!")
rps()

