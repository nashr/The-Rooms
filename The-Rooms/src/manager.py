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
	roomwidth = room.width
	roomheight = room.height
	
	# Arrow's directories
	# 1 - Navigator
	navigatordir = os.path.join(imgdir, "Arrow.png")
	
	# 2 - Back
	backdir = os.path.join(imgdir, "Back.png")
	
	# Door's directories
	# 1 - Left
	leftdoordir = os.path.join(imgdir, "Door_Left.png")
	
	# 2 - Center
	centerdoordir = os.path.join(imgdir, "Door_Center.png")
	
	# 3 - Right
	rightdoordir = os.path.join(imgdir, "Door_Right.png")
	
	# Lamp's directories
	# 1 - Left
	leftlampdir = os.path.join(imgdir, "Lamp_Left.png")

	# 2 - Center
	centerlampdir = os.path.join(imgdir, "Lamp_Center.png")

	# 3 - Right
	rightlampdir = os.path.join(imgdir, "Lamp_Right.png")
