from pydantic import BaseSettings
from pydantic import PostgresDsn
import json
import os 
from enum import Enum


class Environment(str, Enum): 
    """ analyst agent environment types"""
    
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"
    TESTING = "testing"


class Settings(BaseSettings): 
    app_name: str = "Langchain App to mess around with LLMS"
    OPEN_API_KEY: str 
    ANTHROPIC_API_KEY: str

class Config(BaseSettings): 
    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    CORS_ORIGINS: list[str]
    CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]


settings = Settings()

