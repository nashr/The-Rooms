from kivy.core.image import Image
from kivy.core.window import Window
import os.path

# Parent directory of resources
resdir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), "res")

class ImageManager:
	# Directory of images
	imgdir = os.path.join(resdir, "img")
	
	# Room's texture
	roomdir = os.path.join(imgdir, "Room.png")
	room = Image(roomdir).texture
