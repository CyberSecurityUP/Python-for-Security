# Abrimos uma variavel dados_client
# Vamos adicionar informações, nome, endereço e telefone separado por :
dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

# Agora vamos mostrar apenas o que tem dentro dicionario que se refere a nome
# Assim ele traz o nome renan
print(dados_cliente['Nome']) # Renan

# Agora vamos trazer todos os dados de um dicionario
dados_cliente2 = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

print(dados_cliente2) # {'Nome': 'Renan', 'Endereco': 'Rua Cruzeiro do Sul', 'Telefone': '982503645'}

# Vamos adicionar dentro do dicionario a Idade com valor 40
dados_cliente2['Idade'] = 40

# Vamos printar
print(dados_cliente2)
