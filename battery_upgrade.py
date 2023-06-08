class Car:
	def __init__(self, make, model, year):
		self.make=make.title()
		self.model=model.title()
		self.year=year
		self.odometer_reading=0

	def get_descriptive_name(self):
		long_name=f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You cant roll back the odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading+=miles

class Battery:
	def __init__(self, battery_size = 75):
		'''Initialize battery attributes'''
		self.battery_size=battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")
	def upgrade_battery(self):
		if self.battery_size==75:
			self.battery_size=100
			print(f"Upgraded the battery to 100-kWh")
		else:
			print("The battery has already been upgraded")

class ElectricCar(Car):
	'''Represent aspects of a car, specific to electric vehicles'''
	def __init__(self, make, model, year, ):
		'''initialize attributes of parent class'''
		super().__init__(make, model, year)
		self.battery= Battery()

my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()