from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    redis_url: str = "redis://localhost:6379"
    environment: str = "development"
    debug: bool = True
    cors_origins: str = "http://localhost:8080,http://localhost:5173,http://localhost:3000"
    cache_ttl: int = 3600
    
    # Gemini API settings
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash"
    
    # Embedding model (local)
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # Generation settings
    max_new_tokens: int = 65536  # Maximum for comprehensive responses
    temperature: float = 0.7
    
    # Request timeout
    request_timeout: int = 300  # 5 minutes for long responses

    @property
    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_origins.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
