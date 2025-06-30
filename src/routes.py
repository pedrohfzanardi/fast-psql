from fastapi import APIRouter, HTTPException, status
from schemas import ItemBase, ItemResponse, ItemCreate
from schemas import itens as itens_list

router = APIRouter()


@router.get("/list", response_model=list[ItemResponse])
def get_items() -> list[ItemResponse]:
    if not itens_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No items found"
        )
    return itens_list


@router.get("/list-item", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    item = itens_list[item_id - 1] if 0 < item_id <= len(itens_list) else None
    if item:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@router.post("/add-item", response_model=ItemResponse)
def create_item(item: ItemCreate) -> list[ItemResponse]:
    item_dict = item.model_dump()
    item_dict["id"] = len(itens_list) + 1
    itens_list.append(item_dict)
    return item_dict


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
def delete_item(item_id: int) -> dict[str, str]:
    try:
        del itens_list[item_id - 1]
        return {"message": "Item deleted successfully"}
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} not found"
        )
