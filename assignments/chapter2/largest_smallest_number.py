number1 = int (input('Enter a number: '))
number2 = int (input('Enter a number: '))
number3 = int (input('Enter a number: '))

sum = number1 + number2 + number3
average = sum // 3 
product = number1 * number2 * number3
print('The total is ', sum)
print('The average is ', average)
print('The product is ', product)
if (number1 > number2 and number1 > number3): 
	print(number1, ' is the largest')
elif (number2 > number1 and number2 > number3):
	print(number2, 'is the largest')
elif (number3 > number1 and number3 > number2):
	print(number3, 'is the largest')