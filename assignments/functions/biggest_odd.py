def biggest_odd(number):
	largest = 2
	for digit in number:
		new_digit = int(digit)
		if (new_digit % 2 != 0):
			new_number = str(new_digit)
			for neww_digit in new_number:
				neww_number = int(new_number)
				if(neww_number > largest):
					largest = neww_number
	return largest
		

number = input('Enter a number: ')
result = biggest_odd(number)
print(result)
				
				