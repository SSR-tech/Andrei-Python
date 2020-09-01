#oop
class playerCharacter:
	def __init__(self, name="anonymous", age=0):
		if(age > 18):
			self.name = name 
			self.age = age

	def shout(self):
		print(f"my name is {self.name} {self.age}")

	def run(self):
		print(f"my name is {self.name} {self.age}")


player1 = playerCharacter("Sai",21)
player2 = playerCharacter("SSR",17) #Error Code

print(player1.shout())
print(player2.run())