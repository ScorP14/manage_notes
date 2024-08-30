from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, BaseModel

from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class PostgresqlConnectEnv(BaseModel):
    user: str
    password: str
    name: str
    host: str = Field(default="localhost")
    port: int = Field(default=5432)

    def get_url(self, driver: str = "asyncpg"):
        return f"postgresql+{driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class JwtEnv(BaseModel):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=BASE_DIR / ".env",
        extra="allow",
    )

    database: PostgresqlConnectEnv = Field(alias="POSTGRESQL")
    jwt: JwtEnv


@lru_cache(1)
def get_settings():
    return Settings()
