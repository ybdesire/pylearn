import rsa

# generate pubkey, privkey
(pubkey, privkey) = rsa.newkeys(1024)
print(pubkey, privkey)


# save keys
with open('public.pem','w+') as f:
    f.write(pubkey.save_pkcs1().decode())

with open('private.pem','w+') as f:
    f.write(privkey.save_pkcs1().decode())


# import keys
with open('public.pem','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

with open('private.pem','r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

    
# message to be encrypted    
message = 'hello'

# encrypt msg by public key
msg_crypt = rsa.encrypt(message.encode(), pubkey)

# decrypt msg by private key
msg_decrypt = rsa.decrypt(msg_crypt, privkey).decode()


print('\nmsg encrypted: {0}\n'.format(msg_crypt)) 
print('msg decrypted: {0}'.format(msg_decrypt))   
    