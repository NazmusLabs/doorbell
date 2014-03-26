from sys import path

path.append("/home/pi/doorbell/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack")


import Adafruit_7Segment


#import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN)

#prev_input = 0
#count = 1

#while True:
#        input = GPIO.input(17)
#        if ((not prev_input) and input):
#                print (count)
#                count = count +1
#        prev_input = input
#        time.sleep(0.05)

ada7_ctl = Adafruit_7Segment.SevenSegment()

for n in (0, 1, 3, 4):
    ada7_ctl.writeDigit(n, 6, False)

ada7_ctl.setColon(False)

time.sleep(0.5)

ada7_ctl.setColon(True)


time.sleep(0.5)

Adafruit_7Segment.LEDBackpack().clear()
