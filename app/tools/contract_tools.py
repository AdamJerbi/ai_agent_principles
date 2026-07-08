from typing import Any


def register_contract_tools(mcp: Any) -> None:
    @mcp.tool()
    def extract_contract_parties(chunks: list[dict]) -> dict:
        '''Extract parties from candidate contract chunks.'''
        return {'parties': [], 'missing': True, 'source_chunks': [c.get('chunk_id') for c in chunks]}

    @mcp.tool()
    def extract_contract_dates(chunks: list[dict]) -> dict:
        '''Extract important contract dates from candidate chunks.'''
        return {'dates': [], 'missing': True, 'source_chunks': [c.get('chunk_id') for c in chunks]}

    @mcp.tool()
    def extract_payment_terms(chunks: list[dict]) -> dict:
        '''Extract payment terms, amounts, currency and invoice conditions.'''
        return {'payment_terms': [], 'missing': True, 'source_chunks': [c.get('chunk_id') for c in chunks]}
