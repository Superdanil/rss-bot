from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    # ==========APP==========
    APP_HOST: str
    APP_PORT: int

    # ==========POSTGRES==========
    DB_URL: PostgresDsn

    # ==========LOGGING==========
    LOGFILE: str
    ROTATION: str
    COMPRESSION: str


settings = Settings()
