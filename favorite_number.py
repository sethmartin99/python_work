import json

def get_new_number():
	fav_num=input("What is your favorite number?: ")
	filename='fav_num.json'
	with open(filename, 'w') as f:
		json.dump(fav_num, f)
	return fav_num

def get_stored_number():
	filename='fav_num.json'
	try:
		with open(filename) as f:
			fav_num=json.load
	except FileNotFoundError:
		return None 
	else:
		return fav_num

def greet_user():
	fav_num=get_stored_number
	if fav_num:
		print(f"I know your favorite number. It's {fav_num}")
	else:
		fav_num=get_new_number




greet_user()