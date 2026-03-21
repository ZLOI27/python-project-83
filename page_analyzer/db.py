import os
from contextlib import contextmanager

from dotenv import load_dotenv
from flask import g
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


class DATABASE:
    """A separate pool of connections is created for each worker. 
    It is unnecessary to use PgBouncer. 
    And when there is a common pool of connections for workers, 
    an error occurs.
    """
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            cls._pool = ThreadedConnectionPool(
                minconn=1,
                maxconn=4,
                dsn=DATABASE_URL,
                connect_timeout=10,
            )
        return cls._pool


@contextmanager
def get_cursor():
    conn = g.db
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        yield cur
