from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from errors import raise_no_fields_to_update, raise_not_found
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
            raise_not_found(detail="Item with this name already exists.")

    def get_item_by_id(self, item_id: int) -> ItemModel | None:
        if item_id <= 0:
            raise_not_found(detail=f"Item with id {item_id} not found")
        return self.db.query(ItemModel).filter(ItemModel.id == item_id).first()

    def get_all_items(self) -> list[ItemModel]:
        if not self.db.query(ItemModel).count():
            raise_not_found(detail="No items found")
        return self.db.query(ItemModel).all()

    def update_item(self, item_id: int, item: ItemUpdate) -> ItemModel | None:
        db_updated_item = item.model_dump(exclude_unset=True)

        if not db_updated_item:
            raise_no_fields_to_update()

        query = (
            update(ItemModel).where(ItemModel.id == item_id).values(**db_updated_item)
        )

        result = self.db.execute(query)

        self.db.commit()

        if result.rowcount == 0:
            raise_not_found(detail=f"Item with id {item_id} not found")

        return self.get_item_by_id(item_id)

    def delete_item(self, item_id: int) -> None:
        item = self.get_item_by_id(item_id)
        if not item:
            raise_not_found(detail=f"Item with id {item_id} not found")
        self.db.delete(item)
        self.db.commit()
