from picamera import PiCamera
from time import sleep
from gpiozero import Button

button = Button(17)
button2 = Button(18)

camera = PiCamera()
while True:
  if button.is_pressed:
		camera.start_preview()
		camera.annotate_text = ' Night Vision Enabled '
	if button2.is_pressed:
		camera.stop_preview()
