**node first**
- maintain json "blockchain"
- allow clients to connect and add pending transactions, but only accept if the transaction is signed correctly.
- communicate with other nodes, keep the "blockchain" in sync by comparing block levels
- allow miners to add blocks to the blockchain by verifying what they send


"crypto" client - if config doesnt exist, make one and prompt user for remote node ip

verify all hashes in blockchain are correct? or does consensus among a lot of nodes make this not necessary

verify each person has enough funds to make their transaction before adding their transaction to the block

**how to implement addresses instead of names?**
- address is private key, to actually make transactions you need private key.
- remote node will not accept and propogate your transaction to other nodes unless you sign it with your private key or something? do more research on this cuz my understanding sucks here
- nodes need to ensure that the person is not spending twice, once it is determined there are enough funds, the transaction is marked as pending
- then the miners come along and pick up the pending transactions and race to add them to a block
- i dont know how dynamic block size stuff works so i think we set a block size to like 20 transactions or something

nodes verify the transactions, miners SECURE the blockchain to make sure malicious nodes cant add incorrect blocks. they secure different layers of the process
- HOWEVER, if an invalid transaction makes it to a block somehow, the nodes reject the block and waits for a legit block to be mined.
