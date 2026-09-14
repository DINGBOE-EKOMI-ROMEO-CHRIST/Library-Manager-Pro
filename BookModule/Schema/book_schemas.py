from pydantic import BaseModel

class BookCreate(BaseModel):
    title : str
    author : str
    publication_year : int
    available_copies : int

class BookResponse(BaseModel):
    id : int
    title : str
    author : str
    publication_year : int
    available_copies : int
    