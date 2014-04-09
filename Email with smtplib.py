import smtplib
import string
import time    


#The following snippet is taken from http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
#The snippet uses the SMTP library that needs to be downloaded into the raspberry pi if it's not done so already for the code to work
#I have modified the snippet and added a few lines of code to fit our specific needs ~Nazmus
SUBJECT = "Doorbell Monitor Notification"
TO = "nshuddha@hotmail.com"
FROM = "nazmus@outlook.com"
text = "Someone rang your doorbell at" + time.strftime('%Y-%m-%d %H:%M:%S') + "."
#Leave the following BODY block intact. Only change the values above.
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()
#End of code snippet