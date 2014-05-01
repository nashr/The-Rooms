from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

from manager import ImageManager

# Root of app's UI
class TheRoomsGame(Widget):
	imageManager = ImageManager()

	xScale = NumericProperty(1.0)
	yScale = NumericProperty(1.0)
	
	def init_scale(self):
		self.xScale = self.width * 1.0 / self.imageManager.roomwidth
		self.yScale = self.height * 1.0 / self.imageManager.roomheight
	
	def update(self, dt):
		self.init_scale()

# Main app
class TheRoomsApp(App):
	def build(self):
		game = TheRoomsGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Launch app in standalone mode
if __name__ == '__main__':
	TheRoomsApp().run()