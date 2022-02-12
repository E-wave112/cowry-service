from decouple import config

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


metadata = MetaData()

database = Database(DATABASE_URI)


books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100), nullable=False, unique=True),
    Column("description", String(1000)),
    Column("publisher", String(1000), nullable=False),
    Column("category", String(100), nullable=False),
    Column("inStock", BOOLEAN, default=True),
    Column("datePublished", String(20)),
    Column("authors", ARRAY(String(100))),
    Column("DateAvailable", String(100),default=""),
    Column("created_at", String(100), default=date_in_string()),
)
engine = create_engine(DATABASE_URI, echo=True)


metadata.create_all(engine)

