geth --datadir chain_storage/ --networkid 2101233 --http.api "db,eth,net,web3,personal,miner,admin,txpool,debug" --http --http.port 7777 --allow-insecure-unlock --http.corsdomain "*" --http.addr 0.0.0.0 --http.vhosts "*" console 2>> chain_log