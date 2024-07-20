def divide_or_square(number):
	if(number % 5 == 0):
		return number ** 0.5
	else: 
		return number % 5


number = int(input('Enter a number: '))
total = divide_or_square(number)

print(total)