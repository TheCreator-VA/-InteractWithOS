import re

error = r"ERROR"
file = open("syslog.log","r")
file2 = open("errorlogs.log","w+") # create a file for error logs

for line in file:
    if re.search(error, line):
        file2.write(line)