#O método str.encode retorna uma versão codificada da string como um objeto de bytes. A codificação padrão é utf-8.

# O método encode() retorna uma versão codificada da string. 
#A codificação padrão é a codificação de string padrão atual. Os erros podem ser fornecidos para definir um esquema de tratamento de erros diferente.

#Um texto em UTF-8 é simples, é feito completamente em ASCII e, 
#quando precisamos de um caractere do UNICODE, usamos um caractere especial, que indica 'Atenção, o seguinte caractere está em UNICODE'.

#UNICODE CORRESPONDE LETRAS E NUMEROS, NÃO SÓ CÓDIGOS DE 0 A 127

#Em vez de usar apenas os códigos de 0 a 127, o UNICODE utiliza códigos de valor bem maiores. Com isso, pode representar todos os caracteres específicos 
#de diversos idiomas. 
#Novos códigos são regularmente atribuídos para novos caracteres, como caracteres latinos (acentuados ou não), gregos, cirílicos, armênios, hebraicos, 
#tailandeses, hiraganas, katakanas etc. 
#Só o alfabeto chinês Kanji contém 6.879 caracteres. Assim sendo, o UNICODE define uma correspondência entre símbolos e números.

# Existem diferentes códigos. O mais conhecido é o código ASCII (American Standard Code for Information Interchange). 
#Este é um padrão americano, mas é um dos mais utilizados em todo o mundo. O código ASCII define, com precisão, a correspondência 
#entre símbolos e números até o número 127:

#Mas você reparou que não há caracteres acentuados? Pois é, os americanos não pensaram no resto do mundo. 
#Muitas vezes usamos os códigos de 128 a 255 para os acentos, mas os códigos são diferentes de um país para outro. 
#Nada prático para trocar documentos. Assim, foi preciso encontrar um código mais prático: o UNICODE.

# -*- coding: latin-1 -*-

string = "joas"
print(string.encode())

string.encode(encoding='UTF-8',errors='strict')

#Por padrão, o encode()método não requer nenhum parâmetro.

#Ele retorna uma versão codificada em utf-8 da string. Em caso de falha, ele gera uma UnicodeDecodeErrorexceção.

#No entanto, são necessários dois parâmetros:

#codificação - o tipo de codificação em que uma string deve ser codificada
#erros - resposta quando a codificação falha. Existem seis tipos de resposta de erro
#estrito - resposta padrão que gera uma exceção UnicodeDecodeError em caso de falha

# -- EXEMPLO codificação UTF-8
# unicode string
string = 'pythön!'

# print string
print('A string é:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('Versão encodada:', string_utf)



