from langchain_mcp_adapters.client import MultiServerMCPClient


async def load_mcp_tools(command: str = 'python', server_path: str = 'app/mcp_server/server.py'):
    client = MultiServerMCPClient({
        'document_tools': {
            'transport': 'stdio',
            'command': command,
            'args': [server_path],
        }
    })
    return await client.get_tools()


def select_tools_by_prefix(tools: list, prefix: str) -> list:
    return [tool for tool in tools if tool.name.startswith(prefix)]
