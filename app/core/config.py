import logging
from logging.handlers import RotatingFileHandler
from typing import Optional, Any

from pydantic_settings import BaseSettings
from pydantic import EmailStr, field_validator, PostgresDsn

from app.constants import BASE_DIR, DT_FORMAT, LOG_FORMAT


class Settings(BaseSettings):
    app_title: str = 'WISHLIST'
    app_description: str = 'Сервис для учета идей подарков'
    # first_superuser_email: Optional[EmailStr] = None
    # first_superuser_password: Optional[str] = None

    secret: str

    db_host: str
    db_port: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: PostgresDsn | None = None

    @field_validator('database_url', pre=True)
    def assemble_db_connection(cls, v: str | None,
                               values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=values.get('postgres_user'),
            password=values.get('postgres_password'),
            host=values.get('db_host'),
            port=values.get('db_port'),
            path=f'/{values.get("postgres_db") or ""}',
        )

    class Config:
        env_file = '.env'


settings = Settings()


def configure_logging():
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'wishlist.log'
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
