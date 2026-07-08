from pydantic import BaseModel


class Evidence(BaseModel):
    chunk_id: str | None = None
    page_start: int | None = None
    page_end: int | None = None
    quote: str | None = None


class ExtractedField(BaseModel):
    name: str
    value: str | None
    confidence: float | None = None
    evidence: Evidence | None = None


class ExtractionResult(BaseModel):
    document_id: str
    fields: list[ExtractedField] = []
    missing_fields: list[str] = []
