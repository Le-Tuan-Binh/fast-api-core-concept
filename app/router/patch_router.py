from fastapi import APIRouter, HTTPException, Path
from app.core.constants import BOOKS
from app.schema.book_schema import BookCreate, BookResponse

router = APIRouter()


"""
Partially update a book by its ID.

Path Parameters:
    book_id: str

Body:
    book: BookCreate

Returns:
    BookResponse: Updated book object
"""
@router.patch("/books/{book_id}", response_model=BookResponse, summary="Partially update an existing book")
def patch_book(
    book_id: str = Path(..., description="The ID of the book to update"),
    book: BookCreate = ...
):
    for idx, existing_book in enumerate(BOOKS):
        if existing_book["id"] == book_id:
            updated_book = existing_book.copy()
            if book.title is not None:
                updated_book["title"] = book.title
            if book.author is not None:
                updated_book["author"] = book.author
            BOOKS[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


"""
Partially update multiple books by their IDs.

Body:
    books: List[BookResponse]

Returns:
    List[BookResponse]: List of updated book objects
"""
@router.patch("/books/batch", response_model=list[BookResponse], summary="Partially update multiple books")
def patch_books_batch(books: list[BookResponse]):
    updated_books = []
    for book in books:
        for idx, existing_book in enumerate(BOOKS):
            if existing_book["id"] == book.id:
                updated_book = existing_book.copy()
                if book.title is not None:
                    updated_book["title"] = book.title
                if book.author is not None:
                    updated_book["author"] = book.author
                BOOKS[idx] = updated_book
                updated_books.append(updated_book)
                break
        else:
            raise HTTPException(status_code=404, detail=f"Book with id {book.id} not found")
    return updated_books
