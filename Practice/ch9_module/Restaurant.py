class Restaurant():
	def __init__(self, r_name, r_type):
		self.name = r_name
		self.type = r_type
		self.number_served = 0

	def open_restaurant(self):
		print(f'{self.name} is open')

	def describr_restaurant(self):
		print(f'This restaurant name is {self.name}')

	def set_number_served(self, amount):
		self.number_served = amount

	def increment_number_served(self, amount):
		self.number_served += amount