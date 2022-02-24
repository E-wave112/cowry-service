from pydantic import BaseModel
from typing import List, Optional, Union
from .utils import add_days
from datetime import date


class Books(BaseModel):
    title: str
    publisher: str
    description: Optional[str]
    category: str
    datePublished: str
    authors: Optional[List[str]]
    inStock: Optional[bool]


class BorrowBooks(Books):
    id: int
    borrowed_date: date = date.today()
    no_of_days: int = 3
    DateAvailable: str = add_days(borrowed_date, no_of_days)
    inStock: bool = False


class SingleBook(Books):
    id: Union[int, None]
    created_at: Union[str, None]


class getAllBooks(BaseModel):
    books: List[SingleBook]


class FilterBooks(BaseModel):
    publisher: Optional[str] = ""
    category: Optional[str] = ""


class RemoveBooks(BaseModel):
    id: int
