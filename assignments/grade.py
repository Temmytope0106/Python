passes = 0
failures = 0

for student_number in range(1, 16):
	scores = int(input('Enter score for student '))
	if(scores > 45):
		passes = passes + 1
	if(scores < 45):
		failures = failures + 1

print('Number of student that passed is: ', passes)
print('Number of student that failed is: ', failures)

