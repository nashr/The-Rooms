from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

# Root of app's UI
class TheRoomsGame(Widget):
	def update(self, dt):
		pass

# Main app
class TheRoomsApp(App):
	def build(self):
		game = TheRoomsGame()
		Clock.schedule_interval(game.update, 1.0 / 30.0)
		return game

# Launch app in standalone mode
if __name__ == '__main__':
	TheRoomsApp().run()