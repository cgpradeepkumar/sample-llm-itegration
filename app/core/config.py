from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GOOGLE_CLOUD_PROJECT: str
    GOOGLE_CLOUD_LOCATION: str
    GEMINI_MODEL_ID: str
    GEMINI_API_KEY: str
    GOOGLE_APPLICATION_CREDENTIALS: str
    SCOPES: list[str] = ["https://www.googleapis.com/auth/cloud-platform"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()