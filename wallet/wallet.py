import rsa
import json
import hashlib
import socket
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode

user_wallet = []
primary_remote_node = "127.0.0.1"

# User wallet format: [privatekey, publickey, publicaddress, balance]

def send(recipient, amount, private):
    s = socket.socket()
    port = 42069
    s.connect((primary_remote_node, port))

    #user_wallet[2] is this wallets public address
    signature = b64encode(rsa.sign(( user_wallet[2] + recipient + str(amount) ).encode(), private, "SHA-512")).decode()
    transaction = json.dumps([user_wallet[2], recipient, amount, signature]).encode()
    
    s.send(transaction)
    s.close()

def recieve():
    print("Full public key",user_wallet[1])
    print("Actual wallet address:",user_wallet[2])
    pass

def history():
    pass

def sync_wallet_file():
    with open("w.file", "w+") as f:
        f.write(json.dumps(user_wallet))

def main():
    global user_wallet
    global primary_remote_node
    try:
        with open("w.file", "r") as f:
            user_wallet = json.load(f)
            private = RSA.importKey(user_wallet[0],passphrase=None)
    except FileNotFoundError:
        print("Wallet file not found, will create new one")
        
        public, private = rsa.newkeys(2048)
        publickey = public.exportKey('PEM').decode()
        privatekey = private.exportKey('PEM').decode()

        user_wallet = [privatekey, publickey, hashlib.sha256(publickey.encode()).hexdigest(), 0.0]

        with open("w.file", "w+") as f:
            f.write(json.dumps(user_wallet))

    while True:
        user_choice = input("SET REMOTE NODE (I)P, (S)END, (R)ECIEVE, (H)ISTORY, (E)XIT: ").upper()
        if user_choice == "S":
            recipient = input("Enter the recipient's address: ")
            amount = input("Enter the amount to send: ")
            send(recipient, amount, private)
        elif user_choice == "R":
            recieve()
        elif user_choice == "H":
            history()
        elif user_choice == "E":
            sync_wallet_file()
            break
        elif user_choice == "I":
            primary_remote_node = input("Enter IP of node: ")
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
