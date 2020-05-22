#!/usr/bin/env python

import os
import datetime

# check if a file with the given name exists  
print(os.path.exists("output.txt"))

# size of file in bytes
print(os.path.getsize("output.txt"))

# timestamp in secs since the files were first created
print(os.path.getatime("output.txt"))

# Timestamp in a more readable format
timestamp = os.path.getmtime("output.txt")
# .getmtime() get time of last modification
# .getatime() last access time
print(datetime.datetime.fromtimestamp(timestamp))

# Absolute path of a current working directory with file name
print(os.path.abspath("output.txt"))

# Delete file
os.remove("output.txt")