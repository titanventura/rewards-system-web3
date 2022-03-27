from email import utils
from web3 import Web3
from . import utils


class RewardSystem:
    # separated into own method for convenient updation
    def setup(self, bc_url, sc_addr, sc_abi, owner_addr=None, owner_priv_key=None, *args, **kwargs):
        self.w3 = Web3(Web3.HTTPProvider(bc_url))
        self.contract = self.w3.eth.contract(address=sc_addr, abi=sc_abi)

    # (sc_*) means (smart contract *)
    def __init__(self, bc_url, sc_addr, sc_abi, *args, **kwargs) -> None:
        self.setup(bc_url, sc_addr, sc_abi, *args, **kwargs)

    def generate_address(self):
        return utils.generate_address()

    def get_balance(self, addr):
        return self.contract.functions.balanceOf(addr).call()

    def increase_balance(self, addr):
        pass
