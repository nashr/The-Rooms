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
	
	# Door's textures
	# 1 - Left
	leftdoordir = os.path.join(imgdir, "Door_Left.png")
	leftdoor = Image(leftdoordir).texture
	leftdoorwidth = leftdoor.width
	leftdoorheight = leftdoor.height
	leftdoorx = 45
	leftdoory = 25
	
	# 2 - Center
	centerdoordir = os.path.join(imgdir, "Door_Center.png")
	centerdoor = Image(centerdoordir).texture
	centerdoorwidth = centerdoor.width
	centerdoorheight = centerdoor.height
	centerdoorx = 325
	centerdoory = 102
	
	# 3 - Right
	rightdoordir = os.path.join(imgdir, "Door_Right.png")
	rightdoor = Image(rightdoordir).texture
	rightdoorwidth = rightdoor.width
	rightdoorheight = rightdoor.height
	rightdoorx = 640
	rightdoory = 27
	
	# Lamp's textures
	# 1 - Left

	# 2 - Center
	centerlampdir = os.path.join(imgdir, "Lamp_Center.png")
	centerlamp = Image(centerlampdir).texture

	# 3 - Right
