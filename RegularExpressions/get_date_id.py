# Det date and id
import re
pattern = r"(\w+ [1-3]?[0-9] [0-2][0-9]:[0-5][0-9]:[0-5][0-9]).*\[(\d+)\]" # Capture groups used
line = "Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"
a = (re.search(pattern,line))
#print(a)
print(a[1] + " pid: " + a[2])