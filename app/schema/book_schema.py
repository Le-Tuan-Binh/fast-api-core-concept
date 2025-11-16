from pydantic import BaseModel


class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
