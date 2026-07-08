# Agents Overview

The platform uses one orchestrator and several specialist agents.

```mermaid
flowchart LR
    O[Orchestrator] --> E[Extraction Agent]
    O --> C[Comparison Agent]
    O --> A[Annotation Agent]
    O --> V[Validation Agent]
    O --> R[Reviewer Agent]
    E --> MCP[MCP Tools]
    C --> MCP
    A --> MCP
    V --> MCP
    R --> MCP
```

## Design principle

Specialist agents should receive only the tools relevant to their job. This reduces token usage, improves tool selection, and makes behavior easier to test.

## Recommended agents

- Extraction Agent
- Comparison Agent
- Annotation Agent
- Validation Agent
- Reviewer Agent
- Report Generation Agent
