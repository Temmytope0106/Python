number = int(input('Enter a five digit number: '))
digit1 = int(number / 10000 % 10)
digit2 = int(number / 1000 % 10)
digit3 = int(number / 100 % 10)
digit4 = int(number / 10 % 10)
digit5 = int(number / 1 % 10)

if(digit1 == digit5 and digit2 == digit4):
	print('THIS NUMBER IS A PALINDROME')
else: 
	print('THIS NUMBER IS NOT A PALINDROME')



