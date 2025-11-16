from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import uuid

from app.core.constants import BOOKS
from app.schema.book_schema import BookCreate, BookResponse

router = APIRouter()


"""
Create a new book.

Body:
    book: BookCreate

Returns:
    BookResponse: Created book with auto-generated 'id'
"""
@router.post("/books", response_model=BookResponse, status_code=201, summary="Create a new book")
def create_book(book: BookCreate):
    new_book = {
        "id": str(uuid.uuid4()),
        "title": book.title,
        "author": book.author,
    }
    BOOKS.append(new_book)
    return new_book


"""
Create multiple books in batch.

Body:
    books: List[BookCreate]

Returns:
    List[BookResponse]: List of created books with auto-generated 'id's
"""
@router.post("/books/batch", response_model=List[BookResponse], status_code=201, summary="Create multiple books")
def create_books_batch(books: List[BookCreate]):
    created_books = []
    for book in books:
        new_book = {
            "id": str(uuid.uuid4()),
            "title": book.title,
            "author": book.author,
        }
        BOOKS.append(new_book)
        created_books.append(new_book)
    return created_books


"""
Search books by title or author.

Query Parameters:
    title: Optional[str]
    author: Optional[str]

Returns:
    List[BookResponse]: List of books matching the search criteria
"""
@router.post("/books/search", response_model=List[BookResponse], summary="Search books by title or author")
def search_books(
    title: Optional[str] = Query(None, description="Keyword to search in book title"),
    author: Optional[str] = Query(None, description="Keyword to search in book author")
):
    results = []
    for book in BOOKS:
        if title and title.lower() not in book["title"].lower():
            continue
        if author and author.lower() not in book["author"].lower():
            continue
        results.append(book)
    return results
