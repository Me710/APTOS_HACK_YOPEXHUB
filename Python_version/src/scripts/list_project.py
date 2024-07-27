from ..client.yopex_client import YopexClient

async def list_projects(client: YopexClient):
    try:
        projects = await client.list_projects()
        print(f"Projects listed successfully.")
        return projects
    except Exception as e:
        print(f"Failed to list projects: {str(e)}")
        return None