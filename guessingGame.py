import random

noofguesses=1
no=random.randrange(1,10)

while noofguesses<16:
	guess=input("Take a guess ")
	guess=int(guess)
	noofguesses=noofguesses+1
	guessesleft=16-noofguesses
	print ("Guesses left = "), guessesleft
	if guess<no:
		guessesleft=str(guessesleft)
		print ("Your guess is low")
	elif guess>no:
		guessesleft=str(guessesleft)
		print ("Your guess is high")
	else:
		noofguesses=str(noofguesses)
		print ("Your guess is right")
		exit(0)

print ("Game over. You lost. Number = "), no