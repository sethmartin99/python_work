def get_seconds(hours, minutes, seconds):
	total_seconds = 3600 * hours + 60 * minutes + seconds 
	return total_seconds

print(get_seconds(24,0,0))

def lucky_number(name):
	number = len(name)*7
	print(f'Hello {name.title()}, your lucky number is {number}')

lucky_number('seth')

def even_number(num):
	if num % 2 ==0:
		print(f'The number {num} is even.')
	else:
		print(f'{num} is not even')

even_number(2)