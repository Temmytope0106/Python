def equal_strings(string1, string2):

	new_letter = ''
	new_character = ''

	if(len(string1) == len(string2)):
		for character in string1:
			new_character += character
		for letter in string2:
			new_letter += letter
		if(new_letter == new_character):
			return True
		else:		
			return 0
	else: 
		return False

string1 = input('Enter a word: ')
string2 = input('Enter another word: ')
result = equal_strings(string1, string2)
print(result)