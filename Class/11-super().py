# Many forms
 # Users -> Wizards, Archers, Ogers
class User():
	def __init__(self,email):
		self.email = email
	
	def sign_in(self):
			print("Logged in")

class Wizard(User):
	def __init__(self,name,power,email):
		super().__init__(email)
		self.MyName = name
		self.MyPower = power

	def attack(self):
		print(f"Attacking with power of {self.MyPower}")

class Archer(User):
	def __init__(self,name,num_of_arrows):
		self.MyName = name
		self.MyArrows = num_of_arrows

	def attack(self):
		print(f"Attacking with arrows: arrows left {self.MyArrows}")

wizard1 = Wizard("Merlin",60,"ssrstudio99@gmail.com")

print(wizard1.email)

