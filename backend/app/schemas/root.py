from pydantic import BaseModel, Field

class HealthCheck(BaseModel):
    environment: str = Field(...)
    title: str = Field(...)
    version: str = Field(...)
    description: str = Field(...)