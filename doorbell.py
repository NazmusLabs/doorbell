# ********** SOURCE CODE FOR DOORBELL MONITOR (ENGR240) ********** #

# ***** DEVICE DESCRIPTION ******
# The Doorbell Monitor records the time at which the doorbell button was pressed and the number of time it was pressed.
# It displays the number of time the button was pressed to the 7-segment display
# It sends an email to the user with the recorded time of the doorbell pressed

# ***** CODE DESCRIPTION *****
# The code is designed to work with the raspberry pi and select Adafruit hardware and associated libraries.
# The doorbell push button is attached to GPIO pin 17. The 7-segment decoder is attatched as output
# Each time the push button is pressed, the counter variable count up and system time recorded
# Counter variable is outputted to the 7-segment decoder and email is sent to user with recorded time
# Reset button (input connection to be determined) resets counter to 0, and counter is outputted to 7-segment decoder

from sys import path

path.append("/home/pi/doorbell/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack")


import Adafruit_7Segment


import RPi.GPIO as GPIO				#Enables the use of the input pins (known as GPIO)
import time							#Enables time delays and accessing system clock
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)				#Sets pin 17 as an input pin

prev_input = 0
count = 1

while True:
        input = GPIO.input(17)
        if ((not prev_input) and input):
                print (count)
                count = count +1
        prev_input = input
        time.sleep(0.05)

ada7_ctl = Adafruit_7Segment.SevenSegment()

for n in (0, 1, 3, 4):
    ada7_ctl.writeDigit(n, 6, False)

ada7_ctl.setColon(False)

time.sleep(0.5)

ada7_ctl.setColon(True)


time.sleep(0.5)

Adafruit_7Segment.LEDBackpack().clear()
