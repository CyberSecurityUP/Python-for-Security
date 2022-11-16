prn que permite passar uma função que executa a cada pacote sniffado. O objetivo desta função é controlar como o pacote é impresso no console
permitindo que você substitua a exibição de impressão de pacote padrão por um formato de sua escolha.

Para que seu programa/script formate e retorne as informações do pacote como você deseja, 
a sniff função passa o objeto do pacote como o único argumento para a função que você especifica no prnargumento do sniff.

O Lambda ele pega o conteúdo e formata como string

#sniff
sniff(count=4)
a = _
a.summary()
sniff(count=4, prn=lambda x: x.summary())
sniff(iface="enp0s3", prn=lambda x: x.summary())
sniff(count=1, iface="enp0s3", prn=lambda x: x.show())

#read pcaps
scapy
p = rdpcap("example.pcap")
p
len(p)
pkt = p[1000] # imprimir o pacote numero 1000
pkt 
type(pkt)
dir(pkt)
lsc()
hexdump(pkt)
ls(pkt)
pkt.summary()
pkt.show()
