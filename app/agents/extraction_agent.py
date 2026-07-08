from app.workflow.state import WorkflowState


async def run_extraction_agent(state: WorkflowState) -> WorkflowState:
    # TODO: load only extraction-related MCP tools and call the model/tool loop.
    state['extraction_result'] = {
        'document_id': state.get('document_id', 'unknown'),
        'fields': [],
        'missing_fields': [],
    }
    return state
