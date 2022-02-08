from decouple import config
# import the books database
from books.app.api.models import SingleBook
import datetime
from utils import date_in_string

from sqlalchemy import (Column, Integer, MetaData, String, Table,DateTime,
                        create_engine, ARRAY)

from databases import Database

# db config
DATABASE_URI = config('DB_CLIENT')

engine = create_engine(DATABASE_URI)
metadata = MetaData()
# declare a defualt time in string when a new entity is created
default_date_str = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('firstName', String(50), nullable=False),
    Column('lastName', String(50), nullable=False),
    Column('email', String(50), unique=True, nullable=False),
    Column('phone', String(20)),
    Column('role', String(50),default='user'),
    Column('booksBorrowed', ARRAY(SingleBook), default=[]),
    Column('created_at', String(100), default=date_in_string()),
)

database = Database(DATABASE_URI)