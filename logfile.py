import re

logfile="sample-log.log"

logreg ="\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}."
#logreg="\bhttp:\/\/([^\/]*)\/([^\s]*)"
#logreg="\bhttp:\/\/"
logreg2 = "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
with open (logfile) as f:
        fread = f.read()
        ip_list = re.findall(logreg, fread)
        ip_list2 = re.findall(logreg2, fread)
        print(ip_list)
        print(ip_list2)
