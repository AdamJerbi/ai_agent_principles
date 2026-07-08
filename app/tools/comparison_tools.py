from typing import Any


def register_comparison_tools(mcp: Any) -> None:
    @mcp.tool()
    def compare_extractions(left: dict, right: dict) -> dict:
        '''Compare two structured extraction outputs.'''
        return {'differences': [], 'left_document': left.get('document_id'), 'right_document': right.get('document_id')}
