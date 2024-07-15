largest = 0
second_largest = 0

for number_of_times in range(1, 11):
	scores = int(input('Enter a number: '))
	if(scores > largest):
		largest = scores
	if(scores > second_largest and largest > second_largest):
			second_largest = scores
print(largest)
print(second_largest)

