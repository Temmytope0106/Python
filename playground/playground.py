from decimal import Decimal 
name = input('Enter your name: ')
print(name)
print (id(name))
name = name +"ayo" 
print (name)
print(id(name))

number = 1
print(number)
print(id(number))
number += 4
print(number)
print(id(number))

basket = [1, 2, 3, 4]
print(basket)
print(id(basket))
 
basket.append(5)
print(basket)
print(id(basket))

for char in "techblazers":
	print('timothy')
	print(char, 'timothy')

for char in range(100):
	print(char, 'timothy')

for number in range(100):
	print(number, end= ' ')

for number in range(20):
	print(number, end = ', ')

number = 234.56
print(f'{number:.20f}')

print(f'{Decimal('5.67') * Decimal('4.67'):.3f}')

for chracter in range(2, 11, 4):
	print(f'{chracter:.2f}', end=' ')