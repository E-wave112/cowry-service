from decouple import config
import datetime
from .utils import date_in_string
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    BOOLEAN,
    DateTime,
    create_engine,
    ARRAY,
)

from databases import Database

# db config
DATABASE_URI = config("DB_BOOKS")

engine = create_engine(DATABASE_URI, echo=True)
metadata = MetaData()


books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50), nullable=False, unique=True),
    Column("description", String(1000)),
    Column("publisher", String(50), nullable=False),
    Column("category", String(50), nullable=False),
    Column("inStock", BOOLEAN, default=True),
    Column("datePublished", String(20)),
    Column("authors", ARRAY(String(100))),
    Column("DateAvailable", String(20)),
    Column("created_at", String(100), default=date_in_string()),
)

metadata.create_all(engine)
database = Database(DATABASE_URI)
