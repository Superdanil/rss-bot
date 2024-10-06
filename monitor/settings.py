from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    DATABASE_HOST: str
    DATABASE_PORT: int
    WAITING: int

    # ==========LOGGING==========
    MONITOR_LOGFILE: str
    ROTATION: str
    COMPRESSION: str

    @property
    def database_url(self):
        return f"http://{self.DATABASE_HOST}:{self.DATABASE_PORT}"


settings = Settings()
