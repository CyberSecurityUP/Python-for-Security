for i in range(100): #Ele armazena no i o valor de 0 a 99 
    print(i) #Aqui ele mostra na tela até o valor 99, após isso ele para

i = 0 #Toda vez que vai entrar no While, ele passa por esse i = 0, ou seja, enquanto i = 0 ele vai trabalhando com o loop
#caso eu coloque i = 1500, ele só vai imprimir uma vez o valor 5
while True: #Ele entra em um loop enquanto o valor for Verdadeiro, quando o valor não for verdadeiro ele encerra esse laço
    print("5") #Vou imprimir o número 5
    if i == 1500: #Aqui ele imprime o número 5, 1500
        break #Ele encerra a estrutura de laço quando i for maior ou igual a 1, ou seja, quando o valor 5 for imprimido 1500 ele encerra
    i += 1 #Ele conta 1 por 1, exemplo: Contar até 10 em 2 e 2, então seria i += 2 e conta 2,4,6,8,10
print("OK")
