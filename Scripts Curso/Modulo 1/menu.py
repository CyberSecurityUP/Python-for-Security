while True:
    print("programa básico")
    print("1 - Cadastro\n")
    print("2 - Criador\n")
    menu = str(input("Digite a opcao desejada: "))
    if menu == "1":
        print("\nBem vindo ao sistema de cadastro")
        nome = str(input("Digite o seu nome: "))
        print(nome)
        idade = int(input("Qual é a sua idade? "))
        print(idade)
        peso = float(input("Qual é o seu peso? "))
        print(peso)
        print(f"Seu nome é {nome}, sua idade é {idade} o seu peso é {peso}")
    elif menu == "2":
        print("\n Curso Black Hat Python")
    else:
        print("Opção inexistente")
        break
        
