import rsa
 
# generate public and private keys with
# rsa.newkeys method,this method accepts
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)
 
# this is the string that we will be encrypting
message = "RSAA_Flag_Secret"
 
# rsa.encrypt method is used to encrypt
# string with public key string should be
# encode to byte string before encryption
# with encode method
encMessage = rsa.encrypt(message.encode(),
                         publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = rsa.decrypt(message, privateKey).decode()
 
print("decrypted string: ", decMessage)
