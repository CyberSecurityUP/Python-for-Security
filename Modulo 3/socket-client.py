# echo-client.py

#Em comparação com o servidor, o cliente é bastante simples.
#Ele cria um objeto socket, usa .connect()para se conectar ao servidor e chama s.sendall()para enviar sua mensagem.
#Por fim, ele chama s.recv()para ler a resposta do servidor e a imprime.

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
