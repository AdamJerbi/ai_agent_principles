# Orchestrator

The orchestrator is responsible for planning, not extracting.

## Responsibilities

- Understand the user task.
- Decide which specialist agents are required.
- Decide the order of execution.
- Provide task-specific context to each agent.
- Merge and normalize outputs.

## Non-responsibilities

The orchestrator should not:

- Parse documents.
- Extract detailed fields.
- Call Azure services directly.
- Call all MCP tools by itself.

## Example plan

```json
{
  "needs_extraction": true,
  "needs_comparison": true,
  "needs_annotation": false,
  "order": ["extraction", "comparison", "validation"],
  "reason": "Comparison requires structured extraction first."
}
```

## Router vs orchestrator

A deterministic router is enough when the task type is known. An LLM orchestrator is useful when the request is ambiguous, multi-step, or requires dynamic planning.
