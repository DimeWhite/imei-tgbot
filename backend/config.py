from pydantic import SecretStr, ConfigDict, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_DIR = ".env"


class Settings(BaseSettings):
    bot_token_request: SecretStr
    imeicheck_token: SecretStr
    model_config = SettingsConfigDict(env_file=ENV_DIR, env_file_encoding='utf-8')


config = Settings()
