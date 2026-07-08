from app.workflow.state import WorkflowState


async def run_annotation_agent(state: WorkflowState) -> WorkflowState:
    # TODO: produce document annotations from extracted evidence.
    state['annotation_result'] = {'annotations': []}
    return state
