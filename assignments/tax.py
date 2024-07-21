decision = int(input('Enter 0 for single filers, 1 for married filers, 2 for single married filer, 3 for head of household, -1 to quit: '))

while(decision != -1):
	if(decision == 1):
		income = int(input('Enter your income: '))
		if(income >= 0 and income <= 8350):
			result = income * (10 / 100)
			print('Your tax is ', result)
		if(income >= 8351 and income <= 33950):
			result = income * (15 / 100)
			print('Your tax is ', result)
		if(income >= 33951 and income <= 82250):
			result = income * (25 / 100)
			print('Your tax is ', result)
		if(income >= 82251 and income <= 171550):
			result = income * (28 / 100)
			print('Your tax is ', result)
		if(income >= 171551 and income <= 372950):
			result = income * (33 / 100)
			print('Your tax is ', result)
		if(income >= 372951):
			result = income * (35 / 100)
			print('Your tax is ', result)
	
	if(decision == 2):
		income = int(input('Enter your income: '))
		if(income >= 0 and income <= 16700):
			result = income * (10 / 100)
			print('Your tax is ', result)
		if(income >= 16701 and income <= 67900):
			result = income * (15 / 100)
			print('Your tax is ', result)
		if(income >= 67901 and income <= 137050):
			result = income * (25 / 100)
			print('Your tax is ', result)
		if(income >= 137051 and income <= 208850):
			result = income * (28 / 100)
			print('Your tax is ', result)
		if(income >= 208851 and income <= 372950):
			result = income * (33 / 100)
			print('Your tax is ', result)
		if(income >= 372951):
			result = income * (35 / 100)
			print('Your tax is ', result)

	if(decision == 3):
		income = int(input('Enter your income: '))
		if(income >= 0 and income <= 8350):
			result = income * (10 / 100)
			print('Your tax is ', result)
		if(income >= 8351 and income <= 33950):
			result = income * (15 / 100)
			print('Your tax is ', result)
		if(income >= 33951 and income <= 68525):
			result = income * (25 / 100)
			print('Your tax is ', result)
		if(income >= 68526 and income <= 104425):
			result = income * (28 / 100)
			print('Your tax is ', result)
		if(income >= 104426 and income <= 186475):
			result = income * (33 / 100)
			print('Your tax is ', result)
		if(income >= 186476):
			result = income * (35 / 100)
			print('Your tax is ', result)

	if(decision == 4):
		income = int(input('Enter your income: '))
		if(income >= 0 and income <= 11950):
			result = income * (10 / 100)
			print('Your tax is ', result)
		if(income >= 11951 and income <= 45500):
			result = income * (15 / 100)
			print('Your tax is ', result)
		if(income >= 45501 and income <= 117450):
			result = income * (25 / 100)
			print('Your tax is ', result)
		if(income >= 117451 and income <= 190200):
			result = income * (28 / 100)
			print('Your tax is ', result)
		if(income >= 190201 and income <= 372950):
			result = income * (33 / 100)
			print('Your tax is ', result)
		if(income >= 372951):
			result = income * (35 / 100)
			print('Your tax is ', result)
	
	decision = int(input('Enter 0 for single filers, 1 for married filers, 2 for single married filer, 3 for head of household, -1 to quit: '))


	