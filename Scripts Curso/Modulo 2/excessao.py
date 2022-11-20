a = 12
b = 0
try:
    y = a/b
    print(y)
except ZeroDivisionError:
    print("Erro na divisão por zero")

lista = [1,2,3,4]
try:
    parser = lista[6]
except IndexError:
    print("Erro na indexação, não existe esse valor especifico")
finally:
    print("Esta tudo bem")
