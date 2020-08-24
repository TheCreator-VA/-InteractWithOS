#!/usr/bin/env python
# Write the contents of a dictionary to a csv file.
import csv

sudents =[{"name" : "Vansh", "username" : "creator", "roll" : 120},
    {"name" : "Karan", "username" : "sun", "roll" : 121},
    {"name" : "Arjun", "username" : "rj", "roll" : 111}]

keys = ["name", "username", "roll"]
with open("student_username.csv","w") as f:
    writer = csv.DictWriter(f, fieldnames = keys)
    writer.writeheader()
    writer.writerows(sudents)