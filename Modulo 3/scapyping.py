from scapy.all import *

ans = input("Digite o IP: ")

ip = IP()
ping = ICMP()
ip.dst = ans
reply = sr1(ip/ping)
if reply.ttl < 65:
    os = "linux"
else:
    os = "windows"
print(" O sistema operacional é: " + os)
