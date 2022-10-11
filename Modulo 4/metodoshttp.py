# Importar a biblioteca requests
import requests
# passar uma variavel com o host
host = "http://testphp.vulnweb.com/"
# passar os métodos existentes
metodos = ['OPTIONS', 'GET', 'POST', 'DELETE', 'TRACE', 'CONNECT']
# Criar um for loop para ele testar cada metodo
for metodo in metodos:
    # vai validar cada metodo existente para ver se funciona no host
    resposta = requests.request(metodo, host)
    print(metodo, "->", resposta.reason)
