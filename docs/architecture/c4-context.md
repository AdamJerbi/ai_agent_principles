# C4 Context

The context view explains how the platform fits into the wider enterprise environment.

```mermaid
flowchart TB
    User[End Users] --> Platform[AI Document Processing Platform]
    Internal[Internal Applications] --> Platform
    External[External Systems] --> Platform

    Platform --> AOAI[Azure OpenAI]
    Platform --> DI[Azure Document Intelligence]
    Platform --> AIS[Azure AI Search]
    Platform --> Blob[Azure Blob Storage]
    Platform --> DB[(Azure PostgreSQL)]
    Platform --> Bus[Azure Service Bus]
    Platform --> KV[Azure Key Vault]
    Platform --> Monitor[Azure Monitor]
```

## Responsibilities

The platform owns document workflow execution, agent orchestration, MCP tool invocation, and persistence of results. Azure managed services provide AI, storage, messaging, secrets, and observability capabilities.
