#!/usr/bin/env python
# Read the contents of a csv file as a dictionary

import csv

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))