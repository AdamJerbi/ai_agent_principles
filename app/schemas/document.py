from pydantic import BaseModel, Field


class DocumentJobRequest(BaseModel):
    file_name: str = Field(description='Original document name')
    content_type: str | None = None
    task: str = Field(default='analyze', description='extract, compare, annotate, or analyze')


class DocumentJobResponse(BaseModel):
    request_id: str
    status: str


class DocumentChunk(BaseModel):
    chunk_id: str
    document_id: str
    text: str
    page_start: int | None = None
    page_end: int | None = None
    section_title: str | None = None
