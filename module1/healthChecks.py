#!/usr/bin/env python3

"""A script that contains several functions which check the health of the system."""

import shutil

def check_disk_usage(disk):
    # The function returns true if the disk is more than 20% free, false otherwise.
    du = shutil.disk_usage(disk) # disk usage is a function in shutil module
    free = du.free / du.total * 100 # Find % free space
    return free > 20 

