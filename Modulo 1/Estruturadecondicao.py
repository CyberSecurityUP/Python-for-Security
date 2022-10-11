# Variavel idade é 61 
idade = 61
if idade < 12:
    print("criança")
elif idade < 18:
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")

# Aqui criamos um laço, aonde os valores inseridos continuar sendo verdadeiro ele não encerra o programa ate apertar CTRL+C
while True:
    print("Programinha Básico")
    print("1- Cadastrar\n")
    print("2- Crédito\n")
    print("3- Exercicio")
    menu = str(input("Digite a opção desejada: "))
    if menu == "1":
        print("\nBem vindo ao Cadastrar")
        parte1 = str(input("Qual é o seu nome? "))
        print(parte1)
        parte2 = int(input("Qual a sua idade? "))
        print(parte2)
        parte3 = float(input("Qual é a sua altura? "))
        print(parte3)
        print("\n BEM VINDO!")
    elif menu == "2":
        print("\n Criado por Joas")
    elif menu == "3":
        print("\n Crie um programa parecido com esse, ao qual ele faz cadastro de pessoas e que aja uma interação da pessoa com o programa depois de efetuar o cadastro")
