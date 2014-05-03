from kivy.core.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.widget import Widget

from manager import ImageManager

class Door(Widget):
	pass

class Lamp(Widget):
	# Base values
	WIDTH = 150
	HEIGHT = 50
	
	X_UNIT = 50.0
	Y_UNIT = 50.0
	
	X = 375.0
	Y = 410.0
	
	# Changable values
	state = NumericProperty(1)
	
	texture = ObjectProperty(None)
	
	xUnit = NumericProperty(X_UNIT)
	yUnit = NumericProperty(Y_UNIT)
	
	curr_texture = ObjectProperty(None)
	
	x = NumericProperty(X)
	y = NumericProperty(Y)

	def set_texture(self, texture_id):
		self.texture = Image(texture_id).texture

	def is_pressed(self, x, y):
		if x > self.x and y > self.y:
			if x < self.x + self.xUnit and y < self.y + self.yUnit:
				return True
		return False

	def change_state(self):
		self.state += 1
		self.state %= 3
	
	def update(self, xScale, yScale):
		self.xUnit = self.X_UNIT * xScale
		self.yUnit = self.Y_UNIT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale
		
		self.curr_texture = self.texture.get_region(self.state * self.X_UNIT, 0, self.X_UNIT, self.Y_UNIT)
