#  Library Book Management API using FastAPI

## Project Overview
This project is a fully functional backend application built using FastAPI.  
It allows users to manage books in a library system with CRUD operations and advanced features like search, sorting, and pagination.

---

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Pydantic

---

## Features

### CRUD Operations
- GET all books
- GET book by ID
- POST (Add new book)
- PUT (Update book)
- DELETE (Remove book)

### Validation
- Implemented using Pydantic
- Ensures correct data types and required fields

### Advanced Features
- Search books by title/author
- Sorting (by title, author, etc.)
- Pagination (page & limit)

### Additional Endpoints
- Summary API (total, available, unavailable books)
- Borrow records

---

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| GET | / | Home |
| GET | /books | Get all books |
| GET | /books/{book_id} | Get book by ID |
| POST | /books | Add new book |
| PUT | /books/{book_id} | Update book |
| DELETE | /books/{book_id} | Delete book |
| GET | /summary | Get summary |
| GET | /borrow-records | Borrow details |

---

##  Query Parameters

- search → Search books  
- sort_by → Sort field (title, author)  
- order → asc / desc  
- page → Page number  
- limit → Items per page  

---

##  How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/AS-Bhoomika/Library-Book-Management-API-Using-FASTAPI.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the server:
```bash
uvicorn main:app --reload
```
4. Open Swagger UI:
```bash
http://127.0.0.1:8000/
```

# Learning Outcomes

* Built REST APIs using FastAPI
* Implemented CRUD operations
* used Pydantic for validation
* Learned API testing using Swagger
* Implemented search, sorting, pagination


## GitHub Repository:

```bash
https://github.com/AS-Bhoomika/Library-Book-Management-API-Using-FASTAPI/
```
