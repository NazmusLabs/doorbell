#Import modules
import RPi.GPIO as GPIO
import time
import urllib2
import smtplib
import string
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
stop = 0
pause = 0
display.writeDigit(4, 0, False)

def internet_on():
        try:
                response=urllib2.urlopen('http://74.125.228.100', timeout=1)
                return True
        except urllib2.URLError as err: pass
        return False
        
def send_email():
        configFile = open('c:\users\NazmusShakib\Desktop\doorbell config.txt','r')
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

while stop == 0:
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
                    if internet_on() is True:
                        send_email()
        
        if time.time() > pause + 10:
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
                
                #Kill switch: Hold reset for 5s
                holdReset = time.time()
                while (GPIO.input(22)):
                        if time.time() > holdReset + 5:
                                print "Program Ended"
                                stop = 1
