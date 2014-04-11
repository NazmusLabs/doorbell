#The following snippet is the code for using the SMTP library, taken from http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
#It has been modified to work with gmail as outgoing server, courtesy of information provided in http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/
#I have modified the snippet and added a few lines of code to fit our specific needs ~Nazmus

import smtplib
import time
import string

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
