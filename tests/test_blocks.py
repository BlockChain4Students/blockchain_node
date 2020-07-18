import unittest
from datetime import datetime
from blockchain.blockchain_data_structure import Block
from blockchain.blockchain_data_structure import Transaction
from crypto.keygen import generate_key_pair
from Crypto.Hash import SHA256

# --------------------------------------- #
# ----------- Variable Values ----------- #
# --------------------------------------- #

node_identifier = "test"
generate_key_pair(node_identifier)
from_address = "from_address"
to_address = "to_address"
amount = 1.0
difficulty = 2
timestamp = datetime.now
transaction = Transaction(from_address, to_address, amount, node_identifier)

incorrect_transaction = Transaction(from_address, to_address, amount, node_identifier)
incorrect_transaction.amount = -1.0
b_hash = SHA256.new()
b_hash.update("test".encode())
previous_hash = b_hash.hexdigest()

class TestBlockClass(unittest.TestCase):

    # ------------------------------------- #
    # --------- Constructor Tests --------- #
    # ------------------------------------- #

    def test_constructor_correct(self):
        block = Block(timestamp, transaction, 0)
        self.assertEqual(block.timestamp, timestamp)
        self.assertEqual(block.transactions, transaction)
        self.assertEqual(block.index, 0)

    # TODO - Add test for wrong type timestamp
    def test_constructor_null_timestamp(self):
        with self.assertRaises(Exception):
            Block(None, transaction, 0)

    def test_constructor_null_transaction(self):
        with self.assertRaises(Exception):
            Block(timestamp, None, 0)

    def test_constructor_null_transaction_list(self):
        with self.assertRaises(Exception):
            Block(timestamp, [None], 0)

    def test_constructor_transaction_list_with_null(self):
        with self.assertRaises(Exception):
            Block(timestamp, [transaction, None], 0)

    def test_constructor_incorrect_transaction(self):
        with self.assertRaises(Exception):
            Block(timestamp, incorrect_transaction, 0)

    # --------------------------------------- #
    # ------------- Mining Tests ------------ #
    # --------------------------------------- #

    def test_mining_correct_difficulty(self):
        block = Block(timestamp, transaction, 0)
        block.mine_block(difficulty)
        self.assertEqual(block.currentHash[0:difficulty], "".join((["0"] * difficulty)))

    # --------------------------------------- #
    # ------- Transaction Check Tests ------- #
    # --------------------------------------- #

    def test_transaction_check_correct_single(self):
        block = Block(timestamp, transaction, 0)
        self.assertTrue(block.has_valid_transactions(block.transactions))

    def test_transaction_check_correct_list(self):
        block = Block(timestamp, [transaction, transaction], 0)
        self.assertTrue(block.has_valid_transactions(block.transactions))

    def test_transaction_check_invalid_transaction(self):
        block = Block(timestamp, transaction, 0)
        block.transactions = incorrect_transaction
        self.assertFalse(block.has_valid_transactions(block.transactions))

    def test_transaction_check_invalid_transaction_list(self):
        block = Block(timestamp, transaction,  0)
        block.transactions = [transaction, incorrect_transaction]
        self.assertFalse(block.has_valid_transactions(block.transactions))

    # --------------------------------------- #
    # ----------- Integrity Tests ----------- #
    # --------------------------------------- #

    def test_integrity_modified_timestamp(self):
        block = Block(timestamp, transaction, 0)
        block.mine_block(2)
        block.timestamp = datetime.now()
        self.assertNotEqual(block.currentHash, block.calculate_hash())

    def test_integrity_modified_transaction_null(self):
        block = Block(timestamp, Transaction(from_address, to_address, amount, node_identifier), 0)
        block.mine_block(2)
        block.transactions = None
        self.assertNotEqual(block.currentHash, block.calculate_hash())

    def test_integrity_modified_transaction_list(self):
        block = Block(timestamp, [transaction, Transaction(from_address, to_address, amount, node_identifier)], 0)
        block.mine_block(2)
        block.transactions[1] = None
        self.assertNotEqual(block.currentHash, block.calculate_hash())

    def test_integrity_modified_transaction_list_null(self):
        block = Block(timestamp, [transaction, Transaction(from_address, to_address, amount, node_identifier)], 0)
        block.mine_block(2)
        block.transactions = None
        self.assertNotEqual(block.currentHash, block.calculate_hash())

    def test_integrity_modified_index(self):
        block = Block(timestamp, transaction, 0)
        block.mine_block(2)
        block.index = -1
        self.assertNotEqual(block.currentHash, block.calculate_hash())

    def test_integrity_modified_previous_hash(self):
        block = Block(timestamp, transaction, 0, previous_hash)
        block.mine_block(2)
        block.previousHash = "wrongHash"
        self.assertNotEqual(block.currentHash, block.calculate_hash())

    def test_integrity_modified_nonce(self):
        block = Block(timestamp, transaction, 0, previous_hash)
        block.mine_block(2)
        block.nonce = -1    # Pray it doesnt it the correct nonce...
        self.assertNotEqual(block.currentHash, block.calculate_hash())


if __name__ == '__main__':
    unittest.main()