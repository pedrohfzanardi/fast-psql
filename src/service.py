from http.client import HTTPException

from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from repository import ItemRepository
from schemas import ItemCreate, ItemResponse


class ItemService:
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_item(self, item_id: int) -> ItemResponse:
        repo = self.repository.get_item_by_id(item_id)
        if isinstance(repo, HTTPException):
            raise repo
        return ItemResponse.model_validate(repo)

    def get_all_items(self) -> list[ItemResponse]:
        repo = self.repository.get_all_items()
        if isinstance(repo, HTTPException):
            raise repo
        return [ItemResponse.model_validate(item) for item in repo]

    def update_item(self, item_id: int, item_data: ItemCreate) -> ItemResponse:
        repo = self.repository.update_item(item_id, item_data)
        if isinstance(repo, HTTPException):
            raise repo
        return ItemResponse.model_validate(repo)

    def delete_item(self, item_id: int) -> None:
        self.repository.delete_item(item_id)

    def create_item(self, item_data: ItemCreate) -> ItemResponse:
        item = self.repository.create_item(item_data)
        return ItemResponse.model_validate(item)


def get_item_service(session: Session = Depends(get_db)) -> ItemService:
    repository = ItemRepository(session)
    return ItemService(repository)
