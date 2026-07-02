from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import crud, schemas

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
def dashboard_stats(
    db: Session = Depends(get_db)
):
    return crud.get_dashboard_stats(db)


@router.get("/users", response_model=list[schemas.UserResponse])
def view_users(
    db: Session = Depends(get_db)
):
    return crud.get_all_users(db)
from fastapi import HTTPException

@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    result = crud.delete_user(db, user_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result
@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db)
):

    return crud.get_dashboard_stats(db)