class BlobStorageService:
    def __init__(self, container_name: str) -> None:
        self.container_name = container_name

    async def upload_document(self, document_id: str, content: bytes) -> str:
        # TODO: implement Azure Blob Storage upload.
        return f'blob://{self.container_name}/{document_id}'

    async def download_document(self, blob_uri: str) -> bytes:
        # TODO: implement Azure Blob Storage download.
        return b''
