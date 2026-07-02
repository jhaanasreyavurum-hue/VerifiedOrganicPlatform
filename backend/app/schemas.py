from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    phone: str
    district: str
    state: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    phone: str
    district: str
    state: str

    class Config:
        from_attributes = True
class UserLogin(BaseModel):
    email: str
    password: str
class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    category: str
    supplier: str
    stock: int
    image: str


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: int
    category: str
    supplier: str
    stock: int
    image: str

    class Config:
        from_attributes = True
class CartCreate(BaseModel):
    product_id: int
    buyer_name: str
    quantity: int = 1


class CartResponse(BaseModel):
    id: int
    product_id: int
    buyer_name: str
    quantity: int

    class Config:
        orm_mode = True
class OrderCreate(BaseModel):
    buyer_name: str
    product_id: int
    quantity: int
    total_price: float


class OrderResponse(OrderCreate):
    id: int
    status: str

    class Config:
        from_attributes = True