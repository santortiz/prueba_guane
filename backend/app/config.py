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
    AT_PRONOSTICOS_DATABASE: str = Field("http://localhost:80")
    AT_PRONOSTICOS_MIDDLEWARE: str = Field("http://celsia-middleware-service:4000")
    AT_PRONOSTICOS_INFLUX: str = Field("http://20.186.165.95")
    AZURE_BUCKET_NAME: str = Field("asb")
    AT_PRONOSTICOS_REDIS: str = Field("")
    AT_MPT: str = Field("")
    USERNAME: str = Field("root")
    PASSWORD: str = Field("root")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
