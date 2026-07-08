# Azure Services

## Azure OpenAI

Used by extraction, comparison, annotation, validation, and orchestration flows. It should receive focused context, not entire long documents by default.

## Azure Document Intelligence

Used for layout extraction, OCR, tables, page boundaries, and document structure. It is part of the parsing layer, not the agent layer.

## Azure AI Search

Used to index chunks, embeddings, page metadata, section names, and searchable evidence. Agents should retrieve relevant chunks before calling extraction tools.

## Azure Blob Storage

Stores raw input documents, parsed intermediate artifacts, generated annotations, and reports.

## Azure Service Bus

Production-grade durable job queue. Supports retries, dead-lettering, backpressure, and independent worker scaling.

## Azure PostgreSQL

Stores job metadata, workflow state, extraction results, comparison results, annotations, audit events, and user-facing status.

## Azure Cache for Redis

Used for cache, session state, rate limiting, and temporary workflow hints. It is not the durable production queue.
