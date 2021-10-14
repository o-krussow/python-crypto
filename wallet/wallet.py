import rsa
import json
from base64 import b64encode, b64decode

user_wallet = []

def send(recipient, amount):
    pass

def recieve():
    #print address information
    pass

def history():
    pass

def sync_wallet_file():
    with open("w.file", "w+") as f:
        f.write(json.dumps(user_wallet))

def main():
    global user_wallet
    try:
        with open("w.file", "r") as f:
            user_wallet = json.load(f)
    except FileNotFoundError:
        print("Wallet file not found, will create new one")
        with open("w.file", "w+") as f:
            f.write(json.dumps(user_wallet))

    while True:
        user_choice = input("(S)END, (R)ECIEVE, (H)ISTORY, (E)XIT: ").upper()
        if user_choice == "S":
            recipient = input("Enter the recipient's address: ")
            amount = input("Enter the amount to send: ")
            send(recipient, amount)
        elif user_choice == "R":
            recieve()
        elif user_choice == "H":
            history()
        elif user_choice == "E":
            sync_wallet_file()
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()



#msg1 = "Hello Tony, I am Jarvis!"
#msg2 = "Hello Toni, I am Jarvis!"
#keysize = 2048
#(public, private) = rsa.newkeys(keysize)
#encrypted = b64encode(rsa.encrypt(msg1.encode("utf8"), public))
#decrypted = rsa.decrypt(b64decode(encrypted), private)
#signature = b64encode(rsa.sign(msg1.encode("utf8"), private, "SHA-512"))
#verify = rsa.verify(msg1.encode("utf8"), b64decode(signature), public)
#
#print(private.exportKey('PEM'))
#print()
#print(public.exportKey('PEM'))
#print()
#print("Encrypted: " + encrypted.decode("utf8"))
#print()
#print("Decrypted: '%s'" % decrypted.decode("utf8"))
#print()
#print("Signature: " + signature.decode("utf8"))
#print()
#print("Verify: %s" % verify)
#print()
#rsa.verify(msg2.encode("utf8"), b64decode(signature), public)
