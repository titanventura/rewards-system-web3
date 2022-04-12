
import json

import web3

from rewards_system.api import RewardSystem


SC_ADDR = web3.Web3.toChecksumAddress(
    '0x925A9dBF0451082c8eD1EAc8402f6ff155e43C2f'
)
OWNER = web3.Web3.toChecksumAddress(
    '0x235d7c1bfe2d8d9c12490c3b6756755e65777cd7'
)

BC_URL = 'http://localhost:7777'

SC_ABI_STRING = open("./build/contracts/KCLToken.json").read()
SC_ABI = json.loads(SC_ABI_STRING)['abi']

alice_addr = web3.Web3.toChecksumAddress(
    '0x1d65b15FAC39608c0C81Cb8edd9B0A5cB51ef713'
)
alice_priv = '0xa11e078b1544b4ff86b99675408830da03fabed6496f1ade9643db634b63af46'


def main():
    rs = RewardSystem(
        BC_URL,
        SC_ADDR,
        SC_ABI,
        OWNER
    )

    print(rs.balance(alice_addr))

    # rs.increase_balance(alice_addr, 200)

    x = rs.decrease_balance(alice_addr, alice_priv, 200)
    print(x)

    print(rs.balance(alice_addr))


if __name__ == '__main__':
    main()
