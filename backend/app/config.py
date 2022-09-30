from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TITLE: str = Field("Thori Backend", env="WEP_APP_TITLE")
    VERSION: str = Field("0.0.0", env="WEB_APP_VERSION")
    DESCRIPTION: str = Field(
        "Micro service for the manage of the backend services",
        env="WEP_APP_DESCRIPTION",
    )
    ENVIRONMENT: str = Field("dev", env="ENVIRONMENT")
    USERNAME: str = Field("root")
    PASSWORD: str = Field("root")
    PRUEBA_DATABASE: str = Field("http://localhost:3000", env="PRUEBA_DATABASE")
    RABBITMQ_USER: str = Field("user", env="RABBITMQ_USER")
    RABBITMQ_PASSWORD: str = Field("bitnami", env="RABBITMQ_PASSWORD")
    RABBITMQ_HOST: str = Field("rabbitmq", env= "RABBITMQ_HOST")
    RABBITMQ_PORT: int = Field(5672, env="RABBITMQ_PORT")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
