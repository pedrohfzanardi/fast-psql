from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models import Item as ItemModel
from schemas import ItemCreate, ItemUpdate


class ItemRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_item(self, item: ItemCreate) -> ItemModel:
        try:
            db_item = ItemModel(**item.model_dump())
            self.db.add(db_item)
            self.db.commit()
            self.db.refresh(db_item)
            return db_item
        except IntegrityError:
            self.db.rollback()
            return HTTPException(
                status_code=400,
                detail="Item with this name already exists",
            )

    def get_item_by_id(self, item_id: int) -> ItemModel | None:
        if item_id <= 0:
            return HTTPException(
                status_code=400,
                detail="Item ID must be a positive integer",
            )
        return self.db.query(ItemModel).filter(ItemModel.id == item_id).first()

    def get_all_items(self) -> list[ItemModel]:
        if not self.db.query(ItemModel).count():
            return HTTPException(
                status_code=404,
                detail="No items found",
            )
        return self.db.query(ItemModel).all()

    def update_item(self, item_id: int, item: ItemUpdate) -> ItemModel | None:
        db_updated_item = item.model_dump(exclude_unset=True)

        if not db_updated_item:
            return HTTPException(
                status_code=400,
                detail="No fields to update",
            )

        query = (
            update(ItemModel).where(ItemModel.id == item_id).values(**db_updated_item)
        )

        result = self.db.execute(query)

        self.db.commit()

        if result.rowcount == 0:
            return HTTPException(
                status_code=404,
                detail=f"Item with id {item_id} not found",
            )

        return self.get_item_by_id(item_id)

    def delete_item(self, item_id: int) -> None:
        repo = self.get_item_by_id(item_id)
        self.db.delete(repo)
        self.db.commit()
