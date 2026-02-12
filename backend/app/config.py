from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Support Engineer"
    API_V1_STR: str = "/api/v1"
    QDRANT_URL: str = "http://qdrant:6333"

    class Config:
        case_sensitive = True

settings = Settings()
