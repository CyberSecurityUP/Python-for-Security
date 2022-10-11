#COMPARADORES == >= <= != < >

# ==	igual
# !=	diferente
# >	maior
# <	menor
# >=	maior ou igual
# <=	menor ou igual

var = 5

if var == 5:
    print('Os valores são iguais')

if var != 7:
    print('O valor é diferente de 7')

if var > 2:
    print('O valor da variável é maior de 2')

if var >= 5:
    print('O valor da variável é maior ou igual a 5')

if var < 7:
    print('O valor da variável é menor que 7')

if var <= 5:
    print('O valor da variável é menor ou igual a 5')


#and	Retorna True se ambas as afirmações forem verdadeiras
#or	Retorna True se uma das afirmações for verdadeira
#not	retorna Falso se o resultado for verdadeiro

num1 = 7
num2 = 4

# Exemplo and
# Se o numero1 for maior que 3 e  numero 2 menor que 8
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Se o numero 1 for maior que 4 ou numero 2 menor ou igual a 8
# Exemplo or
if num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Se o numero1 não for maior que 8 e o numero 2 não for menor que 8
# Exemplo not
if not (num1 > 8 and num2 < 8):
    print('Uma das condição é falsa')
