class Character:
	def __init__(self, name, location, uni):
		self.location = location
		self.name = name
		self.uni = uni # unicode character representation

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.uni

class Player(Character):
	def __init__(self, loot=None):
		super().__init__('Hero', (9, 5), '👵')
		if loot == None:
			self.loot = []
		else:
			self.loot = loot 