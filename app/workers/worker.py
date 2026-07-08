import asyncio
from app.workflow.graph import build_graph


async def process_document_job(payload: dict) -> dict:
    graph = build_graph()
    return await graph.ainvoke(payload)


async def main() -> None:
    # TODO: replace this local example with Azure Service Bus message consumption.
    result = await process_document_job({
        'request_id': 'local-dev',
        'document_id': 'doc-local',
        'task': 'analyze',
        'raw_text': 'Example agreement between Client A and Vendor B.',
    })
    print(result.get('final_result'))


if __name__ == '__main__':
    asyncio.run(main())
