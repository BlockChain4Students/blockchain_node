import hashlib
from datetime import datetime


class Block:

    def __init__(self, index, timestamp, data):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = ""
        self.currentHash = ""
        self.nonce = 0

    def calculate_hash(self):
        hash_str = str(self.index) + self.timestamp + self.data + self.previousHash + str(self.nonce)
        hash_res = hashlib.sha256(hash_str.encode())
        return hash_res.hexdigest()

    def set_hash(self, hash_code):
        self.currentHash = hash_code

    # Proof-of-work
    def mine_block(self, difficulty):
        compare_str = "".join((["0"] * difficulty))

        while self.currentHash[0:difficulty] != compare_str:
            self.nonce += 1
            self.currentHash = self.calculate_hash()

        print("Block mined:", self.currentHash)

    def print_self(self):
        print("Block with index: ", self.index)
        print(self.timestamp)
        print(self.data)
        print("Previous hash: ", self.previousHash)
        print("Current hash: ", self.currentHash)
        print()


class Blockchain:

    def __init__(self):
        self.chain = [self.calculate_gen_block()]
        self.difficulty = 5  # Determines how long it takes to calculate proof-of-work

    def calculate_gen_block(self):
        gen_block = Block(0, "12/23/2018, 04:59:31", "importantData")
        gen_block.set_hash(gen_block.calculate_hash())
        gen_block.previousHash = "0"
        return gen_block

    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]

    def add_block(self, new_block):
        new_block.previousHash = self.get_latest_block().currentHash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr_block = self.chain[i]
            previous_block = self.chain[i-1]

            if curr_block.currentHash != curr_block.calculate_hash():
                print("Current hash of block", "(" + str(i) + ")",  "is invalid.")
                return False

            elif curr_block.previousHash != previous_block.currentHash:
                print("Hash of previous block", "(" + str(i - 1) + ")",  "is invalid.")
                return False

        return True

    def print_chain(self):
        for bl in self.chain:
            bl.print_self()


########################################################################################################################


blockchain = Blockchain()

block1 = Block(1, "12/24/2018, 04:59:31", "importantData2")
block2 = Block(2, "12/25/2018, 04:59:31", "importantData3")

print("Mining block 1...")
blockchain.add_block(block1)

print("Mining block 2...")
blockchain.add_block(block2)

print("Is chain valid? ", blockchain.is_chain_valid())

print("Tampering block1's data...")
block1.data = "DifferentData"

print("Is chain valid? ", blockchain.is_chain_valid())

print("Tampering block1's hash...")
block1.set_hash(block1.calculate_hash())

print("Is chain valid? ", blockchain.is_chain_valid())
