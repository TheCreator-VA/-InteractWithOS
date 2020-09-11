import re
import csv
import operator

error_msg = {}
user_count = {}

pattern = r"([\w]{4,5}) ([\w\s]+)[\[\]#\d\s]*\((\w*)" 

with open("syslog.log") as f:
  for log in f:
    if re.search(pattern, log):
      result = re.search(pattern, log)
      log_type = result.group(1) 
      emsg = result.group(2).strip() 
      user = result.group(3) 

      error_msg[emsg] = error_msg.get(emsg,0) + 1

      if user not in user_count.keys():
        user_count[user] = {}
        user_count[user]["INFO"] = 0
        user_count[user]["ERROR"] = 0
      else:
        user_count[user]["INFO"] = user_count[user].get("INFO",0) + 1
        user_count[user]["ERROR"] = user_count[user].get("ERROR",0) + 1

error_msg = sorted(error_msg.items(), key = operator.itemgetter(1), reverse=True)
user_count = sorted(user_count.items())


with open("error_message.csv", 'w') as f:
  writer = csv.writer(f)
  writer.writerow(["ERROR", "COUNT"])
  writer.writerows(error_msg)

with open("user_statistics.csv", 'w') as f:
  writer = csv.writer(f)
  writer.writerow(["USERNAME", "INFO", "ERROR"])
  for line in user_count:
    writer.writerow([line[0], line[1]["INFO"], line[1]["ERROR"]])