class Restaurant():

	def __init__(self,name,cuisine):
		self.name=name.title()
		self.cuisine=cuisine
		self.number_served=0
		
	def describe_restaurant(self):
		print(f"{self.name.title()} serves wonderful {self.cuisine}.")
	
	def open_restaurant(self):
		print("\nThe Restaurant is open! :)")
	
	def set_number_served(self,number_served):
		self.number_served=number_served

	def increment_number_served(self, additional_served):
		self.number_served+=additional_served

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine='ice cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()


