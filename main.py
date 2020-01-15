import object
import ocr
import usonic
import online
import offline
import config
import time
import RPi.GPIO as GPIO


def onoff(param):
	if (param == 'online' or param == 'Online'):
		online.run()
	elif (param == 'offline' or param == 'Offline'):
		offline.run()
	else:
		print("Wrong speech mode selection")

def object_callback(channel):
	print("Running object detection")
	object.run()
	onoff(config.onoff)
	GPIO.cleanup()
	time.sleep(2)

def ocr_callback(channel):
	print("Running OCR")
	ocr.run()
	onoff(config.onoff)
	GPIO.cleanup()
	time.sleep(2)

def usonic_callback(channel):
	print("Running ultrasonic")
	usonic.run()
	onoff(config.onoff)
	time.sleep(2)


#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.add_event_detect(11,GPIO.RISING,callback=object_callback, bouncetime=200)
GPIO.add_event_detect(13,GPIO.RISING,callback=ocr_callback, bouncetime=200)
GPIO.add_event_detect(15,GPIO.RISING,callback=usonic_callback, bouncetime=200)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean pull_up_down