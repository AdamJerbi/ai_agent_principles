from typing import Any, TypedDict


class WorkflowState(TypedDict, total=False):
    request_id: str
    document_id: str
    task: str
    raw_text: str
    chunks: list[dict[str, Any]]
    candidate_chunks: dict[str, list[dict[str, Any]]]
    plan: dict[str, Any]
    extraction_result: dict[str, Any]
    comparison_result: dict[str, Any]
    annotation_result: dict[str, Any]
    validation_result: dict[str, Any]
    final_result: dict[str, Any]
    errors: list[str]
