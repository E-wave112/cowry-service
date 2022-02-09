from decouple import config
from .utils import date_in_string

from sqlalchemy import (Column, Integer, MetaData, String, Table, DateTime,
                        create_engine, ARRAY)

from databases import Database

# db config
DATABASE_URI = config('DB_ADMIN')

engine = create_engine(DATABASE_URI)
# ADD METADATA
metadata = MetaData()

admin = Table(
    'admin',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('role', String(20), default='admin'),
    Column('email', String(50), unique=True),
    Column('created_at', String(100), default=date_in_string()),
)

database = Database(DATABASE_URI)