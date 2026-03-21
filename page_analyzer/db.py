import os
from contextlib import contextmanager

from dotenv import load_dotenv
from flask import g
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=4,
    dsn=DATABASE_URL,
)


@contextmanager
def get_cursor():
    conn = g.db
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        yield cur
