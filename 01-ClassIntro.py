#oop
class playerCharacter:
	def __init__(self, name, age):
		#Self refers to playerCharacter
		self.name = name #Attributes
		self.age = age

	def run(self):
		print("run")
		return "done"


player1 = playerCharacter("Sai",21)
player2 = playerCharacter("SSR",21)
player1.attack = 50

print(player1.run()) #When a function returns nothing, we get "None"
print(player1.name,player1.age)
print(player2.name,player2.age)
print(player1.attack)
