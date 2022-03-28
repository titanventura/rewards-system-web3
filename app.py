from rewards_system.api import RewardSystem
import json

blockchain_url = "http://127.0.0.1:7545"
sc_addr = "0x2a018E28091F62FC11deB6197B1b48671C63335e"
sc_abi = json.dumps(
    json.loads(
        open("./build/contracts/RewardsSystem.json").read()
    )['abi']
)
owner_addr = "0x47E2101437202F44c094BFEb6863CCa4678Bf9f3"


def main():
    try:
        rwd = RewardSystem(
            blockchain_url,
            sc_addr,
            sc_abi,
            owner_addr
        )

        alice = rwd.generate_address()

        bob = rwd.generate_address()

        print(" this is alice ", alice)
        print(" this is bob ", bob)

        # alice and bob deposit 100 coins to their account

        rwd.update_balance(alice, 100, to_increase=True)
        rwd.update_balance(bob, 100, to_increase=True)

        alice_bal = rwd.balance(alice)
        bob_bal = rwd.balance(bob)
        print(alice_bal == bob_bal == 100, " both alice and bob bal are 100")

        # alice decreased by 10 coins, bob by 5 coins

        rwd.update_balance(alice, 10, to_increase=False)
        rwd.update_balance(bob, 5, to_increase=False)

        alice_bal = rwd.balance(alice)
        bob_bal = rwd.balance(bob)

        print(alice_bal == 90, " bal updated alice")
        print(bob_bal == 95, " bal updated bob")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
