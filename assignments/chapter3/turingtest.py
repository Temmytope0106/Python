question = input('What is your problem?: ')
question2 = bool(input('Have you had this problem before(Yes or No)?: '))
if(question2 == 'Yes'):
	print('Well, you have it again.')
else: 
	print('Well, you have it now.')