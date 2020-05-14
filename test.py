from blockchain.blockchain_data_structure import Blockchain
from blockchain.blockchain_data_structure import Transaction

blockchain = Blockchain()
print(blockchain)
blockchain.create_transaction(Transaction("address1", "address2", 100))
blockchain.create_transaction(Transaction("address2", "address1", 50))

blockchain.mine_pending_transactions("catarina-address")

print("Balance of catarina-address is: ", blockchain.get_balance("catarina-address"))
print("Balance of address-1 is: ", blockchain.get_balance("address1"))
print("Balance of address-2 is: ", blockchain.get_balance("address2"))

blockchain.mine_pending_transactions("catarina-address")

print("Balance of catarina-address is: ", blockchain.get_balance("catarina-address"))