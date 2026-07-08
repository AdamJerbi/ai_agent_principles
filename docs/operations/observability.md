# Observability

Observability is split between LLM-specific traces and platform-level traces.

## LangSmith

Use LangSmith for:

- Prompt traces
- LLM calls
- Tool calls
- Token usage
- Model costs
- Agent execution traces

## OpenTelemetry

Use OpenTelemetry for:

- API spans
- Worker spans
- Queue waiting time
- MCP tool latency
- Azure service latency
- Distributed traces

## Azure Monitor and Application Insights

Use Azure Monitor and Application Insights for dashboards, alerts, log aggregation, and production monitoring.

## Key questions answered

- Which agent consumes the most tokens?
- Which agent is slowest?
- Which MCP tool is the bottleneck?
- Is the queue backing up?
- Are workers saturated?
- Are LLM calls failing or retrying?
