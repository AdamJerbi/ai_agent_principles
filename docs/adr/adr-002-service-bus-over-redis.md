# ADR-002: Azure Service Bus for Durable Jobs

## Status
Accepted

## Decision
Use Azure Service Bus as the production job queue. Use Redis only for cache, temporary state, session cache and rate limiting.

## Rationale
Document processing jobs are long-running and require durability, retries, dead-letter handling and backpressure.

## Consequences
The platform depends on Azure-native messaging but gains production-grade reliability.
