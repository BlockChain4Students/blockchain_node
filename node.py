#https://flask.palletsprojects.com/en/1.1.x/
from uuid import uuid4
from datetime import datetime
from flask import Flask
from blockchain.blockchain_data_structure import Blockchain
import json

#group of nodes participating on the network
peers = set()

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    result = blockchain.mine_pending_transactions()
    if not result:
        return "No pending tx"
    return result


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()

    tx_data["timestamp"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    #blockchain.create_transaction()

    return "Success", 200


@app.route('/getChain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return json.dumps(response), 200

@app.route('/pendingTransactions', methods=['GET'])
def getPendingTransactions():
    return json.dumps(blockchain.pending_transactions), 200

@app.route('/registerNode', methods=['POST'])
def register_peer_node():
    node_address = request.get_json()["node_address"]
    peers.add(node_address)
    return get_chain()

#TODO
#@app.route('/register_with', methods=['POST'])
#def register_with_existing_node():

#TODO
#@app.route('/add_block', methods=['POST'])
#def add_and_announce_block():


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)