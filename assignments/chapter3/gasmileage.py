result = 0
decision = int(input('Enter the gallons used(-1 to end): ') )
while(decision != -1):
	decision2 = int(input('Enter the miles driven: '))
	result += decision2 / decision 
	print('The miles/gallon for this was', result)
	decision = int(input('Enter the gallons used(-1 to end): ') )
print('The overall miles/gallon for this was ', result)

	