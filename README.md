# rewards-system-web3
A Simple Web3 based rewards system for final semester project.


# local setup

* Install Ganache (A development blockchain).
* Install truffle `npm install truffle -g`.
* Issue `truffle migrate --reset` to deploy the smart contracts to Ganache.
* add truffle project on ganache for it to recognize contracts. Contracts -> add project -> select truffle-config.js file.
* `pip install web3` to install web3.py library. 
* `python app.py` to run the basic test.


# To be done
* Docker setup of Ganache or Geth (Go Ethereum Client).
* Implementing list balances API.
* Integrating with final year project web system.
* Docker set-up on raspberry pi.
* Moving BlockChain parameters into secrets file (or) accessing all those params from Database of the web app.
* add `require(msg.sender == webAppController, "Invalid access")` to contract functions to ensure SC (Smart Contract) access.
* possible conversion to ERC-20 token. (Barely necessary)
