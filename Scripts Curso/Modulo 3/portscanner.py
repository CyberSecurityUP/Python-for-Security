import socket

alvo = input("Digite o IP: ")

for porta in range(1, 65535):

    cliente = socket.socket()
    cliente.settimeout(0.05)

    if cliente.connect_ex((alvo,porta)) == 0:
        print("A porta esta aberta --->", porta)
