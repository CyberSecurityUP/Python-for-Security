import os
import pyaes

file_name = "arquivotest.txt.hacked"
file = open(file_name, "rb")
file_data = file.read()

key = b"blackhatpythoncs"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

new_file = "decrypt.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
