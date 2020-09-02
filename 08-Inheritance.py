# Users -> Wizards, Archers, Ogers
# Inheritance
class User():
	def sign_in(self):
		print("Logged in")

class Wizard(User):
	def __init__(self,name,power):
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

wizard1 = Wizard("Merlin",50)
archer1 = Archer("Robin",100)

wizard1.attack()
archer1.attack()