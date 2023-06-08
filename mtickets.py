prompt="Enter your age for prices."
prompt+="\nAge: "
age=0

active=True
while active:
	age=input(prompt)
	if age(0:2):
		price=0
	elif age>=3 and age<=12:
		price=10
	elif age>12:
		price=15
	elif age=='quit':
		active=False

print(f"Your ticket costs ${price}")

