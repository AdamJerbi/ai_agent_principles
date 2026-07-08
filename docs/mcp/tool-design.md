# MCP Tool Design

A tool should have one responsibility and a clear input/output contract.

## Good tool shape

```text
name: extract_contract_parties
input: candidate_chunks
output: parties, missing, evidence, confidence
```

## Guidelines

- Keep tools domain-specific.
- Avoid one giant `extract_everything` tool.
- Return structured data, not prose.
- Include evidence references.
- Keep tools independently testable.
- Prefer deterministic logic when an LLM is not required.

## Tool groups

- Contract tools
- Invoice tools
- CV tools
- Comparison tools
- Annotation tools
- Validation tools

## Agent exposure

Host many tools in MCP, but expose only the relevant subset to each agent. This avoids prompt bloat and tool-selection confusion.
