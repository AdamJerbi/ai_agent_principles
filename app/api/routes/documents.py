from uuid import uuid4
from fastapi import APIRouter
from app.schemas.document import DocumentJobRequest, DocumentJobResponse

router = APIRouter()


@router.post('/jobs', response_model=DocumentJobResponse)
def create_document_job(payload: DocumentJobRequest) -> DocumentJobResponse:
    request_id = str(uuid4())
    # TODO: upload document metadata, persist job and enqueue Service Bus message.
    return DocumentJobResponse(request_id=request_id, status='queued')


@router.get('/jobs/{request_id}')
def get_document_job(request_id: str) -> dict[str, str]:
    # TODO: read status/result from PostgreSQL or another durable store.
    return {'request_id': request_id, 'status': 'not_implemented'}
