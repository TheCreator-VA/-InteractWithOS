import re
import operator

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

file2 = open("C:\\Users\\Vansh Arora\\Desktop\\FinalProject\\errorlogs.log","r")

errorPattern = r"^.*(ERROR) (.*) (\(.*\))$"
errorDict = {}                      # Dictionary for error type and count
namepattern = r"^.*(\(.*\))$"   
userlogin_error = {}                # Dictionary for no. of errorlogs corresponding to a username

for line in file2:
    name = re.search(namepattern,line)
    userName = name[1][1:-1]
    if userName not in userlogin_error:
        userlogin_error[userName] = 1
    else:
        userlogin_error[userName] += 1

    errorSearch = re.search(errorPattern,line)
    error = errorSearch[2]
    if error not in errorDict:
        errorDict[error] = 1
    else:
        errorDict[error] += 1

file2.close()

file3 = open("infologs.log","r")

userlogin_info = {}

for line in file3:
    name = re.search(namepattern,line)
    userName = name[1][1:-1]
    if userName not in userlogin_info:
        userlogin2[userName]= 1
    else:
        userlogin_info[userName] += 1

file3.close()