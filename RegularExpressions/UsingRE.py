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

print(re.search(r"Py.*n","Pygmalion"))          # <_sre.SRE_Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r"Py.*n","Python"))             # <_sre.SRE_Match object; span=(0, 6), match='Python'>
print(re.search(r"Py.*n","Python Programming")) # <_sre.SRE_Match object; span=(0, 17), match='Python Programmin'>

# using + qualifier 
# + looks for one or more occurences of a character
print(re.search(r"o+l+","ooly"))   # <_sre.SRE_Match object; span=(0, 3), match='ool'>
print(re.search(r"o+l+","woolly")) # <_sre.SRE_Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+","oly"))    # <_sre.SRE_Match object; span=(0, 2), match='ol'>
print(re.search(r"o+l+","oily"))   # None
print(re.search(r"o+l+","cooly"))  # <_sre.SRE_Match object; span=(1, 4), match='ool'>

# Using ? qualifier 
# ? looks for none or single occurrence of a character

print(re.search(r"p?each","To each their own.")) # <_sre.SRE_Match object; span=(3, 7), match='each'>
print(re.search(r"p?each","I like peaches!"))    # <_sre.SRE_Match object; span=(7, 12), match='peach'>

# Escape sequences to match special characters like . ^ etc

print(re.search(r".com","welcome"))     # <_sre.SRE_Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com","welcome"))    # None
print(re.search(r"\.com","google.com")) # <_sre.SRE_Match object; span=(6, 10), match='.com'>


# \w mathes alphanumeric characters or underscores
print(re.search(r"\w*","hello world"))
print(re.search(r"\w*","hello_world"))

# \d matches digits
# \s matches white spaces
# www.regex101.com  for regex reference