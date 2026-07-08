from langgraph.graph import END, StateGraph

from app.agents.annotation_agent import run_annotation_agent
from app.agents.comparison_agent import run_comparison_agent
from app.agents.extraction_agent import run_extraction_agent
from app.workflow.orchestrator import plan_workflow
from app.workflow.state import WorkflowState


def parse_document(state: WorkflowState) -> WorkflowState:
    state['raw_text'] = state.get('raw_text', '')
    return state


def chunk_document(state: WorkflowState) -> WorkflowState:
    text = state.get('raw_text', '')
    state['chunks'] = [{'chunk_id': 'chunk_0', 'document_id': state.get('document_id', 'unknown'), 'text': text}]
    return state


def orchestrate(state: WorkflowState) -> WorkflowState:
    plan = plan_workflow(task=state.get('task', 'analyze')).model_dump()
    state['plan'] = plan
    return state


def validate(state: WorkflowState) -> WorkflowState:
    state['validation_result'] = {'status': 'valid', 'warnings': []}
    return state


def finalize(state: WorkflowState) -> WorkflowState:
    state['final_result'] = {
        'request_id': state.get('request_id'),
        'plan': state.get('plan'),
        'extraction': state.get('extraction_result'),
        'comparison': state.get('comparison_result'),
        'annotation': state.get('annotation_result'),
        'validation': state.get('validation_result'),
    }
    return state


def build_graph():
    graph = StateGraph(WorkflowState)
    graph.add_node('parse', parse_document)
    graph.add_node('chunk', chunk_document)
    graph.add_node('orchestrate', orchestrate)
    graph.add_node('extraction', run_extraction_agent)
    graph.add_node('comparison', run_comparison_agent)
    graph.add_node('annotation', run_annotation_agent)
    graph.add_node('validate', validate)
    graph.add_node('finalize', finalize)
    graph.set_entry_point('parse')
    graph.add_edge('parse', 'chunk')
    graph.add_edge('chunk', 'orchestrate')
    graph.add_edge('orchestrate', 'extraction')
    graph.add_edge('extraction', 'comparison')
    graph.add_edge('comparison', 'annotation')
    graph.add_edge('annotation', 'validate')
    graph.add_edge('validate', 'finalize')
    graph.add_edge('finalize', END)
    return graph.compile()
