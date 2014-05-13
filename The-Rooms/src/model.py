from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

import math, random

class Maze:
	# Dimension of maze (row x column)
	row = NumericProperty(0)
	col = NumericProperty(0)

	def __init__(self, row, col):
		self.row = row
		self.col = col
		
		# What's inside the room? (-1: bomb; >=0: number of bombs in neighbourhood; 9: plant)
		self.rooms = []
		
		for i in range(row * col):
			self.rooms.append(0)

		# Room's lamp's current light. (0: green; 1: grey; 2: red)
		self.lights = []
		
		for i in range(row * col):
			self.lights.append(1)

		self.player = Player(-1, -1)
		self.plant = Plant(-1, -1)

	def load_curr_room_property(self):
		# Is there a door (at) [ahead, right, back, left]
		# Code: -1: no door; 0: door with green light; 1: door with grey light; 2: door with red light
		# and [number of bombs nearby, plant direction]
		# Code: -1: data not available; 0..n: number of bombs or direction of arrow
		retval = [-1, -1, -1, -1, -1, -1]

		if self.player.r == -1: # Only in menu context
			pass
		else: # In game context
			if self.player.r == 0: # The most up rooms
				room_idx = (self.player.r + 1) * self.col + self.player.c
				retval[(2 - self.player.d) % 4] = self.lights[room_idx]
			elif self.player.r == self.row - 1: # The most down rooms
				room_idx = (self.player.r - 1) * self.col + self.player.c
				retval[(0 - self.player.d) % 4] = self.lights[room_idx]
			else: # Middle row rooms
				# Head door
				room_idx = (self.player.r - 1) * self.col + self.player.c
				retval[(0 - self.player.d) % 4] = self.lights[room_idx]
				# Back door
				room_idx = (self.player.r + 1) * self.col + self.player.c
				retval[(2 - self.player.d) % 4] = self.lights[room_idx]
			
			if self.player.c == 0: # The most left rooms
				room_idx = self.player.r * self.col + (self.player.c + 1)
				retval[(1 - self.player.d) % 4] = self.lights[room_idx]
			elif self.player.c == self.col - 1: # The most right rooms
				room_idx = self.player.r * self.col + (self.player.c - 1)
				retval[(3 - self.player.d) % 4] = self.lights[room_idx]
			else: # Middle column rooms
				# Right door
				room_idx = self.player.r * self.col + (self.player.c + 1)
				retval[(1 - self.player.d) % 4] = self.lights[room_idx]
				# Left door
				room_idx = self.player.r * self.col + (self.player.c - 1)
				retval[(3 - self.player.d) % 4] = self.lights[room_idx]
			
			retval[4] = self.rooms[self.player.r * self.col + self.player.c]
			
			angle = 0.0
			if self.player.d == 0 or self.player.d == 2:
				if self.plant.r == self.player.r:
					angle = 90.0
				else:
					angle = math.degrees(math.atan(abs((self.plant.c - self.player.c) * 1.0 / (self.plant.r - self.player.r))))

				if self.plant.r < self.player.r and self.plant.c < self.player.c:
					if self.player.d == 0:
						pass
					else:
						angle += 180.0
				elif self.plant.r < self.player.r and self.plant.c >= self.player.c:
					if self.player.d == 0:
						angle = 360.0 - angle
					else:
						angle = 180.0 - angle
				elif self.plant.r >= self.player.r and self.plant.c >= self.player.c:
					if self.player.d == 0:
						angle += 180.0
					else:
						angle += 360.0
				else:
					if self.player.d == 0:
						angle = 180.0 - angle
					else:
						angle = 360.0 - angle
			else:
				if self.plant.c == self.player.c:
					angle = 90.0
				else:
					angle = math.degrees(math.atan(abs((self.plant.r - self.player.r) * 1.0 / (self.plant.c - self.player.c))))

				if self.plant.r < self.player.r and self.plant.c < self.player.c:
					if self.player.d == 3:
						angle = 360.0 - angle
					else:
						angle = 180.0 - angle
				elif self.plant.r < self.player.r and self.plant.c >= self.player.c:
					if self.player.d == 3:
						angle += 180.0
					else:
						pass
				elif self.plant.r >= self.player.r and self.plant.c >= self.player.c:
					if self.player.d == 3:
						angle = 180.0 - angle
					else:
						angle = 360.0 - angle
				else:
					if self.player.d == 3:
						pass
					else:
						angle += 180.0
			
			if self.plant.r == self.player.r and self.plant.c == self.player.c:
				angle = -1

			retval[5] = angle

		return retval
	
	def generate_rooms(self, row, col):
		self.row = row
		self.col = col

		while len(self.rooms) < row * col:
			self.rooms.append(0)
		
		while len(self.rooms) > row * col:
			self.rooms.pop()

		# Generating bombs
		for i in range(row * col / 4):
			r = random.randint(0, row - 1)
			c = random.randint(0, col - 1)
			while self.rooms[r * col + c] == -1:
				r = random.randint(0, row - 1)
				c = random.randint(0, col - 1)

			for x in [-1, 0, 1]:
				for y in [-1, 0, 1]:
					if x == 0 and y == 0:
						self.rooms[r * col + c] = -1
					elif (r + x) >= 0 and (r + x) < row and (c + y) >= 0 and (c + y) < col:
						if self.rooms[(r + x) * col + (c + y)] != -1:
							self.rooms[(r + x) * col + (c + y)] += 1

		# Generating plant position
		r_plant = random.randint(0, row - 1)
		c_plant = random.randint(0, col - 1)
		while self.rooms[r_plant * col + c_plant] == -1:
			r_plant = random.randint(0, row - 1)
			c_plant = random.randint(0, col - 1)
		
		self.plant.set_pos(r_plant, c_plant)

		# Generating player position
		r = 0
		c = 0

		if r_plant < row / 2:
			r = row - 1

		if c_plant < col / 2:
			c = col - 1

		while self.rooms[r * col + c] == -1:
			if abs(r_plant - r) < abs(c_plant - c):
				c += (c_plant - c) / abs(c_plant - c)
			elif abs(r_plant - r) > abs(c_plant - c):
				r += (r_plant - r) / abs(r_plant - r)
			else:
				if row < col:
					c += (c_plant - c) / abs(c_plant - c)
				else:
					r += (r_plant - r) / abs(r_plant - r)

		self.player.set_pos(r, c)
		
		for i in range(row):
			temp = ''
			for j in range(col):
				if self.rooms[i * col + j] == -1:
					temp += 'B '
				elif i == r_plant and j == c_plant:
					temp += 'X '
				elif i == r and j == c:
					temp += 'O '
				else:
					temp += str(self.rooms[i * col + j]) + ' '
			print temp

	def is_solvable(self):
		pass

	def reset_maze(self):
		self.player.set_pos(-1, -1)

	def change_room(self, code):
		if code == 0:
			self.player.move_ahead()
		elif code == 1:
			self.player.move_right()
		elif code == 2:
			self.player.move_back()
		else: # code == 3
			self.player.move_left()
	
	def change_lamp(self, code, state):
		room_idx = 0
		if code == 0:
			if self.player.d == 0:
				room_idx = (self.player.r - 1) * self.col + self.player.c
			elif self.player.d == 1:
				room_idx = self.player.r * self.col + (self.player.c + 1)
			elif self.player.d == 2:
				room_idx = (self.player.r + 1) * self.col + self.player.c
			else: # d == 3
				room_idx = self.player.r * self.col + (self.player.c - 1)
		elif code == 1:
			if self.player.d == 0:
				room_idx = self.player.r * self.col + (self.player.c + 1)
			elif self.player.d == 1:
				room_idx = (self.player.r + 1) * self.col + self.player.c
			elif self.player.d == 2:
				room_idx = self.player.r * self.col + (self.player.c - 1)
			else: # d == 3
				room_idx = (self.player.r - 1) * self.col + self.player.c
		elif code == 2:
			if self.player.d == 0:
				room_idx = (self.player.r + 1) * self.col + self.player.c
			elif self.player.d == 1:
				room_idx = self.player.r * self.col + (self.player.c - 1)
			elif self.player.d == 2:
				room_idx = (self.player.r - 1) * self.col + self.player.c
			else: # d == 3
				room_idx = self.player.r * self.col + (self.player.c + 1)
		else: # code == 3
			if self.player.d == 0:
				room_idx = self.player.r * self.col + (self.player.c - 1)
			elif self.player.d == 1:
				room_idx = (self.player.r - 1) * self.col + self.player.c
			elif self.player.d == 2:
				room_idx = self.player.r * self.col + (self.player.c + 1)
			else: # d == 3
				room_idx = (self.player.r + 1) * self.col + self.player.c
		
		self.lights[room_idx] = state

class Plant:
	# Position of plant ([row, column] with [0,0] is the most north west)
	r = NumericProperty(0)
	c = NumericProperty(0)
	
	def __init__(self, r, c):
		self.r = r
		self.c = c
	
	def set_pos(self, r, c):
		self.r = r
		self.c = c

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
