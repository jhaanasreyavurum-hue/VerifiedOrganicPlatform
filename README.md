# 🌱 Verified Organic Platform

A full-stack web application that connects **Farmers**, **Suppliers**, and **Administrators** through a secure online marketplace for verified organic agricultural products.

The platform enables users to browse products, manage carts and orders, and provides role-based access for different types of users.

---

# 🚀 Live Demo

## Frontend


https://verified-organic-frontend.onrender.com


## Backend API


https://verified-organic-platform.onrender.com


## API Documentation

https://verified-organic-platform.onrender.com/docs


---

# 📌 Features

### 👨‍🌾 Farmer

* Register & Login
* Browse Organic Products
* Search Products
* View Product Details
* Add Products to Cart
* Place Orders
* View Order History

### 🏭 Supplier

* Supplier Dashboard
* Add Products
* Update Products
* Delete Products
* Manage Inventory

### 🛡️ Admin

* Admin Dashboard
* View Users
* Manage Products
* Monitor Orders

### 🛒 Shopping Cart

* Add to Cart
* Remove from Cart
* Checkout
* Order Management

### 🔐 Authentication

* JWT Authentication
* Password Hashing
* Role-Based Authorization

---

# 🛠️ Technology Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic
* Uvicorn

## Database

* PostgreSQL (Render)

## Deployment

* Render Web Service
* Render PostgreSQL
* Render Static Site

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
VerifiedOrganicPlatform/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── routers/
│   │   │   ├── auth.py          # User registration & login
│   │   │   ├── products.py      # Product CRUD operations
│   │   │   ├── cart.py          # Shopping cart APIs
│   │   │   ├── orders.py        # Order management
│   │   │   ├── farmer.py        # Farmer-specific APIs
│   │   │   ├── supplier.py      # Supplier-specific APIs
│   │   │   └── admin.py         # Admin APIs
│   │   │
│   │   ├── crud.py              # Database CRUD functions
│   │   ├── database.py          # PostgreSQL database connection
│   │   ├── dependencies.py      # Dependency injection & authentication
│   │   ├── models.py            # SQLAlchemy database models
│   │   ├── schemas.py           # Pydantic request/response schemas
│   │   ├── security.py          # JWT token & password hashing
│   │   └── main.py              # FastAPI application entry point
│   │
│   ├── requirements.txt         # Python dependencies
│   ├── .env                     # Environment variables (not committed)
│   └── venv/                    # Virtual environment
│
├── frontend/
│   │
│   ├── css/
│   │   └── style.css            # Website styles
│   │
│   ├── js/
│   │   └── script.js            # Frontend JavaScript
│   │
│   ├── images/                  # Images and assets
│   │
│   ├── pages/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── products.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── orders.html
│   │   ├── farmer.html
│   │   ├── supplier.html
│   │   ├── admin.html
│   │   └── payment.html
│   │
│   └── index.html               # Landing page
│
├── .gitignore                   # Git ignore rules
├── README.md                    # Project documentation
└── LICENSE                      # Project license (optional)
```


---

# ⚙️ Local Installation

## Clone Repository

```bash
git clone https://github.com/jhaanasreyavurum-hue/VerifiedOrganicPlatform.git
```

## Enter Project

```bash
cd VerifiedOrganicPlatform
```

## Backend Setup

```bash
cd backend
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file.

Example:

```env
DATABASE_URL=your_postgresql_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Run the backend

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Frontend

Open `frontend/index.html` using Live Server in Visual Studio Code.

---

# 📷 Screenshots

Add screenshots of:

* Home Page
* Login Page
* Farmer Dashboard
* Supplier Dashboard
* Admin Dashboard
* Products Page
* Shopping Cart
* Orders Page

---

# 📈 Future Enhancements

* Payment Gateway Integration
* Product Ratings & Reviews
* Email Notifications
* SMS Alerts
* AI-Based Product Recommendations
* GIS Integration
* Mobile Application

---

# 👩‍💻 Author

**Shreya Vurum**

GitHub:
https://github.com/jhaanasreyavurum-hue

---

# 📄 License

This project is developed for educational and learning purposes.


