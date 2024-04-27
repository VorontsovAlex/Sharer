import os
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    db_url: str
    session_db_url: Optional[str] = None
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file=DOTENV)
    ss: str = '2'


settings = Settings()
print(settings)