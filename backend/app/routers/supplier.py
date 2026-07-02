from fastapi import APIRouter, Depends

from ..dependencies import supplier_required
from sqlalchemy.orm import Session
from fastapi import Depends
from ..dependencies import get_db
from .. import crud, schemas

router = APIRouter(
    prefix="/supplier",
    tags=["Supplier"]
)


@router.get("/dashboard")
def supplier_dashboard(current_user=Depends(supplier_required)):
    return {
        "message": f"Welcome Supplier {current_user['sub']}",
        "role": current_user["role"]
    }
@router.get("/orders", response_model=list[schemas.OrderResponse])
def supplier_orders(
    db: Session = Depends(get_db)
):

    return crud.get_supplier_orders(db)
@router.put("/orders/{order_id}")
def change_order_status(
    order_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    order = crud.update_order_status(
        db,
        order_id,
        status
    )

    if order is None:

        return {
            "message": "Order not found"
        }

    return order