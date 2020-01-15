import RPi.GPIO as GPIO
import time
import config


#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
 
GPIO_TRIGGER = 12
GPIO_ECHO = 16
GPIO_TRIGGER_TWO = 18
GPIO_ECHO_TWO = 22
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(GPIO_TRIGGER_TWO, GPIO.OUT)
GPIO.setup(GPIO_ECHO_TWO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distance_two():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_TWO, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_TWO, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_TWO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_TWO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance_two = (TimeElapsed * 34300) / 2
 
    return distance_two
    

def run():

    dist = distance()
    dist_two = distance_two()
    print ("Distance = %.1f cm" % dist)
    print ("Distance = %.1f cm" % dist_two)
    output_file=open(config.localfile,'w')
    output_file.writelines("%.1f to the right" % dist)
    output_file.writelines(", and %.1f to the left" % dist_two)
    output_file.close()
    GPIO.cleanup()