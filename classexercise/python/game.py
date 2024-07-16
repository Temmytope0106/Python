from random import *
print('Welcome to Guess The Number Game!!!!!!!!!')

random_number = randint(1, 1000)
runtime = 0
guess = ('Press Yes start or No to quit ')
while guess not in ['No']:
	guess = int(input('Guess my number between 1 to 1000: '))
	runtime = runtime + 1
	if(guess != random_number):
		if(guess > random_number):
			print('Too high, Try again.')
		if(guess < random_number):
			print('Too low, Try again.')
	if(guess == random_number):
		print('Congratulations.You guessed the right number.')
		if(runtime > 10):
			print('Your number of trial is ', runtime)	
		if(runtime < 10):
			print('Your number of trial is ', runtime, 'You tried.')
		guess = input('Press Yes start or No to quit ')
		random_number = randint(1, 1000)
		runtime = 0
	
	
	
	