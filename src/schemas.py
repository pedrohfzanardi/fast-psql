from pydantic import BaseModel

itens = [
    {"id": 1, "name": "Item 1", "description": "Description for Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description for Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description for Item 3"},
]


class ItemBase(BaseModel):
    name: str
    description: str


class ItemResponse(ItemBase):
    id: int = None


class ItemCreate(ItemBase):
    name: str = None
    description: str = None


class ItemUpdate(ItemBase):
    name: str | None = None
    description: str | None = None
