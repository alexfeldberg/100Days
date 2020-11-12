import random

def coin_toss()
	test_seed = int(input("Create a seed number: "))
	random.seed(test_seed)

	rand = random.randint(0,1)
	if rand == 0:
	  print("Tails")
	else:
	  print("Heads")

coin_toss()