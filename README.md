# 🌱 Verified Organic Platform

A full-stack web application developed to connect **farmers**, **organic product suppliers**, and **administrators** through a secure online marketplace. The platform enables users to browse verified organic products, manage orders, and maintain transparency in the organic supply chain.

---

## 📌 Project Overview

The **Verified Organic Platform** is designed to promote organic farming by providing a centralized platform where:

- Farmers can purchase verified organic products.
- Suppliers can manage and list organic products.
- Administrators can monitor users, products, and orders.

The application is built using **FastAPI**, **MySQL**, **HTML**, **CSS**, and **JavaScript**.

---

## ✨ Features

### 👨‍🌾 Farmer Module
- User Registration & Login
- Browse Organic Products
- Product Search
- Product Details
- Add Products to Cart
- Checkout
- Payment Page
- Order History

### 🏭 Supplier Module
- Supplier Dashboard
- Add Products
- Update Products
- Delete Products
- Search Products
- Manage Inventory

### 🛡️ Admin Module
- Admin Dashboard
- View Users
- View Products
- Monitor Orders
- Platform Statistics

### 🛒 Shopping Cart
- Add Items
- Remove Items
- Checkout
- Order Creation

### 🔐 Authentication
- Secure Login
- Password Hashing
- JWT Authentication
- Role-Based Authorization

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- SQLAlchemy
- Pydantic
- JWT Authentication
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- MySQL

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
VerifiedOrganicPlatform/
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── security.py
│   │   └── main.py
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── pages/
│   └── index.html
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/jhaanasreyavurum-hue/VerifiedOrganicPlatform.git
```

### 2. Navigate to the Project

```bash
cd VerifiedOrganicPlatform
```

### 3. Backend Setup

```bash
cd backend
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Create a MySQL database and update the database connection settings in:

```
backend/app/database.py
```

### 5. Run the Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

### 6. Run the Frontend

Open the frontend using **Live Server** in Visual Studio Code.

---

## 📷 Screenshots

You can add screenshots of:

- Home Page
- Product Page
- Shopping Cart
- Checkout
- Supplier Dashboard
- Admin Dashboard

---

## 🎯 Future Improvements

- Online Payment Gateway Integration
- Product Review & Rating System
- Email Notifications
- SMS Alerts
- AI-based Product Recommendations
- GIS Integration for Organic Farm Mapping
- Cloud Deployment (AWS/Azure)
- Mobile Application

---

## 🎓 Academic Purpose

This project was developed as part of postgraduate learning in **Agriculture Analytics**, combining web development, database management, and backend API development.

---

## 👩‍💻 Author

**Shreya Vurum**

- GitHub: https://github.com/jhaanasreyavurum-hue

---

## 📄 License

This project is intended for educational and learning purposes.