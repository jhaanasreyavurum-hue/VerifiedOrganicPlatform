from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/", response_model=schemas.ProductResponse)
def add_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)


@router.get("/", response_model=list[schemas.ProductResponse])
def view_products(
    db: Session = Depends(get_db)
):
    return crud.get_all_products(db)


@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    updated_product = crud.update_product(db, product_id, product)

    if updated_product is None:
        return {
            "success": False,
            "message": "Product not found"
        }

    return updated_product


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    result = crud.delete_product(db, product_id)

    if result is None:
        return {
            "success": False,
            "message": "Product not found"
        }

    return result


@router.get("/search", response_model=list[schemas.ProductResponse])
def search_products(
    keyword: str = Query(...),
    db: Session = Depends(get_db)
):
    return crud.search_products(db, keyword)
@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = crud.get_product_by_id(db, product_id)

    if product is None:
        return {
            "success": False,
            "message": "Product not found"
        }

    return product