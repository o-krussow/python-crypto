import socket
import hashlib
import time
import json
import threading
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64


#each "block" = block number, nonce, data, prevhash, hash
blockchain = [[0, 0, [], "0"*64, hashlib.sha256(("0" + "0" + "" + "0" * 64).encode("utf8")).hexdigest()]]

pending_transactions = []
#TRANSACTION FORMAT: [sender address, reciever address, amount, signature]

#====================================================================
#   TODO This part needs to be figured out
#        Keep in mind, the public crypto address is the computed public key, hashed

def rsakeys():  
    length=1024  
    privatekey = RSA.generate(length, Random.new().read)  
    publickey = privatekey.publickey()  
    return privatekey, publickey

def encrypt(rsa_publickey,plain_text):
    cipher_text=rsa_publickey.encrypt(plain_text,32)[0]
    b64cipher=base64.b64encode(cipher_text)
    return b64cipher

def decrypt(rsa_privatekey,b64cipher):
    decoded_ciphertext = base64.b64decode(b64cipher)
    plaintext = rsa_privatekey.decrypt(decoded_ciphertext)
    return plaintext

def sign(privatekey,data):
    return base64.b64encode(str((privatekey.sign(data,''))[0]).encode())

def verify(publickey,data,sign):
    return publickey.verify(data,(int(base64.b64decode(sign)),))

#======================================================================


def add_pending_transaction(transaction):
    if verify(transaction[0], transaction[2], transaction[3]):
        pending_transactions.append(transaction)
    else:
        print("Tried to add transaction to pending transaction list, but signature was incorrect")

def add_block_to_chain(block):
    if verify_block(block):
        blockchain.append(block)

def verify_block(block):
    for transaction in block[2]:
        if not verify_transaction(transaction):
            return False
    return True

def commit_to_disk():
    with open("currentblockchain.json", "w+") as f:
        f.write(json.dumps(blockchain))

def transaction_recieved(transaction):
    print(transaction)              #TODO input validation stuff, the transmitted transaction format: sender,reciever,amount,signature
    try:
        parsed_transaction = json.loads(transaction)
        add_pending_transaction(parsed_transaction)
    except json.decoder.JSONDecodeError as e:
        print("Transaction sent in a format json loader could not parse")
        print(e)

def block_recieved(block):
    print(block)
    try:
        parsed_block = json.loads(block)
        add_block_to_chain(parsed_block)
    except json.decoder.JSONDecodeError:
        print("Block sent in a format json loader could not parse")

def listen_for_transactions():
    s = socket.socket()
    port = 42069

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind(('', port))
    s.listen()
    try:
        while True:
            c, addr = s.accept()

            print("Got connection for new transaction from",addr)
            
            potential_transaction = c.recv(1024).decode("utf8")

            new_transaction_thread = threading.Thread(target=transaction_recieved, args=(potential_transaction,))
            new_transaction_thread.start()

    except KeyboardInterrupt:
        c.close()


def listen_for_new_blocks():
    s = socket.socket()
    port = 42070

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    s.bind(('', port))
    s.listen()
    try:
        while True:
            c, addr = s.accept()

            print("Got connection for new block from",addr)
            
            potential_block = c.recv(2048).decode("utf8")
            
            new_block_thread = threading.Thread(target=block_recieved, args=(potential_block,))
            new_block_thread.start()

    except KeyboardInterrupt:
        c.close()

def sync_with_newer_chain(newblockchain):
    #Go through newblockchain and make sure all blocks are valid, then add new blocks to current blockchain
    pass

def main():
    transaction_listener = threading.Thread(target=listen_for_transactions, args=())
    block_listener = threading.Thread(target=listen_for_new_blocks, args=())

    transaction_listener.start()
    block_listener.start()
    
    print("Listening for transactions and blocks")



if __name__ == "__main__":
    try:
        with open("currentblockchain.json", "r") as f:
            blockchain = json.load(f)
    except FileNotFoundError:
        print("Blockchain file not found, making a new one for now")
        commit_to_disk()
    main()

