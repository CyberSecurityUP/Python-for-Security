# Importei a biblioteca regex
import re

# Passei o arquivo de log na variavel
logfile="sample-log.log"

cpf="412.111.210-03"

#Dentro das chaves definimos a quantidade que o caractere deve estar presente. Com isso, já podemos encontrar 3 dígitos.
#Agora vem o "ponto" só que aprendemos que esse caractere possui um significado especial.
#No entanto queremos procurar o ponto literalmente e não qualquer caractere.
#Para deixar claro que o ponto deve ser ponto apenas, é preciso escapar o caractere com \. Assim temos:
cpfreg = "\d{3}\.\d{3}\.\d{3}\-\d{2}"

cpf_find = re.findall(cpfreg, cpf)

print(cpf_find, "\n")
# Tudo entre []são caracteres a serem combinados
# \d corresponde a um dígito de [0-9], definimos que apareça digito de 1 a 3 caracteres
# . corresponde a qualquer caractere
# Adicionamos duas colunas a mais, para que a correspodência bata exatamente com os endereços IP
logreg ="\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"

#Nessa expressão regular, vamos filtrar tudo que for HTTPS, que corresponde a unica expressão que corresponda a digitos e caracteres equivalente a minusculos e minusculas
# A quantidade de vezes que essa classe de caracteres deve aparecer é definida por um quantifier
# O ponto de interrogação (?), que significa zero ou uma vez, é mais um quantifier.
# Quantificadores indicam números de caracteres ou expressões para corresponder.
# + Faz com que o resultado seja 1 e faça a repetição do processo regex 
logreg2 ="https?://(?:[-\w.]|(?:%[\da-fA-Z]{2}))+"

with open (logfile) as f:
    fread = f.read()
    # re.findall é para dar matchs em tudo que corresponde o regex passado
    ip_list = re.findall(logreg, fread)
    ip_list2 = re.findall(logreg2, fread)
    #ip_list3 = re.findall(logreg3, fread)
    print(ip_list)
    print(ip_list2)
    #print(ip_list3)
