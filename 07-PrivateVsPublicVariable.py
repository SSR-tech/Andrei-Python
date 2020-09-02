#Private - Underscore
class PlayerCharacter:
	def __init__(self,name,age):
		self._Myname = name 
		self._Myage = age  

	def run(self):
		print("run")

	def speak(self):
		print(f"my name is {self._Myname}, and I am {self._Myage} years old")

player1 = PlayerCharacter("SSR",21)
player1.name = "!!!"
player1.speak = "BOOOO"

print(player1.speak())