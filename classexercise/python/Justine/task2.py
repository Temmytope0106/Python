# collect an input 
# walk through the input and count the number of letters in the string 
# Count the number of digit in the string

word = input('Enter a word: ')
count = 0
for characters in word:
	count = count + 1
	print(characters, end=',')
print(count)