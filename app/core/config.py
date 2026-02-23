from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_ID: str
    LOCATION: str
    GEMINI_MODEL_ID: str
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()