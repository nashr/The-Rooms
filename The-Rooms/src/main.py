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
	
	centerLamp = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super(TheRoomsGame, self).__init__(**kwargs)
		
		self.centerLamp.set_texture(self.imageManager.centerlampdir)
	
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
		self.centerLamp.update(self.xScale, self.yScale)
		
	def on_touch_down(self, touch):
		pass
	
	def on_touch_move(self, touch):
		pass
	
	def on_touch_up(self, touch):
		if self.centerLamp.is_pressed(touch.x, touch.y):
			self.centerLamp.change_state()

# Main app
class TheRoomsApp(App):
	def build(self):
		game = TheRoomsGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Launch app in standalone mode
if __name__ == '__main__':
	TheRoomsApp().run()