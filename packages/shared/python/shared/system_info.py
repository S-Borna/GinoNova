from pydantic import BaseModel

class SystemInfo(BaseModel):
    service: str
    version: str
