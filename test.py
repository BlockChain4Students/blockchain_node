from blockchain.blockchain_data_structure import Blockchain
from crypto.keygen import generate_key_pair


blockchain = Blockchain("catarina-address", "test", '0.0.0.0', 5000)

print(blockchain)
blockchain.create_transaction("address1", "address2", 100.0)
blockchain.create_transaction("address2", "address1", 50.0)
blockchain.create_transaction("address2", "address1", 20.0)

print("Balance of catarina-address is: ", blockchain.get_balance("catarina-address"))
print("Balance of address-1 is: ", blockchain.get_balance("address1"))
print("Balance of address-2 is: ", blockchain.get_balance("address2"))

blockchain.create_transaction("address1", "address2", 20.0)
blockchain.create_transaction("address2", "address1", 50.0)

print("Balance of catarina-address is: ", blockchain.get_balance("catarina-address"))
print("Balance of address-1 is: ", blockchain.get_balance("address1"))
print("Balance of address-2 is: ", blockchain.get_balance("address2"))

print("Blockchain size: ", len(blockchain.chain))