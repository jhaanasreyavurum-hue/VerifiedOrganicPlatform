from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(50), nullable=False)

    phone = Column(String(20))

    district = Column(String(100))

    state = Column(String(100))
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)

    description = Column(String(500))

    price = Column(Integer, nullable=False)

    category = Column(String(100))

    supplier = Column(String(100))

    stock = Column(Integer, default=0)

    image = Column(String(255))
class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    buyer_name = Column(String(255))

    quantity = Column(Integer, default=1)
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    buyer_name = Column(String(255))

    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer)

    total_price = Column(Float)

    status = Column(String(50), default="Pending")