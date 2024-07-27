from ..client.yopex_client import YopexClient

async def list_project(client: YopexClient, project_id: int, price: int):
    try:
        tx_hash = client.list_project(project_id, price)
        print(f"Project listed successfully. Transaction hash: {tx_hash}")
        return await tx_hash
    except Exception as e:
        print(f"Failed to list project: {str(e)}")
        return await None