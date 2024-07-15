totalamount = 0
original_amount = 1000
annual_rate = 7 / 100
for years in range(1, 31):
	principal_of_theyear = original_amount * ((1 + annual_rate) ** years)
	totalamount += principal_of_theyear
	print('The amount for year', years, 'is', totalamount)
print('The total amount for 30 years is ', totalamount)








