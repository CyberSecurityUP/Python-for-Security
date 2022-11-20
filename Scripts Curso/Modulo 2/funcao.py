#def helloworld(meunome, idade):
 #   print(f'Olá {meunome}, sua idade é {idade}')
#def helloworld2(meunome2, idade2):
 #   print("f'Ola {meunome2}, sua idade é {idade2}")
#meunome2 = input("blalbalbal")
#idade2 = input("hfehfhfhe")
#meunome = str(input("Digite o seu nome: "))
#idade = input("Digite a sua idade: ")
#helloworld(meunome, idade)
#helloworld2(meunome2, idade2)

def calcular_pagamento(qtdhoras, valorhora, qtdtaxas):
    horas = float(qtdhoras)
    impostos = float(valorhora)
    taxas = float(qtdtaxas)
    if horas <= 40:
        salario = horas*impostos
    elif horas >= 60:
        salario = horas*impostos
    elif horas == 50:
        salario = horas*impostos*taxas
    else:
        horas_extras = horas * 40
        salario = 40*impostos(horas_extras*(1.5*impostos))
    return salario

horas = input("Digite as horas trabalhadas: ")
impostos = input("Digite os impostos: ")
taxas = input("Digite os valores das taxas: ")
total = calcular_pagamento(horas, impostos, taxas)
print("O valor do seu salário é", total)
