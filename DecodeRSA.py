#import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

f = open ('encryption.txt', 'r')
message = f.read()

decrypted = key.decrypt(message)

print('decrypted', decrypted)

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
