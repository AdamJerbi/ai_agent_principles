# Azure Service Bus

Azure Service Bus is the durable queue for document processing jobs.

## Responsibilities

- Decouple API request submission from long-running processing.
- Buffer bursts of traffic.
- Support worker autoscaling.
- Provide retry and dead-letter behavior.
- Preserve job payloads durably.

## Message payload

A typical message should include:

```json
{
  "request_id": "...",
  "document_id": "...",
  "blob_uri": "...",
  "task": "analyze",
  "tenant_id": "..."
}
```

## Why not Redis for this?

Redis can be used for lightweight queues, but Azure Service Bus is better for durable enterprise workflows because it has built-in delivery guarantees, dead-letter queues, retries, and operational tooling.
