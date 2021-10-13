import random
import hashlib

# Formula: g^x mod p
# g and p are public
#
# g^x mod p stands for the public key, x stands for the private key

g = 21
p = random.getrandbits(512)

def genkeys():
    x = random.getrandbits(20)
    publickey_int = ( g ** x ) % p
    publickey = hashlib.sha256(str(publickey_int).encode('utf8')).hexdigest()
    return x, publickey

privatekey1, publickey1 = genkeys()
privatekey2, publickey2 = genkeys()




