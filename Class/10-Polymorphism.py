# Many forms
 # Users -> Wizards, Archers, Ogers
class User():
	def sign_in(self):
		print("Logged in")

	def attack(self):
		print("Do nothing")

class Wizard(User):
	def __init__(self,name,power):
		self.MyName = name
		self.MyPower = power

	def attack(self):
		User.attack(self)
		print(f"Attacking with power of {self.MyPower}")

class Archer(User):
	def __init__(self,name,num_of_arrows):
		self.MyName = name
		self.MyArrows = num_of_arrows

	def attack(self):
		print(f"Attacking with arrows: arrows left {self.MyArrows}")

wizard1 = Wizard("Merlin",60)
archer1 = Archer("Robin",30)

# Polymorphism - 1
def player_attack(char):
	char.attack()

player_attack(wizard1)
player_attack(archer1)

# Polymorphism - 2
# for char in [wizard1, archer1]:
# 	char.attack()

