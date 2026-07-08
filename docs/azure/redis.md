# Azure Cache for Redis

Redis is an optional supporting service, not the primary workflow queue.

## Recommended uses

- Cache repeated document parsing metadata.
- Cache retrieval results for repeated queries.
- Store short-lived session data.
- Track rate-limit counters.
- Store temporary UI progress hints.

## Not recommended

Redis should not be the main durable queue for production document processing jobs when Azure Service Bus is available.

## Example responsibilities split

| Concern | Service |
|---|---|
| Durable job queue | Azure Service Bus |
| Temporary cache | Redis |
| Long-term state | PostgreSQL |
| Raw documents | Blob Storage |
