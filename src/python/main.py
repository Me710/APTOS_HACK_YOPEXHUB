from aptos_sdk.account import Account
from aptos_sdk.client import RestClient
from aptos_sdk.transactions import EntryFunction, TransactionArgument, TransactionPayload
from aptos_sdk.type_tag import TypeTag, StructTag
from typing import List
import time

# Constants
NODE_URL = "https://fullnode.devnet.aptoslabs.com/v1"
YOPEX_MODULE_ADDRESS = "0x1"  # Replace with your deployed module address
YOPEX_MODULE_NAME = "yopex"

class YopexClient:
    def __init__(self, account: Account):
        self.account = account
        self.client = RestClient(NODE_URL)

    def create_project(self, name: str, description: str, price: int) -> str:
        payload = EntryFunction.natural(
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}",
            "create_project",
            [],
            [
                TransactionArgument(name, Serializer.str),
                TransactionArgument(description, Serializer.str),
                TransactionArgument(price, Serializer.u64),
            ]
        )
        signed_tx = self.client.create_bcs_signed_transaction(self.account, TransactionPayload(payload))
        tx_hash = self.client.submit_bcs_transaction(signed_tx)
        self.client.wait_for_transaction(tx_hash)
        return tx_hash

    def list_project(self, project_id: int, price: int) -> str:
        payload = EntryFunction.natural(
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}",
            "list_project",
            [],
            [
                TransactionArgument(project_id, Serializer.u64),
                TransactionArgument(price, Serializer.u64),
            ]
        )
        signed_tx = self.client.create_bcs_signed_transaction(self.account, TransactionPayload(payload))
        tx_hash = self.client.submit_bcs_transaction(signed_tx)
        self.client.wait_for_transaction(tx_hash)
        return tx_hash

    def buy_project(self, project_id: int) -> str:
        payload = EntryFunction.natural(
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}",
            "buy_project",
            [],
            [TransactionArgument(project_id, Serializer.u64)]
        )
        signed_tx = self.client.create_bcs_signed_transaction(self.account, TransactionPayload(payload))
        tx_hash = self.client.submit_bcs_transaction(signed_tx)
        self.client.wait_for_transaction(tx_hash)
        return tx_hash

    def get_projects(self) -> List[dict]:
        response = self.client.account_resource(
            self.account.address(),
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}::ProjectStore"
        )
        return response["data"]["projects"]

def main():
    # Create two user accounts
    alice = Account.generate()
    bob = Account.generate()

    # Initialize Yopex clients for both users
    alice_client = YopexClient(alice)
    bob_client = YopexClient(bob)

    # Alice creates a project
    print("Alice is creating a project...")
    alice_client.create_project("AI Assistant", "An AI-powered assistant for productivity", 100000000)  # 1 APT

    # Get Alice's projects
    alice_projects = alice_client.get_projects()
    print(f"Alice's projects: {alice_projects}")

    # Alice lists her project for sale
    print("Alice is listing her project for sale...")
    alice_client.list_project(0, 150000000)  # 1.5 APT

    # Bob buys Alice's project
    print("Bob is buying Alice's project...")
    bob_client.buy_project(0)

    # Get updated projects for both users
    alice_projects = alice_client.get_projects()
    bob_projects = bob_client.get_projects()

    print(f"Alice's projects after sale: {alice_projects}")
    print(f"Bob's projects after purchase: {bob_projects}")

if __name__ == "__main__":
    main()