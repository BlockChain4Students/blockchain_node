import hashlib
from datetime import datetime
from uuid import uuid4
import json
from blockchain.consensus import ProofOfWork
from Crypto.Hash import SHA256
import requests


class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.id = str(uuid4())
        self.fromAddress = from_address
        self.toAddress = to_address
        self.amount = amount
        # self.signature = signature

    def __repr__(self):
        return "Transaction " + self.id


class Block:

    def __init__(self, timestamp, transactions, index):
        self.timestamp = timestamp
        self.transactions = transactions
        self.index = index
        self.previousHash = ""
        self.currentHash = ""
        self.nonce = 0
        global h
        h = SHA256.new()  # Find a better place to put this in

    def __repr__(self):
        return self.timestamp + self.transactions + "Previous hash: " + self.previousHash + self.currentHash

    def calculate_hash(self):
        h.update(b'str(self.__dict__)')
        return h.hexdigest()

    def set_hash(self, hash_code):
        self.currentHash = hash_code

    # Proof-of-work
    def mine_block(self, difficulty):
        ProofOfWork(self, difficulty).mine_block()

    def print_self(self):
        print(self.timestamp)
        print(self.transactions)
        print("Previous hash: ", self.previousHash)
        print("Current hash: ", self.currentHash)
        print()

    def serialize(self):
        return json.dumps(self, sort_keys=True).encode('utf-8')


class Blockchain:
    def __init__(self, miner_address, host, port):
        # Node Location
        self.address = '{}:{}'.format(host, port)

        # Node Discovery
        self.discovery_node_address = '0.0.0.0:5000'

        self.chain = [self.calculate_gen_block()]

        self.pending_transactions = []  # Due to proof-of-work phase

        self.peer_nodes = set()

        self.miner_address = miner_address  # Mined block rewards will always want to go to my own address
        # Constants
        self.difficulty = 2  # Determines how long it takes to calculate proof-of-work
        self.miningReward = 100  # Reward if a new block is successfully mined
        self.number_of_transactions = 3  # Number of transactions it waits to create a block


    def __repr__(self):
        return "class" + str(self.__class__)

    def calculate_gen_block(self):
        gen_block = Block(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), Transaction(None, " ", 0), 0)
        gen_block.set_hash(gen_block.calculate_hash())
        gen_block.previousHash = "0"
        return gen_block

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def mine_pending_transactions(self):
        latest_block_index = self.get_latest_block().index + 1
        block = Block(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), self.pending_transactions,
                      latest_block_index)  # Not possible to do it like this in real blockchains
        block.previousHash = self.get_latest_block().currentHash
        block.mine_block(self.difficulty)

        print("Block successfully mined!")
        self.chain.append(block)

        self.pending_transactions = [
            Transaction(None, self.miner_address, self.miningReward)
            # The miner is rewarded with coins for mining this block, but only when the next block is mined
        ]
        #add sanity checks
        return "Block mined"

    def create_transaction(self, from_address, to_address, ammount):
        transaction = Transaction(from_address, to_address, ammount)
        self.pending_transactions.append(transaction)
        if len(self.pending_transactions) >= self.number_of_transactions:
            self.mine_pending_transactions()

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            if isinstance(block.transactions, Transaction):  # If there is only one transaction
                if address == block.transactions.toAddress:
                    balance += block.transactions.amount

                if address == block.transactions.fromAddress:
                    balance -= block.transactions.amount
            else:
                for transaction in block.transactions:
                    if address == transaction.toAddress:
                        balance += transaction.amount

                    if address == transaction.fromAddress:
                        balance -= transaction.amount

        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if curr_block.currentHash != curr_block.calculate_hash():
                print("Current hash of block", "(" + str(i) + ")", "is invalid.")
                return False

            elif curr_block.previousHash != previous_block.currentHash:
                print("Hash of previous block", "(" + str(i - 1) + ")", "is invalid.")
                return False

        return True

    def print_chain(self):
        for bl in self.chain:
            bl.print_self()

    def register_node(self, address):
        self.peer_nodes.add(address)

    def obtain_peer_node(self):
        if self.address != self.discovery_node_address:
            self.peer_nodes.add(self.discovery_node_address)    # Assuming it never crashes
            response = requests.post('http://{}/register/node'.format(self.discovery_node_address),
                                     json={'node_address': '{}'.format(self.address)}).json()

            for address in response['total_nodes']:
                # Add and register all peers
                self.peer_nodes.add(address)
                requests.post('http://{}/register/node'.format(address),
                              json={'node_address': '{}'.format(self.address)})

            print(self.peer_nodes)

########################################################################################################################
