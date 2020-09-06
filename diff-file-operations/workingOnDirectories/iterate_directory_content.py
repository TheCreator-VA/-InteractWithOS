#!/usr/bin/env python
# Iterate through the contents of the directory
# Check for files and directories
import os
for n in os.listdir():
    
    n = os.path.join(os.getcwd(),n)
    # getcwd() returns the absolute path.   
    # Join takes the name of contents and joins it to the absolute path of parent.
    
    # Check for directory.
    if os.path.isdir(n):
        print("{} is directory.".format(n))

    # Check for file.
    elif os.path.isfile(n):
        print(f"{n} is a file.")

    else:
        print(f"{n} is neither a file nor a directory.")