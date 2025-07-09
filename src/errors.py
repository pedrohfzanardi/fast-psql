from fastapi import HTTPException, status


def raise_no_fields_to_update():
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update."
    )


def raise_not_found(detail: str = "Resource not found."):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
