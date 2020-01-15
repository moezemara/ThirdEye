import pyttsx3
import config


def run():
	# One time initialization
	engine = pyttsx3.init()

	# Set properties _before_ you add things to say
	engine.setProperty('rate', config.offlinespeed)    # Speed percent (can go over 100)
	engine.setProperty('volume', config.offlinevolume)  # Volume 0-1

	with open (config.localfile, "r") as myfile:
	    src=myfile.readlines()

	# Queue up things to say.
	# There will be a short break between each one
	# when spoken, like a pause between sentences.
	engine.say(src)

	# Flush the say() queue and play the audio
	engine.runAndWait()
	print("Done")