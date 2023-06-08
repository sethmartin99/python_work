from random import randint

class Die:
	'''respresent a die which can be rolled'''
	def __init__(self, sides=6):
		self.sides=sides

	def roll_die(self):
		return randint(1, self.sides)

#make 6 sided die, and roll it 10 times

d6=Die()

results=[]
for roll_num in range(10):
	result=d6.roll_die()
	results.append(result)
print("10 rolls of a 6 sided die:")
print(results)

#make 10 sided die ad toll it 10 times
d10=Die(sides=10)
results=[]
for roll_num in range(10):
	result=d10.roll_die()
	results.append(result)
print("\n10 rolls of a 10 sided die:")
print(results)

#make 20 sided die ad toll it 10 times
d20=Die(sides=20)
results=[]
for roll_num in range(10):
	result=d20.roll_die()
	results.append(result)
print("\n10 rolls of a 20 sided die:")
print(results)


