factorial = 1
initial_e = 0
total_e = 0

for counter in range(1, 10):
	for count in range(1, counter):
		factorial *= count
	initial_e += 1 / factorial
	total_e += initial_e 
e = 1 + total_e
print(e)