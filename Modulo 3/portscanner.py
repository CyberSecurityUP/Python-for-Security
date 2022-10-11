# Import da lib socket para conexões
import socket
# O alvo será digitado pelo usuário
alvo = input('Digite o IP/Dominio: ')
# Loop de 65535 vezes (quantidade de portas TCP)
for porta in range(1, 65535):
    
    # Setando e configurando o cliente
    client = socket.socket()
    client.settimeout(0.05)
    # Se a porta estiver aberta, jogue ela na tela
    if client.connect_ex((alvo, porta)) == 0:
        print('Porta Aberta ==>', porta)
