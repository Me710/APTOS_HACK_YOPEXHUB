from ..client.yopex_client import YopexClient
from aptos_sdk.account import Account
from aptos_sdk.client import RestClient
from ..utils.constants import NODE_URL

async def create_project(account: Account, name: str, description: str, price: int):
    rest_client = RestClient(NODE_URL)
    client = YopexClient(account,rest_client)
    tx_hash = client.create_project(name, description, price)
    print(f"Project created. Transaction hash: {tx_hash}")