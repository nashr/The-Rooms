from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Maze:
	# Dimension of maze (row x column)
	row = NumericProperty(0)
	col = NumericProperty(0)

	def __init__(self, row, col):
		self.row = row
		self.col = col
		
		# What's inside the room? (0: nothing; 1: bomb; 2: plant)
		self.rooms = []
		
		for i in range(row * col):
			self.rooms.append(0)

		# Room's lamp's current light. (0: green; 1: grey; 2: red)
		self.lights = []
		
		for i in range(row * col):
			self.lights.append(1)

		self.player = Player(-1, -1)

	def load_curr_room_property(self):
		# Is there a door (at) [ahead, right, back, left] and [number of bombs nearby, plant direction]
		# Code: -1: no door; 0: door with green light; 1: door with grey light; 2: door with red light
		retval = [-1, -1, -1, -1, -1, -1]

		if self.player.r == -1: # Only in menu context
			pass
		else: # In game context
			if self.player.r == 0: # The most up rooms
				room_idx = (self.player.r + 1) * self.row + self.player.c
				retval[(2 - self.player.d) % 4] = self.lights[room_idx]
			elif self.player.r == self.row - 1: # The most down rooms
				room_idx = (self.player.r - 1) * self.row + self.player.c
				retval[(0 - self.player.d) % 4] = self.lights[room_idx]
			else: # Middle row rooms
				# Head door
				room_idx = (self.player.r - 1) * self.row + self.player.c
				retval[(0 - self.player.d) % 4] = self.lights[room_idx]
				# Back door
				room_idx = (self.player.r + 1) * self.row + self.player.c
				retval[(2 - self.player.d) % 4] = self.lights[room_idx]
			
			if self.player.c == 0: # The most left rooms
				room_idx = self.player.r * self.row + (self.player.c + 1)
				retval[(1 - self.player.d) % 4] = self.lights[room_idx]
			elif self.player.c == self.col - 1: # The most right rooms
				room_idx = self.player.r * self.row + (self.player.c - 1)
				retval[(3 - self.player.d) % 4] = self.lights[room_idx]
			else: # Middle column rooms
				# Right door
				room_idx = self.player.r * self.row + (self.player.c + 1)
				retval[(1 - self.player.d) % 4] = self.lights[room_idx]
				# Left door
				room_idx = self.player.r * self.row + (self.player.c - 1)
				retval[(3 - self.player.d) % 4] = self.lights[room_idx]

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
	
	def change_lamp(self, code, state):
		room_idx = 0
		if code == 0:
			if self.player.d == 0:
				room_idx = (self.player.r - 1) * self.row + self.player.c
			elif self.player.d == 1:
				room_idx = self.player.r * self.row + (self.player.c + 1)
			elif self.player.d == 2:
				room_idx = (self.player.r + 1) * self.row + self.player.c
			else: # d == 3
				room_idx = self.player.r * self.row + (self.player.c - 1)
		elif code == 1:
			if self.player.d == 0:
				room_idx = self.player.r * self.row + (self.player.c + 1)
			elif self.player.d == 1:
				room_idx = (self.player.r + 1) * self.row + self.player.c
			elif self.player.d == 2:
				room_idx = self.player.r * self.row + (self.player.c - 1)
			else: # d == 3
				room_idx = (self.player.r - 1) * self.row + self.player.c
		elif code == 2:
			if self.player.d == 0:
				room_idx = (self.player.r + 1) * self.row + self.player.c
			elif self.player.d == 1:
				room_idx = self.player.r * self.row + (self.player.c - 1)
			elif self.player.d == 2:
				room_idx = (self.player.r - 1) * self.row + self.player.c
			else: # d == 3
				room_idx = self.player.r * self.row + (self.player.c + 1)
		else: # code == 3
			if self.player.d == 0:
				room_idx = self.player.r * self.row + (self.player.c - 1)
			elif self.player.d == 1:
				room_idx = (self.player.r - 1) * self.row + self.player.c
			elif self.player.d == 2:
				room_idx = self.player.r * self.row + (self.player.c + 1)
			else: # d == 3
				room_idx = (self.player.r + 1) * self.row + self.player.c
		
		self.lights[room_idx] = state

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
