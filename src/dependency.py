from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from config import get_db
from repository import ItemRepository as ItemService


def get_item_service():
    return ItemService()


db_dependency = Annotated[Session, Depends(get_db)]
item_service_dependency = Annotated[ItemService, Depends(get_item_service)]
