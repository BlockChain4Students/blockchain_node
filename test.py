from blockchain.blockchain_data_structure import Blockchain
from blockchain.blockchain_data_structure import Transaction

blockchain = Blockchain("catarina-address")
print(blockchain)
blockchain.create_transaction("address1", "address2", 100)
blockchain.create_transaction("address2", "address1", 50)
blockchain.create_transaction("address2", "address1", 20)

print("Balance of catarina-address is: ", blockchain.get_balance("catarina-address"))
print("Balance of address-1 is: ", blockchain.get_balance("address1"))
print("Balance of address-2 is: ", blockchain.get_balance("address2"))

blockchain.create_transaction("address1", "address2", 20)
blockchain.create_transaction("address2", "address1", 50)

print("Balance of catarina-address is: ", blockchain.get_balance("catarina-address"))
print("Balance of address-1 is: ", blockchain.get_balance("address1"))
print("Balance of address-2 is: ", blockchain.get_balance("address2"))

print("Blockchain size: ", len(blockchain.chain))