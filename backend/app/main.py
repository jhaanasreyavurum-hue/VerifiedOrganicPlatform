from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app import models
from app.routers import (
    auth,
    products,
    farmer,
    supplier,
    admin,
    cart,
    orders
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Verified Organic Platform API",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(farmer.router)
app.include_router(supplier.router)
app.include_router(admin.router)
app.include_router(cart.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Verified Organic Platform API",
        "status": "Running Successfully"
    }


@app.get("/health")
def health():
    return {
        "status": "Backend Connected Successfully"
    }