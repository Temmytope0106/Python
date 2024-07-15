largest = 0
smallest = 2
sum = 0
average = 0
product = 1

for number_of_times in range(1, 4):
	scores = int(input('Enter a number: '))
	if(scores > largest):
		largest = scores
	if(scores < smallest):
		smallest = scores
	if(scores < smallest):
		smallest = scores	
	sum += scores
	average = sum / number_of_times
	product *= scores
print('The largest score is ', largest)
print('The smallest score is ', smallest)
print('The sum is ', sum)
print('The average score is ', average)
print('The product is ', product)
