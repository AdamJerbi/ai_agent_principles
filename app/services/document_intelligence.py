class DocumentIntelligenceService:
    async def analyze_layout(self, content: bytes) -> dict:
        # TODO: call Azure Document Intelligence prebuilt-layout.
        return {'pages': [], 'tables': [], 'text': ''}
