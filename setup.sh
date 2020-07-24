docker build -t blockchain4studets/blockchain-node:0.1 .
docker run -e "PORT=5001" -p 5001:5001 blockchain4studets/blockchain-node:0.1
docker run -e "PORT=5002" -p 5002:5002 blockchain4studets/blockchain-node:0.1
docker run -e "PORT=5003" -p 5003:5003 blockchain4studets/blockchain-node:0.1