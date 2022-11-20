import re

logfile="sample-log.log"

#logreg="\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
logreg2="https?://(?:[-\w.]|(?:%[\da-fA-Z]{2}))+"

with open(logfile) as f:
    fread = f.read()
    ipinfo = re.findall(logreg2, fread)
    print(ipinfo)
