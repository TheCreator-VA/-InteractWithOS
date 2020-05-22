#!/usr/bin/env python

import csv

f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, roll = row
    print(f"Name: {name}, Phone: {phone}, RollNo: {roll}")
     
f.close()