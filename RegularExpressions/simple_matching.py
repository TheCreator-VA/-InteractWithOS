#!/usr/bin/env python

import re

result = re.search(r"aza","plaza") # here r is for raw string 
print(result)

# Raw string : In a raw string any special character is treated as a normal character.
# For eg:
print("Hello\nWorld")
# OUTPUT
# Hello
# World
print(r"Hello\nWorld")

# OUTPUT
# Hello\nWorld