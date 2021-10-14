import rsa
from base64 import b64encode, b64decode

msg1 = "Hello Tony, I am Jarvis!"
msg2 = "Hello Toni, I am Jarvis!"
keysize = 2048
(public, private) = rsa.newkeys(keysize)
encrypted = b64encode(rsa.encrypt(msg1.encode("utf8"), public))
decrypted = rsa.decrypt(b64decode(encrypted), private)
signature = b64encode(rsa.sign(msg1.encode("utf8"), private, "SHA-512"))
verify = rsa.verify(msg1.encode("utf8"), b64decode(signature), public)

print(private.exportKey('PEM'))
print()
print(public.exportKey('PEM'))
print()
print("Encrypted: " + encrypted.decode("utf8"))
print()
print("Decrypted: '%s'" % decrypted.decode("utf8"))
print()
print("Signature: " + signature.decode("utf8"))
print()
print("Verify: %s" % verify)
print()
rsa.verify(msg2.encode("utf8"), b64decode(signature), public)
