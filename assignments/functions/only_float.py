def only_float(a, b):
	if(a == int(a) and b == float(b)):
		return 1
	if(a == float(a) and b == int(b)):
		return 1
	if(a == float(a) and b == float(b)):
		return 2


number1 = float(input('Enter a number: '))
number2 = float(input('Enter a number: '))
total = only_float(number1, number2)

print(total)

# this is your test will always pass as you already cast ur input to float
