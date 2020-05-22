#!/usr/bin/env python

import os
for n in os.listdir():
    n = os.path.join(os.getcwd(),n) 
    if os.path.isdir(n):
        print("{} is directory.".format(n))
    elif os.path.isfile(n):
        print(f"{n} is a file.")
    else:
        print(f"{n} is neither a file nor a directory.")