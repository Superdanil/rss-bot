from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ".env.template"), env_file_encoding="utf-8", extra="allow")

    # ==========TELEGRAM==========
    BOT_TOKEN: str
    NEWSFEED_LIMIT: int

    # ==========DATABASE==========
    DATABASE_HOST: str
    DATABASE_PORT: int

    @property
    def database_url(self):
        return f"http://{self.DATABASE_HOST}:{self.DATABASE_PORT}"


settings = Settings()
