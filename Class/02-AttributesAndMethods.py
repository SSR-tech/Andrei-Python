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
		print(f"my name is {self.name} and I'm {self.age}")


	def run(self,hello):
		return(f"my name is {self.name}")


player1 = playerCharacter("Sai",21)
player2 = playerCharacter("SSR",21)
player1.attack = 50

print(player1.shout())
print(player2.run("Heyy"))


# When there is no return in a function, the function will return a none along with the print