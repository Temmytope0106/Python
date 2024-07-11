score = int(input('Enter your score: '))
if (score > 100):
	print('Invalid score')
elif (score >= 75 and score <= 100):
	print('Your grade is A')
elif (score >= 65 and score <= 74):
	print('Your grade is B')
elif (score >= 50 and score <= 64):
	print('Your grade is C')
elif (score >= 40 and score <= 49):
	print('Your grade is D')
elif (score >= 1 and score <= 39):
	print('Your grade is F')
else :
	print('Invalid score')