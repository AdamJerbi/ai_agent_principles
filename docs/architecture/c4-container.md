# C4 Container

The container view separates runtime responsibilities.

```mermaid
flowchart LR
    APIM[Azure API Management] --> API[FastAPI API Container]
    API --> Blob[Blob Storage]
    API --> Bus[Service Bus Queue]
    Bus --> Worker[Worker Container]
    Worker --> Graph[LangGraph Runtime]
    Graph --> MCPClient[MCP Client]
    MCPClient --> MCP[MCP Server Container]
    MCP --> AzureAI[Azure AI Services]
    Worker --> DB[(PostgreSQL)]
    Worker --> Search[Azure AI Search]
```

## API container

Receives requests, authenticates callers, validates input, uploads documents, creates job records, and enqueues work.

## Worker container

Consumes jobs, runs LangGraph workflows, persists results, and coordinates with MCP tools.

## MCP server container

Hosts reusable tools grouped by domain. It is internal-only and not exposed to the public internet.
