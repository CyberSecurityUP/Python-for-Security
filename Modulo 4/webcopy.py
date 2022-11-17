from pywebcopy import save_webpage

# 
kwargs = {'project_name': 'site folder'}
 
save_webpage(
   
    # url of the website
    url='http://pudim.com.br/',
     
    # pasta que ele vai salvar o website
    project_folder='pycopy/',
    **kwargs
    # **kwargs é argumentos nomeados
    # permitem que você passe um número não especificado de argumentos para uma função.
    #Dessa forma, ao escrever uma função, você não precisa definir quantos argumentos serão passados para sua função.
 #O **kwargs possibilita verificarmos os parâmetros nomeados da função, isto é, aqueles parâmetros que são passados com um nome!
#Eles estarão disponíveis como um dicionário ({'chave': 'valor'}) dentro da função.
)
