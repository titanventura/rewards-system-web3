from web3 import Web3
from . import utils


class RewardSystem:

    def setup(self, bc_url, sc_addr, sc_abi, owner_addr=None, *args, **kwargs):
        self.w3 = Web3(Web3.HTTPProvider(bc_url))
        self.contract = self.w3.eth.contract(address=sc_addr, abi=sc_abi)
        self.owner = owner_addr

    def __init__(self, bc_url, sc_addr, sc_abi, owner_addr=None, *args, **kwargs):
        self.setup(bc_url, sc_addr, sc_abi, owner_addr, *args, **kwargs)

    def generate_address(self):
        return utils.generate_address()

    def balance(self, user):
        return self.contract.functions.balanceOf(user).call()

    def tx_config(self):
        return {
            'from': self.owner
        }

    def update_balance(self, user, amount, to_increase):

        exception_str = "Unable to update balance"

        init_bal = self.balance(user)

        upd_bal_func = self.contract.functions.increaseAsset if to_increase else self.contract.functions.decreaseAsset

        upd_bal_func = upd_bal_func(
            user,
            amount
        )

        upd_bal_res = upd_bal_func.call()

        if not upd_bal_res:
            raise Exception(exception_str)

        tx_hash = upd_bal_func.transact(self.tx_config())

        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)

        latest_bal = self.balance(user)

        upd_amt = amount if to_increase else -amount

        if init_bal + upd_amt != latest_bal:
            raise Exception(exception_str)

        return tx_receipt


