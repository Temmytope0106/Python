def my_discount(price, discount):
	result = price - ((discount / 100) * price)
	return result


price = int(input('Enter a price: '))
discount = int(input('Enter a discount rate: '))
total = my_discount(price, discount)
print('Your new price is ', total)