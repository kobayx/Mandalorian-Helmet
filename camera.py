from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)

camera = PiCamera()
While True:
	button.wait_for_press()
	camera.start_preview()
	camera.annotate_text = ' Night Vision Enabled '
	button.wait_for_release()
	button.wait_for_press()
	camera.stop_preview()
	button.wait_for_release()
