#The following snippet is the code for using the SMTP library, taken from http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
#It has been modified to work with gmail as outgoing server, courtesy of information provided in http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/
#I have modified the snippet and added a few lines of code to fit our specific needs ~Nazmus

import smtplib
import time
import string

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
        print "ERROR: line count of doorbell_config.txt exceeds standard bounds. Make sure the doorbell_config.txt is formatted exactly as specefied. Please see \"How to setup doorbell_config.txt\" for instructions. Line count = " + lineCount + "."
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
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(USERNAME, PASSWORD)
server.sendmail(FROM, [TO], BODY)
server.close()
#End of code snippet
