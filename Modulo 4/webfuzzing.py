#!/usr/bin/python
#realizar requisições web 
import requests
#lidar com entrada e saida de dados, de várias formas 
import io
#Usar um agent aleatório para realizar o crawling
from fake_useragent import UserAgent
# Abrir uma variavel com valor UserAgent
ua = UserAgent()
# por fim gerar um user agent randomico
user_agent = ua.random
# URL do seu alvo
host='https://uniciv.com.br/'
#wordlist list
filepath = 'wordlist.txt'
# Loop para testar linha por linha as páginas
with open(filepath) as fp:
    line = fp.readline()
    # Combinar os resultados dos host e das linhas lidas da wordlist
    while line:
        combined = host+line.strip()
        # Usando um agent usando método Get. E tudo que for 200 ele retorna na tela
        r = requests.get(combined, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            #print('\n',r).format(line.strip())
            print(combined)
        line = fp.readline()
