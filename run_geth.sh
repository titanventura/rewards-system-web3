CUR_DIR="$(pwd)"
docker run -d --name ethereum-dev-chain -p 7777:8545 -v $CUR_DIR/blockchain_dir:/tmp/blockchain_dir ethereum/client-go --datadir /tmp/blockchain_dir --http --http.addr 0.0.0.0 --dev --http.corsdomain "https://remix.ethereum.org,http://remix.ethereum.org"