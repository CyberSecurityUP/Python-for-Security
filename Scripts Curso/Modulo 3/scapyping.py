from scapy.all import *

endereco = input("Digite o IP: ")

ip = IP()
ping = ICMP()
ip.destino = endereco
reply = sr1(ip/ping)
if reply.ttl < 65:
    os = "Linux"
else:
    os = "Windows"
print("O sistema alvo é: " + os)
