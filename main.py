from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# -----------------------------
# Pydantic Model (Validation)
# -----------------------------
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    is_available: bool


# -----------------------------
# Sample Data
# -----------------------------
books: List[Book] = [
    Book(id=1, title="Python Basics", author="John", genre="Tech", is_available=True),
    Book(id=2, title="Data Science", author="Alice", genre="Tech", is_available=True),
    Book(id=3, title="History of India", author="Ravi", genre="History", is_available=False),
    Book(id=4, title="Machine Learning", author="David", genre="Tech", is_available=True),
    Book(id=5, title="Fiction Story", author="Emma", genre="Fiction", is_available=True),
    Book(id=6, title="Science Book", author="Rahul", genre="Science", is_available=False),
]


# -----------------------------
# HOME
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to City Public Library"}


# -----------------------------
# GET ALL BOOKS (Search + Sort + Pagination)
# -----------------------------
@app.get("/books")
def get_books(
    search: Optional[str] = None,
    sort_by: Optional[str] = None,
    order: Optional[str] = "asc",
    page: int = 1,
    limit: int = 3
):
    result = books

    # 🔍 Search
    if search:
        result = [
            b for b in result
            if search.lower() in b.title.lower() or search.lower() in b.author.lower()
        ]

    # 🔽 Sorting
    if sort_by:
        reverse = True if order == "desc" else False
        try:
            result = sorted(result, key=lambda x: getattr(x, sort_by), reverse=reverse)
        except:
            raise HTTPException(status_code=400, detail="Invalid sort field")

    # 📄 Pagination
    start = (page - 1) * limit
    end = start + limit
    paginated = result[start:end]

    return {
        "total": len(result),
        "page": page,
        "limit": limit,
        "data": paginated
    }


# -----------------------------
# GET SINGLE BOOK
# -----------------------------
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


# -----------------------------
# POST (ADD BOOK)
# -----------------------------
@app.post("/books")
def add_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")

    books.append(book)
    return {"message": "Book added successfully", "data": book}


# -----------------------------
# PUT (UPDATE BOOK)
# -----------------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return {"message": "Book updated successfully", "data": updated_book}

    raise HTTPException(status_code=404, detail="Book not found")


# -----------------------------
# DELETE BOOK
# -----------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(index)
            return {"message": "Book deleted successfully", "data": deleted}

    raise HTTPException(status_code=404, detail="Book not found")


# -----------------------------
# SUMMARY
# -----------------------------
@app.get("/summary")
def get_summary():
    total = len(books)
    available = len([b for b in books if b.is_available])
    unavailable = total - available

    return {
        "total_books": total,
        "available_books": available,
        "unavailable_books": unavailable
    }