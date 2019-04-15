docker build -t data-node .
docker run -p 8000:80 -d data-node 