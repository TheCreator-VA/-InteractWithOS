#!/usr/bin/env python3

"""A script that contains several functions which check the health of the system."""

import shutil
import psutil

def check_disk_usage(disk):
    # The function returns true if the disk is more than 20% free, false otherwise.
    du = shutil.disk_usage(disk) # disk usage is a function in shutil module
    free = du.free / du.total * 100 # Find % free space
    return free > 20 

def check_cpu_usage():
    # The function returns true if cpu usage is less than 75%, false otherwise.
    usage = psutil.cpu_percent(1) # Check the cpu usage for 1 second.
    return usage < 75