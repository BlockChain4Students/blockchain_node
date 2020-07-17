import unittest
from blockchain.blockchain_data_structure import Transaction
from crypto.keygen import generate_key_pair

# --------------------------------------- #
# ----------- Variable Values ----------- #
# --------------------------------------- #

node_identifier = "test"
from_address = "from_address"
to_address = "to_address"
amount = 1.0

class TestTransactionClass(unittest.TestCase):


    generate_key_pair(node_identifier)

    # ------------------------------------- #
    # --------- Constructor Tests --------- #
    # ------------------------------------- #

    def test_constructor_correct(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        self.assertEqual(transaction.fromAddress, from_address)
        self.assertEqual(transaction.toAddress, to_address)
        self.assertEqual(transaction.amount, amount)

    def test_constructor_null_to_address(self):
        with self.assertRaises(Exception):
            Transaction(from_address, None, amount, node_identifier)

    def test_constructor_negative_amount(self):
        with self.assertRaises(Exception):
            Transaction(from_address, to_address, -1.0, node_identifier)

    def test_constructor_non_float_amount(self):
        with self.assertRaises(Exception):
            Transaction(from_address, to_address, 2, node_identifier)

    def test_constructor_none_amount(self):
        with self.assertRaises(Exception):
            Transaction(from_address, to_address, None, node_identifier)

    def test_constructor_none_node_id(self):
        with self.assertRaises(Exception):
            Transaction(from_address, to_address, amount, None)

    # TODO - Add to and from address type check test
    # TODO - Add amount type check test

    # --------------------------------------- #
    # ----------- Integrity Tests ----------- #
    # --------------------------------------- #

    # TODO - Can we test if hash/signature itself is correct?

    def test_integrity_modified_id(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        transaction.id = "fake_id"
        self.assertFalse(transaction.check_valid())

    def test_integrity_modified_from_address(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        transaction.fromAddress = "fake_from_address"
        self.assertFalse(transaction.check_valid())

    def test_integrity_modified_to_address(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        transaction.toAddress = "fake_to_address"
        self.assertFalse(transaction.check_valid())

    def test_integrity_modified_amount(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        transaction.amount = 2
        self.assertFalse(transaction.check_valid())

    def test_integrity_modified_node_id(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        transaction.node_id = "test2"
        self.assertFalse(transaction.check_valid())

    def test_integrity_modified_signature(self):
        transaction = Transaction(from_address, to_address, amount, node_identifier)
        transaction.signature = bytes('test', encoding='utf-8')
        self.assertFalse(transaction.check_valid())

if __name__ == '__main__':
    unittest.main()