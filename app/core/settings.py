from pydantic import BaseSettings

class Settings(BaseSettings): 
    app_name: str = "Langchain App to mess around with LLMS"
    OPEN_API_KEY: str 
    ANTHROPIC_API_KEY: str

settings = Settings()

