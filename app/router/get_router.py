from fastapi import APIRouter, HTTPException

from app.core.constants import BOOKS

router = APIRouter()


"""
GET endpoint in FastAPI.

This endpoint demonstrates how to define a GET endpoint

Returns:
    list: A list of all books with their id, title, and author.
"""
@router.get("/books/")
def get_all_books():
    return BOOKS

"""
GET endpoint with a **Path Parameter** in FastAPI.

This endpoint demonstrates how to define a path parameter in the url and access its value inside the function.

Path Parameter:
    user_id: str

Returns:
    dict: A dictionary containing the book's id, title, and author.

Raises:
    HTTPException: 404 if the book is not found.
"""
@router.get("/books/{book_id}")
def get_book(book_id: str):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


"""
GET endpoint with **Query Parameters** in FastAPI.

This endpoint demonstrates how to define optional query parameters that clients can use to filter or limit results.

Query Parameters:
    keyword: str, optional
    limit: int, optional

Returns:
    list: A list of books matching the search criteria.
"""
@router.get("/books/search")
def search_books(keyword: str = "", limit: int = 10):
    results = [
        book for book in BOOKS
        if keyword.casefold() in book["title"].casefold() or keyword.casefold() in book["author"].casefold()
    ]
    return results[:limit]