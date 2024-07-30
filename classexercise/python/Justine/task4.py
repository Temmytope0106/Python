# define the function 
# receive int parameters 
# compare if it is even and display 'it is even' if true 
# compare if it is odd and display 'it is odd' if true 
# return string

def decide(number):
	if(number % 2 == 0):
		result = 'It is an even number'

	else:
		result = 'It is an odd number'

	return result

	
		
number = int(input('Enter a number'))
result = decide(number)
print(result)