original_amount = 1000
annual_rate = 7 / 100
number_of_firstyear = 10
number_of_secondyear = 20
number_of_thirdyear = 30

principal_of_firstyear = original_amount * ((1 + annual_rate) ** number_of_firstyear)
principal_of_secondyear = original_amount * ((1 + annual_rate) ** number_of_secondyear)
principal_of_thirdyear = original_amount * ((1 + annual_rate) ** number_of_thirdyear)

print('The amount of deposit at the end of', number_of_firstyear, 'is', principal_of_firstyear)
print('The amount of deposit at the end of', number_of_secondyear, 'is',principal_of_secondyear)
print('The amount of deposit at the end of', number_of_thirdyear, 'is', principal_of_thirdyear)

