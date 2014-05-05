from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

from Numeric import *

class Maze:
	# Dimension of maze (row x column)
	row = NumericProperty(0)
	col = NumericProperty(0)

	def __init__(self, row, col):
		self.row = row
		self.col = col
		
		self.rooms = zeros(row * col, Int)
		
		for i in range(len(self.rooms)):
			self.rooms[i] = 1

		self.player = Player(row, col)

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
	
	def move_right(self):
		self.d -= 1
		self.d %= 4
		
		self.move_ahead()
