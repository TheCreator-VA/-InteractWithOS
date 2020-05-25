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

print(re.search(r"cloud[A-za-z0-9]","cloudy")) # <_sre.SRE_Match object; span=(0, 6), match='cloudy'>
print(re.search(r"cloud[A-za-z0-9]","cloudY")) # <_sre.SRE_Match object; span=(0, 6), match='cloudY'>
print(re.search(r"cloud[A-za-z0-9]","cloud9")) # <_sre.SRE_Match object; span=(0, 6), match='cloud9'>

# Look for any character except the mentioned ones
print(re.search(r"[^a-zA-z]",s3)) # <_sre.SRE_Match object; span=(5, 6), match=' '>

# here the search return the first un-mentioned character that is space.

# Let's try includng space.
print(re.search(r"[^a-zA-z ]",s3)) # <_sre.SRE_Match object; span=(60, 61), match='.'>

# As expected now we recieve period as a match.


# Look for either of two strings or a string combination

print(re.search(r"cats|dogs","I like big cats."))                 # <_sre.SRE_Match object; span=(11, 15), match='cats'>
print(re.search(r"cats|dogs","I rarely like a breed of dogs."))   # <_sre.SRE_Match object; span=(25, 29), match='dogs'>
print(re.search(r"cats|dogs","I rarely like dogs or cats."))      # <_sre.SRE_Match object; span=(14, 18), match='dogs'>

# to finnd all strings that match
print(re.findall(r"cats|dogs","I rarely like dogs or cats."))     # ['dogs', 'cats']


# What is .*?
# . means any character and * means repeated any number of times.

print(re.search(r"Py.*n","Pygmalion")) # <_sre.SRE_Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r"Py.*n","Python")) # <_sre.SRE_Match object; span=(0, 6), match='Python'>
print(re.search(r"Py.*n","Python Programming")) # <_sre.SRE_Match object; span=(0, 17), match='Python Programmin'>

