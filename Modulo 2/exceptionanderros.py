#Vamos ver no interpretador um erro de divisão por zero e depois vamos tratá-lo para gerar uma saída mais amistosa
#x = 12
#y = 0
#z = x/y

a = 12
b = 0
try:
    y = a/b
except ZeroDivisionError:
         print('Erro: divisão por zero')

#Outro erro
#sempre que usamos uma classe menos especifica podemos capturar os erros das suas filhas também por exemplo a classe ZeroDivisionError é filha de ArithmeticError
c = 12
d = 0
try:
    w = c/d
except ArithmeticError:
     print('Erro na aritmética')

 
#Outro erro, podemos usar o maior número de excepts dentro das exceções
#Demonstrando em um erro de lógica
e = 12
f = 2
li = [1, 2, 3, 4]
try:
    z = int(e/f)
    p = li[z]
except ZeroDivisionError:
     print('Erro divisão por zero')
except IndexError:
    print('Erro: tentando alcançar um índice que não existe na lista')

#Outro exemplo
#podemos ter uma cláusula finally que é sempre executada no final independente de uma exceção ser ou não lançada da cláusula else ter sido não usada
try:
     arq = open('data/arquivo.txt', 'r')
except FileNotFoundError:
    print('Erro: arquivo não encontrado')
else:
    print('Esta suite não é executa')
finally:
    print('Sempre executado') 
