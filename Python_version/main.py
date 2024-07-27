import asyncio
from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
from src.client.yopex_client import YopexClient
from src.scripts.create_project import create_project
from src.scripts.list_project import list_project
from src.scripts.buy_project import buy_project
from src.utils.constants import NODE_URL, FAUCET_URL

async def main():
    rest_client = RestClient(NODE_URL)
    faucet_client = FaucetClient(FAUCET_URL, rest_client)

    # Alice's account details
    alice = Account.load_key("0xe2e30d389b2963377be892787620cc918603f5f4c40229523fb08231e4ff3611")
    bob = Account.generate()

    print("\n=== Addresses ===")
    print(f"Alice: {alice.address()}")
    print(f"Bob: {bob.address()}")

    # Fund accounts
    faucet_client.fund_account(alice.address(), 100_000_000)
    faucet_client.fund_account(bob.address(), 100_000_000)

    print("\n=== Initial Balances ===")
    alice_balance = rest_client.account_balance(alice.address())
    bob_balance = rest_client.account_balance(bob.address())
    print(f"Alice: {alice_balance}")
    print(f"Bob: {bob_balance}")

    # Create YopexClients
    alice_client = YopexClient(alice, rest_client)
    bob_client = YopexClient(bob, rest_client)

    # Alice creates a project
    project_name = "AI Assistant"
    project_description = "An AI-powered assistant for productivity"
    project_price = 100000000  # 1 APT = 100000000 octas

    create_result = create_project(alice_client, project_name, project_description, project_price)
    if create_result is None:
        print("Project creation failed. Exiting.")
        return

    print(f"Project created with transaction hash: {create_result}")

    # List projects
    projects = await list_project(alice_client)
    if projects:
        print("Available projects:")
        for project in projects:
            print(f"Name: {project['name']}, Description: {project['description']}, Price: {project['price']}")
    else:
        print("No projects available.")
        return

    # Bob buys the project
    if projects:
        project_to_buy = projects[0]  # Assuming we want to buy the first project
        buy_result = await buy_project(bob_client, project_to_buy['name'])
        if buy_result:
            print(f"Project bought successfully. Transaction hash: {buy_result}")
        else:
            print("Failed to buy the project.")

    print("\n=== Final Balances ===")
    alice_balance = await rest_client.account_balance(alice.address())
    bob_balance = await rest_client.account_balance(bob.address())
    print(f"Alice: {alice_balance}")
    print(f"Bob: {bob_balance}")

    await rest_client.close()

if __name__ == "__main__":
    asyncio.run(main())