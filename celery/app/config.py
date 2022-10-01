from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    RABBITMQ_USER: str = Field(...)
    RABBITMQ_PASSWORD: str = Field(...)
    RABBITMQ_HOST: str = Field(...)
    RABBITMQ_PORT: int = Field(...)
    ENVIRONMENT: str = Field(...)
    PRUEBA_DATABASE: str = Field(...)


settings = Settings()
