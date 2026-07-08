from app.workflow.state import WorkflowState


async def run_comparison_agent(state: WorkflowState) -> WorkflowState:
    # TODO: compare structured extractions or retrieved evidence from two documents.
    state['comparison_result'] = {'differences': [], 'warnings': []}
    return state
