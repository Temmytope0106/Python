factorial = 1
number = int(input('Enter a number: '))
for count in range(1, (number + 1)):
	factorial *= count
print(factorial)