#!/usr/bin/env python3

# python would erase all content and write new data if dile with this name exists.
# Otherwise a new file with the given name will be created in the same folder as the file is created.
# We can also use absolute path to create file at any other location.
file = open("output.txt","w") # w specifies the mode, here w is for write mode
# other modes available are a: append, r: read(default), r+: read and write etc.
file.write("Adding data to file\nPython uses escape sequences for newline, tabs etc\nThis code is a simple example of writting data to a file from python.")
file.close()