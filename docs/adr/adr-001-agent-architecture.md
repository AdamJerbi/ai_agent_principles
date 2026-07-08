# ADR-001: Agent Architecture

## Status
Accepted

## Decision
Use one orchestrator agent and multiple specialist agents: extraction, comparison, annotation and validation.

## Rationale
A single agent with too many tools increases prompt size, cost, latency and tool-selection confusion. Specialist agents keep tool sets smaller and responsibilities clearer.

## Consequences
The system requires orchestration logic, but gains modularity, observability and easier testing.
