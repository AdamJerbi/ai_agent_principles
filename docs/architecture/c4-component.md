# C4 Component

The component view describes the main internal modules.

```mermaid
flowchart TB
    API[API Routes] --> JobService[Job Service]
    JobService --> BlobService[Blob Storage Service]
    JobService --> QueueService[Queue Service]

    Worker[Worker Handler] --> Parser[Parsing Layer]
    Worker --> Retriever[Retrieval Layer]
    Worker --> Graph[LangGraph Workflow]
    Graph --> Orchestrator[Orchestrator]
    Graph --> Agents[Specialist Agents]
    Agents --> MCPClient[MCP Client]
    MCPClient --> MCPServer[MCP Server]
    MCPServer --> Tools[Domain Tools]
    Tools --> AzureServices[Azure AI Services]
```

## Component boundaries

- API modules should not contain extraction logic.
- Worker modules should not expose public endpoints.
- Agents should not directly call cloud services.
- MCP tools should hide service-specific implementation details.
- Schemas define the contracts between layers.
