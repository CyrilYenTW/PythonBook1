class Car():
	def __init__(self, color, brand):
		self.color = color
		self.brand = brand
		self.year = '1990'

	def get_color(self):
		print(self.color)

class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battary(self):
		print(f'Battery size => {self.battery_size}')

	def get_range(self):
		print(f'{self.battery_size}')

	def upgrade_battery(self):
		if(self.battery_size < 85):
			self.battery_size = 85

class ElectricCar(Car):
	def __init__(self, color, brand):
		super().__init__(color, brand)
		self.battery = Battery()