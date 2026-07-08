from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = 'local'
    log_level: str = 'INFO'
    openai_deployment: str = 'gpt-4o-mini'
    openai_api_version: str = '2024-08-01-preview'
    blob_container: str = 'documents'
    queue_name: str = 'document-jobs'
    search_index: str = 'document-chunks'


@lru_cache
def get_settings() -> Settings:
    return Settings()
