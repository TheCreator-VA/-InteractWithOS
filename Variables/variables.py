#!/usr/bin/env python

import os

print("HOME: " + os.environ.get("HOME",""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT",""))
# To set path for something which is not already present: export name=path
# EXAMPLE
# export FRUIT=Pineapple