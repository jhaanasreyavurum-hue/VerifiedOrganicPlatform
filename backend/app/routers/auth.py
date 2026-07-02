from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="",
    tags=["Authentication"]
)


@router.post("/register", response_model=schemas.UserResponse)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user)


@router.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    result = crud.login_user(
        db,
        user.email,
        user.password
    )

    if result is None:
        return {
            "success": False,
            "message": "Invalid Email or Password"
        }

    return {
        "success": True,
        "message": "Login Successful",
        "access_token": result["token"],
        "token_type": "bearer",
        "user": {
            "id": result["user"].id,
            "name": result["user"].name,
            "email": result["user"].email,
            "role": result["user"].role,
            "phone": result["user"].phone,
            "district": result["user"].district,
            "state": result["user"].state
        }
    }