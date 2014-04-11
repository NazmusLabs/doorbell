********** DOORBELL MONITOR (V 1.0) README ********** #

Project by: Kendall Knapp and Nazmus Shakib Khandaker

***** DEVICE DESCRIPTION ******
The Doorbell Monitor records the time at which the doorbell button was pressed and the number of time it was pressed.
It displays the number of time the button was pressed to the 7-segment display
It sends an email to the user with the recorded time of the doorbell pressed

***** CODE DESCRIPTION *****
The code is designed to work with the raspberry pi and select Adafruit hardware and associated libraries.
The doorbell push button is attached to GPIO pin 17. The 7-segment decoder is attached as output
Each time the push button is pressed, the counter variable count up and system time recorded
Counter variable is outputted to the 7-segment decoder and email is sent to user with recorded time
Reset button (input connection to be determined) resets counter to 0, and counter is outputted to 7-segment decoder

***** FILES *****
* Doorbell.py: responsible for the entire device logic operation. This file has all the source code you need
* config_path.txt: this file tells the program where to locate doorbell_config.txt. This file is required for program operation.
* doorbell_config.txt: this file includes sample gmail SMTP information. User should create a new file with the same name and replace the generic values with their specefic ones. The user_created version can be placed anywhere. Just remember to type the path in the config_path.txt file's first line so the program can locate it. doorbell_config.txt is required for the program's operation.
* How to use doorbell_config.txt: This file explains how to format the doorbell_config.txt file properly and provides security and privacy information regarding username and password
* Email with smtplib.py: ohnly includes the code to send email to the user. This code is already included with Doorbell.py. This file is not needed for the operation of the device
* sandox.py: python file solely for testing code. It is not needed for the oporation of the device.

***** LINKS *****
Adafruit 7-segment python library on GitHub: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_LEDBackpack/Adafruit_7Segment.py
SMTP Library info page: http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
Getting SMTP to work with gmail: http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/
