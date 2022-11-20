import requests

host = "https://nubank.com.br/"

metodos = ['OPTIONS', 'GET', 'POST', 'DELETE', 'TRACE', 'CONNECT', 'PUT']

for metodo in metodos:
    resposta = requests.request(metodo, host)
    print(f"{metodo} --> {resposta.reason}")
