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


#Import modules
import RPi.GPIO as GPIO		#Enables the use of the input pins (GPIO)
import time			#Enables time delays and accessing system clock
import urllib2
import smtplib			#SMTP library: Internet Mail Transfer protocol. Needed for email
import string			#Enables the use of strings in variable
from sys import path
path.append("/home/pi/doorbell/Adafruit-Raspberry-Pi-Python-Code/Adafruit_LEDBackpack")
import Adafruit_7Segment
import Adafruit_LEDBackpack

#Set-up and variables
GPIO.setmode (GPIO.BCM)
GPIO.setup (17,GPIO.IN)		#Sets pin 17 as an input pin (Used for doorbell push button)
GPIO.setup (22,GPIO.IN)		#Sets pin 22 as an input pin (Used for reset button)
display = Adafruit_7Segment.SevenSegment()
reset = Adafruit_LEDBackpack.LEDBackpack()
count = 0
dig_1 = 0
dig_2 = 0
dig_3 = 0
dig_4 = 0
wait = 0
stop = 0
pause = 0
display.writeDigit(4, 0, False)

def internet_on():
        try:
                response=urllib2.urlopen('http://74.125.228.100', timeout=1)
                return True
        except urllib2.URLError as err: pass
        return False
        
def send_email():\
#The following snippet is the code for using the SMTP library, taken from http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
#It has been modified to work with gmail as outgoing server, courtesy of information provided in http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/
#The function makes use of an external text file which contain email account information, including username and password (or application specefic password if two-step authentication is enabled)
#Please see documentation for information on how to set up the config file. You may also refer to the dedicated text file avilable on this program directory

        configFile = open('c:\users\NazmusShakib\Desktop\doorbell_config.txt','r')	#IMPORTANT: Replace this directory to the directory where the doorbell_config.txt file is located
        lineCount = 0
        for line in configFile:
                lineCount = lineCount + 1

                if lineCount == 1:
                        FROM = line
                elif lineCount == 2:
                        TO = line
                elif lineCount == 3:
                        USERNAME = line
                elif lineCount == 4:
                        PASSWORD = line
                else:
                        print "ERROR: line count of doorbell_config.txt exceeds standard bounds. Make sure the doorbell_config.txt is formatted exactly as specified. Please see \"How to    setup doorbell_config.txt\" for instructions. Line count = " + lineCount + "."
        
        lineCount = 0
        configFile.close()

        SUBJECT = "Doorbell Monitor Notification"
        text = "Someone rang your doorbell at " + time.strftime('%Y-%m-%d %H:%M:%S') + "."
        #Leave the following BODY block intact. Only change the values above.
        BODY = string.join((
	       "From: %s" % FROM,
	       "To: %s" % TO,
	       "Subject: %s" % SUBJECT ,
	       "",
	       text
	       ), "\r\n")
        try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
        except smtplib.SMTPServerDisconnected:
                print "Connection timed out:"
                return False
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME, PASSWORD)
        server.sendmail(FROM, [TO], BODY)
        server.close()

while stop == 0:		#The program will continuously loop until the user invokes the Hardware Stop button, wich turns the "stop" variable to 1
        if wait == 0:		#Time Delay (See documentation)
        	#The following code will set the seven-segment display
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
	#This controls the time delay
                    wait = 1
                    pause = time.time()
                    if internet_on() is True:
                        send_email()
        
        if time.time() > pause + 10:
                wait = 0
        
        #This code runs if the reset button is pushed
        if (GPIO.input(22)):
                display.writeDigitRaw(3, 0)
                display.writeDigitRaw(1, 0)
                display.writeDigitRaw(0, 0)
                dig_1 = 0
                dig_2 = 0
                dig_3 = 0
                dig_4 = 0
                display.writeDigit(4, 0, False)
                
                wait = 0	#Resets time delay
                
                #Kill switch: Hold reset for 5s
                holdReset = time.time()
                while (GPIO.input(22)):
                        if time.time() > holdReset + 5:
                                print "Program Ended"
                                stop = 1
