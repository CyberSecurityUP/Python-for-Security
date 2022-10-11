import os
import pyaes

#abrir o arquivo criptografado
file_name = "test.txt.hacked"
file = open(file_name, "rb")
file_data = file.read()

#minha chave para descriptografar
key = b"blackhatpythoncs" #chave de 16 bytes
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#remover o arquivo criptografado
#os.remove(file_name)

# criar um novo arquivo descriptografado
new_file = "decrypted.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
