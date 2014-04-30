#Import modules
import RPi.GPIO as GPIO
import time
from sys import path
path.append("/home/pi/doorbell/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack")
import Adafruit_7Segment
import Adafruit_LEDBackpack

#Set-up and variables
GPIO.setmode (GPIO.BCM)
GPIO.setup (17,GPIO.IN)
GPIO.setup (22,GPIO.IN)
display = Adafruit_7Segment.SevenSegment()
reset = Adafruit_LEDBackpack.LEDBackpack()
count = 0
dig_1 = 0
dig_2 = 0
dig_3 = 0
dig_4 = 0
wait = 0
pause = 0
holdReset = 0
quit = 0
display.writeDigit(4, 0, False)

while (quit == 0):
        if wait == 0:
                if (GPIO.input(17)):
                    dig_1 += 1
                    
                    if dig_1 > 9:
                            dig_1 = 0
                            dig_2 += 1

                            if dig_2 > 9:
                                    dig_2 = 0
                                    dig_3 += 1
                                    
                                    if dig_3 > 9:
                                            dig_3 = 0
                                            dig_4 += 1
                                            
                                            display.writeDigit(0, dig_4, False)
                                    display.writeDigit(1, dig_3, False)              
                            display.writeDigit(3, dig_2, False)
                    display.writeDigit(4, dig_1, False)

                    wait = 1
                    pause = time.time()
        
        if time.time() > pause + .05:
                wait = 0
        
        if (GPIO.input(22)):
                display.writeDigitRaw(3, 0)
                display.writeDigitRaw(1, 0)
                display.writeDigitRaw(0, 0)
                dig_1 = 0
                dig_2 = 0
                dig_3 = 0
                dig_4 = 0
                display.writeDigit(4, 0, False)
				
				holdReset = time.time()
				while (GPIO.input(22)):
					if time.time() > holdReset + 5
						quit = 1

GPIO.cleanup()		#Cleans up GPIO on exit
