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
	
	centerLamp = Lamp(imageManager.centerlamp)
	
	def __init__(self, **kwargs):
		super(TheRoomsGame, self).__init__(**kwargs)
		
		self.texture = self.imageManager.room
		self.texture_size = {800, 600}

		# create the graphics
		with self.canvas:
			Color(.5, .5, .5)
			self.rect_bg = Rectangle(pos=self.pos, size=self.size)
			Color(1, 1, 1)
			cx = self.center_x - 800 / 2.
			cy = self.center_y - 600 / 2.
			self.rect_text = Rectangle(texture=self.texture, pos=(cx, cy), size=self.texture_size)
			
		self.bind(pos=self.update_graphics_pos, size=self.update_graphics_size)
		
	def update_graphics_pos(self, instance, value):
		print 'KOKOKOKO'
		self.rect_bg.pos = value
		cx = self.center_x - 800 / 2.
		cy = self.center_y - 600 / 2.
		self.rect_text.pos = cx, cy

	def update_graphics_size(self, instance, value):
		self.rect_bg.size = value
		cx = self.center_x - 800 / 2.
		cy = self.center_y - 600 / 2.
		self.rect_text.pos = cx, cy
	
	def init_scale(self):
		self.xScale = self.width * 1.0 / self.imageManager.roomwidth
		self.yScale = self.height * 1.0 / self.imageManager.roomheight
	
	def update(self, dt):
		self.init_scale()
		
	def on_touch_down(self, touch):
		self.update_graphics_pos(self.rect_bg, [50, 50])
	
	def on_touch_move(self, touch):
		pass
	
	def on_touch_up(self, touch):
		if self.centerLamp.is_pressed(touch.x / self.xScale, touch.y / self.yScale):
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