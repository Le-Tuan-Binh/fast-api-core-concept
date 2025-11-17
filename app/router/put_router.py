from fastapi import APIRouter, HTTPException, Path
from typing import List
import uuid

from app.core.constants import BOOKS
from app.schema.book_schema import BookCreate, BookResponse

router = APIRouter()


"""
Update a book entirely by its ID.

Path Parameters:
    book_id: str

Body:
    book: BookCreate

Returns:
    BookResponse: Updated book object
"""
@router.put("/books/{book_id}", response_model=BookResponse, summary="Update an existing book")
def update_book(
    book_id: str = Path(..., description="The ID of the book to update"),
    book: BookCreate = ...
):
    for idx, existing_book in enumerate(BOOKS):
        if existing_book["id"] == book_id:
            updated_book = {
                "id": book_id,
                "title": book.title,
                "author": book.author,
            }
            BOOKS[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


"""
Update multiple books entirely by their IDs.

Body:
    books: List[BookResponse]

Returns:
    List[BookResponse]: List of updated book objects
"""
@router.put("/books/batch", response_model=List[BookResponse], summary="Update multiple books")
def update_books_batch(books: List[BookResponse]):
    updated_books = []
    for book in books:
        for idx, existing_book in enumerate(BOOKS):
            if existing_book["id"] == book.id:
                updated_book = {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                }
                BOOKS[idx] = updated_book
                updated_books.append(updated_book)
                break
        else:
            raise HTTPException(status_code=404, detail=f"Book with id {book.id} not found")
    return updated_books
