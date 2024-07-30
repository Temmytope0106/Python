# Collect number
# walk through the digits from the back with a loop 
# store the digits together in a new variable
# After getting all the digits back in a reversed form, compare with the real number that #	was imputed


def reverse(number):
	reverse = 0
	userrinput= 0
	reversee = ''
	while (number > 0):

		reverse = (reverse * 10) + (int(number % 10))
		reversee = str(reverse)
		userrinput = number % 10
		number = int((number / 10))

	return (reversee)


def is_palindrome(number):
	reverse = 0
	userrinput= 0
	reversee = ''
	while (number > 0):

		reverse = (reverse * 10) + (int(number % 10))
		reversee = str(reverse)
		userrinput = number % 10
		number = int((number / 10))

	if(reversee == number):
		result = 'True'
	else: 
		result = 'False'
	return result

number = 12321
result = reverse(number)
resultt = is_palindrome(number)
print(result)
print(resultt)
	