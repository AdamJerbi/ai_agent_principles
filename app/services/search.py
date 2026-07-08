class SearchService:
    async def index_chunks(self, document_id: str, chunks: list[dict]) -> None:
        # TODO: index chunks in Azure AI Search.
        return None

    async def retrieve(self, document_id: str, query: str, top_k: int = 5) -> list[dict]:
        # TODO: retrieve semantically relevant chunks.
        return []
