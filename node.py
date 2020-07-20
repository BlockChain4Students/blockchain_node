#https://flask.palletsprojects.com/en/1.1.x/
from uuid import uuid4
from datetime import datetime
from flask import Flask
from flask import request
from blockchain.blockchain_data_structure import Blockchain
from crypto.keygen import generate_key_pair
import json
import jsonpickle

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Obtain public/private key_pair for this node
generate_key_pair(node_identifier)


@app.route('/getChain', methods=['GET'])
def get_chain():
    response = {
        'chain': jsonpickle.encode(blockchain.chain),   # We may want to create a JSON encoder for "prettier" results
        'blockIndex': len(blockchain.chain),
        'metadata': blockchain.miningReward
    }
    return json.dumps(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()

    tx_data["timestamp"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    try:
        check_transaction_arguments(tx_data["from_address"], tx_data["to_address"], tx_data["amount"])
    except Exception as e:
        json_arguments = ["from_address", "to_address", "amount"]
        for argument in json_arguments:
            if argument not in tx_data:
                return "Transaction must have a " + argument

        return str(e), 200

    blockchain.create_transaction(tx_data["from_address"], tx_data["to_address"], tx_data["amount"])
    return "Success", 200


@app.route('/transactions/pending', methods=['GET'])
def get_pending_transactions():
    return jsonpickle.encode(blockchain.pending_transactions), 200


@app.route('/register/node', methods=['POST'])
def register_peer_node():
    node_address = request.get_json()["node_address"]

    response = {
        'message': 'Node added',
        'total_nodes': list(blockchain.peer_nodes),
    }
    blockchain.register_node(node_address)
    return json.dumps(response), 200


@app.route('/peers', methods=['GET'])
def get_known_peers():
    return json.dumps(list(blockchain.peer_nodes)), 200

# Do we still need these functions?
#TODO
#@app.route('/register_with', methods=['POST'])
#def register_with_existing_node():

#TODO
#@app.route('/add_block', methods=['POST'])
#def add_and_announce_block():

def check_transaction_arguments(from_address, to_address, amount):
    if not to_address or not from_address:
        raise Exception("Transaction must have a from and to destination address")

    # What type should from and to address be? How do we define public keys?
    # TODO - Add from and to address type checks

    if not type(amount) is float:
        raise Exception("Transaction amount must be a float value")

    if amount < 0:
        raise Exception("Transaction amount must be greater or equal than 0")

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    host = '0.0.0.0'
    blockchain = Blockchain("catarina-address", node_identifier, host, port)
    blockchain.obtain_peer_node()
    app.run(host=host, port=port)