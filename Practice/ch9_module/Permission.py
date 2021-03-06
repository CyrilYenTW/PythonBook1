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

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

class Privileges():
	def __init__(self):
		self.privileges = "Create, Edit, Delete"

	def show_privileges(self):
		print(self.privileges)