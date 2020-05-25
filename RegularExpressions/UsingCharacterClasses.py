#!/usr/bin/env python

import re

# Using
s1 = "Python is a cool language" # capital P
s2 = "python is a cool language" # small p

print(re.search(r"[Pp]ython",s1)) # <_sre.SRE_Match object; span=(0, 6), match='Python'>
print(s1[0:6]) # Python

print(re.search(r"[Pp]ython",s2))
print(s2[0:6]) # python

# Look for a character from a range of characters

s3 = "there is always an alternative way to stay away from trouble."
print(re.search("[a-z]way",s3))   # <_sre.SRE_Match object; span=(10, 14), match='lway'>