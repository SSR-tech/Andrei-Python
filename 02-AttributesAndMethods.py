#oop
class playerCharacter:
	#Class Object Attribute
	membership = True

	#This is more like the constructor and the super keywords in JS
	def __init__(self, name, age):
		if (self.membership):
			self.name = name 
			self.age = age

	def shout(self):
		print(f"my name is {self.name}")

	def run(self,hello):
		print(f"my name is {self.name}")


player1 = playerCharacter("Sai",21)
player2 = playerCharacter("SSR",21)
player1.attack = 50

print(player1.shout())
print(player2.run("Heyy"))