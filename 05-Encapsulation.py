class PlayerCharacter:
	def __init__(self,name,age):
		self.name = name
		self.age = age
player1 = PlayerCharacter("SSR",21)

print(player1.name)
print(player1.age)

# Don't have to create a dictionary for passing in data
player2 = {"name":"SAI SHRI RAM","age":21}
print(player2['name'])