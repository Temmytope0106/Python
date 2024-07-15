print('Pattern A') 

for row in range(1, 11):
	for column in range(1, row):
		print(' *', end='')
	print()

		
print('Pattern B')

N = 10
for row in range(1, 11):
	for column in range(1, (N - row + 1)):
		print('*', end='')
	print()

print('Patter C')

N = 10
for row in range(1, 11):
	for space in range(0, ((9 + row) - N)):
		print(' ', end='')
	for column in range(1, (N - row + 2)):
		print('*', end='')
		
	print()