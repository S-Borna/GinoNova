from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_VERSION: str = "v1.0.0"
    API_ORIGINS: str = "*"
    RAILWAY_ENV: str = ""

    class Config:
        env_file = "env/backend.env.example"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
