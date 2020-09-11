import re

error = r"ERROR"
info = r"INFO"

file = open("syslog.log","r")
file2 = open("errorlogs.log","w+") # create a file for error logs
file3 = open("infologs.log","w+")  # create a file for info logs

for line in file:
    if re.search(error, line):
        file2.write(line)
    elif re.search(info, line):
        file3.write(line)
file.close()
file2.close()
file3.close()