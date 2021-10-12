import socket
import json

#each "block" = block number, nonce, data, prevhash, hash
blockchain = [[0, 0, [], "0"*64, hashlib.sha256(("0" + "0" + "" + "0" * 64).encode("utf8")).hexdigest()]]

pending_transactions = []
#TRANSACTION FORMAT: [sender, reciever, amount]

def add_pending_transaction(transaction):
    pending_transactions.append(transaction)

def add_block_to_chain(block):
    




def network():
    s = socket.socket()
    port = 12345

    s.bind(('', port))

    s.listen()

    c, addr = s.accept()

    print("Got connection from",addr)

    c.send("what is up".encode())



    c.close()
