from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.documents import router as documents_router

app = FastAPI(title='Enterprise AI Document Platform', version='0.1.0')
app.include_router(health_router, prefix='/health', tags=['health'])
app.include_router(documents_router, prefix='/documents', tags=['documents'])
