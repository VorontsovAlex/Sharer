import os
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    db_url: str
    session_db_url: Optional[str] = None
    items_per_user: int = 50

    model_config = SettingsConfigDict(env_file=DOTENV)
    db_url: str = "postgresql://postgres:postgres@localhost:5444/postgres"
    secret: str = "ea270b06-bf10-46fd-9d1a-088c559f1694"
    algorithm: str = "HS256"


settings = Settings()
print(settings)