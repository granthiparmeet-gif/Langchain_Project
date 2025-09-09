from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    CHAT_MODEL: str = "gpt-4o-mini"
    EMBED_MODEL: str = "text-embedding-3-small"
    K: int = 4
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 120

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()