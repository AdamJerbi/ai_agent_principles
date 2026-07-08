from typing import Any


def register_annotation_tools(mcp: Any) -> None:
    @mcp.tool()
    def create_annotations(extraction: dict) -> dict:
        '''Create page or chunk-level annotations from extraction evidence.'''
        return {'annotations': [], 'source_document': extraction.get('document_id')}
