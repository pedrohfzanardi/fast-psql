from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from config import Settings

Base = declarative_base()
engine = create_engine(Settings().DATABASE_URL)
session = sessionmaker(bind=engine)


def get_db() -> Iterator[Session]:
    db = session()
    try:
        yield db
    finally:
        db.close()
