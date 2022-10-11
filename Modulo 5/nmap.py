# pip install python-nmap
import nmap 

# começar da porta 75
begin = 75
end = 443
target = '127.0.0.1'

# aqui chamamos a funçao do portscanner da biblioteca nmap
scanner = nmap.PortScanner() 


# criamos um for loop para realizar o scanner em cada uma das portas
for i in range(begin,end+1): 
   
    
    res = scanner.scan(target,str(i))     
    
    res = res['scan'][target]['tcp'][i]['state'] 
   
    print(f'port {i} is {res}.') 
