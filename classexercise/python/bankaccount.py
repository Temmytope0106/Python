amount = 0
remainder = 0
balance = 0
decision = 0


while(decision != -1):
	decision = int(input('Enter 1 to deposit or 2 to withdraw or 3 to see balance or -1 to quit: '))

	
	if(decision == 1):
		deposit = int(input('Enter amount to deposit: '))
		amount += deposit
	

	elif(decision == 2):
		withdraw = int(input('Enter amount to withdraw: '))	
		if(withdraw > amount):
			print('Invalid balance')
		else:
			amount -= withdraw
	elif(decision == 3):
		print(amount)
	else: 
		break





