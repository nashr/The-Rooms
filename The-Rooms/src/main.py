from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Callback, Color, Rectangle
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from manager import ImageManager
from model import Lamp

# Root of app's UI
class TheRoomsGame(Widget):
	imageManager = ImageManager()

	xScale = NumericProperty(1.0)
	yScale = NumericProperty(1.0)
	
	leftLamp = ObjectProperty(None)
	centerLamp = ObjectProperty(None)
	RightLamp = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super(TheRoomsGame, self).__init__(**kwargs)
		
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
		
		self.leftLamp.update(self.xScale, self.yScale)
		self.centerLamp.update(self.xScale, self.yScale)
		self.rightLamp.update(self.xScale, self.yScale)
		
	def on_touch_down(self, touch):
		pass
	
	def on_touch_move(self, touch):
		pass
	
	def on_touch_up(self, touch):
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