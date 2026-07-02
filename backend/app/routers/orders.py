from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=schemas.OrderResponse)
def place_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):
    return crud.create_order(db, order)


@router.get("/", response_model=list[schemas.OrderResponse])
def view_orders(
    db: Session = Depends(get_db)
):
    return crud.get_orders(db)
@router.get("/{buyer_name}", response_model=list[schemas.OrderResponse])
def get_my_orders(
    buyer_name: str,
    db: Session = Depends(get_db)
):
    return crud.get_orders_by_buyer(db, buyer_name)
@router.get("/all/orders", response_model=list[schemas.OrderResponse])
def view_all_orders(
    db: Session = Depends(get_db)
):
    return crud.get_all_orders(db)