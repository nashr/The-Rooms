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
	
	# Arrow's directory
	arrowdir = os.path.join(imgdir, "Arrow.png")
	
	# Door's directories
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
	
	# Lamp's directories
	# 1 - Left
	leftlampdir = os.path.join(imgdir, "Lamp_Left.png")

	# 2 - Center
	centerlampdir = os.path.join(imgdir, "Lamp_Center.png")

	# 3 - Right
	rightlampdir = os.path.join(imgdir, "Lamp_Right.png")
