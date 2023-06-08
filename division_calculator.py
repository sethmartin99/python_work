print("Give me two numbers and I will divide them.")
print('Enter \'q\' to quit')

while True:
	first_num = int(input("\nFirst Number: " ))
	if first_num=='q':
		break
	second_num=int(input("Second Number: "))
	if second_num=='q':
		break
	try:
		answer=first_num/second_num
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)