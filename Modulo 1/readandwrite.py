
#Instrução With
# A instrução with é utilizada para garantir a finalização de recursos adquiridos.
#Por exemplo: quando um arquivo é aberto, podemos utilizar try e finally,
#para fazer a execução da nossa lógica e depois fechar o arquivo

#with open('readme.txt', 'w') as f:
 #   f.write('readme')


#lines = ['Readme', 'How to write text files in Python']
#with open('readme.txt', 'w') as f:
# O loop for permite que a gente leia linha por linha
 #   for line in lines:
  #      f.write(line)
   #     f.write('\n')

# O A é de acrescentar
#more_lines = ['', 'Append text files', 'The End']
#with open('readme.txt', 'a') as f:
 #   f.write('\n'.join(more_lines))


#f = open("readme.txt", "r")
#print(f.read())


#with open('readme.txt') as f:
 #   lines = f.readlines()
  #  print(lines)
