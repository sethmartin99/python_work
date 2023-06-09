import random

number = random.randint(1,25)
number_of_guesses = 0 

while number_of_guesses < 5:
	print('Guess a number between 1 and 25: ')
	guess = input()
	guess = int(guess)
	number_of_guesses += 1 

	if guess == number:
		break
	elif number_of_guesses == 5:
		break
	else:
		print("Nope, try again!")

if guess == number:
	print(f'Correct, you guessed the number in {number_of_guesses} tries.')
else:
	print(f'You did not guess the number. The number was {number}')