import hashlib
import random

#random.randint()

#each "block" = block number, nonce, data, prevhash, hash
blockchain = [[0, 0, [], "0"*64, hashlib.sha256(("0" + "0" + "" + "0" * 64).encode("utf8")).hexdigest()]]
some_names = "Farozia Swadeka Vidousha Jaulim Karoona Aniisah Tibye Pasnin Keenoo Soonil Ruhomally Roomila Yudhish Pavaday Jaunky Goinden Kalani Kindra Rayshawn Mstph".split(" ")
#some_names = "jeff arnold bob jessica".split()

def initial_transactions():
    temp_names = list(some_names)
    return_list = []
    for i in range(len(temp_names)):
        return_list.append({"your mom": [temp_names.pop(), random.randint(0, 1000)]})
    return return_list

#TRANSACTION FORMAT: {sender: [reciever, amount]}
def generate_random_transactions(number_of_trans):
    return_list = []
    for i in range(number_of_trans):
        return_list.append({random.choice(some_names): [random.choice(some_names), random.randint(0, 1000)]})
    return(return_list)



def mine():
    block_counter = 1
    difficulty = 5
    data = initial_transactions()
    while True:
        #data = list(input("Enter some data: "))
        nonce = 0
        cont_nonce_increment_loop = True
        while cont_nonce_increment_loop:
            
            prevhash = blockchain[-1][4]
            current_hash = hashlib.sha256((str(block_counter) + str(nonce) + str(data) + prevhash).encode("utf8")).hexdigest()
        
            if current_hash[:difficulty] == "0"*difficulty:
                newblock = [block_counter, nonce, data, prevhash, current_hash]
                blockchain.append(newblock)
                
                #print()
                #print(nonce)
                #print(newblock)
                #print()

                cont_nonce_increment_loop = False    
            
            nonce += 1
 
        #if block_counter % 5 == 0:
        print(blockchain[-1])
        print()


        block_counter += 1
        data = generate_random_transactions(random.randint(1, 3))



mine()

