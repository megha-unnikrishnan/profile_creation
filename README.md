# 📌 Profile Creation System – Full Documentation

Framework: FastAPI<br>
Database: PostgreSQL<br>
Migrations: Alembic<br>
API Testing: Postman<br>


## 📖 Table of Contents



- [Project Overview](#project-overview)
- [System Requirements](#system-requirements)
- [Project Setup](#project-setup)
- [Database & Migrations (Alembic)](#database--migrations-alembic)
- [Running the FastAPI Server](#running-the-fastapi-server)
- [Postman Collection](#postman-collection)



## 📌 Project Overview

The Profile Creation System is a FastAPI-based API that allows users to register, ensuring proper validation of email and passwords. It includes:

✅ Database migrations with Alembic<br>
✅ Password strength enforcement<br>
✅ Postman collection for easy testing<br>

## 📌 System Requirements

| Component     | Version / Requirement |
|--------------|----------------------|
| Python       | 3.8+                 |
| FastAPI      | Latest Stable        |
| PostgreSQL   | 12+ / SQLite         |
| Alembic      | Latest               |
| uvicorn      | Latest               |



## 📌 Project Setup

### 🔹 Step 1: Clone the Repository

    - git clone https://github.com/megha-unnikrishnan/profile_creation.git
    
        -cd profile_creation
        
### 🔹 Step 2: Create a Virtual Environment

    - python -m venv venv
    
      -  Activate Virtual Environment:

          - Windows: venv\Scripts\activate
          
          - Mac/Linux: source venv/bin/activate
          
### 🔹 Step 3: Install Dependencies

      - pip install -r requirements.txt
      
### 🔹 Step 4: Create .env File for Configuration

    - Create a .env file in the root directory and define the database connection:

        - For PostgreSQL:
        
            - DATABASE_URL=postgresql://username:password@localhost/profile_db

## 📌 Database & Migrations (Alembic)

### 🔹 Step 1: Initialize Alembic

    - alembic init migrations
    
### 🔹 Step 2: Configure Alembic

  - Modify sqlalchemy.url in alembic.ini:

    - For PostgreSQL:


      - sqlalchemy.url = postgresql://username:password@localhost/profile_db

### 🔹 Step 3: Generate Migration File

    - alembic revision --autogenerate -m "Initial migration"
    
### 🔹 Step 4: Apply Migrations

    - alembic upgrade head

    
## 📌 Running the FastAPI Server

    - Start the FastAPI application:

        - uvicorn app.main:app --reload

        
## Access API Documentation:

    - Swagger UI: http://127.0.0.1:8000/docs
 
## 📌 POSTMAN COLLECTION

 ### The sample request body is:

## 🔹 User Registration (POST /create-profile)

  - Request Body:

```json
{
  "name": "Alice",
  "email": "alice@example.com",
  "phone": "9876543210",
  "password": "Strong@123"
}
```




  - Response:

```json
{
  "message": "User registered successfully",
  "profile_details": {
    "name": "Alice",
    "email": "alice@example.com",
    "phone": "9876543210",
    "password": "Strong@123"
  }
}
```



## 🚀 Your Profile Creation System is Now Ready! 🚀
