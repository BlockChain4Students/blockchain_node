Simple project for illustrating a simple blockchain, testing and learning.

## Requirements:
Python 3.8.3
Docker version 19 (tested with version 19.03.8, build afacb8b7f0)

## Instructions:
Run `./setup` or do the following steps:

### Create Venv
python3 -m pip install --user virtualenv
sudo apt-get install python3-venv
python3 -m venv env_blockchain4students
source env_blockchain4students/bin/activate

You are now in a virtual env

### Define env vars
Duplicate the file .env-example, and rename it to .env. Change the variables value accordingly

### To install requirements run:
pip install -r requirements.txt

## Running the server
Run ```python3 node.py``` to run a node.
The endpoints can be tested with Postman

## Key Management
To delete all keys run `rm *.pem`

## Debugging 
Run `docker ps -a` to list your containers. 
Copy the ID of your container and run `docker logs CONTAINER_ID`