#https://flask.palletsprojects.com/en/1.1.x/
from uuid import uuid4
from datetime import datetime
from flask import Flask
from flask import request
from blockchain.blockchain_data_structure import Blockchain
import json
import jsonpickle

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain



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
    #TODO input sanitization
    tx_data = request.get_json()

    tx_data["timestamp"] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    blockchain.create_transaction(tx_data["from_address"], tx_data["to_address"], tx_data["ammount"])

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


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    host = '0.0.0.0'
    blockchain = Blockchain("catarina-address", host, port)
    blockchain.obtain_peer_node()
    app.run(host=host, port=port)