from web3 import Web3


class RewardSystem:

    def setup(self, bc_url, sc_addr, sc_abi, owner_addr=None, *args, **kwargs):
        self.w3 = Web3(Web3.HTTPProvider(bc_url))
        from web3.middleware import geth_poa_middleware
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.contract = self.w3.eth.contract(address=sc_addr, abi=sc_abi)
        self.owner = owner_addr

    def __init__(self, bc_url, sc_addr, sc_abi, owner_addr=None, *args, **kwargs):
        self.setup(bc_url, sc_addr, sc_abi, owner_addr, *args, **kwargs)

    def balance(self, user):
        return self.contract.functions.balanceOf(user).call()

    def tx_config(self):
        return {
            'from': self.owner
        }

    def increase_balance(self, user, amount):
        tx_hash = self.contract.functions.mint(
            user, amount).transact(self.tx_config())
        receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt

    def decrease_balance(self, user, user_priv_key, amount):

        exception_str = "Unable to update balance"

        init_bal = self.balance(user)

        burn_func_call = self.contract.functions.burn(amount)

        tx = burn_func_call.buildTransaction({
            'chainId': self.w3.eth.chain_id,
            'gas': 1000000,
            'gasPrice': self.w3.toWei(100, 'gwei'),
            'nonce': self.w3.eth.get_transaction_count(user),
            # 'gasLimit': Web3.toHex(100000),
            # 'nonce': self.w3.eth.getBlock("latest"),
            'from': user
        })

        from eth_account import Account

        signed_tx = Account.sign_transaction(tx, user_priv_key)

        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        final_bal = self.balance(user)

        if init_bal - amount != final_bal:
            raise Exception(exception_str)

        return tx_receipt
