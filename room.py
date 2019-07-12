import item
class Coord():
	def __init__(self, in_coord, item=None):
		self.coord = in_coord
		self.has = item

	def __repr__(self):
		return str(self.coord)

	def announce(self):
		return str(self.has)

	def place(self, in_item):
		self.has = in_item

class Room():
	def __init__(self, characters):
		self.characters = characters
		self.coord_dict = {}
		
		# Fill the room with coordinates that have no item
		for i in range(10):
			for j in range(10):
				self.coord_dict[(i, j)] = Coord((i, j))

		# Make a single sample box at 1 down, 5 right
		single_box = item.Item('box', '☐')
		self.coord_dict[(1, 5)].place(single_box)
	
