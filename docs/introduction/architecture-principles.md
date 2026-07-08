# Architecture Principles

## 1. Separate orchestration from execution

The orchestrator decides what should happen, but specialist agents and MCP tools perform the work.

## 2. Keep agents focused

Each agent should have a limited responsibility and a small set of relevant tools. A practical target is 5 to 20 tools per agent.

## 3. Do not send full long documents to every LLM call

Long documents must be parsed, chunked, indexed, and retrieved. Extraction skills receive candidate chunks and evidence metadata, not the full document by default.

## 4. Make every output auditable

Structured outputs should include evidence, page references, chunk identifiers, confidence, and warnings.

## 5. Prefer durable queues for production jobs

Azure Service Bus is the production queue. Redis is used only for cache, temporary state, rate limiting, or session data.

## 6. Observe every layer

LLM traces, tool calls, backend latency, queue waiting time, retries, and failures must be measurable.

## 7. Secure by default

Use Managed Identity, Key Vault, RBAC, private networking, and least privilege access.
