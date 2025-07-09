from typing import Annotated, Iterator

from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker


class Settings(BaseSettings):
    PROJECT_NAME: str = "fast-psql"
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
engine = create_engine(Settings().DATABASE_URL)
session = sessionmaker(bind=engine)
Base = declarative_base()


def get_db() -> Iterator[Session]:
    db = session()
    try:
        yield db
    finally:
        db.close()


SessionDB = Annotated[Session, Depends(get_db)]
