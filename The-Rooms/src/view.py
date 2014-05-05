from kivy.core.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.widget import Widget

from manager import ImageManager

class Back(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X = NumericProperty(1.0)
	Y = NumericProperty(1.0)

	# Run variables
	width = NumericProperty(1.0)
	height = NumericProperty(1.0)
	
	x = NumericProperty(1.0)
	y = NumericProperty(1.0)

	def set_base(self, texture_dir, x, y):
		self.TEXTURE = Image(texture_dir).texture
		
		self.WIDTH = self.TEXTURE.width
		self.HEIGHT = self.TEXTURE.height
		
		self.X = x
		self.Y = y

	def update(self, xScale, yScale):
		self.width = self.WIDTH * xScale
		self.height = self.HEIGHT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale

class Door(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X_UNIT = NumericProperty(1.0)
	Y_UNIT = NumericProperty(1.0)
	
	X = NumericProperty(1.0)
	Y = NumericProperty(1.0)
	
	# Run variables
	state = NumericProperty(0)
	
	xUnit = NumericProperty(1.0)
	yUnit = NumericProperty(1.0)
	
	curr_texture = ObjectProperty(None)
	
	x = NumericProperty(1.0)
	y = NumericProperty(1.0)

	def set_base(self, texture_dir, x, y):
		self.TEXTURE = Image(texture_dir).texture
		
		self.WIDTH = self.TEXTURE.width
		self.HEIGHT = self.TEXTURE.height
		
		self.X_UNIT = self.WIDTH / 2
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
		self.state %= 2
	
	def update(self, xScale, yScale):
		self.xUnit = self.X_UNIT * xScale
		self.yUnit = self.Y_UNIT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale
		
		self.curr_texture = self.TEXTURE.get_region(self.state * self.X_UNIT, 0, self.X_UNIT, self.Y_UNIT)

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

class Navigator(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X_UNIT = NumericProperty(1.0)
	Y_UNIT = NumericProperty(1.0)
	
	X = NumericProperty(1.0)
	Y = NumericProperty(1.0)

	# Run variables
	angle = NumericProperty(0.0)
	
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
		self.angle += 1.0
		self.angle %= 360.0

		self.xUnit = self.X_UNIT * xScale
		self.yUnit = self.Y_UNIT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale
		
		self.curr_texture = self.TEXTURE.get_region(0, 0, self.X_UNIT, self.Y_UNIT)

class Room(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X = NumericProperty(1.0)
	Y = NumericProperty(1.0)

	# Run variables
	width = NumericProperty(1.0)
	height = NumericProperty(1.0)
	
	x = NumericProperty(1.0)
	y = NumericProperty(1.0)

	# Children (by default)
	navi = ObjectProperty(None)
	
	back = ObjectProperty(None)
	
	leftDoor = ObjectProperty(None)
	centerDoor = ObjectProperty(None)
	RightDoor = ObjectProperty(None)
	
	leftLamp = ObjectProperty(None)
	centerLamp = ObjectProperty(None)
	RightLamp = ObjectProperty(None)

	def set_base(self):
		# Get resources
		self.imageManager = ImageManager()
		
		self.TEXTURE = Image(self.imageManager.roomdir).texture
		
		self.WIDTH = self.TEXTURE.width
		self.HEIGHT = self.TEXTURE.height
		
		self.X = 0.0
		self.Y = 0.0

		# Instantiate children
		self.navi.set_base(self.imageManager.navigatordir, 700.0, 525.0)
		
		self.back.set_base(self.imageManager.backdir, 350.0, 0.0)

		self.leftDoor.set_base(self.imageManager.leftdoordir, 45.0, 25.0)
		self.centerDoor.set_base(self.imageManager.centerdoordir, 325.0, 102.0)
		self.rightDoor.set_base(self.imageManager.rightdoordir, 640.0, 27.0)
		
		self.leftLamp.set_base(self.imageManager.leftlampdir, 80.0, 437.5)
		self.centerLamp.set_base(self.imageManager.centerlampdir, 375.0, 410.0)
		self.rightLamp.set_base(self.imageManager.rightlampdir, 668.0, 437.5)

	def update(self, xScale, yScale):
		self.width = self.WIDTH * xScale
		self.height = self.HEIGHT * yScale
		
		self.navi.update(xScale, yScale)
		
		self.back.update(xScale, yScale)
		
		self.leftDoor.update(xScale, yScale)
		self.centerDoor.update(xScale, yScale)
		self.rightDoor.update(xScale, yScale)
		
		self.leftLamp.update(xScale, yScale)
		self.centerLamp.update(xScale, yScale)
		self.rightLamp.update(xScale, yScale)

	def on_touch_down(self, touch):
		pass
	
	def on_touch_move(self, touch):
		pass
	
	def on_touch_up(self, touch):
		if self.leftDoor.is_pressed(touch.x, touch.y):
			self.leftDoor.change_state()

		if self.centerDoor.is_pressed(touch.x, touch.y):
			self.centerDoor.change_state()
		
		if self.rightDoor.is_pressed(touch.x, touch.y):
			self.rightDoor.change_state()

		if self.leftLamp.is_pressed(touch.x, touch.y):
			self.leftLamp.change_state()

		if self.centerLamp.is_pressed(touch.x, touch.y):
			self.centerLamp.change_state()
		
		if self.rightLamp.is_pressed(touch.x, touch.y):
			self.rightLamp.change_state()
