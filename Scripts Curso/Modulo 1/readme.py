with open('readme.txt', 'w') as f:
    f.write('test')

lines = ['Readme', 'Esse é um arquivo criado pelo python', 'dsdsd', 'Matheus', 'ls -lha']
with open('readme2.sh', 'w') as f:
    for linha in lines:
        f.write(linha)
        f.write('\n')

more_lines = ['add', 'the end']
with open('readme2.txt', 'a') as f:
    f.write('\n'.join(more_lines))

f = open("readme2.txt", "r")
print(f.read())
