# Feedback API with FastAPI and PostgreSQL

This project is a **Feedback Management REST API** built using **FastAPI** and **PostgreSQL**.  
It allows users to create, retrieve, delete, and list feedback entries.  
The project follows **PEP8 standards** and uses **Swagger UI** for API testing.

---

## 🚀 Features

- Create user feedback
- Get feedback by ID
- Delete feedback
- List all feedbacks
- PostgreSQL for persistent storage
- FastAPI with automatic Swagger documentation
- PEP8-compliant, modular code structure

---

## 🛠️ Tech Stack

- **Python**: 3.8.10  
- **FastAPI**: Web framework  
- **PostgreSQL**: Database  
- **SQLAlchemy**: ORM  
- **Pydantic**: Data validation  
- **Uvicorn**: ASGI server  

---

## 📂 Project Structure

* feedback_api/
* |
* |-- main.py # FastAPI application and routes
* |-- database.py # Database connection setup
* |-- models.py # SQLAlchemy models
* |-- schemas.py # Pydantic schemas
* |-- crud.py # Database operations
* |-- requirements.txt # Project dependencies
* |-- README.md # Project documentation
* |-- feedback_API.doc # Project steps and output 


---

## ⚙️ Setup Instructions (WSL / Ubuntu)

### 1️⃣ Clone or open the project
cd feedback_api

### 2️⃣ Create and activate virtual environment
python3 -m venv venv
. venv/bin/activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Configure Database
Ensure PostgreSQL is running and a database named feedback_db exists.

Database URL used in database.py:

postgresql://user:password@localhost:5432/feedback_db

### 5️⃣ Run the application
uvicorn main:app --reload


### 🌐 API Documentation (Swagger UI)
Open your browser and go to:

http://127.0.0.1:8000/docs
Swagger UI provides an interactive interface to test all APIs.

### 📌 API Endpoints

➤ Create Feedback
POST /feedback

➤ Get Feedback by ID
GET /feedback/{feedback_id}

➤ Delete Feedback
DELETE /feedback/{feedback_id}

➤ List All Feedbacks
GET /feedbacks


