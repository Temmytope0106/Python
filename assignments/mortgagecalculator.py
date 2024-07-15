from decimal import Decimal
principalamount = int(input('Enter the principal amount in dollars: '))
annualrate = int(input('Enter the annual rate: '))
duration = int(input('Enter the duration in years: '))

converted_annualrate = (annualrate / 100) / duration
duration_in_months = duration * 12

numerator = converted_annualrate * ((1 + converted_annualrate) ** duration_in_months)
denominator = ((1 + converted_annualrate) ** duration_in_months) - 1

monthly_payment = Decimal(principalamount * ( numerator / denominator ))

print(f'{'Your monthly payment is $'}{monthly_payment:.3f}')


