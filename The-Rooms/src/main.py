from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Callback, Color, Rectangle
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from manager import ImageManager
from model import Back, Lamp, Navigator

# Root of app's UI
class TheRoomsGame(Widget):
	imageManager = ImageManager()

	xScale = NumericProperty(1.0)
	yScale = NumericProperty(1.0)
	
	fontSize = NumericProperty(64.0)
	
	navi = ObjectProperty(None)
	
	back = ObjectProperty(None)
	
	leftDoor = ObjectProperty(None)
	centerDoor = ObjectProperty(None)
	RightDoor = ObjectProperty(None)
	
	leftLamp = ObjectProperty(None)
	centerLamp = ObjectProperty(None)
	RightLamp = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super(TheRoomsGame, self).__init__(**kwargs)
		
		self.navi.set_base(self.imageManager.navigatordir, 700.0, 525.0)
		
		self.back.set_base(self.imageManager.backdir, 350.0, 0.0)

		self.leftDoor.set_base(self.imageManager.leftdoordir, 45.0, 25.0)
		self.centerDoor.set_base(self.imageManager.centerdoordir, 325.0, 102.0)
		self.rightDoor.set_base(self.imageManager.rightdoordir, 640.0, 27.0)
		
		self.leftLamp.set_base(self.imageManager.leftlampdir, 80.0, 437.5)
		self.centerLamp.set_base(self.imageManager.centerlampdir, 375.0, 410.0)
		self.rightLamp.set_base(self.imageManager.rightlampdir, 668.0, 437.5)
	
	def take_scale(self):
		retval = False

		xScale = self.width * 1.0 / self.imageManager.roomwidth
		yScale = self.height * 1.0 / self.imageManager.roomheight

		if self.xScale != xScale:
			self.xScale = xScale
			retval = True
		if self.yScale != yScale:
			self.yScale = yScale
			retval = True
		
		return retval
	
	def update(self, dt):
		self.take_scale()
		
		self.fontSize = 64.0 * self.yScale * 1.2
		
		self.navi.update(self.xScale, self.yScale)
		
		self.back.update(self.xScale, self.yScale)
		
		self.leftDoor.update(self.xScale, self.yScale)
		self.centerDoor.update(self.xScale, self.yScale)
		self.rightDoor.update(self.xScale, self.yScale)
		
		self.leftLamp.update(self.xScale, self.yScale)
		self.centerLamp.update(self.xScale, self.yScale)
		self.rightLamp.update(self.xScale, self.yScale)
		
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

# Main app
class TheRoomsApp(App):
	def build(self):
		game = TheRoomsGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Launch app in standalone mode
if __name__ == '__main__':
	TheRoomsApp().run()