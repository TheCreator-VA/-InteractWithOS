#!/usr/bin/env python

import csv

hosts_list = [["workstation.local", "192.168.25.31"],["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv","w") as f:
    writer = csv.writer(f)
    writer.writerows(hosts_list)