#Declarando uma função basica em python
def hello(meu_nome):
     print('Olá',meu_nome)
hello('Joas')

#Declarando uma função com nome e idade
def hello2(meu_nome2,idade):
        print('Olá',meu_nome2,'\nSua idade é:',idade)
hello2('José',21)

#Agora temos uma função que faz o cálculo do salário e retorna o valor a ser pago conforme o número de horas trabalhadas.
#a função calcular_pagamento() recebe dois parâmetros, qtd_horas e valor_hora, que representam, respectivamente,
#a quantidade de horas a serem calculadas e o valor da hora.
def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario = horas*taxa #Se as horas for igual ou menor que 40 ele abre a variavel salario ao qual faz o calculo de vezes das horas e taxas
  else:
    h_excd = horas - 40 #Caso ao contrário ele calcula as horas extras - 40
    salario = 40*taxa+(h_excd*(1.5*taxa)) #Se for + que 40 horas, adiciona ao salário um valor adicional pelas horas extras
  return salario

#Agora vamos utilizar essa função para entrar com os valors e imprimir na tela posteriormente
str_horas = input('Digite as horas: ') #Informações que serão armazenadas em strings
str_taxa = input('Digite a taxa: ')
total_salario = calcular_pagamento(str_horas,str_taxa) #Em seguida obtemos o resultado da função e o atribuímos à variável total_salario
print('O valor de seus rendimentos é R$',total_salario)

#Funções builtin no Python
#Funções sem a necessidade de importar uma biblioteca
maior_numero = max(1, 2, 3)
maior_letra = max('a', 'b', 'c')
print(maior_numero) #Recebera o valor 3
print(maior_letra) #Recebera o valor c

#Outras funções só são disponível em módulos
import math
exponencial = math.exp(3)
print(exponencial)
#Nesse caso para utilizar o comando exp é necessário importar o módulo MATH
