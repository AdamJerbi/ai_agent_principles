from pydantic import BaseModel


class OrchestrationPlan(BaseModel):
    needs_extraction: bool = True
    needs_comparison: bool = False
    needs_annotation: bool = False
    needs_validation: bool = True
    order: list[str] = ['extraction', 'validation']
    reason: str = 'Default document analysis workflow.'


def plan_workflow(task: str, has_second_document: bool = False) -> OrchestrationPlan:
    normalized = task.lower().strip()
    if normalized == 'compare' or has_second_document:
        return OrchestrationPlan(
            needs_extraction=True,
            needs_comparison=True,
            needs_annotation=False,
            needs_validation=True,
            order=['extraction', 'comparison', 'validation'],
            reason='Comparison requires extraction before comparing structured outputs.',
        )
    if normalized == 'annotate':
        return OrchestrationPlan(
            needs_extraction=True,
            needs_comparison=False,
            needs_annotation=True,
            needs_validation=True,
            order=['extraction', 'annotation', 'validation'],
            reason='Annotation requires extracted evidence and page/chunk references.',
        )
    return OrchestrationPlan()
