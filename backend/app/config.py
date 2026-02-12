from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=True,
    )

    PROJECT_NAME: str = "AI Support Engineer"
    API_V1_STR: str = "/api/v1"
    QDRANT_URL: str = "http://qdrant:6333"
    OPENAI_API_KEY: str

settings = Settings()