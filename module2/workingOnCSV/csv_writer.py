#!/usr/bin/env python

import csv

# Writting CSV from a list of lists

hosts_list = [["workstation.local", "192.168.25.31"],["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(hosts_list) # Each sub-list will be written in a seperate row


# CSV file created would be like this:

    # workstation.local,192.168.25.31

    # webserver.cloud,10.2.5.6
