from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/", response_model=schemas.CartResponse)
def add_to_cart(
    cart: schemas.CartCreate,
    db: Session = Depends(get_db)
):
    return crud.add_to_cart(db, cart)


@router.get("/", response_model=list[schemas.CartResponse])
def view_cart(
    db: Session = Depends(get_db)
):
    return crud.get_cart(db)


@router.delete("/{cart_id}")
def remove_from_cart(
    cart_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_cart_item(db, cart_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    return result
@router.delete("/clear/{buyer_name}")
def clear_cart(
    buyer_name: str,
    db: Session = Depends(get_db)
):
    crud.clear_cart(db, buyer_name)

    return {
        "message": "Cart Cleared Successfully"
    }