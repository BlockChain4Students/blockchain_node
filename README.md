Simple project for illustrating a simple blockchain, testing and learning.
This project can be installed with ``pip install . ``
## Requirements:
Python 3.8.3

## Create Venv
python3 -m pip install --user virtualenv
sudo apt-get install python3-venv
python3 -m venv env_blockchain4students
source env_blockchain4students/bin/activate
You are now in a virtual env

## Define env vars
Duplicate the file .env-example, and rename it to .env. Change the variables value accordingly
### To install requirements run:
pip install -r requirements.txt

## Running the server
Run ```python node.py``` to run a node.
The endpoints can be tested with Postman

## Using Docker
Run ``docker build -t blockchain4students-node .``

Run ``docker run --rm -p 8001:5000 blockchain4students-node`` to start node 1

Run ``docker run --rm -p 8002:5000 blockchain4students-node`` to start node 2
