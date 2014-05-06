from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Maze:
	# Dimension of maze (row x column)
	row = NumericProperty(0)
	col = NumericProperty(0)

	def __init__(self, row, col):
		self.row = row
		self.col = col
		
		self.rooms = []
		
		for i in range(row * col):
			self.rooms.append(1)

		self.player = Player(-1, -1)

	def load_curr_room_property(self):
		# Is there a door (at) [ahead, right, back, left]
		retval = [False, False, False, False]

		if self.player.r == -1:
			pass
		elif self.player.r == 0:
			retval[(2 - self.player.d) % 4] = True
			if self.player.c == 0:
				retval[(1 - self.player.d) % 4] = True
			elif self.player.c == self.col - 1:
				retval[(3 - self.player.d) % 4] = True
			else:
				retval[(1 - self.player.d) % 4] = True
				retval[(3 - self.player.d) % 4] = True
		elif self.player.r == self.row - 1:
			retval[(0 - self.player.d) % 4] = True
			if self.player.c == 0:
				retval[(1 - self.player.d) % 4] = True
			elif self.player.c == self.col - 1:
				retval[(3 - self.player.d) % 4] = True
			else:
				retval[(1 - self.player.d) % 4] = True
				retval[(3 - self.player.d) % 4] = True
		else:
			retval[(0 - self.player.d) % 4] = True
			retval[(2 - self.player.d) % 4] = True
			if self.player.c == 0:
				retval[(1 - self.player.d) % 4] = True
			elif self.player.c == self.col - 1:
				retval[(3 - self.player.d) % 4] = True
			else:
				retval[(1 - self.player.d) % 4] = True
				retval[(3 - self.player.d) % 4] = True
		
		return retval
	
	def generate_rooms(self):
		self.player.set_pos(self.row - 1, self.col - 1)
		print str(self.player.r) + ' ' + str(self.player.c)
	
	def change_room(self, code):
		if code == 0:
			self.player.move_ahead()
		elif code == 1:
			self.player.move_right()
		elif code == 2:
			self.player.move_back()
		else: # code == 3
			self.player.move_left()
		
		print str(self.player.r) + ' ' + str(self.player.c)

class Player:
	# Player's Direction (0: North (default); 1: East; 2: South; 3:West)
	d = NumericProperty(0)

	# Position of player ([row, column] with [0,0] is the most north west)
	r = NumericProperty(0)
	c = NumericProperty(0)
	
	pos = ReferenceListProperty(r, c)

	def __init__(self, r, c):
		self.r = r
		self.c = c
		
		self.d = 0

	def set_pos(self, r, c):
		self.r = r
		self.c = c

	def move_ahead(self):
		if self.d == 0:
			self.r -= 1
		elif self.d == 1:
			self.c += 1
		elif self.d == 2:
			self.r += 1
		elif self.d == 3:
			self.c -= 1
	
	def move_right(self):
		self.d += 1
		self.d %= 4
		
		self.move_ahead()
	
	def move_back(self):
		self.d += 2
		self.d %= 4
		
		self.move_ahead()
	
	def move_left(self):
		self.d -= 1
		self.d %= 4
		
		self.move_ahead()
