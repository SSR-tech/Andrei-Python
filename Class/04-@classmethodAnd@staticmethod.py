#OOP
class PlayerCharacter:
	membership = True
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def shout(self):
		print(f"my name is {self.name}")

	@classmethod #cls refers to the actual class
	def adding_things(cls,num1,num2):
		return cls("SSR",num1 + num2)
	
	@staticmethod #No access to the class directly
	def adding_things(num1,num2):
		return num1 + num2

player1 = PlayerCharacter("SAI",21)

print(player1)

