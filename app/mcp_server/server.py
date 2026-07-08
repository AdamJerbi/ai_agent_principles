from mcp.server.fastmcp import FastMCP
from app.tools.contract_tools import register_contract_tools
from app.tools.comparison_tools import register_comparison_tools
from app.tools.annotation_tools import register_annotation_tools

mcp = FastMCP('enterprise-document-tools')
register_contract_tools(mcp)
register_comparison_tools(mcp)
register_annotation_tools(mcp)


if __name__ == '__main__':
    mcp.run()
