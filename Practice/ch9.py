'''
9-1 餐馆 ： 创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名
			为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
			根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
'''
class Restaurant():
	def __init__(self, r_name, r_type):
		self.name = r_name
		self.type = r_type

	def open_restaurant(self):
		print(f'{self.name} is open')

	def describr_restaurant(self):
		print(f'This restaurant name is {self.name}')


'''
9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
'''
ponda_food = Restaurant('Ponda', 'CN')
ponda_food.describr_restaurant()

McD_food = Restaurant('McD', 'US')
McD_food.describr_restaurant()

Kfc_food = Restaurant('KFC', 'N/A')
Kfc_food.describr_restaurant()


'''
9-3 用户 ： 创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User 中定义一个名
			为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。
			创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
'''
class User():
	
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(f'This user is {self.first_name} {self.last_name}')

	def greet_user(self):
		print(f'Hi, {self.first_name}')

user1 = User('Cyril', 'Yen')

user1.describe_user()
user1.greet_user()


'''
9-4 就餐人数 ：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实
	例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
'''
# 添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

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

kfc = Restaurant('KFC', 'N/A')
print(kfc.number_served)

kfc.set_number_served(10)
print(kfc.number_served)

kfc.increment_number_served(12)
print(kfc.number_served)


'''
9-5 尝试登录次数 ：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。编写一个名为increment_login_attempts() 的方法，
	它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
	根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方
	法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
'''
class User():
	
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		print(f'This user is {self.first_name} {self.last_name}')

	def greet_user(self):
		print(f'Hi, {self.first_name}')

	def increment_login_attempts(self, amout):
		self.login_attempts += amout

	def reset_login_attempts(self):
		self.login_attempts = 0


user1 = User('Cyril', 'Yen')
print(user1.login_attempts)

user1.increment_login_attempts(3)
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)


'''
9-6 冰淇淋小店 ：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。这两个版
	本的Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋
	的方法。创建一个IceCreamStand 实例，并调用这个方法。
'''
class IceCreamStand(Restaurant):
	def __init__(self, name, type):
		super().__init__(name, type)
		self.flavors = ['Apple', 'Sugar', 'Strawberry']

	def get_flavors(self):
		print(self.flavors)

store = IceCreamStand('小美冰店', '賣冰')
store.get_flavors()


'''
9-7 管理员 ：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。添加一个名为privileges 的属性，用
	于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。编写一个名为show_privileges() 的方法，它
	显示管理员的权限。创建一个Admin 实例，并调用这个方法。
'''
class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = "Create, Edit, Delete"

	def show_privileges(self):
		print(self.privileges)

admin = Admin('Cyril', 'Yen')
admin.show_privileges()


'''
9-8 权限 ：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。将方法show_privileges() 移到这
	个类中。在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。
'''
class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

class Privileges():
	def __init__(self):
		self.privileges = "Create, Edit, Delete"

	def show_privileges(self):
		print(self.privileges)

admin = Admin('WJ', 'Hsu')
admin.privileges.show_privileges()


'''
9-9 电瓶升级 ：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。这个方法检查电瓶容量，如果它不是85，就将它
	设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，并再次调用get_range() 。你会看到这辆汽车的续航里程增
	加了。
'''
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

CarA = ElectricCar('Green', 'Toyota')
CarA.battery.get_range()
CarA.battery.upgrade_battery()
CarA.battery.get_range()

'''
9-10 导入Restaurant 类 ：将最新的Restaurant 类存储在一个模块中。在另一个文件中，导入Restaurant 类，创建一个Restaurant 实例，并调
	 用Restaurant 的一个方法，以确认import 语句正确无误。
'''
from ch9_module.Restaurant import Restaurant

R1 = Restaurant('McD', 'fast food')
R1.describr_restaurant()


'''
9-11 导入Admin 类 ：以为完成练习9-8而做的工作为基础，将User 、Privileges 和Admin 类存储在一个模块中，再创建一个文件，在其中创建一个Admin 实例
	 并对其调用方法show_privileges() ，以确认一切都能正确地运行。
'''
from ch9_module.Permission import Admin

user = Admin('Cyril', 'Yen')
user.privileges.show_privileges()


'''
9-12 多个模块 ：将User 类存储在一个模块中，并将Privileges 和Admin 类存储在另一个模块中。再创建一个文件，在其中创建一个Admin 实例，并对其调用方
	 法show_privileges() ，以确认一切都依然能够正确地运行。
'''
import ch9_module.User as User
import ch9_module.Admin as Admin

user = Admin.Admin('Cyril', 'Yen')
user.privileges.show_privileges()


