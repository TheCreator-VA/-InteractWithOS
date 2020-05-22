#!/usr/bin/env python


# using the with option eliminated the need of explicily closing the file.
# As soon as the block ends file is automatically closed.
with open("output.txt") as file:
    for line in file:
        print(line.upper())