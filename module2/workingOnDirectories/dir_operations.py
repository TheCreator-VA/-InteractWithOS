#!/usr/bin/env python

import os
# get current wprking dirctory
print(os.getcwd())

# make directory
os.mkdir("our_dir")

# switch directory
os.chdir("our_dir")
print(os.getcwd())

os.mkdir("new_Dir")

# List the contents of current working directory
print(os.listdir())

# Delete directory
os.rmdir("new_dir")
print(os.listdir())
