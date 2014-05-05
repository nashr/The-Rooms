from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Callback, Color, Rectangle
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from view import Menu, Room

# Root of app's UI
class TheRoomsGame(Widget):
	# Set base values for
	# 1 - scales
	xScale = NumericProperty(1.0)
	yScale = NumericProperty(1.0)
	
	# 2 - font size
	fontSize = NumericProperty(64.0)
	
	# 3 - current state (0: menu; 1: game; 2: gameover)
	state = NumericProperty(0)

	# Child widgets
	menu = ObjectProperty(None)
	room = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super(TheRoomsGame, self).__init__(**kwargs)

		self.menu.set_base(self)
		self.room.set_base(self)

	def take_scale(self):
		retval = False

		xScale = self.width * 1.0 / self.room.WIDTH
		yScale = self.height * 1.0 / self.room.HEIGHT

		if self.xScale != xScale:
			self.xScale = xScale
			retval = True
		if self.yScale != yScale:
			self.yScale = yScale
			retval = True
		
		return retval
	
	def play(self):
		self.remove_widget(self.menu)
		self.state = 1
	
	def update(self, dt):
		self.take_scale()
		
		self.fontSize = 64.0 * self.yScale * 1.2
		
		self.menu.update(self.width, self.height, self.fontSize)
		self.room.update(self.xScale, self.yScale)

# Main app
class TheRoomsApp(App):
	def build(self):
		game = TheRoomsGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Launch app in standalone mode
if __name__ == '__main__':
	TheRoomsApp().run()