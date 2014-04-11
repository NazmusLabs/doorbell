# ********** SOURCE CODE FOR DOORBELL MONITOR (ENGR240) ********** #

# ***** DEVICE DESCRIPTION ******
# The Doorbell Monitor records the time at which the doorbell button was pressed and the number of time it was pressed.
# It displays the number of time the button was pressed to the 7-segment display
# It sends an email to the user with the recorded time of the doorbell pressed

# ***** CODE DESCRIPTION *****
# The code is designed to work with the raspberry pi and select Adafruit hardware and associated libraries.
# The doorbell push button is attached to GPIO pin 17. The 7-segment decoder is attached as output
# Each time the push button is pressed, the counter variable count up and system time recorded
# Counter variable is outputted to the 7-segment decoder and email is sent to user with recorded time
# Reset button (input connection to be determined) resets counter to 0, and counter is outputted to 7-segment decoder

# ***** LINKS *****
# Adafruit 7-segment python library on GitHub: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_LEDBackpack/Adafruit_7Segment.py

from sys import path

path.append("/home/pi/doorbell/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack")

#Import statements
import Adafruit_7Segment
import smtplib						#SMTP library: Internet Mail Transfer protocol. Needed for email
import string						#Enables the use of strings in variable
import RPi.GPIO as GPIO				#Enables the use of the input pins (known as GPIO)
import time							#Enables time delays and accessing system clock
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)				#Sets pin 17 as an input pin

#Variable declarations
prev_input = 0
count = 1
ada7_ctl = Adafruit_7Segment.SevenSegment()
input = GPIO.input(17)
clear = GPIO.input(16)

while True:
	while ( not GPIO.input(16)):
			if ((not prev_input) and input):
					print (count)
					for n in (0,1,3,4):
					ada7_ctl.writeDigit(n, count, False)
					count = count +1
					
					#The following snippet is the code for using the SMTP library, taken from http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
					#It has been modified to work with gmail as outgoing server, courtesy of information provided in http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/
					#I have modified the snippet and added a few lines of code to fit our specific needs ~Nazmus

					SUBJECT = "Doorbell Monitor Notification"
					TO = "nazmus@outlook.com"
					FROM = "exosphir@gmail.com"
					text = "Someone rang your doorbell at " + time.strftime('%Y-%m-%d %H:%M:%S') + "."
					#Leave the following BODY block intact. Only change the values above.
					BODY = string.join((
						"From: %s" % FROM,
						"To: %s" % TO,
						"Subject: %s" % SUBJECT ,
						"",
						text
						), "\r\n")
					server = smtplib.SMTP('smtp.gmail.com', 587)
					server.ehlo()
					server.starttls()
					server.ehlo()
					server.login('exosphir@gmail.com', 'saieblaquriihphg')
					server.sendmail(FROM, [TO], BODY)
					server.close()
					#End of code snippet
					
			prev_input = input
			time.sleep(0.05)
	count = 1
	prev_input = 0
	Adafruit_7Segment.LEDBackpack().clear()	


#for n in (0, 1, 3, 4):
#    ada7_ctl.writeDigit(n, 6, False)
#
#ada7_ctl.setColon(False)
#
#time.sleep(0.5)
#
#ada7_ctl.setColon(True)
#
#
#time.sleep(0.5)
#
#Adafruit_7Segment.LEDBackpack().clear()