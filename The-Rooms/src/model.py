from kivy.core.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.widget import Widget

class Arrow(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X_UNIT = NumericProperty(1.0)
	Y_UNIT = NumericProperty(1.0)
	
	X = NumericProperty(1.0)
	Y = NumericProperty(1.0)

	# Run variables
	xUnit = NumericProperty(1.0)
	yUnit = NumericProperty(1.0)
	
	curr_texture = ObjectProperty(None)
	
	x = NumericProperty(1.0)
	y = NumericProperty(1.0)

	def set_base(self, texture_dir, x, y):
		self.TEXTURE = Image(texture_dir).texture
		
		self.WIDTH = self.TEXTURE.width
		self.HEIGHT = self.TEXTURE.height
		
		self.X_UNIT = self.WIDTH / 1
		self.Y_UNIT = self.HEIGHT / 1
		
		self.X = x
		self.Y = y

	def update(self, xScale, yScale):
		self.xUnit = self.X_UNIT * xScale
		self.yUnit = self.Y_UNIT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale
		
		self.curr_texture = self.TEXTURE.get_region(0, 0, self.X_UNIT, self.Y_UNIT)

class Door(Widget):
	pass

class Lamp(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X_UNIT = NumericProperty(1.0)
	Y_UNIT = NumericProperty(1.0)
	
	X = NumericProperty(1.0)
	Y = NumericProperty(1.0)
	
	# Run variables
	state = NumericProperty(1)
	
	xUnit = NumericProperty(1.0)
	yUnit = NumericProperty(1.0)
	
	curr_texture = ObjectProperty(None)
	
	x = NumericProperty(1.0)
	y = NumericProperty(1.0)

	def set_base(self, texture_dir, x, y):
		self.TEXTURE = Image(texture_dir).texture
		
		self.WIDTH = self.TEXTURE.width
		self.HEIGHT = self.TEXTURE.height
		
		self.X_UNIT = self.WIDTH / 3
		self.Y_UNIT = self.HEIGHT / 1
		
		self.X = x
		self.Y = y

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
		
		self.curr_texture = self.TEXTURE.get_region(self.state * self.X_UNIT, 0, self.X_UNIT, self.Y_UNIT)
