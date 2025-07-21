from fastapi import APIRouter, Depends

from schemas import ItemBase, ItemCreate, ItemResponse
from service import ItemService, get_item_service

router = APIRouter()


@router.get("/list-items", response_model=list[ItemResponse])
def get_items(item_service: ItemService = Depends(get_item_service)):
    return item_service.get_all_items()


@router.get("/list-item", response_model=ItemResponse)
def get_item(item_id: int, item_service: ItemService = Depends(get_item_service)):
    return item_service.get_item(item_id)


@router.post("/add-item", response_model=ItemResponse)
def create_item(
    item: ItemCreate, item_service: ItemService = Depends(get_item_service)
):
    return item_service.create_item(item)


@router.patch("/update-item/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int, item: ItemBase, item_service: ItemService = Depends(get_item_service)
):
    return item_service.update_item(item_id, item)


@router.delete("/delete-item/{item_id}")
def delete_item(item_id: int, item_service: ItemService = Depends(get_item_service)):
    item_service.delete_item(item_id)
