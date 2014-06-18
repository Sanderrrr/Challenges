import random

coin = ["heads", "tails"]
flip = random.choice(coin)
pick = input("heads or tails? ")

if flip == pick:
	print(flip)
	print("You won!")
else:
	print(flip)
	print("You lost")