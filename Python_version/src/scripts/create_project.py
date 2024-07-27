from ..client.yopex_client import YopexClient
from aptos_sdk.account import Account
from aptos_sdk.client import RestClient
from ..utils.constants import NODE_URL

async def create_project(client: YopexClient, name: str, description: str, price: int):
    try:
        tx_hash = await client.create_project(name, description, price)
        print(f"Project created successfully. Transaction hash: {tx_hash}")
        return tx_hash
    except Exception as e:
        print(f"Failed to create project: {str(e)}")
        return None