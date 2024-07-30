# walk through number 1000 to 3000
# get each digit 
# check if each digit is even and if true print that number


for numbers in range(1000, 3001):
	digit1 = numbers // 1000
	digit2 = numbers // 100 % 10
	digit3 = numbers // 10 % 10
	digit4 = numbers % 10

	if(digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0 and digit4 % 2 == 0):
		print(numbers, end=',')