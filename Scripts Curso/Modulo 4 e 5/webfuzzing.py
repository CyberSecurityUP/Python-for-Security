import requests

import io

from fake_useragent import UserAgent

ua = UserAgent()

user_agent = ua.random

host="https://www.faculdadevincit.edu.br/"

word = 'wordlist.txt'

with open(word) as wl:
    line = wl.readline()

    while line:
        combinar = host+line.strip()
        r = requests.get(combinar, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            print(combinar)
        line = wl.readline()
