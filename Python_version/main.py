import asyncio
from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
from src.client.yopex_client import YopexClient
from src.storage.project_storage import ProjectStorage
from src.utils.constants import NODE_URL, FAUCET_URL

async def main():
    rest_client = RestClient(NODE_URL)
    faucet_client = FaucetClient(FAUCET_URL, rest_client)

    alice = Account.load_key("0xe2e30d389b2963377be892787620cc918603f5f4c40229523fb08231e4ff3611")
    bob = Account.generate()

    print("\n=== Addresses ===")
    print(f"Alice: {alice.address()}")
    print(f"Bob: {bob.address()}")

    faucet_client.fund_account(bob.address(), 100_000_000)

    print("\n=== Initial Balances ===")
    alice_balance = rest_client.account_balance(alice.address())
    bob_balance = rest_client.account_balance(bob.address())
    print(f"Alice: {alice_balance}")
    print(f"Bob: {bob_balance}")

    alice_client = YopexClient(alice, rest_client)
    bob_client = YopexClient(bob, rest_client)

    project_storage = ProjectStorage()

    # Bob creates a project
    project = project_storage.create_project(
        name="AI Assistant",
        description="An AI-powered assistant for productivity",
        price=1_000_000,  # 0.01 APT
        owner=bob.address().hex()
    )
    print(f"Project created: {project}")

    # Alice buys the project
    try:
        txn_hash = rest_client.transfer(alice, bob.address(), 1_000)
        rest_client.wait_for_transaction(txn_hash)
        print(f"Payment successful. Transaction hash: {txn_hash}")

    except Exception as e:
        print(f"Error making payment: {str(e)}")

    print("\n=== Final Balances ===")
    alice_balance = rest_client.account_balance(alice.address())
    bob_balance = rest_client.account_balance(bob.address())
    print(f"Alice: {alice_balance}")
    print(f"Bob: {bob_balance}")

    rest_client.close()

if __name__ == "__main__":
    asyncio.run(main())