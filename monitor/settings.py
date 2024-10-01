from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ".env.template"), env_file_encoding='utf-8', extra="allow")

    BOT_TOKEN: str


settings = Settings()
