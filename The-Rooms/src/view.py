from kivy.animation import Animation
from kivy.core.image import Image
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

import kivy.uix.image

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

	def is_pressed(self, x, y):
		if x > self.x and y > self.y:
			if x < self.x + self.width and y < self.y + self.height:
				return True
		return False

	def update(self, xScale, yScale):
		self.width = self.WIDTH * xScale
		self.height = self.HEIGHT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale

class Bomb(Widget):
	# Base variables
	DIR = StringProperty('')
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
		self.DIR = texture_dir
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

class Menu(Widget):
	# Run variables
	fontSize = NumericProperty(64.0)

	width = NumericProperty(1.0)
	height = NumericProperty(1.0)
	
	centerX = NumericProperty(0.0)
	centerY = NumericProperty(0.0)
	
	name = StringProperty('')

	def set_base(self, game):
		self.game = game
		self.name = game.name

	def update(self, width, height, fontSize):
		self.width = width
		self.height = height
		
		self.centerX = width * 1.0 / 2
		self.centerY = height * 1.0 / 2
		
		self.fontSize = fontSize
	
	def edit_name(self):
		content = TextInput(text = self.name, font_size = self.fontSize * .4, multiline = False, padding = (2, 0))
		popup = Popup(title = 'Input new name:', content = content, size_hint = (None, None), size = (self.width / 2, self.height / 5))
		popup.bind(on_dismiss = self.update_name)
		
		popup.open()

	def update_name(self, instance):
		self.name = instance.content.text
		self.game.name = self.name

	def play(self):
		self.game.play()

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
		self.xUnit = self.X_UNIT * xScale
		self.yUnit = self.Y_UNIT * yScale
		
		self.x = self.X * xScale
		self.y = self.Y * yScale
		
		self.curr_texture = self.TEXTURE.get_region(0, 0, self.X_UNIT, self.Y_UNIT)

class Plant(Widget):
	# Base variables
	DIR = StringProperty('')
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
		self.DIR = texture_dir
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

class Room(Widget):
	# Base variables
	TEXTURE = ObjectProperty(None)
	
	WIDTH = NumericProperty(1.0)
	HEIGHT = NumericProperty(1.0)
	
	X = NumericProperty(0.0)
	Y = NumericProperty(0.0)

	# Run variables
	width = NumericProperty(1.0)
	height = NumericProperty(1.0)

	fontSize = NumericProperty(64.0)

	n_room = NumericProperty(0)

	n_bomb = NumericProperty(0)

	# Children (by default)
	nBomb = ObjectProperty(None)

	navi = ObjectProperty(None)
	
	back = ObjectProperty(None)
	
	leftDoor = ObjectProperty(None)
	centerDoor = ObjectProperty(None)
	RightDoor = ObjectProperty(None)
	
	leftLamp = ObjectProperty(None)
	centerLamp = ObjectProperty(None)
	RightLamp = ObjectProperty(None)
	
	plant = ObjectProperty(None)
	
	pause = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(Room, self).__init__(**kwargs)
		
		# Define transitions
		# 1 - Out once
		self.transOut = Animation(opacity = 0) + Animation(opacity = 1)
		self.transOut.bind(on_progress = self.remove_all_children)
		
		self.received = False

	def remove_all_children(self, anim, widget, progress):
		if progress > 0.5 and progress < 0.51:
			self.received = False
			self.n_room = 0
			self.roomProperty = [-1, -1, -1, -1, -1, -1]

			self.clear_widgets()

			self.game.home()

	def set_base(self, game):
		self.game = game

		# Get resources
		self.imageManager = ImageManager()
		
		# Set background
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

		self.plant.set_base(self.imageManager.plantdir, 368.0, 268.0)
		
		self.bomb = Bomb()
		self.bomb.set_base(self.imageManager.bombdir, 368.0, 268.0)

		# Is there a door (at) [ahead, right, back, left]
		# Code: -1: no door; 0: door with green light; 1: door with grey light; 2: door with red light
		# and [number of bombs nearby, plant direction]
		# Code: -1: data not available; 0..n: number of bombs or direction of arrow
		self.roomProperty = [-1, -1, -1, -1, -1, -1]
		
		self.remove_widget(self.nBomb)
		self.remove_widget(self.navi)
		self.remove_widget(self.back)
		self.remove_widget(self.leftDoor)
		self.remove_widget(self.centerDoor)
		self.remove_widget(self.rightDoor)
		self.remove_widget(self.leftLamp)
		self.remove_widget(self.centerLamp)
		self.remove_widget(self.rightLamp)
		self.remove_widget(self.plant)
		self.remove_widget(self.pause)

	def set_room(self, property):
		for i in range(6):
			if self.roomProperty[i] != property[i]:
				if self.roomProperty[i] == -1:
					if i == 0:
						self.add_widget(self.centerDoor)
						self.add_widget(self.centerLamp)

						self.centerLamp.state = property[i]
					elif i == 1:
						self.add_widget(self.rightDoor)
						self.add_widget(self.rightLamp)

						self.rightLamp.state = property[i]
					elif i == 2:
						self.add_widget(self.back)
					elif i == 3:
						self.add_widget(self.leftDoor)
						self.add_widget(self.leftLamp)

						self.leftLamp.state = property[i]
					elif i == 4:
						self.add_widget(self.nBomb)
						self.n_bomb = property[i]
					else: # i == 5
						self.add_widget(self.navi)
						self.navi.angle = property[i]
				elif property[i] == -1:
					if i == 0:
						self.remove_widget(self.centerDoor)
						self.remove_widget(self.centerLamp)
					elif i == 1:
						self.remove_widget(self.rightDoor)
						self.remove_widget(self.rightLamp)
					elif i == 2:
						self.remove_widget(self.back)
					elif i == 3:
						self.remove_widget(self.leftDoor)
						self.remove_widget(self.leftLamp)
					elif i == 4:
						self.remove_widget(self.nBomb)
					else: # i == 5
						self.add_widget(self.plant)
						self.remove_widget(self.navi)
				else:
					if i == 0:
						self.centerLamp.state = property[i]
					elif i == 1:
						self.rightLamp.state = property[i]
					elif i == 2:
						pass
					elif i == 3:
						self.leftLamp.state = property[i]
					elif i == 4:
						self.n_bomb = property[i]
					else: # i == 5
						self.navi.angle = property[i]

				self.roomProperty[i] = property[i]
		
		self.n_room += 1
		if self.n_room == 1:
			self.add_widget(self.pause)

	def update(self, xScale, yScale, fontSize, gameOver):
		self.width = self.WIDTH * xScale
		self.height = self.HEIGHT * yScale
		
		self.navi.update(xScale, yScale)
		
		self.plant.update(xScale, yScale)
		
		if self.roomProperty[0] > -1:
			self.centerDoor.update(xScale, yScale)
			self.centerLamp.update(xScale, yScale)
		
		if self.roomProperty[1] > -1:
			self.rightDoor.update(xScale, yScale)
			self.rightLamp.update(xScale, yScale)
		
		if self.roomProperty[2] > -1:
			self.back.update(xScale, yScale)
		
		if self.roomProperty[3] > -1:
			self.leftDoor.update(xScale, yScale)
			self.leftLamp.update(xScale, yScale)
		
		self.fontSize = fontSize
		
		if gameOver == 1 and not self.received: # Win
			self.received = True
			content = BoxLayout(orientation = 'vertical')

			image = kivy.uix.image.Image(source = self.plant.DIR)
			menu = Button(text = 'Menu', font_size = self.fontSize * .4)
			
			content.add_widget(image)
			content.add_widget(menu)

			popup = Popup(title = 'Congratulation!\nYou found the plant!', content = content, size_hint = (.3, .5), auto_dismiss = False)
			
			menu.bind(on_press = popup.dismiss)
			popup.bind(on_dismiss = self.stop_game)
			
			popup.open()
		elif gameOver == -1 and not self.received: # Lose
			self.received = True
			content = BoxLayout(orientation = 'vertical')

			image = kivy.uix.image.Image(source = self.bomb.DIR)
			menu = Button(text = 'Menu', font_size = self.fontSize * .4)
			
			content.add_widget(image)
			content.add_widget(menu)

			popup = Popup(title = 'You hit a bomb!', content = content, size_hint = (.3, .5), auto_dismiss = False)
			
			menu.bind(on_press = popup.dismiss)
			popup.bind(on_dismiss = self.stop_game)
			
			popup.open()
	
	def stop_game(self, instance):
		self.received = True
		self.transOut.start(self)

	def on_touch_down(self, touch):
		super(Room, self).on_touch_down(touch)

		if self.centerDoor.is_pressed(touch.x, touch.y) and self.roomProperty[0] > -1:
			self.centerDoor.change_state()
		
		if self.rightDoor.is_pressed(touch.x, touch.y) and self.roomProperty[1] > -1:
			self.rightDoor.change_state()

		if self.leftDoor.is_pressed(touch.x, touch.y) and self.roomProperty[3] > -1:
			self.leftDoor.change_state()

		if self.centerLamp.is_pressed(touch.x, touch.y) and self.roomProperty[0] > -1:
			self.centerLamp.change_state()
			self.roomProperty[0] = self.centerLamp.state
			self.game.change_lamp_state(0, self.centerLamp.state)
		
		if self.rightLamp.is_pressed(touch.x, touch.y) and self.roomProperty[1] > -1:
			self.rightLamp.change_state()
			self.roomProperty[1] = self.rightLamp.state
			self.game.change_lamp_state(1, self.rightLamp.state)
		
		if self.leftLamp.is_pressed(touch.x, touch.y) and self.roomProperty[3] > -1:
			self.leftLamp.change_state()
			self.roomProperty[3] = self.leftLamp.state
			self.game.change_lamp_state(3, self.leftLamp.state)

	def on_touch_move(self, touch):
		super(Room, self).on_touch_move(touch)
	
	def on_touch_up(self, touch):
		super(Room, self).on_touch_up(touch)

		if self.centerDoor.is_pressed(touch.x, touch.y) and self.roomProperty[0] > -1:
			self.centerDoor.change_state()
			self.game.go(0)
		
		if self.rightDoor.is_pressed(touch.x, touch.y) and self.roomProperty[1] > -1:
			self.rightDoor.change_state()
			self.game.go(1)

		if self.back.is_pressed(touch.x, touch.y) and self.roomProperty[2] > -1:
			self.game.go(2)

		if self.leftDoor.is_pressed(touch.x, touch.y) and self.roomProperty[3] > -1:
			self.leftDoor.change_state()
			self.game.go(3)
