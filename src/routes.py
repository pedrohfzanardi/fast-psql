from fastapi import APIRouter, Depends, HTTPException, status

from schemas import ItemBase, ItemCreate, ItemResponse
from schemas import itens as itens_list
from service import ItemService, get_item_service

router = APIRouter()


@router.get("/list-items", response_model=list[ItemResponse])
def get_items(item_service: ItemService = Depends(get_item_service)):
    items = item_service.get_all_items()
    if items:
        return items
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No items found")


@router.get("/list-item", response_model=ItemResponse)
def get_item(item_id: int, item_service: ItemService = Depends(get_item_service)):
    item = item_service.get_item_by_id(item_id)
    if item:
        return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found"
    )


@router.post("/add-item", response_model=ItemResponse)
def create_item(
    item: ItemCreate, item_service: ItemService = Depends(get_item_service)
):
    created_item = item_service.create_item(item)
    return created_item


@router.patch("/update-item/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemBase):
    for i in range(len(itens_list)):
        if itens_list[i]["id"] == item_id:
            itens_list[i].update(item)
            return itens_list[i]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found"
    )


@router.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    try:
        del itens_list[item_id - 1]
        return {"message": "Item deleted successfully"}
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found"
        )
