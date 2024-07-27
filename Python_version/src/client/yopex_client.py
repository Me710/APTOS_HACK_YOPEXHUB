# src/client/yopex_client.py
from aptos_sdk.account import Account
from aptos_sdk.client import RestClient
from aptos_sdk.transactions import EntryFunction, TransactionArgument
from aptos_sdk.bcs import Serializer


class YopexClient:
    def __init__(self, account: Account, client: RestClient):
        self.account = account
        self.client = client

    async def pay_for_project(self, recipient: str, amount: int):
        payload = EntryFunction.natural(
            "0x1::coin",  # The Coin module in the Aptos standard library
            "transfer",
            [TransactionArgument("0x1::aptos_coin::AptosCoin", Serializer.struct)],  # Type argument for AptosCoin
            [
                TransactionArgument(recipient, Serializer.struct),  # Recipient address
                TransactionArgument(amount, Serializer.u64),  # Amount to transfer
            ],
        )

        signed_transaction = await self.client.create_bcs_signed_transaction(
            self.account, payload
        )
        return await self.client.submit_bcs_transaction(signed_transaction)