password = 'hunterhuang'
chance = 3
while chance > 0:
	user_try = input('Please enter your code: ')
	chance = chance - 1
	if user_try != password and chance > 0:
		print('You have', chance, 'chances left.')
	elif user_try == password:
		print('You have logged in.')
		break
	elif chance == 0:
		print('You failed.')
