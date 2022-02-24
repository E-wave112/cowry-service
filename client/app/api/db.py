from decouple import config

from .utils import date_in_string
from typing import Any

from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    ForeignKey,
    create_engine,
    ARRAY,
)

from databases import Database

# db config
DATABASE_URI = config("DB_CLIENT")

database = Database(DATABASE_URI)

engine = create_engine(DATABASE_URI, echo=True)
metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("firstName", String(50), nullable=False),
    Column("lastName", String(50), nullable=False),
    Column("email", String(50), unique=True, nullable=False),
    Column("phone", String(20)),
    Column("role", String(50), default="user"),
    Column("booksBorrowed", ARRAY(Integer), ForeignKey("books.id")),
    Column("created_at", String(100), default=date_in_string()),
)
metadata.create_all(engine)
