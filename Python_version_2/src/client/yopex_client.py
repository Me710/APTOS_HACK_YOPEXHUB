from aptos_sdk.account import Account
from aptos_sdk.client import RestClient
from aptos_sdk.transactions import EntryFunction, TransactionArgument, TransactionPayload
from aptos_sdk.type_tag import TypeTag, StructTag
from src.utils.constants import YOPEX_MODULE_ADDRESS, YOPEX_MODULE_NAME

class YopexClient:
    def __init__(self, account: Account, rest_client: RestClient):
        self.account = account
        self.rest_client = rest_client

    async def create_project(self, name: str, description: str, price: int):
        payload = EntryFunction(
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}",
            "create_project",
            [],
            [
                TransactionArgument(name, Seq[U8]),
                TransactionArgument(description, Seq[U8]),
                TransactionArgument(price, U64),
            ],
        )
        return await self._submit_transaction(payload)

    async def list_projects(self):
        payload = EntryFunction(
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}",
            "list_projects",
            [],
            [],
        )
        return await self._submit_transaction(payload)

    async def buy_project(self, name: str):
        payload = EntryFunction(
            f"{YOPEX_MODULE_ADDRESS}::{YOPEX_MODULE_NAME}",
            "buy_project",
            [],
            [TransactionArgument(name, Seq[U8])],
        )
        return await self._submit_transaction(payload)

    async def _submit_transaction(self, payload: EntryFunction):
        try:
            txn_hash = await self.rest_client.submit_bcs_transaction(self.account, TransactionPayload(payload))
            await self.rest_client.wait_for_transaction(txn_hash)
            return txn_hash
        except Exception as e:
            print(f"Error submitting transaction: {e}")
            return None