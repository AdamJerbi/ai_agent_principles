# MCP Overview

MCP is used to expose tools to agents through a stable interface.

## Why MCP

MCP separates agent reasoning from implementation details. Agents choose tools; tools execute capabilities.

## Architecture

```mermaid
flowchart LR
    Agent[Specialist Agent] --> Client[MCP Client]
    Client --> Server[MCP Server]
    Server --> Tools[Domain Tools]
    Tools --> Azure[Azure Services]
```

## Benefits

- Tools can be reused by multiple agents.
- Tool implementations can evolve independently.
- Agents do not need direct access to cloud service clients.
- Tool grouping makes large systems easier to maintain.
