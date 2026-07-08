# Requirements

## Functional requirements

The platform must support:

- Document upload and job creation.
- PDF, DOCX, PPTX, and scanned document processing.
- Azure Document Intelligence parsing.
- Chunking and retrieval for long documents.
- Structured extraction with evidence.
- Document comparison.
- Document annotation.
- Workflow validation and result persistence.
- Asynchronous processing and job status tracking.

## Non-functional requirements

The platform must be:

- Scalable through independent API, worker, and MCP deployments.
- Observable through LangSmith, OpenTelemetry, and Azure Monitor.
- Secure through Azure Entra ID, Managed Identity, Key Vault, and private networking.
- Reliable through retries, idempotency, dead-letter queues, and workflow checkpointing.
- Maintainable through clear code boundaries and documented architecture decisions.

## Key constraints

- Azure is the primary cloud provider.
- Azure Document Intelligence is used for document layout and OCR.
- Azure OpenAI is used for LLM tasks.
- LangGraph is used for orchestration.
- MCP is used as the tool exposure mechanism.
