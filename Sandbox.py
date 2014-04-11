import os #needed to work with relative paths
import linecache #Information about linechache courtesy of http://python.about.com/od/simplerscripts/qt/Getlinebynumber.htm

#The next three lines of code are courtesy of user "Russ" from http://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "config_path.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#configPathFile = open(abs_file_path, 'r')

configPath = linecache.getline(abs_file_path,1)

#configPath.close()

print configPath

configFile = open(configPath, 'r')

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

print FROM
print TO
print USERNAME
print PASSWORD

configFile.close()
