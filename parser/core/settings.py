from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env.template", ".env"), env_file_encoding='utf-8', extra="allow")

    # ==========PARSER==========
    PARSER_HOST: str
    PARSER_PORT: int

    # ==========POSTGRES==========
    DB_URL: str
    # POSTGRES_ECHO: bool
    # POSTGRES_ECHO_POOL: bool
    # POSTGRES_POOL_SIZE: int
    # POSTGRES_MAX_OVERFLOW: int


settings = Settings()
# print(settings.DB_URL)
