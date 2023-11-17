import logging
from logging.handlers import RotatingFileHandler
from typing import Optional, Any

from pydantic_settings import BaseSettings
from pydantic import EmailStr, field_validator, PostgresDsn
from pydantic_core.core_schema import FieldValidationInfo

from api.constants import BASE_DIR, DT_FORMAT, LOG_FORMAT


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
    database_url: Optional[PostgresDsn] = None

    @field_validator('database_url', mode='after')
    def assemble_db_connection(
            cls,
            v: Optional[str],
            info: FieldValidationInfo
    ) -> PostgresDsn:
        if isinstance(v, str):
            return v
        return str(
            PostgresDsn.build(
                scheme='postgresql+asyncpg',
                username=info.data.get('postgres_user'),
                password=info.data.get('postgres_password'),
                host=info.data.get('db_host'),
                port=int(info.data.get('db_port')),
                path=f'{info.data.get("postgres_db") or ""}',
            )
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
