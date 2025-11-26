from pydantic_settings import BaseSettings

class WorkerSettings(BaseSettings):
    REDIS_URL: str = "redis://localhost:6379/0"

    class Config:
        env_file = "env/worker.env.example"
        env_file_encoding = "utf-8"

settings = WorkerSettings()
