# Vamos criar uma lista simples
lista = ['O carro','peixe',123,111,True]
print(lista)

# Vamos criar uma nova lista e adicionando a lista anterior
nova_lista = ['pedra',lista]
print(nova_lista)

#ACESSANDO ELEMENTOS UTILIZANDO SINTAXE E INDICE
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print(nova_lista[0])
print(nova_lista[1][2])

#COmprimento de uma lista
print(len(lista))
print(len(nova_lista))

#Ajuntar e repetir lista
lista+nova_lista
lista*3

#Verificando a existência de uma informação dentro de uma lista
exist1 = 'peixe' in lista
exist2 = 'gato' in lista
exist3 = 'felipe' in lista

print(exist1)
print(exist2)
print(exist3)

#Encontrar os menores valores, maiores valores e somar tudo depois
numeros = [14.55, 67, 89.88, 10, 21.5]
print(min(numeros))
print(max(numeros))
print(sum(numeros))
print(numeros)


programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana

programadores.append('Renato')
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato']

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programadores.insert(1, 'Rafael')

print(programadores) # ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']
