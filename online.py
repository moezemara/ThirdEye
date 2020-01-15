#import sys
import voicerss_tts
import pyglet
#import argparse
import config


def run():

    #parser = argparse.ArgumentParser(description='Sentence to translate')
    #parser.add_argument("--src")
    #args = parser.parse_args()
    #src = args.src

    with open (config.localfile, "r") as myfile:
        src=myfile.readlines()

    voice = voicerss_tts.speech({
        'key': config.voicersskey,
        'hl': config.voicelanguage,
        'src': src,
        'r': config.onlinespeed,
        'c': config.audiocodec,
        'f': config.audioformat
    })

    newFile = open ("voicerss."+config.audiocodec, "wb")
    newFile.write(voice['response'])
    newFile.close()

    #play
    music = pyglet.resource.media('voicerss.'+config.audiocodec)
    music.play()

    def exiter(dt):
        pyglet.app.exit()

    print ("Audio length is: %f" % music.duration)
   
    duration = music.duration + 3
    pyglet.clock.schedule_once(exiter, duration)
    pyglet.app.run()
    print ("Done")