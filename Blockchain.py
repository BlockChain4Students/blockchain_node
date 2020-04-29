import hashlib
from datetime import datetime


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previous_hash
        self.currentHash = ""

    def calculate_hash(self):
        hash_str = str(self.index) + self.timestamp + self.data + self.previousHash
        hash_res = hashlib.sha256(hash_str.encode())
        return hash_res.hexdigest()


class Blockchain:

    def __init__(self):
        self.chain = [self.calculate_gen_block()]

    def calculate_gen_block(self):
        return Block(0, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "VIPdata", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previousHash = self.get_latest_block().currentHash
        new_block.currentHash = new_block.calculate_hash()
        self.chain.append(new_block)


blockchain = Blockchain()
block = Block