#!/usr/bin/python
#realizar requisições web 
import requests
#lidar com entrada e saida de dados, de várias formas 
import io
#Usar um agent aleatório para realizar o fuzzing
from fake_useragent import UserAgent
ua = UserAgent()
user_agent = ua.random
host='target'
filepath = 'wordlist.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        combined = host+line.strip()
        r = requests.get(combined, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            #print('\n',r).format(line.strip())
            print(combined)
        line = fp.readline()
