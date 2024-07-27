from ..client.yopex_client import YopexClient

async def buy_project(client: YopexClient, project_id: int):
    try:
        tx_hash = client.buy_project(project_id)
        print(f"Project purchased successfully. Transaction hash: {tx_hash}")
        return await tx_hash
    except Exception as e:
        print(f"Failed to buy project: {str(e)}")
        return await None