import uuid
from pydantic import BaseModel



class AuthorCreate(BaseModel):
    name: str



class AuthorResponse(BaseModel):
    id: uuid.UUID
    name: str


    model_config ={
        "from_attributes": True
    }


class BookCreate(BaseModel):
    name: str
    published_year: int
    author_id: uuid.UUID




class BookResponse(BaseModel):
    id: uuid.UUID
    name: str
    published_year: int
    # author_id: uuid.UUID
    author: AuthorResponse


    model_config ={
        "from_attributes": True
    }

class BookSummary(BaseModel):
    id: uuid.UUID
    name: str
    published_year: int


    model_config ={
        "from_attributes": True
    }



class AuthorWithBooks(BaseModel):
    id: uuid.UUID
    name: str
    books: list[BookSummary]

    model_config ={
        "from_attributes": True
    }