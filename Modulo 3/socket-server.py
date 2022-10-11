#Os argumentos passados socket()​​são constantes usadas para especificar a família de endereços e o tipo de soquete. AF_INETé a família de endereços da Internet para IPv4 . SOCK_STREAMé o tipo de soquete para TCP ,
#o protocolo que será usado para transportar mensagens na rede.

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #O .bind()método é usado para associar o soquete a uma interface de rede e número de porta específicos:
    s.bind((HOST, PORT))
    #No exemplo do servidor, .listen()permite que um servidor aceite conexões. Isso torna o servidor um soquete de “escuta”:
    s.listen()
    #conn, é um objeto de soquete que você pode usar para enviar e receber dados do cliente conectado.
    # addr, contém informações de endereço sobre o cliente que está conectado (por exemplo, endereço IP e parte remota).
    #O soquete deve estar vinculado a um endereço e escutar conexões.
    conn, addr = s.accept()
    #A with instrução é usada com compara fechar automaticamente o soquete no final do bloco.
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
