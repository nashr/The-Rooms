from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Callback, Color, Rectangle
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from model import Maze
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

		# Define transitions
		# 1 - Out once
		self.transOut = Animation(opacity = 0)
		self.transOut.bind(on_complete = self.remove)

		# 2 - Inter rooms
		self.transRoom = Animation(opacity = 0, d = 1.5) + Animation(opacity = 1)
		self.transRoom.bind(on_progress = self.prepare_room)
		
		self.menu.set_base(self)
		self.room.set_base(self)
		
		self.maze = Maze(4, 6)
		
		self.room.set_room(self.maze.load_curr_room_property())

	def remove(self, anim, widget):
		widget.parent.remove_widget(widget)

	def prepare_room(self, anim, widget, progress):
		if progress > 0.5 and progress < 0.52:
			self.room.set_room(self.maze.load_curr_room_property())

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
		self.transOut.start(self.menu)

		self.state = 1
		
		self.maze.generate_rooms()
		
		self.transRoom.start(self.room)

	## 
	#  @brief intermethod between input on widget with its logic structure
	#  
	#  @param [in] code move direction (0: ahead; 1: right; 2: back; 3: left)
	#  @return none
	#  
	def go(self, code):
		self.maze.change_room(code)
		self.transRoom.start(self.room)

	def update(self, dt):
		self.take_scale()
		
		self.fontSize = 64.0 * self.yScale * 1.2
		
		self.menu.update(self.width, self.height, self.fontSize)
		self.room.update(self.xScale, self.yScale, self.fontSize)

# Main app
class TheRoomsApp(App):
	def build(self):
		game = TheRoomsGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Launch app in standalone mode
if __name__ == '__main__':
	TheRoomsApp().run()