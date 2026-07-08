# Scaling

The system scales each runtime independently.

## API scaling

The API scales based on HTTP traffic, CPU, memory, and request latency.

## Worker scaling

Workers scale based on Azure Service Bus queue depth and processing latency. KEDA is the recommended Kubernetes autoscaler for queue-driven worker scaling.

## MCP scaling

MCP servers scale based on tool-call latency, active connections, CPU, and memory.

## Bottleneck indicators

| Signal | Likely issue |
|---|---|
| High queue depth | Not enough workers |
| High API latency | API saturation or downstream slowness |
| High MCP latency | Tool server bottleneck |
| High token usage | Too much context passed to LLM |
| High Azure Search latency | Retrieval bottleneck |
| High retry rate | Unstable dependency |
