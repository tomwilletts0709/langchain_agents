from pydantic_settings import BaseSettings
from pydantic import field_validator
from enum import Enum
from typing import Optional


class Environment(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class Settings(BaseSettings):
    app_name: str = "England 2026 World Cup Agent"
    environment: Environment = Environment.DEVELOPMENT

    # LLM
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: Optional[str] = None

    # Football API
    FOOTBALL_STATS_API: str
    FOOTBALL_API_BASE_URL: str = "https://api.football-data.org/v4"

    # Database
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Redis
    REDIS_URL: str = "redis://localhost:6379"

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
