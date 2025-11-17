from fastapi import APIRouter, HTTPException, Path
from typing import List

from app.core.constants import BOOKS
from app.schema.book_schema import BookResponse

router = APIRouter()


"""
Delete a book entirely by its ID.

Path Parameters:
    book_id: str

Returns:
    BookResponse: Deleted book object
"""
@router.delete("/books/{book_id}", response_model=BookResponse, summary="Delete an existing book")
def delete_book(
    book_id: str = Path(..., description="The ID of the book to delete")
):
    for idx, existing_book in enumerate(BOOKS):
        if existing_book["id"] == book_id:
            deleted_book = BOOKS.pop(idx)
            return deleted_book
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


"""
Delete multiple books entirely by their IDs.

Body:
    books: List[BookResponse]

Returns:
    List[BookResponse]: List of deleted book objects
"""
@router.delete("/books/batch", response_model=List[BookResponse], summary="Delete multiple books")
def delete_books_batch(books: List[BookResponse]):
    deleted_books = []
    for book in books:
        for idx, existing_book in enumerate(BOOKS):
            if existing_book["id"] == book.id:
                deleted_book = BOOKS.pop(idx)
                deleted_books.append(deleted_book)
                break
        else:
            raise HTTPException(status_code=404, detail=f"Book with id {book.id} not found")
    return deleted_books
