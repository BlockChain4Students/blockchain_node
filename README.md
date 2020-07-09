Simple project for illustrating a simple blockchain, testing and learning.
This project can be installed with ``pip install . ``
## Requirements:
Python 3.8.3

### To install requirements run:
pip install -r requirements.txt

## Running the server
Run ```python node.py``` to run a node.
The endpoints can be tested with Postman

## Using Docker
Run ``docker build -t blockchain4students-node .``

Run ``docker run --rm -p 8001:5000 blockchain4students-node`` to start node 1

Run ``docker run --rm -p 8002:5000 blockchain4students-node`` to start node 2
