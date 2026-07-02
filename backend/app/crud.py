from sqlalchemy.orm import Session
from . import models, schemas
from .security import (
    hash_password,
    verify_password,
    create_access_token
)


def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
        phone=user.phone,
        district=user.district,
        state=user.state
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(db: Session, email: str, password: str):

    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role,
            "id": user.id
        }
    )

    return {
        "user": user,
        "token": token
    }
from . import schemas


def create_product(db: Session, product: schemas.ProductCreate):

    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        supplier=product.supplier,
        stock=product.stock,
        image=product.image
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_all_products(db: Session):

    return db.query(models.Product).all()
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):

    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if db_product is None:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.category = product.category
    db_product.supplier = product.supplier
    db_product.stock = product.stock
    db_product.image = product.image

    db.commit()
    db.refresh(db_product)

    return db_product
def delete_product(db: Session, product_id: int):

    db_product = db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()

    if db_product is None:
        return None

    db.delete(db_product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }
def search_products(db: Session, keyword: str):

    return db.query(models.Product).filter(
        models.Product.name.ilike(f"%{keyword}%")
    ).all()
def get_product_by_id(db: Session, product_id: int):

    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()
def add_to_cart(db: Session, cart: schemas.CartCreate):

    db_cart = models.Cart(
        product_id=cart.product_id,
        buyer_name=cart.buyer_name,
        quantity=cart.quantity
    )

    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)

    return db_cart


def get_cart(db: Session):

    return db.query(models.Cart).all()


def delete_cart_item(db: Session, cart_id: int):

    item = db.query(models.Cart).filter(
        models.Cart.id == cart_id
    ).first()

    if item is None:
        return None

    db.delete(item)
    db.commit()

    return {
        "message": "Item removed from cart"
    }
def create_order(db: Session, order: schemas.OrderCreate):

    db_order = models.Order(**order.dict())

    db.add(db_order)

    db.commit()

    db.refresh(db_order)

    return db_order
def get_orders(db: Session):

    return db.query(models.Order).all()
def clear_cart(db: Session, buyer_name: str):

    db.query(models.Cart).filter(
        models.Cart.buyer_name == buyer_name
    ).delete()

    db.commit()
def get_orders_by_buyer(db: Session, buyer_name: str):

    return db.query(models.Order).filter(
        models.Order.buyer_name == buyer_name
    ).all()
def get_all_orders(db: Session):
    return db.query(models.Order).all()
def get_dashboard_stats(db: Session):

    total_users = db.query(models.User).count()

    total_products = db.query(models.Product).count()

    total_orders = db.query(models.Order).count()

    return {
        "users": total_users,
        "products": total_products,
        "orders": total_orders
    }
def get_all_users(db: Session):

    return db.query(models.User).all()
def delete_user(db: Session, user_id: int):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }
def get_supplier_orders(db: Session):

    return db.query(models.Order).all()
def update_order_status(db: Session, order_id: int, status: str):

    order = db.query(models.Order).filter(
        models.Order.id == order_id
    ).first()

    if order is None:
        return None

    order.status = status

    db.commit()
    db.refresh(order)

    return order
def get_dashboard_stats(db: Session):

    users = db.query(models.User).count()

    products = db.query(models.Product).count()

    orders = db.query(models.Order).count()

    suppliers = db.query(models.User).filter(
        models.User.role == "supplier"
    ).count()

    farmers = db.query(models.User).filter(
        models.User.role == "farmer"
    ).count()

    return {
        "users": users,
        "products": products,
        "orders": orders,
        "suppliers": suppliers,
        "farmers": farmers
    }