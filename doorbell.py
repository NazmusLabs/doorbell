import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

prev_input = 0
count = 1

while True:
        input = GPIO.input(17)
        if ((not prev_input) and input):
                print (count)
                count = count +1
        prev_input = input
        time.sleep(0.05)
