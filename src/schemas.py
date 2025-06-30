from pydantic import BaseModel, Field

itens = [
    {"id": 1, "name": "Item 1", "description": "Description for Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description for Item 2"},
    {"id": 3, "name": "Item 3", "description": "Description for Item 3"},
]


class ItemBase(BaseModel):
    name: str
    description: str


class ItemResponse(ItemBase):
    id: int = Field(...)


class ItemCreate(ItemBase):
    name: str = Field(..., example=f"Item {len(itens) + 1}")
    description: str = Field(..., example=f"Description for Item {len(itens) + 1}")
